#!/usr/bin/env python3
"""
Script para testar apenas um produto antes de executar o lote completo
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time
from browser import criar_driver_automatico

def extrair_numero(texto):
    """
    Extrai número de um texto, retornando 0 se não encontrar
    """
    if not texto:
        return 0
    
    # Remove espaços e procura por números
    match = re.search(r'(\d+(?:\.\d+)?)', texto.replace(',', '.'))
    if match:
        return float(match.group(1))
    return 0

def testar_um_produto():
    """
    Testa coleta de dados de um produto específico
    """
    url = "https://maxtitanium.eu/products/top-whey-3w-sabor-900g-brigadeiro"
    categoria = "Proteínas"
    
    # Configurar Chrome
    # Criar driver automaticamente
    driver = criar_driver_automatico(headless=True)
    
    try:
        print(f"🔗 Testando produto: {url}")
        
        # Navegar para a página do produto
        driver.get(url)
        
        # Aguardar a página carregar
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        # Extrair nome do produto
        nome_produto = driver.find_element(By.TAG_NAME, "h1").text.strip()
        print(f"📦 Produto: {nome_produto}")
        
        # Dados nutricionais padrão
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
        
        # Aguardar carregamento completo
        time.sleep(3)
        
        # Rolar para baixo e procurar pelo dropdown "Informação Nutricional"
        print("🔍 Procurando dropdown 'Informação Nutricional'...")
        
        dropdown = None
        max_scrolls = 10
        scroll_count = 0
        
        while not dropdown and scroll_count < max_scrolls:
            try:
                # Estratégia 1: Procurar pelo h2 específico com o texto "Informação Nutricional"
                h2_elemento = driver.find_element(By.XPATH, "//h2[@class=' font-heading h5 inline-richtext' and text()='Informação Nutricional']")
                dropdown = h2_elemento.find_element(By.XPATH, "./ancestor::summary[@class='accordion-details__summary flex items-center justify-between focus-inset']")
                print("✅ Estratégia 1: Dropdown encontrado via h2 específico")
                break
            except:
                try:
                    # Estratégia 2: Procurar por qualquer summary que contenha "Informação Nutricional"
                    dropdown = driver.find_element(By.XPATH, "//summary[contains(., 'Informação Nutricional')]")
                    print("✅ Estratégia 2: Dropdown encontrado via texto")
                    break
                except:
                    try:
                        # Estratégia 3: Procurar por todos os summary e verificar o texto
                        summaries = driver.find_elements(By.TAG_NAME, "summary")
                        for summary in summaries:
                            if "Informação Nutricional" in summary.text:
                                dropdown = summary
                                print("✅ Estratégia 3: Dropdown encontrado via varredura")
                                break
                        if dropdown:
                            break
                    except:
                        pass
            
            # Se não encontrou, rolar para baixo
            if not dropdown:
                print(f"⬇️ Rolando para baixo... (tentativa {scroll_count + 1}/{max_scrolls})")
                driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(2)
                scroll_count += 1
        
        # Procurar e clicar no dropdown "Informação Nutricional"
        try:
            
            if dropdown:
                print(f"✅ Dropdown encontrado: {dropdown.text[:50]}...")
                
                # Rolar até o elemento com offset para evitar o header
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
                time.sleep(2)
                
                # Clicar no dropdown usando JavaScript para evitar interceptação
                driver.execute_script("arguments[0].click();", dropdown)
                print("✅ Dropdown clicado!")
                
                # Aguardar conteúdo abrir
                time.sleep(3)
                
                # Verificar tabelas
                tabelas = driver.find_elements(By.TAG_NAME, "table")
                
                if tabelas:
                    print(f"✅ {len(tabelas)} tabela(s) encontrada(s)!")
                    
                    # Extrair dados da primeira tabela
                    tabela = tabelas[0]
                    linhas = tabela.find_elements(By.TAG_NAME, "tr")
                    
                    print(f"📋 Processando {len(linhas)} linhas:")
                    
                    for i, linha in enumerate(linhas):
                        try:
                            colunas = linha.find_elements(By.TAG_NAME, "td")
                            if len(colunas) >= 2:
                                campo = colunas[0].text.strip()
                                valor = colunas[1].text.strip()
                                
                                print(f"  {i+1}. {campo}: {valor}")
                                
                                # Extrair valores específicos
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
                        except Exception as e:
                            print(f"    ❌ Erro na linha {i+1}: {str(e)}")
                            continue
                    
                    # Mostrar dados extraídos
                    print(f"\n📊 DADOS EXTRAÍDOS:")
                    print(f"  • Nome: {dados['nome_produto']}")
                    print(f"  • Categoria: {dados['categoria']}")
                    print(f"  • Porção: {dados['porcao_g']}g")
                    print(f"  • Calorias: {dados['calorias_kcal']}kcal")
                    print(f"  • Carboidratos: {dados['carboidratos_g']}g")
                    print(f"  • Proteínas: {dados['proteinas_g']}g")
                    print(f"  • Gorduras Totais: {dados['gorduras_totais_g']}g")
                    print(f"  • Gorduras Saturadas: {dados['gorduras_saturadas_g']}g")
                    print(f"  • Fibras: {dados['fibras_g']}g")
                    print(f"  • Açúcares: {dados['acucares_g']}g")
                    print(f"  • Sódio: {dados['sodio_mg']}mg")
                    
                    # Salvar em CSV de teste
                    with open('dados/teste_um_produto.csv', 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f, delimiter='\t')
                        writer.writerow([
                            'NOME_PRODUTO', 'URL', 'CATEGORIA', 'PORCAO (g)', 'CALORIAS (kcal)',
                            'CARBOIDRATOS (g)', 'PROTEINAS (g)', 'GORDURAS_TOTAIS (g)', 'GORDURAS_SATURADAS (g)',
                            'FIBRAS (g)', 'ACUCARES (g)', 'SODIO (mg)'
                        ])
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
                    
                    print(f"\n✅ Dados salvos em 'dados/teste_um_produto.csv'")
                    
                else:
                    print("❌ Nenhuma tabela encontrada após clicar no dropdown")
            else:
                print("❌ Dropdown encontrado mas não contém 'Informação Nutricional'")
                
        except Exception as e:
            print(f"❌ Erro ao encontrar/clicar no dropdown: {str(e)}")
        
        # Aguardar para análise visual
        print("\n⏱️  Aguardando 5 segundos...")
        time.sleep(5)
        
    except Exception as e:
        print(f"❌ Erro geral: {str(e)}")
        
    finally:
        driver.quit()
        print("\n🏁 Teste concluído")

if __name__ == "__main__":
    print("🧪 TESTE DE UM PRODUTO")
    print("=" * 40)
    testar_um_produto() 