"""
=== Desafio do Dia 30 – Calculadora de Impacto Ambiental Pessoal (Completa) ===

Objetivo:
Criar um sistema interativo que estime a pegada de carbono anual de uma pessoa
com base em transporte, alimentação, consumo de energia e gestão de resíduos,
ofereça comparações, gere dicas personalizadas, permita simulações ("e se..."),
salve histórico, acompanhe metas e aplique uma pontuação gamificada para hábitos verdes.

Características principais:
- Coleta de dados sobre transporte, alimentação, energia e resíduos.
- Cálculo aproximado de emissões (kg CO2e / ano) por categoria e total.
- Comparação com médias (global e brasileira) e classificação por perfil.
- Simulações de cenários (ex.: trocar carro por bicicleta 2x/semana).
- Geração de dicas personalizadas e ranking das maiores fontes de emissão.
- Persistência em arquivo JSON (histórico de registros, metas e pontos).
- Sistema de metas (definir meta anual de redução) e acompanhamento.
- Gamificação: pontos para hábitos sustentáveis (acumuláveis no histórico).

"""



import os
import json
from datetime import datetime
from copy import deepcopy

# ---------------------------
# Configurações e constantes - Informações geradas por IA
# ---------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "usuario_data.json")


# Emissões (kg CO2e)
EM_FACTOR = {
    # transporte (kg CO2 per km)
    "carro": 0.21,     # por km rodado (média)
    "moto": 0.11,
    "onibus": 0.089,
    "bicicleta_pe": 0.0,  # sem emissão direta
    # aviação por voo médio (aprox): we'll ask number of voos per ano and type
    "aviao_curto": 110.0,  # kg CO2 per short-haul flight (média)
    "aviao_longo": 440.0,  # kg CO2 per long-haul flight (média)
    # energia (kg CO2 per kWh) — média global baixa; usamos 0.09 (padrão BR aproximado)
    "kwh": 0.09,
    # resíduos (kg CO2 per kg/ano) approximation for household waste
    "residuos_por_kg": 0.21
}

# Alimentação: emissões por refeição média (kg CO2e)
FOOD_FACTOR_PER_MEAL = {
    "carne_vermelha": 7.0,   # por refeição com carne vermelha
    "frango_peixe": 1.5,     # por refeição com frango/peixe
    "vegetariana": 0.5       # por refeição vegetariana
}

PLASTIC_IMPACT = {
    "baixo": 10.0,
    "medio": 30.0,
    "alto": 70.0
}

PONTOS = {
    "usa_bicicleta": 10,        
    "usa_energia_renovavel": 20,
    "recicla": 15,
    "reduz_carne": 12,         
    "evita_voo": 25
}

# Comparações de referência (kg CO2 per ano) — valores simplificados
REFERENCIAS = {
    "media_mundial": 4750,  # approximate per capita global per year (kg CO2)
    "media_brasil": 2500    # approximate per capita Brazil per year
}

# Perfil thresholds (kg CO2/ano)
PERFIL_THRESHOLDS = {
    "baixo": 2000,
    "moderado": 5000
}  # <=2000 low, 2000-5000 moderate, >5000 high





def carregar_dados():
    """Carrega dados do usuário (histórico, metas, pontos) do arquivo JSON."""
    if not os.path.exists(DATA_FILE):
        return {
            "historico": [],  
            "meta_anual_kg": None,
            "pontos": 0
        }
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    """Salva dados no arquivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)






def entrada_usuario():
    print("\nBem-vindo ao calculador de impacto ambiental pessoal.\n"
          "Você responderá algumas perguntas sobre seus hábitos; no final verá um relatório e dicas.\n")

    print("=-= Transporte (insira valores aproximados) =-=")
    def ler_float(prompt, default=0.0):
        while True:
            v = input(f"{prompt} (enter para {default}): ").strip()
            if v == "":
                return default
            try:
                return float(v.replace(",", "."))
            except ValueError:
                print("Valor inválido. Tente novamente.")

    transporte_info = {}
    transporte_info["km_carro_semanais"] = ler_float("Km rodados de carro por semana", 0.0)
    transporte_info["km_moto_semanais"] = ler_float("Km rodados de moto por semana", 0.0)
    transporte_info["km_onibus_semanais"] = ler_float("Km rodados de ônibus por semana", 0.0)
    transporte_info["km_bicicleta_pe_semanais"] = ler_float("Km percorridos a pé/bicicleta por semana", 0.0)
    transporte_info["voos_curto_mes"] = int(ler_float("Número de voos curtos por mês (0 se nenhum)", 0))
    transporte_info["voos_longo_mes"] = int(ler_float("Número de voos longos por mês (0 se nenhum)", 0))

    print("\n=-= Alimentação (número de refeições por semana) =-=")
    alim_info = {}
    alim_info["carne_vermelha_semanais"] = int(ler_float("Refeições com carne vermelha por semana", 0))
    alim_info["frango_peixe_semanais"] = int(ler_float("Refeições com frango/peixe por semana", 0))
    alim_info["vegetariana_semanais"] = int(ler_float("Refeições vegetarianas por semana", 0))

    print("\n=-= Energia e consumo elétrico =-=")
    energia_info = {}
    energia_info["kwh_mes"] = ler_float("Consumo médio em kWh por mês", 200.0)
    renov = input("Você usa alguma fonte de energia renovável (painel solar ou fornecedor verde)? (s/n): ").strip().lower()
    energia_info["usa_renovavel"] = (renov == "s")
    energia_info["aparelhos_standby"] = int(ler_float("Quantos aparelhos costuma deixar em standby (estimativa)", 2))

    print("\n=-= Resíduos e reciclagem =-=")
    res_info = {}
    res_info["lixo_litros_semanais"] = ler_float("Litros de lixo por semana (estimativa)", 10.0)
    recic = input("Você recicla regularmente? (s/n): ").strip().lower()
    res_info["recicla"] = (recic == "s")
    plastic = ""

    while plastic not in ("baixo", "medio", "alto", ""):
        plastic = input("Uso de plástico descartável (baixo/medio/alto) [medio]: ").strip().lower()
        if plastic == "":
            plastic = "medio"
    res_info["plastic_usage"] = plastic
