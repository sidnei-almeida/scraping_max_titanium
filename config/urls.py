                                                                                                                                                                        #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import csv
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import criar_driver_automatico

class ColetorURLsEuropaEstruturaReal:
    def __init__(self):
        self.base_url = "https://maxtitanium.eu"
        self.driver = None
        self.urls_coletadas = []
        
    def setup_driver(self):
        """Configura o driver do Selenium"""
        # Criar driver automaticamente com zoom de 25%
        self.driver = criar_driver_automatico(headless=True, zoom=25)
        return self.driver
    
    def aguardar_carregamento_grid(self):
        """Aguarda o grid de produtos carregar"""
        print("    → Aguardando grid de produtos carregar...")
        
        # Aguarda o grid principal carregar
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "ProductsList"))
        )
        
        # Aguarda os produtos aparecerem
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#ProductsList .product-card"))
        )
        
        time.sleep(3)
        print("    → Grid carregado com sucesso")
    
    def extrair_produtos_grid_real(self, categoria_nome):
        """Extrai produtos usando a estrutura HTML real"""
        print(f"    → Extraindo produtos do grid principal...")
        
        # Seletor baseado na estrutura HTML real mostrada
        seletor_grid = "#ProductsList .f-column .product-card"
        
        try:
            # Encontra todos os cards de produtos no grid principal
            product_cards = self.driver.find_elements(By.CSS_SELECTOR, seletor_grid)
            print(f"    → {len(product_cards)} product cards encontrados")
            
            produtos_encontrados = []
            
            for card in product_cards:
                try:
                    # Busca o link do produto dentro do card
                    link_element = card.find_element(By.CSS_SELECTOR, "a[href*='/products/']")
                    href = link_element.get_attribute('href')
                    
                    if href and '/products/' in href:
                        # Busca o nome do produto no título
                        try:
                            titulo_element = card.find_element(By.CSS_SELECTOR, "h3.product-card__title a")
                            nome = titulo_element.text.strip()
                        except:
                            # Fallback para o texto do link
                            nome = link_element.get_attribute('aria-label') or ''
                            if not nome:
                                # Último fallback: slug da URL
                                slug = href.split('/products/')[-1]
                                nome = slug.replace('-', ' ').title()
                        
                        produto = {
                            'nome_produto': nome,
                            'url': href,
                            'slug': href.split('/products/')[-1],
                            'categoria': categoria_nome,
                            'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }
                        
                        produtos_encontrados.append(produto)
                        
                except Exception as e:
                    print(f"      • Erro ao processar card: {e}")
                    continue
            
            print(f"    → {len(produtos_encontrados)} produtos extraídos:")
            for i, produto in enumerate(produtos_encontrados):
                print(f"      {i+1}. {produto['nome_produto']}")
            
            return produtos_encontrados
            
        except Exception as e:
            print(f"    ❌ Erro ao extrair produtos: {e}")
            return []
    
    def coletar_urls_categoria(self, categoria_url, categoria_nome):
        """Coleta URLs de uma categoria específica"""
        print(f"\n=== COLETANDO: {categoria_nome} ===")
        print(f"URL: {categoria_url}")
        
        try:
            # Navega para a categoria
            self.driver.get(categoria_url)
            
            # Aguarda o grid carregar
            self.aguardar_carregamento_grid()
            
            # Extrai produtos do grid principal
            produtos = self.extrair_produtos_grid_real(categoria_nome)
            
            print(f"    → ✅ {len(produtos)} produtos coletados de {categoria_nome}")
            return produtos
            
        except Exception as e:
            print(f"    ❌ Erro ao coletar {categoria_nome}: {e}")
            return []
    
    def coletar_todas_urls(self):
        """Coleta URLs de todas as categorias"""
        print("=== COLETOR BASEADO NA ESTRUTURA HTML REAL ===")
        
        # Configura o driver
        self.setup_driver()
        
        categorias = [
            {'nome': 'Pré-treinos', 'url': 'https://maxtitanium.eu/collections/pre-treinos'},
            {'nome': 'Proteínas', 'url': 'https://maxtitanium.eu/collections/proteinas'},
            {'nome': 'Creatinas e Aminoácidos', 'url': 'https://maxtitanium.eu/collections/creatinas-e-aminoacidos'}
        ]
        
        try:
            todas_urls = []
            
            for categoria in categorias:
                urls_categoria = self.coletar_urls_categoria(categoria['url'], categoria['nome'])
                todas_urls.extend(urls_categoria)
                
                print(f"    → Total acumulado: {len(todas_urls)} URLs")
                print("=" * 80)
                
                # Pausa entre categorias
                time.sleep(3)
            
            # Remove duplicatas globais
            urls_unicas = []
            urls_vistas = set()
            
            for url_info in todas_urls:
                if url_info['url'] not in urls_vistas:
                    urls_unicas.append(url_info)
                    urls_vistas.add(url_info['url'])
            
            self.urls_coletadas = urls_unicas
            
            print(f"\n=== COLETA FINALIZADA ===")
            print(f"Total de URLs únicas: {len(self.urls_coletadas)}")
            
            return self.urls_coletadas
            
        finally:
            if self.driver:
                self.driver.quit()
    
    def salvar_arquivos(self, base_filename='urls_produtos_europa_estrutura_real'):
        """Salva as URLs coletadas em CSV e TXT"""
        if not self.urls_coletadas:
            print("Nenhuma URL para salvar!")
            return
        
        # Cria pasta dados se não existir
        os.makedirs('dados', exist_ok=True)
        
        # Salva CSV
        csv_path = os.path.join('dados', f'{base_filename}.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nome_produto', 'url', 'slug', 'categoria', 'data_coleta']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for url_info in self.urls_coletadas:
                writer.writerow(url_info)
        
        # Salva TXT (apenas URLs)
        txt_path = os.path.join('dados', f'{base_filename}.txt')
        with open(txt_path, 'w', encoding='utf-8') as txtfile:
            for url_info in self.urls_coletadas:
                txtfile.write(f"{url_info['url']}\n")
        
        print(f"Arquivos salvos:")
        print(f"  • CSV: {csv_path}")
        print(f"  • TXT: {txt_path}")
    
    def exibir_resumo(self):
        """Exibe resumo detalhado das URLs coletadas"""
        if not self.urls_coletadas:
            print("Nenhuma URL coletada!")
            return
        
        print(f"\n=== RESUMO FINAL (ESTRUTURA HTML REAL) ===")
        print(f"Total: {len(self.urls_coletadas)} URLs")
        
        # Conta por categoria
        categorias_count = {}
        for url_info in self.urls_coletadas:
            cat = url_info['categoria']
            categorias_count[cat] = categorias_count.get(cat, 0) + 1
        
        print("\n📊 Por categoria:")
        for cat, count in categorias_count.items():
            print(f"  • {cat}: {count} produtos")
            
            # Mostra os produtos desta categoria
            produtos_categoria = [url for url in self.urls_coletadas if url['categoria'] == cat]
            for i, produto in enumerate(produtos_categoria):
                print(f"    {i+1}. {produto['nome_produto']}")
                print(f"       {produto['url']}")
            print()

def main():
    """Função principal"""
    coletor = ColetorURLsEuropaEstruturaReal()
    
    try:
        # Coleta todas as URLs
        urls = coletor.coletar_todas_urls()
        
        if urls:
            # Salva em CSV e TXT
            coletor.salvar_arquivos()
            
            # Exibe resumo detalhado
            coletor.exibir_resumo()
        else:
            print("❌ Nenhuma URL foi coletada!")
            
    except KeyboardInterrupt:
        print("\n⚠️  Coleta interrompida pelo usuário.")
    except Exception as e:
        print(f"❌ Erro durante a coleta: {e}")

if __name__ == "__main__":
    main() 