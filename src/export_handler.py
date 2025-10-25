import os
import json
import pandas as pd
from datetime import datetime
from config import csv_folder, json_folder

class ExportHandler:
    """
    Classe responsável por exportar dados de QR Codes para diferentes formatos.
    Suporta CSV e JSON, podendo ser expandida futuramente (Excel, BD, etc).
    """

    def __init__(self):
        # Caminhos dos arquivos e criação das pastas
        self.csv_path = os.path.join(csv_folder, "qrcode_data.csv")
        self.json_path = os.path.join(json_folder, "qrcode_data.json")
        os.makedirs(csv_folder, exist_ok=True)
        os.makedirs(json_folder, exist_ok=True)

    def exportar_csv(self, dados: dict):
        """
        Exporta os dados do QR code para um arquivo CSV.
        """
        novo_df = pd.DataFrame([dados])
        if os.path.exists(self.csv_path):
            df_antigo = pd.read_csv(self.csv_path)
            df_final = pd.concat([df_antigo, novo_df], ignore_index=True)
        else:
            df_final = novo_df

        df_final.to_csv(self.csv_path, index=False)

    def exportar_json(self, dados: dict):
        """
        Exporta os dados do QR code para um arquivo JSON (lista cumulativa).
        """
        if os.path.exists(self.json_path):
            with open(self.json_path, "r", encoding="utf-8") as f:
                antigos = json.load(f)
            if not isinstance(antigos, list):
                antigos = [antigos]
            antigos.append(dados)
        else:
            antigos = [dados]

        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(antigos, f, indent=4, ensure_ascii=False)


    def registrar(self, ssid: str, password: str, security: str, arquivo: str):
        """
        Cria o dicionário de dados e exporta automaticamente para CSV e JSON.
        """
        dados = {
            "SSID": ssid,
            "Password": password,
            "Security": security,
            "arquivo": arquivo,
            "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.exportar_csv(dados)
        self.exportar_json(dados)
        return dados
