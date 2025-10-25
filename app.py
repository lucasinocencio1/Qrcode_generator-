import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
import streamlit as st
from dotenv import load_dotenv
from src.qr_code_generator import QrcodeGenerator
from src.export_handler import ExportHandler
import os

st.set_page_config(page_title="Gerador de QR Code Wi-Fi", page_icon="📶")

st.title("📶 Gerador de QR Code Wi-Fi")
st.write("Crie e compartilhe QR Codes do seu Wi-Fi com seus amigos! 😄")

ssid = st.text_input("Nome da rede Wi-Fi (SSID):")
password = st.text_input("Senha do Wi-Fi:")
security = st.selectbox("Tipo de segurança:", ["WPA", "WEP", "Nenhuma"])

gerar = st.button("Gerar QR Code")

if gerar:
    if not ssid or not password:
        st.warning("Por favor, preencha o SSID e a senha!")
    else:
        generator = QrcodeGenerator(ssid, password, security)
        caminho_qr = generator.salvar_qrcode(filename=f"{ssid}_wifi_qrcode.png", mostrar=False)

        exporter = ExportHandler()
        exporter.registrar(ssid, password, security, caminho_qr)

        st.image(caminho_qr, caption="Seu QR Code", use_column_width=True)

        with open(caminho_qr, "rb") as f:
            st.download_button(
                label="📥 Baixar QR Code",
                data=f,
                file_name=f"{ssid}_wifi_qrcode.png",
                mime="image/png",
            )
