import qrcode # para gerar o Qrcode
import os # para acessar as variáveis de ambiente
from dotenv import load_dotenv # para carregar as variáveis de ambiente
import pandas as pd # para trabalhar com DataFrames
from datetime import datetime # para trabalhar com datas
from config import output_folder
from config import back_color as default_back_color
from config import fill_color as default_fill_color
from config import border as default_border
from config import box_size as default_box_size

#Criar uma classe para o Qrcode Generator
class QrcodeGenerator:
    def __init__(self, ssid:str, password:str, security:str, box_size:float=None, border:float=None, fill_color:str=None, back_color:str=None):
        self.ssid = ssid
        self.password = password
        self.security = security
        self.box_size = box_size if box_size is not None else default_box_size
        self.border = border if border is not None else default_border
        self.fill_color = fill_color if fill_color is not None else default_fill_color
        self.back_color = back_color if back_color is not None else default_back_color
        self.output_folder = output_folder
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
            return caminho  # Retorna o caminho do arquivo salvo
