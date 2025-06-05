import calculadora_indices as calc

def obtener_valor_genero(genero_str: str) -> float:
    if genero_str.lower() == "masculino":
        return 10.8
    elif genero_str.lower() == "femenino":
        return 0.0
    else:
        raise ValueError("Género inválido. Debe ser 'masculino' o 'femenino'.")

try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad: "))
    genero_input = input("Ingrese su género (masculino/femenino): ")
    valor_genero = obtener_valor_genero(genero_input)

    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

    print(f"\nTu porcentaje estimado de grasa corporal es: {porcentaje_grasa:.2f}%")

except ValueError as e:
    print(f"Error: {e}")
