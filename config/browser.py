#!/usr/bin/env python3
"""
🌐 Browser Configuration Module
Detecta e configura automaticamente o WebDriver para Chrome/Chromium
Compatível com Linux e Windows
"""

import os
import sys
import platform
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserDetector:
    """Classe para detectar e configurar navegadores automaticamente"""
    
    def __init__(self):
        self.sistema = platform.system().lower()
        self.navegador_encontrado = None
        self.caminho_navegador = None
        self.driver_path = None
        
    def detectar_navegador(self):
        """Detecta qual navegador está disponível no sistema"""
        print("🔍 Detectando navegador disponível...", flush=True)
        
        # Lista de possíveis executáveis por sistema
        if self.sistema == "linux":
            navegadores = [
                ("Google Chrome", ["google-chrome", "google-chrome-stable", "chrome"]),
                ("Chromium", ["chromium", "chromium-browser", "chromium-bin"])
            ]
        elif self.sistema == "windows":
            navegadores = [
                ("Google Chrome", ["chrome.exe", "chrome"]),
                ("Chromium", ["chromium.exe", "chromium"])
            ]
        else:
            # macOS ou outros
            navegadores = [
                ("Google Chrome", ["google-chrome", "chrome"]),
                ("Chromium", ["chromium", "chromium-browser"])
            ]
        
        # Procurar por navegadores instalados
        for nome, executaveis in navegadores:
            for executavel in executaveis:
                caminho = shutil.which(executavel)
                if caminho:
                    self.navegador_encontrado = nome
                    self.caminho_navegador = caminho
                    print(f"✅ {nome} encontrado em: {caminho}", flush=True)
                    return True
        
        # Se não encontrou, tentar caminhos padrão do Windows
        if self.sistema == "windows":
            caminhos_windows = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files\Chromium\Application\chromium.exe",
                r"C:\Program Files (x86)\Chromium\Application\chromium.exe"
            ]
            
            for caminho in caminhos_windows:
                caminho_expandido = os.path.expandvars(caminho)
                if os.path.exists(caminho_expandido):
                    if "chrome" in caminho.lower():
                        self.navegador_encontrado = "Google Chrome"
                    else:
                        self.navegador_encontrado = "Chromium"
                    self.caminho_navegador = caminho_expandido
                    print(f"✅ {self.navegador_encontrado} encontrado em: {caminho_expandido}", flush=True)
                    return True
        
        print("❌ Nenhum navegador compatível encontrado!", flush=True)
        return False
    
    def configurar_opcoes(self, headless=True, zoom=100):
        """Configura as opções do Chrome/Chromium"""
        options = Options()
        
        # Opções básicas
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")
        options.add_argument("--disable-javascript")
        options.add_argument("--window-size=1920,1080")
        
        # Configurar zoom
        if zoom != 100:
            zoom_factor = zoom / 100
            options.add_argument(f"--force-device-scale-factor={zoom_factor}")
        
        # Modo headless
        if headless:
            options.add_argument("--headless")
        
        # Configurar caminho do navegador se encontrado
        if self.caminho_navegador:
            options.binary_location = self.caminho_navegador
        
        # Configurações específicas do sistema
        if self.sistema == "linux":
            options.add_argument("--disable-software-rasterizer")
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-backgrounding-occluded-windows")
            options.add_argument("--disable-renderer-backgrounding")
        
        elif self.sistema == "windows":
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-backgrounding-occluded-windows")
            options.add_argument("--disable-renderer-backgrounding")
        
        return options
    
    def detectar_chromedriver(self):
        """Detecta o ChromeDriver disponível"""
        print("🔍 Procurando ChromeDriver...", flush=True)
        
        # Tentar encontrar chromedriver no PATH
        driver_executaveis = ["chromedriver", "chromedriver.exe"]
        
        for executavel in driver_executaveis:
            caminho = shutil.which(executavel)
            if caminho:
                self.driver_path = caminho
                print(f"✅ ChromeDriver encontrado em: {caminho}", flush=True)
                return True
        
        # Caminhos padrão para Windows
        if self.sistema == "windows":
            caminhos_windows = [
                r"C:\chromedriver\chromedriver.exe",
                r"C:\WebDrivers\chromedriver.exe",
                r"C:\Program Files\chromedriver\chromedriver.exe",
                r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
            ]
            
            for caminho in caminhos_windows:
                if os.path.exists(caminho):
                    self.driver_path = caminho
                    print(f"✅ ChromeDriver encontrado em: {caminho}", flush=True)
                    return True
        
        print("⚠️ ChromeDriver não encontrado no PATH", flush=True)
        print("💡 Tentando usar ChromeDriver padrão do Selenium...", flush=True)
        return False
    
    def criar_driver(self, headless=True, zoom=100):
        """Cria e retorna uma instância do WebDriver configurada"""
        print("🚀 Configurando WebDriver...", flush=True)
        
        # Detectar navegador
        if not self.detectar_navegador():
            raise Exception("❌ Nenhum navegador compatível encontrado. Instale Google Chrome ou Chromium.")
        
        # Configurar opções
        options = self.configurar_opcoes(headless=headless, zoom=zoom)
        
        # Detectar ChromeDriver
        self.detectar_chromedriver()
        
        try:
            # Tentar criar driver com caminho específico
            if self.driver_path:
                service = Service(self.driver_path)
                driver = webdriver.Chrome(service=service, options=options)
            else:
                # Usar driver padrão do Selenium
                driver = webdriver.Chrome(options=options)
            
            print(f"✅ WebDriver criado com sucesso!", flush=True)
            print(f"📱 Navegador: {self.navegador_encontrado}", flush=True)
            print(f"🖥️ Sistema: {self.sistema.title()}", flush=True)
            print(f"👁️ Modo: {'Headless' if headless else 'Visual'}", flush=True)
            print(f"🔍 Zoom: {zoom}%", flush=True)
            
            return driver
            
        except Exception as e:
            print(f"❌ Erro ao criar WebDriver: {str(e)}", flush=True)
            
            # Tentar novamente sem caminho específico
            if self.driver_path:
                print("🔄 Tentando sem caminho específico do driver...", flush=True)
                try:
                    driver = webdriver.Chrome(options=options)
                    print("✅ WebDriver criado com sucesso (método alternativo)!", flush=True)
                    return driver
                except Exception as e2:
                    print(f"❌ Erro no método alternativo: {str(e2)}", flush=True)
            
            raise Exception(f"❌ Falha ao criar WebDriver: {str(e)}")
    
    def info_sistema(self):
        """Retorna informações sobre o sistema"""
        info = {
            'sistema': self.sistema,
            'navegador': self.navegador_encontrado,
            'caminho_navegador': self.caminho_navegador,
            'driver_path': self.driver_path,
            'python_version': sys.version,
            'platform': platform.platform()
        }
        return info

# Funções de conveniência
def criar_driver_automatico(headless=True, zoom=100):
    """Cria um driver automaticamente detectando o navegador"""
    detector = BrowserDetector()
    return detector.criar_driver(headless=headless, zoom=zoom)

def testar_configuracao():
    """Testa a configuração do navegador"""
    print("🧪 TESTANDO CONFIGURAÇÃO DO NAVEGADOR")
    print("=" * 50)
    
    detector = BrowserDetector()
    
    # Mostrar informações do sistema
    print(f"🖥️ Sistema Operacional: {detector.sistema.title()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"🌐 Plataforma: {platform.platform()}")
    
    try:
        # Tentar criar driver
        driver = detector.criar_driver(headless=True, zoom=100)
        
        # Testar navegação
        print("\n🔍 Testando navegação...", flush=True)
        driver.get("https://www.google.com")
        
        # Verificar se a página carregou
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        titulo = driver.title
        print(f"✅ Página carregada: {titulo}", flush=True)
        
        # Fechar driver
        driver.quit()
        print("✅ Teste concluído com sucesso!", flush=True)
        
        # Mostrar informações finais
        info = detector.info_sistema()
        print(f"\n📋 CONFIGURAÇÃO FINAL:")
        print(f"  • Navegador: {info['navegador']}")
        print(f"  • Caminho: {info['caminho_navegador']}")
        print(f"  • Driver: {info['driver_path'] or 'Padrão do Selenium'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {str(e)}", flush=True)
        return False

if __name__ == "__main__":
    # Executar teste se chamado diretamente
    testar_configuracao() 