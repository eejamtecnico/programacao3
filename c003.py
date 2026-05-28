a=10
b=3

# Operações aritméticas
print(f"Soma de 10 + 3: {a + b}")
print(f"Subtração de 10 - 3: {a - b}")
print(f"Multiplicação de 10 * 3: {a * b}")
print(f"Divisão de 10 / 3: {a / b}")
print(f"Divisão Inteira de 10 // 3: {a // b}")
print(f"Resto da divisão de 10 % 3: {a % b}")
print(f"Potência de 10 ** 3: {a ** b}")

#operações relacionais
print(f"10 é igual a 3? {a == b}")
print(f"10 é diferente de 3? {a != b}")
print(f"10 é maior que 3? {a > b}")
print(f"10 é menor que 3? {a < b}")
print(f"10 é maior ou igual a 3? {a >= b}")
print(f"10 é menor ou igual a 3? {a <= b}")

#operações lógicas
#and só retorna True quando todas as partes forem True
print(f"10 é diferente de 3? e 10 é menor que 3? {(a != b) and (a < b)}")
#or retorna True quando pelo menos uma parte for True
print(f"10 é diferente de 3? e 10 é menor que 3? {(a != b) or (a < b)}")
#(a == b) é False, então not (a == b) vira True
print(f"10 não é igual a 3? {not (a == b)}")
#(a > b) é True, então not (a > b) vira False
print(f"10 não é maior que 3? {not (a > b)}")

