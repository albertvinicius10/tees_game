# Changelog - Projeto Tees Game

## Versão 1.1.0 - [Data Atual]

### 🎯 Correções de Interface

#### **Correção da Fonte do Triângulo - Drag and Drop**
- **Arquivo**: `game/templates/game/drag_and_drop.html`
- **Problema**: Texto dentro dos triângulos estava sendo cortado pelo `clip-path`
- **Solução Implementada**:
  - Reposicionamento do texto: `top: 45%` → `top: 60%`
  - Redução do tamanho da fonte: `0.8em` → `0.7em`
  - Adição de `max-width: 80%` para limitar largura do texto
  - Implementação de `overflow: hidden` e `text-overflow: ellipsis`
  - Aumento do tamanho das formas: 90px → 100px (arrastáveis), 80px → 90px (colocadas)

#### **Melhorias Responsivas**
- **Dispositivos móveis**: Fonte reduzida para `0.6em` em triângulos
- **Posicionamento móvel**: `top: 65%` para melhor visibilidade
- **Tamanho responsivo**: Formas aumentadas para 80px em telas pequenas

### 🚀 Novas Funcionalidades

#### **Rolagem Automática Durante Arraste**
- **Arquivo**: `game/templates/game/drag_and_drop.html`
- **Funcionalidade**: Rolagem automática que acompanha o mouse durante o arraste
- **Implementação**:
  - Zonas de ativação: 100px do topo e da parte inferior da tela
  - Velocidade adaptativa baseada na proximidade das bordas
  - Performance otimizada com `setInterval` de 16ms (~60fps)
  - Desativação automática ao soltar objeto ou pressionar ESC

#### **Características da Rolagem Automática**:
- ✅ Ativação automática durante arraste
- ✅ Velocidade proporcional à proximidade das bordas
- ✅ Compatível com todas as formas geométricas
- ✅ Não interfere com outras funcionalidades
- ✅ Suporte para cancelamento com ESC

### 🔧 Melhorias Técnicas

#### **CSS Aprimorado**
- Adição de `overflow-y: auto` no body para suporte à rolagem
- Melhor posicionamento de texto em formas geométricas
- Tratamento de overflow para textos longos

#### **JavaScript Otimizado**
- Sistema de rolagem automática com controle de performance
- Gerenciamento adequado de event listeners
- Limpeza automática de intervalos para evitar vazamentos de memória

### 📱 Responsividade

#### **Melhorias para Dispositivos Móveis**
- Tamanhos de fonte ajustados para telas pequenas
- Posicionamento otimizado de texto em triângulos
- Rolagem automática adaptada para diferentes tamanhos de tela

### 🐛 Correções de Bugs

#### **Problema de Instalação de Dependências**
- **Problema**: Erro de certificados SSL/TLS do PostgreSQL
- **Solução**: Uso de flags `--trusted-host` no pip
- **Comando**: `pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt`

### 📋 Dependências Instaladas
- Django 5.2.3
- django-tailwind 4.0.1
- asgiref 3.8.1
- sqlparse 0.5.3
- tzdata 2025.2
- whitenoise 6.7.0

---

## Como Usar as Novas Funcionalidades

### Rolagem Automática
1. Inicie o arraste de qualquer forma geométrica
2. Mova o mouse para próximo ao topo ou parte inferior da tela
3. A página rolará automaticamente na direção do mouse
4. Para cancelar, pressione ESC ou solte o objeto

### Melhorias Visuais
- Texto em triângulos agora aparece completamente visível
- Formas ligeiramente maiores para melhor usabilidade
- Melhor legibilidade em dispositivos móveis

---

## Próximas Atualizações Planejadas

- [ ] Adicionar animações suaves para transições
- [ ] Implementar sistema de pontuação
- [ ] Adicionar mais formas geométricas
- [ ] Melhorar feedback visual durante arraste
- [ ] Implementar modo escuro

---

*Documentação gerada automaticamente - Projeto Tees Game* 