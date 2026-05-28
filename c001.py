import sys #biblioteca usada para descobrir o tamanho das variáveis

# inicializa variáveis (nome e valor)
x=3
y=3.142128
w='Oi'
z=True

# escreve as classes dos quatro tipos de dados primitivos do python
print(type(x))
print(type(y))
print(type(w))
print(type(z)) 

# tamanho da variável em bytes
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(w))
print(sys.getsizeof(z))

# escreve, na tela, os endereços de memória que as variáveis estão alocadas
print(id(x))
print(id(y))
print(id(w))
print(id(z))