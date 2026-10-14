"""Chatbot Customer Service "Kopi Senja" (versi web dengan Streamlit).

Jalankan:  streamlit run app.py
"""
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

from chatbot import minta_jawaban

load_dotenv()

st.set_page_config(page_title="Kopi Senja CS", page_icon="☕")
st.title("☕ Kopi Senja")
st.caption("Customer Service dengan asisten Sena")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY belum diisi. Lihat README.md.")
    st.stop()

client = genai.Client(api_key=api_key)

if "riwayat" not in st.session_state:
    st.session_state.riwayat = [
        {"role": "assistant", "text": "Halo! Saya Sena dari Kopi Senja. Ada yang bisa saya bantu?"}
    ]

# tampilkan riwayat chat
for item in st.session_state.riwayat:
    with st.chat_message(item["role"]):
        st.write(item["text"])

pesan = st.chat_input("Tulis pertanyaanmu di sini...")
if pesan:
    st.session_state.riwayat.append({"role": "user", "text": pesan})
    with st.chat_message("user"):
        st.write(pesan)

    with st.chat_message("assistant"):
        with st.spinner("Sena sedang mengetik..."):
            jawaban = minta_jawaban(client, st.session_state.riwayat)
        st.write(jawaban)

    st.session_state.riwayat.append({"role": "assistant", "text": jawaban})
