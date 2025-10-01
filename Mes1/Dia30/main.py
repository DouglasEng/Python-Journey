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




def calcular_transporte_emissoes(transporte_info):
    """
    transporte_info: dict com chaves:
        km_carro_semanais, km_moto_semanais, km_onibus_semanais,
        km_bicicleta_pe_semanais, voos_curto_mes, voos_longo_mes
    retorna emissões anuais em kg CO2e (transporte)
    """
    km_carro_ano = transporte_info.get("km_carro_semanais", 0) * 52
    km_moto_ano = transporte_info.get("km_moto_semanais", 0) * 52
    km_onibus_ano = transporte_info.get("km_onibus_semanais", 0) * 52
    km_bike_pe_ano = transporte_info.get("km_bicicleta_pe_semanais", 0) * 52

    em_carro = km_carro_ano * EM_FACTOR["carro"]
    em_moto = km_moto_ano * EM_FACTOR["moto"]
    em_onibus = km_onibus_ano * EM_FACTOR["onibus"]
    em_bike_pe = 0  

    voos_curto_ano = transporte_info.get("voos_curto_mes", 0) * 12
    voos_longo_ano = transporte_info.get("voos_longo_mes", 0) * 12
    em_voos = voos_curto_ano * EM_FACTOR["aviao_curto"] + voos_longo_ano * EM_FACTOR["aviao_longo"]

    total_transp = em_carro + em_moto + em_onibus + em_bike_pe + em_voos
    detalhe = {
        "carro": em_carro,
        "moto": em_moto,
        "onibus": em_onibus,
        "bike_pe": em_bike_pe,
        "voos": em_voos
    }
    return total_transp, detalhe

def calcular_alimentacao_emissoes(alim_info):
    """
    alim_info: dict com chaves:
        carne_vermelha_semanais (num refeições/semana),
        frango_peixe_semanais,
        vegetariana_semanais
    retorna emissões anuais em kg CO2e (alimentação)
    """
    carne_semana = alim_info.get("carne_vermelha_semanais", 0)
    frango_semana = alim_info.get("frango_peixe_semanais", 0)
    veg_semana = alim_info.get("vegetariana_semanais", 0)

    carne_ano = carne_semana * 52 * FOOD_FACTOR_PER_MEAL["carne_vermelha"]
    frango_ano = frango_semana * 52 * FOOD_FACTOR_PER_MEAL["frango_peixe"]
    veg_ano = veg_semana * 52 * FOOD_FACTOR_PER_MEAL["vegetariana"]

    total_food = carne_ano + frango_ano + veg_ano
    detalhe = {
        "carne_vermelha": carne_ano,
        "frango_peixe": frango_ano,
        "vegetariana": veg_ano
    }
    return total_food, detalhe

def calcular_energia_emissoes(energia_info):
    """
    energia_info: dict com chaves:
        kwh_mes (float), usa_renovavel (bool), aparelhos_standby (int)
    retorna emissões anuais em kg CO2e e detalhe
    """
    kwh_mes = energia_info.get("kwh_mes", 0.0)
    usa_renovavel = energia_info.get("usa_renovavel", False)
    aparelhos_standby = energia_info.get("aparelhos_standby", 0)

    kwh_ano = kwh_mes * 12
    fator = EM_FACTOR["kwh"]
    if usa_renovavel:
        #  redução de 50% se usa fonte renovável local 
        fator = fator * 0.5

    em_energia = kwh_ano * fator

    # impacto por aparelhos em standby, cada aparelho adiciona 15 kg CO2/ano
    em_standby = aparelhos_standby * 15.0

    total_energia = em_energia + em_standby
    detalhe = {
        "energia_red": em_energia,
        "standby": em_standby
    }
    return total_energia, detalhe

def calcular_residuos_emissoes(res_info):
    """
    res_info: dict com chaves:
        lixo_litros_semanais (float) -> convert liters to kg roughly 1L=1kg
        recicla (bool)
        plastic_usage ('baixo'/'medio'/'alto')
    retorna emissões anuais kg CO2e e detalhe
    """
    lixo_litros_semanais = res_info.get("lixo_litros_semanais", 0.0)
    recicla = res_info.get("recicla", False)
    plastic = res_info.get("plastic_usage", "medio")

    kg_ano = lixo_litros_semanais * 52  # aproximadamente 1L/1kg
    em_residuos = kg_ano * EM_FACTOR["residuos_por_kg"]

    if recicla:
        em_residuos *= 0.7

    em_plastic = PLASTIC_IMPACT.get(plastic, PLASTIC_IMPACT["medio"])

    total_residuos = em_residuos + em_plastic
    detalhe = {
        "residuos": em_residuos,
        "plastic": em_plastic
    }
    return total_residuos, detalhe


def calcular_pegada(transporte_info, alim_info, energia_info, res_info):
    """
    calcula pegada total anual, retorna dict com totais por categoria, detalhes e total
    """
    trans_total, trans_det = calcular_transporte_emissoes(transporte_info)
    alim_total, alim_det = calcular_alimentacao_emissoes(alim_info)
    energia_total, energia_det = calcular_energia_emissoes(energia_info)
    res_total, res_det = calcular_residuos_emissoes(res_info)

    total = trans_total + alim_total + energia_total + res_total

    resultado = {
        "transporte": {"total": trans_total, "detalhe": trans_det},
        "alimentacao": {"total": alim_total, "detalhe": alim_det},
        "energia": {"total": energia_total, "detalhe": energia_det},
        "residuos": {"total": res_total, "detalhe": res_det},
        "total_ano": total
    }
    return resultado



def perfil_por_total(total_kg):
    """Classifica perfil por total anual (kg CO2)."""
    if total_kg <= PERFIL_THRESHOLDS["baixo"]:
        return "Baixo impacto"
    elif total_kg <= PERFIL_THRESHOLDS["moderado"]:
        return "Moderado"
    else:
        return "Alto impacto"
    

def comparar_com_medias(total_kg):
    """Retorna diferenças percentuais em relação às médias."""
    diff_mundial = ((total_kg - REFERENCIAS["media_mundial"]) / REFERENCIAS["media_mundial"]) * 100
    diff_brasil = ((total_kg - REFERENCIAS["media_brasil"]) / REFERENCIAS["media_brasil"]) * 100
    return {"vs_mundial_%": diff_mundial, "vs_brasil_%": diff_brasil}

def gerar_dicas(resultado, transporte_info, alim_info, energia_info, res_info):
    """
    Gera dicas personalizadas segundo as maiores categorias de emissão
    e hábitos do usuário.
    """
    dicas = []
    # ordenar categorias por impacto
    categorias = [
        ("transporte", resultado["transporte"]["total"]),
        ("alimentacao", resultado["alimentacao"]["total"]),
        ("energia", resultado["energia"]["total"]),
        ("residuos", resultado["residuos"]["total"])
    ]
    categorias.sort(key=lambda x: x[1], reverse=True)


    # dica baseada na maior fonte
    maior = categorias[0][0]
    if maior == "transporte":
        if transporte_info.get("km_carro_semanais", 0) > 20:
            dicas.append("Considere reduzir o uso do carro algumas vezes por semana ou fazer carona solidária.")

        if transporte_info.get("voos_curto_mes", 0) > 0 or transporte_info.get("voos_longo_mes", 0) > 0:
            dicas.append("Evite voos desnecessários; prefira ônibus/trecho ferroviário quando possível.")

        dicas.append("Alternar alguns trajetos curtos por bicicleta ou caminhada reduz bastante emissões.")

    elif maior == "alimentacao":
        carne = alim_info.get("carne_vermelha_semanais", 0)
        if carne > 2:
            dicas.append("Diminuir refeições com carne vermelha para 1-2x/semana pode reduzir emissões consideravelmente.")
        dicas.append("Incluir mais refeições vegetarianas e substituir carne vermelha por frango/peixe reduz impacto.")

    elif maior == "energia":
        if not energia_info.get("usa_renovavel", False):
            dicas.append("Se possível, migre parte do consumo para fontes renováveis ou escolha um fornecedor verde.")
        dicas.append("Trocar lâmpadas por LED e desligar aparelhos em standby reduz consumo elétrico.")

    else:  # residuos
        if not res_info.get("recicla", False):
            dicas.append("Pratique reciclagem e compostagem para reduzir impactos do lixo.")
        if res_info.get("plastic_usage", "medio") == "alto":
            dicas.append("Reduza o uso de plástico descartável (use recipientes reutilizáveis).")

    dicas.append("Monitore seu progresso semanalmente e tente pequenas metas para redução contínua.")
    return dicas


def top_3_fontes(resultado):
    items = [
        ("Transporte", resultado["transporte"]["total"]),
        ("Alimentação", resultado["alimentacao"]["total"]),
        ("Energia", resultado["energia"]["total"]),
        ("Resíduos", resultado["residuos"]["total"])
    ]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:3]



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

    resultado = calcular_pegada(transporte_info, alim_info, energia_info, res_info)
    total = resultado["total_ano"]
    perfil = perfil_por_total(total)
    comparar = comparar_com_medias(total)
    top3 = top_3_fontes(resultado)


if __name__ == "__main__":
    entrada_usuario()
