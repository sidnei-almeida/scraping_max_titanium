# 🏋️ Scraping Max Titanium Europa

Sistema de scraping automatizado para coleta de dados nutricionais de produtos Max Titanium do site europeu com menu interativo e detecção automática de navegador.

## 🎯 Objetivo

Coletar informações nutricionais completas de todos os produtos das categorias:
- **Pré-treinos** (7 produtos)
- **Proteínas** (9 produtos) 
- **Creatinas e Aminoácidos** (4 produtos)

**Total: 20 produtos únicos**

## 🚀 Início Rápido

### 1. Ativar Ambiente Virtual
```bash
source venv/bin/activate
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar Sistema
```bash
python main.py
```

## 📋 Menu Interativo

O sistema oferece um menu principal com 7 opções:

```
🏋️  MAX TITANIUM EUROPA - SISTEMA DE COLETA

1️⃣  🔗 Coletar URLs dos Produtos
2️⃣  🧪 Teste de Um Produto
3️⃣  🚀 Coleta Completa (URLs + Dados Nutricionais)
4️⃣  📊 Apenas Dados Nutricionais (usar URLs existentes)
5️⃣  📖 Informações do Sistema
6️⃣  🎯 Teste de Feedback Visual
7️⃣  🌐 Testar Configuração do Navegador
0️⃣  ❌ Sair
```

## 📁 Estrutura do Projeto

```
scraping_max_titanium/
├── main.py                      # 🚀 Menu principal interativo
├── config/                      # 📂 Módulos e scripts funcionais
│   ├── browser.py               # 🌐 Detecção automática de navegador
│   ├── urls.py                  # 🔗 Coletor de URLs
│   ├── teste.py                 # 🧪 Teste de um produto
│   ├── coleta.py                # 📊 Coleta de dados nutricionais
│   ├── teste_feedback.py        # 🎯 Teste de feedback visual
│   ├── requirements.txt         # 📦 Dependências
│   └── README.md               # 📖 Documentação detalhada
├── dados/                       # 📁 Arquivos de dados
│   ├── urls_produtos_europa_estrutura_real.csv  # URLs coletadas
│   ├── teste_um_produto.csv                     # Resultado do teste
│   └── dados_nutricionais.csv                   # Resultado final
├── venv/                        # 🐍 Ambiente virtual Python
├── .gitignore                   # 🚫 Arquivos ignorados
└── requirements.txt             # 📦 Dependências do projeto
```

## 🌐 Detecção Automática de Navegador

O sistema detecta automaticamente navegadores compatíveis:

### Navegadores Suportados
- **Google Chrome** (preferido)
- **Chromium** (alternativo)

### Sistemas Operacionais
- ✅ **Linux** (testado em CachyOS)
- ✅ **Windows** (caminhos padrão)
- ✅ **macOS** (suporte básico)

### Recursos Automáticos
- 🔍 **Detecção de navegador** no PATH do sistema
- 🚗 **Configuração automática** do ChromeDriver
- ⚙️ **Otimizações por sistema** operacional
- 🎛️ **Zoom configurável** (25% para coleta de URLs)
- 👻 **Modo headless** para performance

## 📊 Dados Coletados

### Estrutura do CSV Final
| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| NOME_PRODUTO | Nome completo do produto | Top Whey 3W +Sabor 900g - Brigadeiro |
| URL | Link direto do produto | https://maxtitanium.eu/products/... |
| CATEGORIA | Categoria do produto | Proteínas |
| PORCAO (g) | Tamanho da porção em gramas | 40 |
| CALORIAS (kcal) | Valor energético | 163 |
| CARBOIDRATOS (g) | Carboidratos totais | 4.3 |
| PROTEINAS (g) | Proteínas | 32 |
| GORDURAS_TOTAIS (g) | Gorduras totais | 2.0 |
| GORDURAS_SATURADAS (g) | Gorduras saturadas | 1.1 |
| FIBRAS (g) | Fibras alimentares | 0 |
| ACUCARES (g) | Açúcares | 0 |
| SODIO (mg) | Sódio em miligramas | 73 |

## 🔧 Tecnologias

- **Python 3.13+** - Linguagem principal
- **Selenium** - Automação web e JavaScript
- **BeautifulSoup** - Parsing HTML
- **WebDriver Manager** - Gerenciamento automático de drivers
- **Chrome/Chromium** - Navegador automatizado
- **CSV** - Formato de saída dos dados

## ✨ Características Avançadas

### 🎯 Busca Inteligente
- ✅ **Múltiplas estratégias** de localização de elementos
- ✅ **Scroll automático** até encontrar dropdowns
- ✅ **Clique via JavaScript** para evitar interceptação
- ✅ **Busca por conteúdo** em elementos `<h2>` e `<summary>`
- ✅ **Varredura completa** da página como último recurso

### 📱 Feedback Visual
- ✅ **Progresso em tempo real** durante coleta
- ✅ **Contadores de produtos** processados
- ✅ **Mensagens informativas** detalhadas
- ✅ **Indicadores de sucesso/erro** coloridos
- ✅ **Estimativa de tempo** restante

### 🛡️ Tratamento de Erros
- ✅ **Valores padrão 0** quando dados não encontrados
- ✅ **Múltiplas tentativas** de localização
- ✅ **Logs detalhados** de debugging
- ✅ **Continuidade** mesmo com falhas individuais
- ✅ **Recuperação automática** de erros temporários

### 🚀 Performance
- ✅ **Modo headless** para velocidade
- ✅ **Desabilitação** de imagens e plugins
- ✅ **Otimizações** específicas por sistema
- ✅ **Delays inteligentes** entre requisições
- ✅ **Reutilização** de sessões do navegador

## 🔍 Casos de Uso

### 1️⃣ Coleta Completa (Recomendado)
```bash
python main.py
# Escolher opção 3: Coleta Completa
```
- Coleta URLs primeiro
- Depois coleta dados nutricionais
- Processo automatizado completo

### 2️⃣ Teste Individual
```bash
python main.py
# Escolher opção 2: Teste de Um Produto
```
- Testa um produto específico
- Útil para debugging
- Salva resultado em CSV separado

### 3️⃣ Apenas URLs
```bash
python main.py
# Escolher opção 1: Coletar URLs
```
- Coleta apenas URLs dos produtos
- Útil para verificar produtos disponíveis

### 4️⃣ Apenas Dados Nutricionais
```bash
python main.py
# Escolher opção 4: Apenas Dados Nutricionais
```
- Usa URLs já coletadas
- Extrai apenas informações nutricionais

## 🔧 Execução Manual (Desenvolvimento)

### Scripts Individuais
```bash
# Coletar URLs
python config/urls.py

# Testar um produto
python config/teste.py

# Coleta completa de dados
python config/coleta.py

# Testar navegador
python config/browser.py
```

## 🏗️ Desenvolvimento

### Histórico de Melhorias
1. **v1.0** - Scripts básicos com BeautifulSoup
2. **v2.0** - Migração para Selenium por causa de JavaScript
3. **v3.0** - Implementação de múltiplas estratégias de busca
4. **v4.0** - Adição de menu interativo e feedback visual
5. **v5.0** - Detecção automática de navegador multiplataforma

### Problemáticas Resolvidas
- ❌ **Dropdowns não encontrados** → ✅ Múltiplas estratégias de busca
- ❌ **Cliques interceptados** → ✅ Execução via JavaScript
- ❌ **Elementos não visíveis** → ✅ Scroll automático inteligente
- ❌ **Configuração manual** → ✅ Detecção automática de navegador
- ❌ **Feedback limitado** → ✅ Progresso em tempo real

## 📖 Documentação Avançada

Para configurações detalhadas, troubleshooting e desenvolvimento:
**[config/README.md](config/README.md)**

## 📝 Observações Técnicas

- ✅ **Testado em Linux CachyOS** com Fish Shell
- ✅ **Compatível com Windows** e macOS
- ✅ **Site alvo**: maxtitanium.eu (versão europeia)
- ✅ **Dados oficiais** extraídos das tabelas nutricionais
- ✅ **Respeita delays** para não sobrecarregar servidor
- ✅ **OCR-free** - extração direta do HTML

## 🎯 Próximos Passos

- [ ] Suporte a mais navegadores (Firefox, Edge)
- [ ] Interface web para visualização de dados
- [ ] Notificações quando novos produtos são adicionados
- [ ] Integração com APIs de nutrição
- [ ] Exportação em múltiplos formatos (JSON, Excel)

---

**🏆 Sistema completo de scraping Max Titanium Europa**
