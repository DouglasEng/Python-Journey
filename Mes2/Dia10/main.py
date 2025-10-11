"""
=== Desafio do Dia 40 – Calculadora de Exposição Solar e Vitamina D ===

Objetivo:
Criar um programa que ajude o usuário a estimar o tempo de exposição solar necessário para sintetizar vitamina D de forma segura, levando em consideração fatores como tipo de pele, hora do dia, latitude e intensidade solar.

Fórmula simplificada (aproximação):
- Tempo recomendado ≈ (Quantidade diária de vitamina D desejada / Intensidade solar ajustada)

Funcionalidades:
1. Inserir dados do usuário: idade, tipo de pele, latitude, hora do dia.
2. Calcular tempo estimado de exposição solar seguro para síntese de vitamina D.
3. Alertar sobre risco de exposição excessiva ao sol.
4. Salvar resultados em arquivo histórico para acompanhar hábitos diários de exposição.
"""






import os
from datetime import datetime




ARQUIVO = "vitamina_d_historico.txt"

TIPOS_PELE = {
    1: {"descricao": "Muito clara", "fator": 1.0},
    2: {"descricao": "Clara", "fator": 1.2},
    3: {"descricao": "Média", "fator": 1.5},
    4: {"descricao": "Morena", "fator": 2.0},
    5: {"descricao": "Escura", "fator": 2.5},
    6: {"descricao": "Muito escura", "fator": 3.0}
}







def salvar_historico(data, idade, tipo_pele, latitude, hora, tempo_exposicao):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data} | Idade: {idade} | Pele: {tipo_pele} | Latitude: {latitude} | Hora: {hora} | Tempo recomendado: {tempo_exposicao:.1f} min\n")



def calcular_exposicao(tipo_pele, latitude, hora):
    """
    Estima o tempo de exposição em minutos baseado em tipo de pele, latitude e hora do dia.
    Formula simplificada: quanto mais escura a pele, maior o tempo necessário; 
    quanto mais alta a intensidade solar (meio-dia, baixa latitude), menor o tempo.
    """




    fator_pele = TIPOS_PELE[tipo_pele]["fator"]
    # intensidade solar aproximada: mais forte entre 10h e 14h, mais fraca cedo ou tarde
    if 10 <= hora <= 14:
        intensidade = max(0.8, 1 - abs(latitude)/90)  # ajusta intensidade pela latitude
    else:
        intensidade = max(0.4, 1 - abs(latitude)/90)  # fora do pico solar

    tempo = 20 * fator_pele / intensidade  # 20 minutos base ajustado
    return tempo







def mostrar_historico():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum histórico registrado.\n")
        return
    print("\n=-= Histórico de Exposição Solar =-=\n")
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print(f.read())





def menu():
    while True:
        print("\n=-=- Calculadora de Exposição Solar e Vitamina D -=-=")
        print("( 1 ) Calcular tempo de exposição")
        print("( 2 ) Ver histórico")
        print("( 3 ) Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            try:
                idade = int(input("Digite sua idade: ").strip())
                print("Tipos de pele:")
                for k, v in TIPOS_PELE.items():
                    print(f"{k}. {v['descricao']}")
                tipo_pele = int(input("Escolha seu tipo de pele (1-6): ").strip())
                latitude = float(input("Digite a latitude em graus (-90 a 90): ").strip())
                hora = int(input("Digite a hora do dia (0-23): ").strip())
                tempo = calcular_exposicao(tipo_pele, latitude, hora)
                print(f"\nTempo recomendado de exposição solar seguro: {tempo:.1f} minutos\n")

                salvar_historico(datetime.now().strftime("%d/%m/%Y %H:%M"), idade, TIPOS_PELE[tipo_pele]["descricao"], latitude, hora, tempo)
            except Exception as e:
                print("Erro nos dados inseridos, tente novamente.", e)




        elif escolha == "2":
            mostrar_historico()


        elif escolha == "3":
            print("Encerrando o programa. Cuide-se ao se expor ao sol!")
            break

        else:
            print("Opção inválida, tente novamente.\n")







if __name__ == "__main__":
    menu()
