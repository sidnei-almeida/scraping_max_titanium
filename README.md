# Scraping Max Titanium Europa

Sistema de scraping para coleta de dados nutricionais dos produtos Max Titanium do site europeu.

## 🎯 Objetivo

Coletar informações nutricionais de todos os produtos das categorias:
- **Pré-treinos** (7 produtos)
- **Proteínas** (9 produtos) 
- **Creatinas e Aminoácidos** (4 produtos)

Total: **20 produtos** únicos

## 📁 Estrutura do Projeto

```
scraping_max_titanium/
├── config/                          # Scripts funcionais principais
│   ├── coletar_dados_nutricionais_final.py  # Script principal
│   ├── teste_um_produto.py                  # Script de teste
│   ├── coletor_urls_europa_estrutura_real.py # Coletor de URLs
│   ├── requirements.txt                     # Dependências
│   └── README.md                           # Documentação detalhada
├── dados/                           # Arquivos de dados
│   ├── urls_produtos_europa_estrutura_real.csv  # URLs coletadas
│   ├── teste_um_produto.csv                    # Resultado do teste
│   └── dados_nutricionais.csv                 # Resultado final
├── venv/                           # Ambiente virtual Python
├── README.md                       # Este arquivo
└── requirements.txt               # Dependências do projeto
```

## 🚀 Início Rápido

### 1. Ativar Ambiente Virtual
```bash
source venv/bin/activate
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar Scripts

**Testar um produto:**
```bash
python config/teste_um_produto.py
```

**Processar todos os produtos:**
```bash
python config/coletar_dados_nutricionais_final.py
```

**Coletar URLs (se necessário):**
```bash
python config/coletor_urls_europa_estrutura_real.py
```

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

- **Python 3.13+**
- **Selenium** - Automação web e JavaScript
- **BeautifulSoup** - Parsing HTML
- **Chrome WebDriver** - Navegador automatizado
- **CSV** - Formato de saída dos dados

## ✨ Características

### Scripts Principais (/config)
- ✅ **Busca inteligente** pelo dropdown "Informação Nutricional"
- ✅ **Scroll automático** até encontrar elementos
- ✅ **Clique via JavaScript** para evitar interceptação
- ✅ **Múltiplas estratégias** de localização de elementos
- ✅ **Valores padrão 0** quando dados não encontrados
- ✅ **Tratamento robusto de erros**
- ✅ **Modo headless** para performance

### Dados Coletados
- ✅ **20 produtos únicos** de 3 categorias
- ✅ **Informações nutricionais completas**
- ✅ **CSV estruturado** pronto para análise
- ✅ **URLs organizadas** por categoria

## 🏗️ Desenvolvimento

### Histórico do Projeto
1. **Coleta de URLs** - Desenvolvido coletor específico para o site europeu
2. **Testes de scraping** - Múltiplas versões testadas para diferentes abordagens
3. **Problema de dropdown** - Identificado que tabelas estão em dropdowns JavaScript
4. **Solução Selenium** - Implementado clique automático e scroll inteligente
5. **Organização final** - Scripts funcionais organizados em `/config`

### Melhorias Implementadas
- **Interceptação resolvida**: Clique via JavaScript em vez de clique direto
- **Busca robusta**: Múltiplas estratégias de localização de elementos
- **Scroll inteligente**: Busca automática em toda a página
- **Valores consistentes**: 0 para campos não encontrados
- **Documentação completa**: READMEs detalhados

## 📝 Observações

- Scripts testados e funcionais em **05/07/2025**
- Compatível com **Linux (CachyOS)** e **Fish Shell**
- Site alvo: **maxtitanium.eu** (versão europeia)
- Dados extraídos das **tabelas nutricionais oficiais**
- Respeita **delays** para não sobrecarregar o servidor

## 📖 Documentação Detalhada

Para instruções completas, configurações e troubleshooting, consulte:
**[config/README.md](config/README.md)**

---

**Desenvolvido para coleta automatizada de dados nutricionais Max Titanium Europa** 🥇
