import calculadora_indices as calc

def clasificar_imc(imc: float) -> str:
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    elif imc < 50:
        return "Obesidad tipo III o mórbida"
    else:
        return "Obesidad tipo IV o extrema"

try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calc.calcular_IMC(peso, altura)
    categoria = clasificar_imc(imc)

    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Clasificación: {categoria}")

except ValueError:
    print("Error: Ingresá valores numéricos válidos.")