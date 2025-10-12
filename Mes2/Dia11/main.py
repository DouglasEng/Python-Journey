"""
=== Desafio do Dia 41 – Simulador de Viagem Espacial ===

Objetivo:
Simular uma viagem da Terra até outro planeta do Sistema Solar,
calculando o tempo necessário com base na velocidade média da nave.

Funcionalidades:
1. Escolher planeta de destino
2. Inserir velocidade média (km/h)
3. Calcular tempo estimado de viagem
4. Exibir resultados em horas, dias, meses e anos
5. Salvar histórico de viagens em um arquivo .txt
"""

def calcular_tempo(distancia_km, velocidade_kmh):
    horas = distancia_km / velocidade_kmh
    dias = horas / 24
    meses = dias / 30
    anos = dias / 365
    return horas, dias, meses, anos




def salvar_resultado(texto):
    with open("viagens_espaciais.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")






def main():
    planetas = {
        "Mercúrio": 91_700_000,
        "Vênus": 41_400_000,
        "Marte": 78_300_000,
        "Júpiter": 628_700_000,
        "Saturno": 1_275_000_000,
        "Urano": 2_723_000_000,
        "Netuno": 4_351_000_000
    }

    print("=-= Simulador de Viagem Espacial =-=")
    print("Escolha seu destino:\n")

    for i, planeta in enumerate(planetas.keys(), start=1):
        print(f"{i}. {planeta}")

    escolha = input("\nDigite o número do planeta: ")

    try:
        indice = int(escolha) - 1
        planeta_escolhido = list(planetas.keys())[indice]
    except (ValueError, IndexError):
        print("Opção inválida. Tente novamente.")
        return

    distancia = planetas[planeta_escolhido]
    print(f"\nDistância aproximada até {planeta_escolhido}: {distancia:,} km")

    try:
        velocidade = float(input("Digite a velocidade média da nave (km/h): "))
        if velocidade <= 0:
            print("A velocidade deve ser maior que zero.")
            return
    except ValueError:
        print("Entrada inválida para velocidade.")
        return

    horas, dias, meses, anos = calcular_tempo(distancia, velocidade)

    resultado = (
        f"\n=-=- Viagem Espacial -=-=\n"
        f"Destino: {planeta_escolhido}\n"
        f"Distância: {distancia:,} km\n"
        f"Velocidade: {velocidade:,.2f} km/h\n"
        f"Tempo estimado:\n"
        f"  - {horas:,.0f} horas\n"
        f"  - {dias:,.2f} dias\n"
        f"  - {meses:,.2f} meses\n"
        f"  - {anos:,.2f} anos\n"
        f"{'-='*17}"
    )

    print(resultado)
    salvar_resultado(resultado)







if __name__ == "__main__":
    main()
