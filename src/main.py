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
    
    # Salvar o QR code e obter o caminho
    caminho_qr = generator.salvar_qrcode()
    
    # Criar DataFrame com os dados usando o caminho real
    df = generator.criar_dataframe(caminho_qr)
    print("📊 DataFrame:")
    print(df)
    
    # Criar JSON com os dados usando o caminho real
    json_data = generator.criar_json(caminho_qr)
    print("📄 JSON:")
    print(json_data)


if __name__ == "__main__":
    main()    
