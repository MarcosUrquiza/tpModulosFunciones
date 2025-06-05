def calcular_IMC(peso: float, altura: float) -> float:
    imc = peso / (altura ** 2)
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_IMC(peso, altura)
    grasa = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    return grasa


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    altura_cm = altura * 100
    tmb = (10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero
    return tmb


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_con_actividad = tmb * valor_actividad
    return calorias_con_actividad


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    minimo = round(tmb * 0.80, 2)
    maximo = round(tmb * 0.85, 2)
    return f"Para adelgazar es recomendado que consumas entre: {minimo} y {maximo} calorías al día."
