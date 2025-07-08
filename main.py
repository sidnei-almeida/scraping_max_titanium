#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 MAX TITANIUM EUROPA - Sistema de Coleta
==========================================
Sistema profissional para coleta de dados nutricionais dos produtos Max Titanium Europa

FUNCIONALIDADES:
• Coleta de URLs dos produtos
• Extração de dados nutricionais  
• Testes individuais e completos
• Interface visual elegante
"""

import os
import sys
import time
import glob
import subprocess
from datetime import datetime
from typing import List, Dict, Optional

# Adicionar pasta config ao path
config_path = os.path.join(os.path.dirname(__file__), 'config')
sys.path.append(config_path)

# ============================================================================
# 🎨 SISTEMA DE CORES ANSI PARA TERMINAL
# ============================================================================
class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    VERDE = '\033[92m'
    AZUL = '\033[94m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    CIANO = '\033[96m'
    MAGENTA = '\033[95m'
    BRANCO = '\033[97m'

# ============================================================================
# 🛠️ FUNÇÕES UTILITÁRIAS
# ============================================================================
def limpar_terminal():
    """Limpa o terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_banner():
    """Exibe o banner principal do programa"""
    banner = f"""
{Cores.CIANO}{Cores.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                  🏋️  MAX TITANIUM EUROPA                     ║
║                                                              ║
║              Sistema de Coleta de Dados v1.0                ║
║                                                              ║
║  🔗 Coleta URLs dos Produtos                                 ║
║  📊 Extrai Dados Nutricionais                                ║
║  🧪 Testes Individuais e Completos                           ║
╚══════════════════════════════════════════════════════════════╝
{Cores.RESET}"""
    print(banner)

def mostrar_barra_progresso(texto: str, duracao: float = 2.0):
    """Exibe uma barra de progresso animada"""
    print(f"\n{Cores.AMARELO}⏳ {texto}...{Cores.RESET}")
    barra_tamanho = 40
    for i in range(barra_tamanho + 1):
        progresso = i / barra_tamanho
        barra = "█" * i + "░" * (barra_tamanho - i)
        porcentagem = int(progresso * 100)
        print(f"\r{Cores.VERDE}[{barra}] {porcentagem}%{Cores.RESET}", end="", flush=True)
        time.sleep(duracao / barra_tamanho)
    print()

def mostrar_menu():
    """Exibe o menu principal"""
    menu = f"""
{Cores.AZUL}{Cores.BOLD}═══════════════════ MENU PRINCIPAL ═══════════════════{Cores.RESET}

{Cores.VERDE}🚀 OPERAÇÕES PRINCIPAIS:{Cores.RESET}
  {Cores.AMARELO}1.{Cores.RESET} 🔗 {Cores.BRANCO}Coletar URLs{Cores.RESET} - Coleta URLs dos produtos
  {Cores.AMARELO}2.{Cores.RESET} 🧪 {Cores.BRANCO}Teste Produto{Cores.RESET} - Teste individual de produto
  {Cores.AMARELO}3.{Cores.RESET} 🚀 {Cores.BRANCO}Coleta Completa{Cores.RESET} - URLs + Dados nutricionais
  {Cores.AMARELO}4.{Cores.RESET} 📊 {Cores.BRANCO}Dados Nutricionais{Cores.RESET} - Usar URLs existentes

{Cores.VERDE}📁 GERENCIAR DADOS:{Cores.RESET}
  {Cores.AMARELO}5.{Cores.RESET} 📋 {Cores.BRANCO}Ver Arquivos{Cores.RESET} - Lista arquivos gerados
  {Cores.AMARELO}6.{Cores.RESET} 🗑️  {Cores.BRANCO}Limpar Dados{Cores.RESET} - Remove arquivos antigos

{Cores.VERDE}🛠️ FERRAMENTAS:{Cores.RESET}
  {Cores.AMARELO}7.{Cores.RESET} 🎯 {Cores.BRANCO}Teste Feedback{Cores.RESET} - Teste visual de feedback
  {Cores.AMARELO}8.{Cores.RESET} 🌐 {Cores.BRANCO}Teste Navegador{Cores.RESET} - Verificar configuração

{Cores.VERDE}ℹ️  INFORMAÇÕES:{Cores.RESET}
  {Cores.AMARELO}9.{Cores.RESET} 📖 {Cores.BRANCO}Sobre o Sistema{Cores.RESET} - Informações e estatísticas
  {Cores.AMARELO}0.{Cores.RESET} ❌ {Cores.BRANCO}Sair{Cores.RESET} - Encerrar programa

{Cores.AZUL}══════════════════════════════════════════════════════{Cores.RESET}
"""
    print(menu)

def obter_escolha() -> str:
    """Obtém a escolha do usuário"""
    try:
        escolha = input(f"{Cores.MAGENTA}👉 Digite sua opção (0-9): {Cores.RESET}").strip()
        return escolha
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}⚠️  Programa interrompido pelo usuário{Cores.RESET}")
        sys.exit(0)

# ============================================================================
# 🎯 FUNÇÕES ESPECÍFICAS DO PROJETO MAX TITANIUM
# ============================================================================

def coletar_urls():
    """Executa coleta de URLs com feedback visual"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🔗 COLETANDO URLs DOS PRODUTOS{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.VERDE}✅ Configurações:{Cores.RESET}")
    print(f"   🌐 Site: {Cores.AMARELO}https://maxtitanium.eu{Cores.RESET}")
    print(f"   📊 Categorias: {Cores.AMARELO}Pré-treinos, Proteínas, Creatinas{Cores.RESET}")
    print(f"   🎯 Total esperado: {Cores.AMARELO}~20 produtos{Cores.RESET}")
    
    confirmar = input(f"\n{Cores.MAGENTA}🤔 Iniciar coleta de URLs? (s/N): {Cores.RESET}").lower()
    
    if confirmar in ['s', 'sim', 'y', 'yes']:
        try:
            mostrar_barra_progresso("Inicializando coleta de URLs", 1.5)
            
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
            
            print(f"\n{Cores.VERDE}🚀 Executando coleta...{Cores.RESET}")
            
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
                print(f"\n{Cores.VERDE}✅ Coleta de URLs concluída com sucesso!{Cores.RESET}")
                print(f"{Cores.CIANO}📁 Arquivo salvo em: dados/urls.csv{Cores.RESET}")
                return True
            else:
                print(f"\n{Cores.VERMELHO}❌ Erro na coleta de URLs:{Cores.RESET}")
                stderr = processo.stderr.read()
                if stderr:
                    print(stderr)
                return False
                
        except Exception as e:
            print(f"\n{Cores.VERMELHO}❌ Erro durante coleta de URLs: {str(e)}{Cores.RESET}")
            return False
    else:
        print(f"{Cores.AMARELO}⏭️  Operação cancelada{Cores.RESET}")
        return False

def teste_produto():
    """Executa teste em um produto específico"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🧪 TESTE DE PRODUTO INDIVIDUAL{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.AMARELO}ℹ️  INFORMAÇÕES:{Cores.RESET}")
    print(f"   • Este teste coleta dados de {Cores.VERDE}um produto específico{Cores.RESET}")
    print(f"   • Útil para verificar se a coleta está funcionando")
    print(f"   • Resultado salvo em: {Cores.CIANO}dados/teste_um_produto.csv{Cores.RESET}")
    
    confirmar = input(f"\n{Cores.MAGENTA}🤔 Executar teste? (s/N): {Cores.RESET}").lower()
    
    if confirmar in ['s', 'sim', 'y', 'yes']:
        try:
            mostrar_barra_progresso("Preparando teste", 1.0)
            
            processo = subprocess.Popen(
                [sys.executable, os.path.join(config_path, 'teste.py')],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=os.path.dirname(__file__)
            )
            
            print(f"\n{Cores.VERDE}🚀 Executando teste...{Cores.RESET}")
            
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
                print(f"\n{Cores.VERDE}✅ Teste concluído com sucesso!{Cores.RESET}")
                print(f"{Cores.CIANO}📁 Resultado salvo em: dados/teste_um_produto.csv{Cores.RESET}")
            else:
                print(f"\n{Cores.VERMELHO}❌ Teste falhou:{Cores.RESET}")
                stderr = processo.stderr.read()
                if stderr:
                    print(stderr)
                
        except Exception as e:
            print(f"\n{Cores.VERMELHO}❌ Erro durante teste: {str(e)}{Cores.RESET}")
    else:
        print(f"{Cores.AMARELO}⏭️  Operação cancelada{Cores.RESET}")

def coletar_dados_nutricionais():
    """Executa coleta de dados nutricionais"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}📊 COLETA DE DADOS NUTRICIONAIS{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.AMARELO}⚠️  ATENÇÃO:{Cores.RESET}")
    print(f"   • Esta operação usa as {Cores.VERDE}URLs já coletadas{Cores.RESET}")
    print(f"   • Pode demorar {Cores.VERMELHO}vários minutos{Cores.RESET}")
    print(f"   • Coleta informações nutricionais completas")
    
    confirmar = input(f"\n{Cores.MAGENTA}🤔 Continuar com a coleta? (s/N): {Cores.RESET}").lower()
    
    if confirmar in ['s', 'sim', 'y', 'yes']:
        try:
            mostrar_barra_progresso("Preparando coleta de dados", 1.5)
            
            processo = subprocess.Popen(
                [sys.executable, os.path.join(config_path, 'coleta.py')],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=os.path.dirname(__file__)
            )
            
            print(f"\n{Cores.VERDE}🚀 Coletando dados nutricionais...{Cores.RESET}")
            
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
                print(f"\n{Cores.VERDE}✅ Coleta de dados nutricionais concluída!{Cores.RESET}")
                print(f"{Cores.CIANO}📁 Resultado salvo em: dados/dados_nutricionais.csv{Cores.RESET}")
            else:
                print(f"\n{Cores.VERMELHO}❌ Falha na coleta de dados nutricionais:{Cores.RESET}")
                stderr = processo.stderr.read()
                if stderr:
                    print(stderr)
                
        except Exception as e:
            print(f"\n{Cores.VERMELHO}❌ Erro durante coleta de dados: {str(e)}{Cores.RESET}")
    else:
        print(f"{Cores.AMARELO}⏭️  Operação cancelada{Cores.RESET}")

def coleta_completa():
    """Executa fluxo completo: URLs + Dados Nutricionais"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🚀 COLETA COMPLETA - PROCESSO TOTAL{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.VERDE}📋 ETAPAS DO PROCESSO:{Cores.RESET}")
    print(f"   {Cores.AMARELO}1.{Cores.RESET} Coleta de URLs dos produtos")
    print(f"   {Cores.AMARELO}2.{Cores.RESET} Extração de dados nutricionais")
    
    print(f"\n{Cores.AMARELO}⚠️  TEMPO ESTIMADO: {Cores.VERMELHO}10-15 minutos{Cores.RESET}")
    
    confirmar = input(f"\n{Cores.MAGENTA}🤔 Iniciar processo completo? (s/N): {Cores.RESET}").lower()
    
    if confirmar in ['s', 'sim', 'y', 'yes']:
        # Etapa 1: Coletar URLs
        print(f"\n{Cores.CIANO}📍 ETAPA 1/2: Coletando URLs dos produtos...{Cores.RESET}")
        urls_sucesso = coletar_urls()
        
        if not urls_sucesso:
            print(f"{Cores.VERMELHO}❌ Coleta completa cancelada - falha na coleta de URLs{Cores.RESET}")
            return
        
        # Pausa entre etapas
        print(f"\n{Cores.AMARELO}⏱️  Aguardando 3 segundos antes da próxima etapa...{Cores.RESET}")
        time.sleep(3)
        
        # Etapa 2: Coletar dados nutricionais
        print(f"\n{Cores.CIANO}📍 ETAPA 2/2: Coletando dados nutricionais...{Cores.RESET}")
        coletar_dados_nutricionais()
        
        print(f"\n{Cores.VERDE}🎉 COLETA COMPLETA FINALIZADA!{Cores.RESET}")
        print(f"{Cores.VERDE}🏆 Todos os dados foram coletados e salvos com sucesso!{Cores.RESET}")
    else:
        print(f"{Cores.AMARELO}⏭️  Operação cancelada{Cores.RESET}")

def listar_arquivos_gerados():
    """Lista arquivos gerados pelo programa"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}📋 ARQUIVOS GERADOS{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    pasta_dados = "dados"
    
    if not os.path.exists(pasta_dados):
        print(f"{Cores.AMARELO}📁 Pasta '{pasta_dados}' não encontrada{Cores.RESET}")
        return
    
    arquivos = glob.glob(f"{pasta_dados}/*.csv")
    
    if not arquivos:
        print(f"{Cores.AMARELO}📄 Nenhum arquivo CSV encontrado em '{pasta_dados}'{Cores.RESET}")
        return
    
    print(f"\n{Cores.VERDE}📊 Total de arquivos: {len(arquivos)}{Cores.RESET}\n")
    
    for i, arquivo in enumerate(sorted(arquivos, reverse=True), 1):
        nome_arquivo = os.path.basename(arquivo)
        tamanho = os.path.getsize(arquivo)
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(arquivo))
        
        # Calcula o tamanho em formato legível
        if tamanho < 1024:
            tamanho_str = f"{tamanho} B"
        elif tamanho < 1024 * 1024:
            tamanho_str = f"{tamanho / 1024:.1f} KB"
        else:
            tamanho_str = f"{tamanho / (1024 * 1024):.1f} MB"
        
        print(f"{Cores.AMARELO}{i:2d}.{Cores.RESET} {Cores.BRANCO}{nome_arquivo}{Cores.RESET}")
        print(f"     📅 {data_modificacao.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"     📏 {tamanho_str}")
        print()

def limpar_dados_antigos():
    """Remove arquivos antigos"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🗑️  LIMPAR DADOS ANTIGOS{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    pasta_dados = "dados"
    
    if not os.path.exists(pasta_dados):
        print(f"{Cores.AMARELO}📁 Pasta '{pasta_dados}' não encontrada{Cores.RESET}")
        return
    
    arquivos = glob.glob(f"{pasta_dados}/*.csv")
    
    if not arquivos:
        print(f"{Cores.VERDE}✅ Nenhum arquivo para limpar{Cores.RESET}")
        return
    
    print(f"\n{Cores.AMARELO}⚠️  ATENÇÃO:{Cores.RESET}")
    print(f"   • Serão removidos {Cores.VERMELHO}{len(arquivos)} arquivos CSV{Cores.RESET}")
    print(f"   • Esta ação {Cores.VERMELHO}NÃO PODE ser desfeita{Cores.RESET}")
    
    # Listar arquivos que serão removidos
    print(f"\n{Cores.CIANO}📄 Arquivos que serão removidos:{Cores.RESET}")
    for arquivo in arquivos:
        print(f"   • {Cores.BRANCO}{os.path.basename(arquivo)}{Cores.RESET}")
    
    confirmar = input(f"\n{Cores.MAGENTA}🤔 Tem certeza? Digite 'CONFIRMAR' para prosseguir: {Cores.RESET}")
    
    if confirmar == "CONFIRMAR":
        try:
            mostrar_barra_progresso("Removendo arquivos", 1.0)
            for arquivo in arquivos:
                os.remove(arquivo)
            print(f"\n{Cores.VERDE}✅ {len(arquivos)} arquivos removidos com sucesso!{Cores.RESET}")
        except Exception as e:
            print(f"\n{Cores.VERMELHO}❌ Erro ao remover arquivos: {e}{Cores.RESET}")
    else:
        print(f"{Cores.AMARELO}⏭️  Operação cancelada{Cores.RESET}")

def teste_feedback():
    """Testa o feedback visual em tempo real"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🎯 TESTE DE FEEDBACK VISUAL{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.VERDE}📋 OPÇÕES DE TESTE:{Cores.RESET}")
    print(f"   {Cores.AMARELO}1.{Cores.RESET} Simular coleta de URLs")
    print(f"   {Cores.AMARELO}2.{Cores.RESET} Simular coleta de dados nutricionais")
    
    opcao = input(f"\n{Cores.MAGENTA}👉 Escolha uma opção (1-2): {Cores.RESET}").strip()
    
    try:
        if opcao == "1":
            mostrar_barra_progresso("Preparando teste de URLs", 1.0)
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
            mostrar_barra_progresso("Preparando teste de dados", 1.0)
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
            print(f"{Cores.VERMELHO}❌ Opção inválida{Cores.RESET}")
            return
        
        # Ler saída em tempo real
        while True:
            output = processo.stdout.readline()
            if output == '' and processo.poll() is not None:
                break
            if output:
                print(output.strip())
        
        processo.wait()
        print(f"\n{Cores.VERDE}✅ Teste de feedback concluído!{Cores.RESET}")
        
    except Exception as e:
        print(f"\n{Cores.VERMELHO}❌ Erro no teste: {str(e)}{Cores.RESET}")

def testar_navegador():
    """Testa a configuração do navegador"""
    print(f"\n{Cores.CIANO}{Cores.BOLD}🌐 TESTE DE CONFIGURAÇÃO DO NAVEGADOR{Cores.RESET}")
    print(f"{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}")
    
    print(f"\n{Cores.VERDE}🔧 Verificando:{Cores.RESET}")
    print(f"   • Selenium WebDriver")
    print(f"   • Chrome/Chromium")
    print(f"   • Conectividade com o site")
    
    try:
        mostrar_barra_progresso("Executando testes", 1.5)
        
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
            print(f"\n{Cores.VERDE}✅ Configuração do navegador está funcionando!{Cores.RESET}")
        else:
            print(f"\n{Cores.VERMELHO}❌ Problemas na configuração do navegador:{Cores.RESET}")
            stderr = processo.stderr.read()
            if stderr:
                print(stderr)
        
    except Exception as e:
        print(f"\n{Cores.VERMELHO}❌ Erro no teste do navegador: {str(e)}{Cores.RESET}")

def mostrar_sobre():
    """Exibe informações sobre o programa"""
    sobre = f"""
{Cores.CIANO}{Cores.BOLD}📖 SOBRE O MAX TITANIUM EUROPA SCRAPER{Cores.RESET}
{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}

{Cores.VERDE}🎯 OBJETIVO:{Cores.RESET}
   Coletar dados nutricionais completos dos produtos Max Titanium Europa
   para análise, comparação e pesquisa de suplementos

{Cores.VERDE}🌐 SITE ALVO:{Cores.RESET}
   https://maxtitanium.eu

{Cores.VERDE}📊 FUNCIONALIDADES:{Cores.RESET}
   • Coleta automática de URLs dos produtos
   • Extração de informações nutricionais detalhadas  
   • Teste individual de produtos
   • Interface visual profissional
   • Gerenciamento de arquivos de dados

{Cores.VERDE}🛠️  TECNOLOGIAS:{Cores.RESET}
   • Python 3.8+
   • Selenium WebDriver
   • BeautifulSoup
   • Chrome (modo headless)

{Cores.VERDE}📋 CATEGORIAS COLETADAS:{Cores.RESET}
   • Pré-treinos (7 produtos)
   • Proteínas (9 produtos) 
   • Creatinas e Aminoácidos (4 produtos)
   • Total: ~20 produtos únicos

{Cores.VERDE}📂 ARQUIVOS GERADOS:{Cores.RESET}
   • Formato: CSV (Excel compatível)
   • Localização: dados/
   • Principais: dados_nutricionais.csv, urls.csv

{Cores.VERDE}⚡ CARACTERÍSTICAS:{Cores.RESET}
   • Modo headless para melhor performance
   • Delays inteligentes entre requisições
   • Múltiplas estratégias de busca
   • Tratamento robusto de erros
   • Feedback visual em tempo real

{Cores.VERDE}📝 DESENVOLVIDO POR:{Cores.RESET}
   • Sistema de Scraping Max Titanium
   • Versão: 1.0
   • Data: {datetime.now().strftime('%B %Y')}

{Cores.AZUL}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Cores.RESET}
"""
    print(sobre)

def pausar():
    """Pausa o programa aguardando input do usuário"""
    input(f"\n{Cores.CIANO}⏯️  Pressione Enter para continuar...{Cores.RESET}")

# ============================================================================
# 🚀 FUNÇÃO PRINCIPAL
# ============================================================================
def main():
    """Função principal do programa"""
    try:
        while True:
            limpar_terminal()
            mostrar_banner()
            mostrar_menu()
            
            escolha = obter_escolha()
            
            if escolha == "1":
                coletar_urls()
                pausar()
                
            elif escolha == "2":
                teste_produto()
                pausar()
                
            elif escolha == "3":
                coleta_completa()
                pausar()
                
            elif escolha == "4":
                coletar_dados_nutricionais()
                pausar()
                
            elif escolha == "5":
                listar_arquivos_gerados()
                pausar()
                
            elif escolha == "6":
                limpar_dados_antigos()
                pausar()
                
            elif escolha == "7":
                teste_feedback()
                pausar()
                
            elif escolha == "8":
                testar_navegador()
                pausar()
                
            elif escolha == "9":
                mostrar_sobre()
                pausar()
                
            elif escolha == "0":
                print(f"\n{Cores.VERDE}👋 Obrigado por usar o Max Titanium Europa Scraper!{Cores.RESET}")
                print(f"{Cores.CIANO}🚀 Até a próxima!{Cores.RESET}\n")
                break
                
            else:
                print(f"\n{Cores.VERMELHO}❌ Opção inválida! Por favor, escolha entre 0-9{Cores.RESET}")
                time.sleep(2)
                
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}👋 Programa encerrado pelo usuário. Até logo!{Cores.RESET}\n")
    except Exception as e:
        print(f"\n{Cores.VERMELHO}❌ Erro inesperado: {e}{Cores.RESET}")

if __name__ == "__main__":
    print(f"{Cores.CIANO}🏋️  MAX TITANIUM EUROPA SCRAPER{Cores.RESET}")
    print(f"{Cores.VERDE}📅 Iniciado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}{Cores.RESET}")
    main() 