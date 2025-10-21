"""
=== Desafio do Dia 50 – Automatizador de Rotina de Arquivos ===

Objetivo:
Criar um programa que automatize a organização de arquivos em uma pasta,
classificando-os automaticamente em subpastas conforme sua extensão
(ex: imagens, documentos, vídeos, áudios e outros).

Contexto:
No dia a dia, acumulamos muitos arquivos no computador (downloads, documentos, prints, etc).
Esse desafio propõe criar uma automação simples que organiza esses arquivos
automaticamente, poupando tempo e mantendo o sistema limpo.

Funcionalidades:
1. Pedir o caminho da pasta a ser organizada
2. Criar subpastas automaticamente (imagens, documentos, vídeos, áudios, outros)
3. Mover cada arquivo para a subpasta correta
4. Mostrar um resumo da ação (quantos arquivos foram movidos para cada categoria)

"""

import os
import shutil

CATEGORIAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".mkv", ".mov", ".avi"],
    "Áudios": [".mp3", ".wav", ".aac", ".flac"]
}

def organizar_pasta(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        print("Caminho invalido. Verifique e tente novamente.")
        return
    arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
    resumo = {categoria: 0 for categoria in CATEGORIAS}
    resumo["Outros"] = 0
    for arquivo in arquivos:
        _, extensao = os.path.splitext(arquivo)
        movido = False
        for categoria, extensoes in CATEGORIAS.items():
            if extensao.lower() in extensoes:
                pasta_destino = os.path.join(caminho_pasta, categoria)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(os.path.join(caminho_pasta, arquivo), os.path.join(pasta_destino, arquivo))
                resumo[categoria] += 1
                movido = True
                break
        if not movido:
            pasta_outros = os.path.join(caminho_pasta, "Outros")
            os.makedirs(pasta_outros, exist_ok=True)
            shutil.move(os.path.join(caminho_pasta, arquivo), os.path.join(pasta_outros, arquivo))
            resumo["Outros"] += 1


    print("\nOrganização concluida!")
    print("Resumo:")
    for categoria, quantidade in resumo.items():
        print(f"- {categoria}: {quantidade} arquivo(s)")





if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta que deseja organizar: ").strip()
    organizar_pasta(caminho)
