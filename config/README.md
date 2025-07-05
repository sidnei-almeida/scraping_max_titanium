# Scripts de Scraping Max Titanium Europa

Esta pasta contém os scripts finais e funcionais para coleta de dados dos produtos Max Titanium Europa.

## 📋 Scripts Principais

### 1. `coletar_dados_nutricionais_final.py`
**Script principal para coleta de dados nutricionais**

- **Função**: Processa todos os produtos das URLs coletadas
- **Entrada**: `dados/urls_produtos_europa_estrutura_real.csv`
- **Saída**: `dados/dados_nutricionais.csv`
- **Recursos**:
  - Busca inteligente pelo dropdown "Informação Nutricional"
  - Scroll automático até encontrar o elemento
  - Clique via JavaScript para evitar interceptação
  - Extração completa da tabela nutricional
  - Valores padrão 0 quando não encontrados
  - Processamento de 20 produtos (3 categorias)

**Como usar:**
```bash
python config/coletar_dados_nutricionais_final.py
```

### 2. `teste_um_produto.py`
**Script de teste para um produto específico**

- **Função**: Testa a coleta em um produto individual
- **Produto teste**: Top Whey 3W +Sabor 900g - Brigadeiro
- **Saída**: `dados/teste_um_produto.csv`
- **Recursos**:
  - Debug detalhado do processo
  - Visualização de todas as linhas da tabela
  - Ideal para testar melhorias antes de processar todos

**Como usar:**
```bash
python config/teste_um_produto.py
```

### 3. `coletor_urls_europa_estrutura_real.py`
**Coletor de URLs dos produtos**

- **Função**: Coleta URLs dos produtos das páginas de categoria
- **Categorias**:
  - Pré-treinos (7 produtos)
  - Proteínas (9 produtos)
  - Creatinas e Aminoácidos (4 produtos)
- **Saída**: `dados/urls_produtos_europa_estrutura_real.csv`
- **Recursos**:
  - Seletores específicos para cada categoria
  - Evita produtos dos dropdowns do header
  - Zoom 25% para visualizar mais produtos
  - Remoção de duplicatas

**Como usar:**
```bash
python config/coletor_urls_europa_estrutura_real.py
```

## 📦 Dependências

### `requirements.txt`
```
requests>=2.32.0
beautifulsoup4>=4.12.3
lxml>=5.0.0
selenium>=4.15.0
```

**Instalação:**
```bash
pip install -r config/requirements.txt
```

## 🔄 Fluxo Completo

1. **Coletar URLs** (se necessário):
   ```bash
   python config/coletor_urls_europa_estrutura_real.py
   ```

2. **Testar um produto**:
   ```bash
   python config/teste_um_produto.py
   ```

3. **Processar todos os produtos**:
   ```bash
   python config/coletar_dados_nutricionais_final.py
   ```

## 📊 Estrutura do CSV Final

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| NOME_PRODUTO | Nome do produto | Top Whey 3W +Sabor 900g - Brigadeiro |
| URL | Link do produto | https://maxtitanium.eu/products/... |
| CATEGORIA | Categoria do produto | Proteínas |
| PORCAO (g) | Tamanho da porção | 40 |
| CALORIAS (kcal) | Valor energético | 163 |
| CARBOIDRATOS (g) | Carboidratos | 4.3 |
| PROTEINAS (g) | Proteínas | 32 |
| GORDURAS_TOTAIS (g) | Gorduras totais | 2.0 |
| GORDURAS_SATURADAS (g) | Gorduras saturadas | 1.1 |
| FIBRAS (g) | Fibras alimentares | 0 |
| ACUCARES (g) | Açúcares | 0 |
| SODIO (mg) | Sódio | 73 |

## ⚙️ Configurações Importantes

- **Selenium**: Executa em modo headless para performance
- **Timeouts**: 10 segundos para carregamento de páginas
- **Delays**: 2-3 segundos entre ações para estabilidade
- **Scroll**: Automático até encontrar elementos
- **JavaScript**: Usado para cliques para evitar interceptação

## 🐛 Troubleshooting

1. **ModuleNotFoundError**: Ativar ambiente virtual
2. **Clique interceptado**: Scripts já corrigidos com JavaScript
3. **Elemento não encontrado**: Scripts fazem scroll automático
4. **ChromeDriver**: Selenium gerencia automaticamente

## 📝 Notas

- Scripts testados e funcionais em 05/07/2025
- Compatível com Python 3.13+
- Estrutura específica para site Max Titanium Europa
- Valores 0 quando informações não disponíveis 