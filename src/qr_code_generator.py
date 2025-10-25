import qrcode # para gerar o Qrcode
import os # para acessar as variáveis de ambiente
from dotenv import load_dotenv # para carregar as variáveis de ambiente
from config import OUTPUT_FOLDER, BACK_COLOR, FILL_COLOR, BORDER, BOX_SIZE # para acessar as configurações

#Criar uma classe para o Qrcode Generator
class QrcodeGenerator:
    def __init__(self, ssid:str, password:str, security:str, box_size:float=None, border:float=None, fill_color:str=None, back_color:str=None):
        self.ssid = ssid
        self.password = password
        self.security = security
        self.box_size = box_size or BOX_SIZE
        self.border = border or BORDER
        self.fill_color = fill_color or FILL_COLOR
        self.back_color = back_color or BACK_COLOR
        self.output_folder = OUTPUT_FOLDER
        os.makedirs(self.output_folder, exist_ok=True)

    def criar_qrcode(self):    #função para criar o Qrcode
        """
        Cria um QR code com parâmetros personalizáveis
        """
        wifi_data = f"WIFI:S:{self.ssid};T:{self.security};P:{self.password};;"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(wifi_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        return img

    def salvar_qrcode(self, filename:str="qrcode.png", mostrar:bool=True):
            """
            Gera e salva o QR code em um arquivo PNG.
            """
            img = self.criar_qrcode()
            caminho = os.path.join(self.output_folder, filename)
            img.save(caminho)
            print(f"✅ QR code salvo em: {caminho}")
            if mostrar:
                img.show()
