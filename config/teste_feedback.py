#!/usr/bin/env python3
"""
Teste de feedback visual em tempo real
"""
import time
import sys

def simular_coleta_urls():
    """Simula coleta de URLs com feedback"""
    print("🚀 Iniciando coleta de URLs dos produtos Max Titanium Europa...", flush=True)
    print("=" * 60, flush=True)
    
    categorias = [
        ("Pré-treinos", "https://maxtitanium.eu/collections/pre-treinos", 7),
        ("Proteínas", "https://maxtitanium.eu/collections/proteinas", 9),
        ("Creatinas e Aminoácidos", "https://maxtitanium.eu/collections/creatinas-e-aminoacidos", 4)
    ]
    
    todas_urls = []
    
    for categoria, url, quantidade in categorias:
        print(f"\n=== COLETANDO: {categoria} ===", flush=True)
        print(f"URL: {url}", flush=True)
        
        time.sleep(1)
        
        for i in range(quantidade):
            produto = f"Produto {i+1}"
            print(f"    → Extraindo: {produto}", flush=True)
            todas_urls.append(f"{url}/produto-{i+1}")
            time.sleep(0.5)
        
        print(f"    → ✅ {quantidade} produtos coletados de {categoria}", flush=True)
    
    print(f"\n📊 RESUMO FINAL:", flush=True)
    print(f"Total de URLs coletadas: {len(todas_urls)}", flush=True)
    print("✅ Coleta de URLs concluída!", flush=True)

def simular_coleta_dados():
    """Simula coleta de dados nutricionais com feedback"""
    print("🚀 Iniciando coleta de dados nutricionais...", flush=True)
    print("=" * 60, flush=True)
    
    produtos = [
        "Top Whey 3W +Sabor 900g - Brigadeiro",
        "100% Whey Protein 900g - Baunilha",
        "Horus Pre-Treino 300g - Blue Ice",
        "Creatina Monohidratada 300g"
    ]
    
    print(f"📋 Processando {len(produtos)} produtos", flush=True)
    
    for i, produto in enumerate(produtos, 1):
        print(f"\n[{i}/{len(produtos)}]", flush=True)
        print(f"🔗 Processando: https://maxtitanium.eu/produto-{i}", flush=True)
        print(f"📦 Produto: {produto}", flush=True)
        
        time.sleep(2)
        
        print(f"⏱️  Aguardando página carregar...", flush=True)
        time.sleep(1)
        
        print(f"🔍 Procurando tabela nutricional...", flush=True)
        time.sleep(1)
        
        print(f"✅ Dados extraídos: 150kcal, 30g proteína", flush=True)
        time.sleep(1)
    
    print(f"\n✅ Coleta de dados concluída!", flush=True)
    print(f"📁 Arquivo salvo: dados/dados_nutricionais.csv", flush=True)

def main():
    """Função principal"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "urls":
            simular_coleta_urls()
        elif sys.argv[1] == "dados":
            simular_coleta_dados()
    else:
        print("Uso: python teste_feedback.py [urls|dados]")

if __name__ == "__main__":
    main() 