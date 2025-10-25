import qrcode # para gerar o Qrcode
import os # para acessar as variáveis de ambiente
from dotenv import load_dotenv # para carregar as variáveis de ambiente

def criar_qrcode(ssid, password, security, box_size, border, fill_color, back_color):    #função para criar o Qrcode
    """
    Cria um QR code com parâmetros personalizáveis
    """
    wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def main():
    load_dotenv()
    
    # Configurações do WiFi
    ssid = os.getenv("my_ssid", "Minha Rede Wifi") # Mudar para o SSID da rede WiFi (Usar .env para garantir segurança)
    password = os.getenv("my_password", "123456") # Mudar para a senha da rede WiFi (Usar .env para garantir segurança)
    security = os.getenv("my_security", "WPA") # Mudar para a segurança da rede WiFi (Usar .env para garantir segurança)
    
    # Configurações visuais do QR code
    box_size = 10      # Tamanho dos quadrados
    border = 4         # Espessura da borda
    fill_color = "black"    # Cor dos quadrados
    back_color = "white"    # Cor de fundo
    
    # Criar e salvar o QR code
    img = criar_qrcode(ssid, password, security, box_size, border, fill_color, back_color)
    img.save("qrcode.png")
    print("QR code salvo como 'qrcode.png'")
    
    # Mostrar na tela
    img.show()

#Executar o programa diretamente no terminal: python src/exemple.py
if __name__ == "__main__":
    main()
