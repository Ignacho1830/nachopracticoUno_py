numeros_pares = []

for i in range(10):
    numero = int(input(f"Ingresa el numero {i + 1}: "))

    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Los numeros pares ingresados son: ", numeros_pares)
