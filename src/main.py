import os
from dotenv import load_dotenv
from qr_code_generator import criar_qrcode, salvar_qrcode
from config import BOX_SIZE, BORDER, FILL_COLOR, BACK_COLOR

def main():
    load_dotenv()

    ssid = os.getenv("my_ssid", "Minha Rede Wifi")
    password = os.getenv("my_password", "123456")
    security = os.getenv("my_security", "WPA")

    img = criar_qrcode(ssid, password, security, BOX_SIZE, BORDER, FILL_COLOR, BACK_COLOR)
    salvar_qrcode(img)


if __name__ == "__main__":
    main()    
