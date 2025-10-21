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
