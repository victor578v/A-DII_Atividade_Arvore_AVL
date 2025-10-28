# A&DII_Atividade_Arvore_AVL
## Sequencia de numeros da arvore avaliados: 10, 5, 15, 3, 1, 20, 25, 18

**Objetivo:** Compreender a lógica de balanceamento (rotações) numa árvore AVL, implementada de forma iterativa (com laços) dentro da função Inserir.
Contexto: Partimos do princípio que vocês já possuem uma Árvore Binária de Busca (BST) funcional em Python, com uma Classe Node e uma Classe Arvore (com funções inserir e buscar iterativas).
### **Parte 1:** Modificações Essenciais
A nossa Classe Node precisa de uma nova informação:
1. Atributo altura:
No __init__ da Classe Node, adicione self.altura = 1. Todo novo nó, quando inserido como folha, tem altura 1.
Precisaremos também de três "funções auxiliares" que o nosso algoritmo principal usará o tempo todo.
1. Função obter_altura(no):
Recebe um nó.
Se o nó for Nulo (None), ela deve retornar 0.
Caso contrário, ela retorna o atributo no.altura.
2. Função atualizar_altura(no):
Recebe um nó.
Esta função recalcula a altura de um nó com base nos seus filhos.
altura_esquerda = obter_altura(no.filho_esquerda)
altura_direita = obter_altura(no.filho_direita)
no.altura = 1 + max(altura_esquerda, altura_direita)
3. Função obter_fator_balanceamento(no):
Recebe um nó.
Se o nó for Nulo, retorna 0.
Calcula obter_altura(no.filho_esquerda) - obter_altura(no.filho_direita).
O resultado (fator) ideal é -1, 0 ou 1. Se for > 1 (maior que 1), a árvore está "pesada" para a esquerda. Se for < -1 (menor que -1), está "pesada" para a direita.

### **Parte 2:** O Algoritmo Inserir da AVL (Iterativo)
Este algoritmo é dividido em duas grandes fases: (A) a inserção normal da BST, mas "gravando o caminho", e (B) a "subida" de volta para a raiz, verificando o balanceamento.

**Fase A:** Inserção Normal (BST) + Rastreamento do Caminho
O desafio de não usar recursão é que, após descer até uma folha para inserir, precisamos "subir" de volta para a raiz. Para fazer isso, vamos usar uma lista para "gravar" cada nó que visitamos no caminho da raiz até o local de inserção.

1. Crie o novo_no (com valor_para_inserir e altura = 1).
2. Crie uma lista (ou pilha) vazia chamada caminho.
3. Tratar Árvore Vazia: Se a raiz da árvore for Nula, atribua o novo_no à raiz e termine a função.
4. *Encontrar o Local:*

Inicie um ponteiro atual na raiz.

Inicie um laço (while True):

**IMPORTANTE:** Adicione o nó atual à lista caminho.

Compare o valor_para_inserir com atual.valor:

**Caso Menor:**

Se atual.filho_esquerda for Nulo:

Atribua o novo_no como atual.filho_esquerda.

Termine o laço (break).

Se não for Nulo:

Mova o ponteiro atual para atual.filho_esquerda.

**Caso Maior:** 

Se atual.filho_direita for Nulo:

Atribua o novo_no como atual.filho_direita.

Termine o laço (break).

Se não for Nulo:

Mova o ponteiro atual para atual.filho_direita.

Ao fim desta fase, o novo_no foi inserido e a lista caminho contém todos os ancestrais dele, da raiz até o seu pai.

### **Fase B:** Verificação de Balanceamento (A "Subida")

Agora, vamos percorrer a lista caminho de trás para frente (do pai do novo_no até a raiz), verificando o balanceamento em cada nó.

Inicie um laço for que percorre a lista caminho em ordem reversa. Para cada no_ancestral no laço:

**Passo A: Atualizar a Altura**

Sempre que "subimos", a primeira coisa a fazer é atualizar a altura do nó que estamos a visitar.

Chame atualizar_altura(no_ancestral).

**Passo B: Verificar o Balanceamento**

Calcule o fator_balanceamento = obter_fator_balanceamento(no_ancestral).

**Passo C: Decidir se Rotaciona**

o aqui está a lógica principal. Precisamos verificar se o fator_balanceamento saiu dos limites (-1, 0, 1).

o Se fator_balanceamento > 1: (Pesado à Esquerda)

- Precisamos decidir: Rotação Simples (LL) ou Dupla (LR)?

- Olhe para o filho da esquerda do no_ancestral.

- Se o valor_para_inserir for menor que o valor desse filho:

- É um caso Simples (LL). Execute a Rotação à Direita no no_ancestral.

- Se o valor_para_inserir for maior que o valor desse filho:

- É um caso Duplo (LR).

- Primeiro, execute a Rotação à Esquerda no no_ancestral.filho_esquerda.

- Depois, execute a Rotação à Direita no no_ancestral.

o Se fator_balanceamento < -1: (Pesado à Direita)

- Precisamos decidir: Rotação Simples (RR) ou Dupla (RL)?

- Olhe para o filho da direita do no_ancestral.

- Se o valor_para_inserir for maior que o valor desse filho:

- É um caso Simples (RR). Execute a Rotação à Esquerda no no_ancestral.

- Se o valor_para_inserir for menor que o valor desse filho:

- É um caso Duplo (RL).

- Primeiro, execute a Rotação à Direita no no_ancestral.filho_direita.

- Depois, execute a Rotação à Esquerda no no_ancestral.

**Passo D: Reconectar a Sub-árvore (Após a Rotação)**

o Este passo é crucial e fácil de errar na implementação iterativa!

o Pense no seguinte: após uma rotação, o nó que estava desbalanceando (no_ancestral) não é mais o "topo" daquela sub-árvore. Um outro nó (a nova_sub_raiz que a sua função de rotação deve retornar) "subiu" e tomou o lugar dele.

o Porém, o "pai" do no_ancestral (o nó que vem antes dele na lista caminho) ainda está "segurando" (apontando) para o nó antigo.

o Pergunta-chave: Como pode usar a lista caminho para encontrar esse "pai"?

o Uma vez que encontrou o "pai", precisa decidir: o ponteiro filho_esquerda ou filho_direita dele é que deve ser atualizado para apontar para a nova_sub_raiz?

o E o caso especial: O que acontece se o no_ancestral que rotacionou era a própria raiz principal da árvore (ou seja, ele não tem "pai")? Qual referência principal da sua árvore (self.raiz) precisa ser atualizada?

### Parte 3: Algoritmos das Rotações

Estes são os algoritmos detalhados para as rotações (Simples) que irá precisar.

Lógica Rotação Simples à Direita (para o caso LL)

Função chamada como: nova_raiz = rotacao_direita(no_desbalanceado_Z)

- O nó desbalanceado é Z.

- Identifique o filho da esquerda de Z. Chame-o de Y.

- Identifique o filho da direita de Y. Chame-o de T3 (esta é a sub-árvore que mudará de "pai").

**Executar Rotação:**

- O filho_direita de Y agora se torna Z.

- O filho_esquerda de Z agora se torna T3.

Atualizar Alturas (A ORDEM IMPORTA):

- Primeiro, chame atualizar_altura(Z). (Pois Z está agora "embaixo").

- Segundo, chame atualizar_altura(Y). (Pois Y está agora "em cima").

**Retorne Y (ele é a nova raiz desta sub-árvore, e será usado no "Passo D").**

**Lógica Rotação Simples à Esquerda (para o caso RR)**

Função chamada como: nova_raiz = rotacao_esquerda(no_desbalanceado_Z)

- O nó desbalanceado é Z.

- Identifique o filho da direita de Z. Chame-o de Y.

- Identifique o filho da esquerda de Y. Chame-o de T2 (a sub-árvore que mudará de "pai").

**Executar Rotação:**

- O filho_esquerda de Y agora se torna Z.

- O filho_direita de Z agora se torna T2.

**Atualizar Alturas (A ORDEM IMPORTA):**

- Primeiro, chame atualizar_altura(Z).

- Segundo, chame atualizar_altura(Y).

**Retorne Y (para ser usado no "Passo D").**