
print("Aplicativo que informa se é triângulo e seu tipo")

a = float(input("Informe o lado a: "))
b = float(input("Informe o lado b: "))
c = float(input("Informe o lado c: "))


if (a > 0 and b > 0 and c > 0) and (a < b + c) and (b < a + c) and (c < a + b):
    print("É um triângulo.")
    
    
    if a == b == c:
        print("Tipo: Triângulo equilátero - Os 3 lados são iguais")
    elif a == b or b == c or a == c:
        print("Tipo: Triângulo isósceles - Dois lados iguais e um diferente")
    else:
        print("Tipo: Triângulo escaleno - Os 3 lados são diferentes")
else:
    print("Os valores informados não formam um triângulo.")