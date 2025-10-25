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

def salvar_qrcode(img):
   """
   Essa função cria o Qrcode e salva na pasta de destino
   """
   #path para pasta de destino
   path_destino = "qrcode_png"
   os.makedirs(path_destino, exist_ok=True)

   #path completo par o arquivo
   caminho_arquivo = os.path.join(path_destino, "qrcode.png") #salar na pasta qrcode_png

   #salvar o Qrcode  
   img.save(caminho_arquivo)
   print(f"QR code salvo como '{caminho_arquivo}'")
   img.show() #mostrar o Qrcode na tela


#criamos uma pasta main para executar o programa
# def main():
#     load_dotenv()
    
#     # Configurações do WiFi
#     ssid = os.getenv("my_ssid", "Minha Rede Wifi") # Mudar para o SSID da rede WiFi (Usar .env para garantir segurança)
#     password = os.getenv("my_password", "123456") # Mudar para a senha da rede WiFi (Usar .env para garantir segurança)
#     security = os.getenv("my_security", "WPA") # Mudar para a segurança da rede WiFi (Usar .env para garantir segurança)
    
#     # Configurações visuais do QR code
#     box_size = BOX_SIZE      # Tamanho dos quadrados
#     border = BORDER         # Espessura da borda
#     fill_color = FILL_COLOR    # Cor dos quadrados
#     back_color = BACK_COLOR    # Cor de fundo
    
#     # Criar o Qrcode
#     img = criar_qrcode(ssid, password, security, box_size, border, fill_color, back_color)

#     #salvar o Qrcode
#     salvar_qrcode(img)


# #Executar o programa diretamente no terminal: python src/exemple.py
# if __name__ == "__main__":
#     main()
