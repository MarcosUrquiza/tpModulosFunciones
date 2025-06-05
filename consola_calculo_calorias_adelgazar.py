import calculadora_indices as calc

def obtener_valor_genero(genero_str: str) -> int:
    if genero_str.lower() == "masculino":
        return 5
    elif genero_str.lower() == "femenino":
        return -161
    else:
        raise ValueError("Género inválido. Debe ser 'masculino' o 'femenino'.")

try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad: "))
    genero_input = input("Ingrese su género (masculino/femenino): ")

    valor_genero = obtener_valor_genero(genero_input)

    mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)

    print(f"\n{mensaje}")

except ValueError as e:
    print(f"Error: {e}")
