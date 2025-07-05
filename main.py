#!/usr/bin/env python3
"""
🚀 Main - Sistema de Coleta Max Titanium Europa
Menu principal para todas as operações de scraping
"""

import sys
import os
import subprocess
from datetime import datetime

# Adicionar pasta config ao path
config_path = os.path.join(os.path.dirname(__file__), 'config')
sys.path.append(config_path)

def exibir_menu():
    """Exibe o menu principal com opções disponíveis"""
    print("\n" + "=" * 60)
    print("🏋️  MAX TITANIUM EUROPA - SISTEMA DE COLETA")
    print("=" * 60)
    print()
    print("📋 OPÇÕES DISPONÍVEIS:")
    print()
    print("1️⃣  🔗 Coletar URLs dos Produtos")
    print("2️⃣  🧪 Teste de Um Produto")
    print("3️⃣  🚀 Coleta Completa (URLs + Dados Nutricionais)")
    print("4️⃣  📊 Apenas Dados Nutricionais (usar URLs existentes)")
    print("5️⃣  📖 Informações do Sistema")
    print("6️⃣  🎯 Teste de Feedback Visual")
    print("7️⃣  🌐 Testar Configuração do Navegador")
    print("0️⃣  ❌ Sair")
    print()
    print("=" * 60)

def coletar_urls():
    """Executa coleta de URLs com feedback em tempo real"""
    print("\n🔗 INICIANDO COLETA DE URLs...")
    print("=" * 50)
    
    try:
        # Executar script de URLs com saída em tempo real
        processo = subprocess.Popen(
            [sys.executable, os.path.join(config_path, 'urls.py')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=os.path.dirname(__file__)
        )
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Aguardar finalização
        processo.wait()
        
        if processo.returncode == 0:
            print("\n✅ Coleta de URLs concluída com sucesso!")
            return True
        else:
            print("\n❌ Erro na coleta de URLs:")
            stderr = processo.stderr.read()
            if stderr:
                print(stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erro durante coleta de URLs: {str(e)}")
        return False

def teste_produto():
    """Executa teste em um produto específico com feedback em tempo real"""
    print("\n🧪 EXECUTANDO TESTE EM PRODUTO ESPECÍFICO...")
    print("=" * 50)
    
    try:
        processo = subprocess.Popen(
            [sys.executable, os.path.join(config_path, 'teste.py')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=os.path.dirname(__file__)
        )
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Aguardar finalização
        processo.wait()
        
        if processo.returncode == 0:
            print("\n✅ Teste concluído com sucesso!")
            print("📁 Resultado salvo em: dados/teste_um_produto.csv")
        else:
            print("\n❌ Teste falhou:")
            stderr = processo.stderr.read()
            if stderr:
                print(stderr)
            
    except Exception as e:
        print(f"❌ Erro durante teste: {str(e)}")

def coletar_dados_nutricionais():
    """Executa coleta de dados nutricionais com feedback em tempo real"""
    print("\n📊 INICIANDO COLETA DE DADOS NUTRICIONAIS...")
    print("=" * 50)
    
    try:
        processo = subprocess.Popen(
            [sys.executable, os.path.join(config_path, 'coleta.py')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=os.path.dirname(__file__)
        )
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Aguardar finalização
        processo.wait()
        
        if processo.returncode == 0:
            print("\n✅ Coleta de dados nutricionais concluída!")
            print("📁 Resultado salvo em: dados/dados_nutricionais.csv")
        else:
            print("\n❌ Falha na coleta de dados nutricionais:")
            stderr = processo.stderr.read()
            if stderr:
                print(stderr)
            
    except Exception as e:
        print(f"❌ Erro durante coleta de dados: {str(e)}")

def coleta_completa():
    """Executa fluxo completo: URLs + Dados Nutricionais"""
    print("\n🚀 INICIANDO COLETA COMPLETA...")
    print("=" * 50)
    
    # Etapa 1: Coletar URLs
    print("\n📍 ETAPA 1/2: Coletando URLs dos produtos...")
    urls_sucesso = coletar_urls()
    
    if not urls_sucesso:
        print("❌ Coleta completa cancelada - falha na coleta de URLs")
        return
    
    # Pausa entre etapas
    print("\n⏱️  Aguardando 3 segundos antes da próxima etapa...")
    import time
    time.sleep(3)
    
    # Etapa 2: Coletar dados nutricionais
    print("\n📍 ETAPA 2/2: Coletando dados nutricionais...")
    coletar_dados_nutricionais()
    
    print("\n🎉 COLETA COMPLETA FINALIZADA!")
    print("🏆 Todos os dados foram coletados e salvos com sucesso!")

def teste_feedback():
    """Testa o feedback visual em tempo real"""
    print("\n🎯 TESTE DE FEEDBACK VISUAL")
    print("=" * 50)
    
    print("\n1️⃣  Simular coleta de URLs")
    print("2️⃣  Simular coleta de dados nutricionais")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    try:
        if opcao == "1":
            processo = subprocess.Popen(
                [sys.executable, os.path.join(config_path, 'teste_feedback.py'), 'urls'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=os.path.dirname(__file__)
            )
        elif opcao == "2":
            processo = subprocess.Popen(
                [sys.executable, os.path.join(config_path, 'teste_feedback.py'), 'dados'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=os.path.dirname(__file__)
            )
        else:
            print("❌ Opção inválida")
            return
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        processo.wait()
        print("\n✅ Teste de feedback concluído!")
        
    except Exception as e:
        print(f"❌ Erro no teste: {str(e)}")

def testar_navegador():
    """Testa a configuração do navegador"""
    print("\n🌐 TESTE DE CONFIGURAÇÃO DO NAVEGADOR")
    print("=" * 50)
    
    try:
        processo = subprocess.Popen(
            [sys.executable, os.path.join(config_path, 'browser.py')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=os.path.dirname(__file__)
        )
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        processo.wait()
        
        if processo.returncode == 0:
            print("\n✅ Configuração do navegador está funcionando!")
        else:
            print("\n❌ Problemas na configuração do navegador:")
            stderr = processo.stderr.read()
            if stderr:
                print(stderr)
        
    except Exception as e:
        print(f"❌ Erro no teste do navegador: {str(e)}")

def exibir_informacoes():
    """Exibe informações do sistema"""
    print("\n📖 INFORMAÇÕES DO SISTEMA")
    print("=" * 50)
    print()
    print("🎯 OBJETIVO:")
    print("   Coletar dados nutricionais dos produtos Max Titanium Europa")
    print()
    print("🌐 SITE ALVO:")
    print("   https://maxtitanium.eu")
    print()
    print("📋 CATEGORIAS:")
    print("   • Pré-treinos (7 produtos)")
    print("   • Proteínas (9 produtos)")
    print("   • Creatinas e Aminoácidos (4 produtos)")
    print("   • Total: 20 produtos únicos")
    print()
    print("🔧 TECNOLOGIAS:")
    print("   • Python 3.13+")
    print("   • Selenium WebDriver")
    print("   • BeautifulSoup")
    print("   • Chrome (modo headless)")
    print()
    print("📊 DADOS COLETADOS:")
    print("   • Nome do produto")
    print("   • URL completa")
    print("   • Categoria")
    print("   • Informações nutricionais completas")
    print("   • Porção, calorias, macronutrientes, etc.")
    print()
    print("📁 ARQUIVOS GERADOS:")
    print("   • dados/dados_nutricionais.csv (resultado final)")
    print("   • dados/teste_um_produto.csv (teste individual)")
    print()
    print("⚙️ CONFIGURAÇÕES:")
    print("   • Modo headless para performance")
    print("   • Delays entre requisições")
    print("   • Valores 0 para campos não encontrados")
    print("   • Múltiplas estratégias de busca")

def main():
    """Função principal do menu"""
    print("🚀 Carregando sistema...")
    
    while True:
        try:
            exibir_menu()
            
            opcao = input("🔢 Digite sua opção: ").strip()
            
            if opcao == "0":
                print("\n👋 Encerrando sistema...")
                print("🙏 Obrigado por usar o Max Titanium Scraper!")
                break
                
            elif opcao == "1":
                urls_sucesso = coletar_urls()
                if urls_sucesso:
                    print("✅ URLs coletadas e salvas com sucesso!")
                else:
                    print("❌ Falha na coleta de URLs")
                
            elif opcao == "2":
                teste_produto()
                
            elif opcao == "3":
                coleta_completa()
                
            elif opcao == "4":
                coletar_dados_nutricionais()
                
            elif opcao == "5":
                exibir_informacoes()
                
            elif opcao == "6":
                teste_feedback()
                
            elif opcao == "7":
                testar_navegador()
                
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            if opcao != "0":
                input("\n⏸️  Pressione ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Operação cancelada pelo usuário")
            print("👋 Encerrando sistema...")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {str(e)}")
            input("\n⏸️  Pressione ENTER para continuar...")

if __name__ == "__main__":
    print("🏋️  MAX TITANIUM EUROPA SCRAPER")
    print(f"📅 Iniciado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    main() 