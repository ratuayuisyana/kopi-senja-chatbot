"""Chatbot Customer Service "Kopi Senja" (versi terminal).

Jalankan:  python chatbot.py
"""
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # baca GEMINI_API_KEY dari file .env

# Daftar model dicoba berurutan. Kalau satu sibuk (503) atau tidak ada (404),
# bot otomatis pindah ke model berikutnya. Edit daftar ini sesuai AI Studio.
DAFTAR_MODEL = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
]
PERCOBAAN_PER_MODEL = 2  # berapa kali mencoba ulang tiap model
JEDA_DETIK = 3           # jeda antar percobaan

# Data toko fiktif. Ubah sesuai kreativitasmu.
SYSTEM_PROMPT = """
Kamu adalah "Sena", asisten customer service dari toko online fiktif bernama "Kopi Senja".
Gaya bicara: ramah, sopan, santai, memakai Bahasa Indonesia, dan singkat (maksimal 4 kalimat).

INFORMASI TOKO:
- Produk: Kopi Arabika Gayo (Rp85.000/250g), Kopi Robusta Lampung (Rp60.000/250g),
  Kopi Toraja (Rp95.000/250g), Cold Brew Botol (Rp28.000/botol).
- Jam operasional CS: Senin-Sabtu, 08.00-20.00 WIB.
- Pengiriman: seluruh Indonesia lewat JNE dan J&T. Estimasi 2-5 hari kerja.
- Ongkir: gratis untuk pembelian di atas Rp150.000.
- Pembayaran: transfer bank, QRIS, dan e-wallet (GoPay, OVO, DANA).
- Retur: maksimal 3 hari setelah barang diterima, kirim foto bukti jika barang rusak.
- Kontak: cs@kopisenja.example | WhatsApp 0812-0000-0000 (fiktif).

ATURAN:
- Jawab hanya seputar Kopi Senja (produk, pesanan, pengiriman, pembayaran, retur).
- Jika ditanya hal di luar topik, tolak dengan sopan dan arahkan kembali ke topik toko.
- Jika informasi tidak ada di atas, jangan mengarang. Arahkan pelanggan ke kontak CS.
- Jangan pernah meminta password atau data kartu kredit pelanggan.
"""


def minta_jawaban(client, riwayat):
    """Kirim riwayat chat ke Gemini dengan retry dan model cadangan.

    riwayat: list of {"role": "user" | "assistant", "text": "..."}
    Mengembalikan teks jawaban, atau pesan gangguan jika semua model gagal.
    """
    contents = [
        types.Content(
            role="user" if h["role"] == "user" else "model",
            parts=[types.Part(text=h["text"])],
        )
        for h in riwayat
    ]
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)

    error_terakhir = None
    for model in DAFTAR_MODEL:
        for percobaan in range(PERCOBAAN_PER_MODEL):
            try:
                respon = client.models.generate_content(
                    model=model, contents=contents, config=config
                )
                if respon.text:
                    return respon.text
            except Exception as e:
                error_terakhir = e
                pesan_error = str(e)
                if "404" in pesan_error or "NOT_FOUND" in pesan_error:
                    break  # model tidak ada, langsung coba model berikutnya
                if "503" in pesan_error or "UNAVAILABLE" in pesan_error or "429" in pesan_error:
                    time.sleep(JEDA_DETIK)
                    continue  # server sibuk, coba lagi
                break  # error lain (misalnya API key salah), pindah model
    return f"Maaf, semua server sedang sibuk. Coba lagi beberapa saat. ({error_terakhir})"


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY belum diisi. Lihat README.md.")

    client = genai.Client(api_key=api_key)
    riwayat = []

    print("=== Kopi Senja Customer Service ===")
    print("Ketik 'keluar' untuk mengakhiri.\n")
    print("Sena: Halo! Saya Sena dari Kopi Senja. Ada yang bisa saya bantu?\n")

    while True:
        pesan = input("Kamu: ").strip()
        if not pesan:
            continue
        if pesan.lower() in ("keluar", "exit", "quit"):
            print("Sena: Terima kasih sudah menghubungi Kopi Senja. Sampai jumpa!")
            break
        riwayat.append({"role": "user", "text": pesan})
        jawaban = minta_jawaban(client, riwayat)
        riwayat.append({"role": "assistant", "text": jawaban})
        print(f"Sena: {jawaban}\n")


if __name__ == "__main__":
    main()