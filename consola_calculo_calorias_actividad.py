import calculadora_indices as calc

def obtener_valor_genero(genero_str: str) -> int:
    if genero_str.lower() == "masculino":
        return 5
    elif genero_str.lower() == "femenino":
        return -161
    else:
        raise ValueError("Género inválido. Debe ser 'masculino' o 'femenino'.")

def obtener_valor_actividad(nivel: int) -> float:
    valores = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    if nivel not in valores:
        raise ValueError("Nivel de actividad inválido. Debe ser un número del 1 al 5.")
    return valores[nivel]

try:
    print("Nivel de actividad física semanal:")
    print("1. Poco o ningún ejercicio")
    print("2. Ejercicio ligero (1 a 3 días/semana)")
    print("3. Ejercicio moderado (3 a 5 días/semana)")
    print("4. Deportista (6 a 7 días/semana)")
    print("5. Atleta (entrenamientos dobles)")

    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad: "))
    genero_input = input("Ingrese su género (masculino/femenino): ")
    nivel_actividad = int(input("Ingrese el número correspondiente a su nivel de actividad física (1-5): "))

    valor_genero = obtener_valor_genero(genero_input)
    valor_actividad = obtener_valor_actividad(nivel_actividad)

    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

    print(f"\nTu gasto calórico diario estimado, según tu actividad, es de: {calorias_actividad:.2f} calorías.")

except ValueError as e:
    print(f"Error: {e}")
