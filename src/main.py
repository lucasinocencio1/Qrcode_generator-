import os
from dotenv import load_dotenv
from qr_code_generator import QrcodeGenerator

def main():
    load_dotenv()

    # Configurações do WiFi
    ssid = os.getenv("my_ssid", "Minha Rede Wifi")
    password = os.getenv("my_password", "123456")
    security = os.getenv("my_security", "WPA")

    # Criar instância do gerador
    generator = QrcodeGenerator(ssid, password, security)
    #Salvar o QR code
    generator.salvar_qrcode()


if __name__ == "__main__":
    main()    
