import os
from dotenv import load_dotenv
from qr_code_generator import QrcodeGenerator
from export_handler import ExportHandler
from config import csv_folder, json_folder

def main():
    load_dotenv()

    # Configurações do WiFi
    ssid = os.getenv("my_ssid", "Minha Rede Wifi")
    password = os.getenv("my_password", "123456")
    security = os.getenv("my_security", "WPA")

    # Criar instância do gerador
    generator = QrcodeGenerator(ssid, password, security)
    
    # Salvar o QR code e obter o caminho
    caminho_qr = generator.salvar_qrcode()
    
    # Exporta resultados (CSV + JSON)
    exporter = ExportHandler()
    exporter.registrar(ssid, password, security, caminho_qr)


if __name__ == "__main__":
    main()    
