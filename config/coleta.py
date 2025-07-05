
#!/usr/bin/env python3
"""
Script final para coletar dados nutricionais de todos os produtos Max Titanium Europa
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time
import sys
from browser import criar_driver_automatico

def extrair_numero(texto):
    """Extrai número de um texto, retornando 0 se não encontrar"""
    if not texto:
        return 0
    match = re.search(r'(\d+(?:\.\d+)?)', texto.replace(',', '.'))
    if match:
        return float(match.group(1))
    return 0

def coletar_dados_produto(driver, url, categoria):
    """Coleta dados nutricionais de um produto"""
    try:
        print(f"🔗 Processando: {url}", flush=True)
        
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        # Nome do produto
        nome_produto = driver.find_element(By.TAG_NAME, "h1").text.strip()
        print(f"📦 Produto: {nome_produto}", flush=True)
        
        # Dados padrão
        dados = {
            'nome_produto': nome_produto,
            'url': url,
            'categoria': categoria,
            'porcao_g': 0,
            'calorias_kcal': 0,
            'carboidratos_g': 0,
            'proteinas_g': 0,
            'gorduras_totais_g': 0,
            'gorduras_saturadas_g': 0,
            'fibras_g': 0,
            'acucares_g': 0,
            'sodio_mg': 0
        }
        
        time.sleep(2)
        
        # Rolar para baixo e procurar pelo dropdown "Informação Nutricional"
        dropdown = None
        max_scrolls = 10
        scroll_count = 0
        
        while not dropdown and scroll_count < max_scrolls:
            try:
                # Estratégia 1: Procurar pelo h2 específico com o texto "Informação Nutricional"
                h2_elemento = driver.find_element(By.XPATH, "//h2[@class=' font-heading h5 inline-richtext' and text()='Informação Nutricional']")
                dropdown = h2_elemento.find_element(By.XPATH, "./ancestor::summary[@class='accordion-details__summary flex items-center justify-between focus-inset']")
                break
            except:
                try:
                    # Estratégia 2: Procurar por qualquer summary que contenha "Informação Nutricional"
                    dropdown = driver.find_element(By.XPATH, "//summary[contains(., 'Informação Nutricional')]")
                    break
                except:
                    try:
                        # Estratégia 3: Procurar por todos os summary e verificar o texto
                        summaries = driver.find_elements(By.TAG_NAME, "summary")
                        for summary in summaries:
                            if "Informação Nutricional" in summary.text:
                                dropdown = summary
                                break
                        if dropdown:
                            break
                    except:
                        pass
            
            # Se não encontrou, rolar para baixo
            if not dropdown:
                driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(2)
                scroll_count += 1
        
        # Clicar no dropdown
        try:
            
            if dropdown:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
                time.sleep(2)
                driver.execute_script("arguments[0].click();", dropdown)
                time.sleep(3)
                
                # Extrair dados da tabela
                tabelas = driver.find_elements(By.TAG_NAME, "table")
                
                if tabelas:
                    tabela = tabelas[0]
                    linhas = tabela.find_elements(By.TAG_NAME, "tr")
                    
                    for linha in linhas:
                        colunas = linha.find_elements(By.TAG_NAME, "td")
                        if len(colunas) >= 2:
                            campo = colunas[0].text.strip()
                            valor = colunas[1].text.strip()
                            
                            if 'Porção' in campo:
                                dados['porcao_g'] = extrair_numero(valor)
                            elif 'Valor Energético' in campo:
                                match = re.search(r'(\d+(?:\.\d+)?)\s*kcal', valor)
                                if match:
                                    dados['calorias_kcal'] = float(match.group(1))
                            elif 'Carboidratos' in campo:
                                dados['carboidratos_g'] = extrair_numero(valor)
                            elif 'Proteínas' in campo:
                                dados['proteinas_g'] = extrair_numero(valor)
                            elif 'Gorduras Totais' in campo:
                                dados['gorduras_totais_g'] = extrair_numero(valor)
                            elif 'Gorduras Saturadas' in campo:
                                dados['gorduras_saturadas_g'] = extrair_numero(valor)
                            elif 'Fibra Alimentar' in campo:
                                dados['fibras_g'] = extrair_numero(valor)
                            elif 'Sódio' in campo:
                                dados['sodio_mg'] = extrair_numero(valor)
                    
                    print(f"✅ Dados extraídos: {dados['calorias_kcal']}kcal, {dados['proteinas_g']}g proteína", flush=True)
                else:
                    print("❌ Tabela não encontrada", flush=True)
        
        except Exception as e:
            print(f"❌ Erro no dropdown: {str(e)}", flush=True)
        
        return dados
        
    except Exception as e:
        print(f"❌ Erro geral: {str(e)}", flush=True)
        return None

def main():
    """Função principal"""
    # Criar driver automaticamente
    driver = criar_driver_automatico(headless=True)
    
    try:
        # Ler URLs
        produtos = []
        with open('dados/urls_produtos_europa_estrutura_real.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produtos.append({'url': row['url'], 'categoria': row['categoria']})
        
        print(f"📋 Processando {len(produtos)} produtos", flush=True)
        
        # Coletar dados
        dados_nutricionais = []
        
        for i, produto in enumerate(produtos, 1):
            print(f"\n[{i}/{len(produtos)}]", flush=True)
            
            dados = coletar_dados_produto(driver, produto['url'], produto['categoria'])
            if dados:
                dados_nutricionais.append(dados)
            
            time.sleep(3)
        
        # Salvar CSV
        if dados_nutricionais:
            with open('dados/dados_nutricionais.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter='\t')
                writer.writerow([
                    'NOME_PRODUTO', 'URL', 'CATEGORIA', 'PORCAO (g)', 'CALORIAS (kcal)',
                    'CARBOIDRATOS (g)', 'PROTEINAS (g)', 'GORDURAS_TOTAIS (g)', 'GORDURAS_SATURADAS (g)',
                    'FIBRAS (g)', 'ACUCARES (g)', 'SODIO (mg)'
                ])
                
                for dados in dados_nutricionais:
                    writer.writerow([
                        dados['nome_produto'],
                        dados['url'],
                        dados['categoria'],
                        dados['porcao_g'],
                        dados['calorias_kcal'],
                        dados['carboidratos_g'],
                        dados['proteinas_g'],
                        dados['gorduras_totais_g'],
                        dados['gorduras_saturadas_g'],
                        dados['fibras_g'],
                        dados['acucares_g'],
                        dados['sodio_mg']
                    ])
            
            print(f"\n✅ Dados salvos! Total: {len(dados_nutricionais)} produtos")
            
            # Resumo
            print("\n📊 RESUMO:")
            for dados in dados_nutricionais:
                print(f"• {dados['nome_produto']} ({dados['categoria']})")
                print(f"  {dados['calorias_kcal']}kcal | {dados['proteinas_g']}g proteína | {dados['carboidratos_g']}g carbo")
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
    
    finally:
        driver.quit()
        print("\n🏁 Concluído")

if __name__ == "__main__":
    print("🚀 COLETA DE DADOS NUTRICIONAIS")
    print("=" * 50)
    main() 