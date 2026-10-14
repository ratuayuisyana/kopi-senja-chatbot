# Chatbot Customer Service "Kopi Senja"

Chatbot customer service untuk toko online fiktif "Kopi Senja", dibuat dengan Python dan Google Gemini API (gratis).

## Fitur
- Menjawab pertanyaan seputar produk, harga, pengiriman, pembayaran, dan retur
- Mengingat riwayat percakapan
- Menolak pertanyaan di luar topik toko
- Tersedia versi terminal (`chatbot.py`) dan versi web (`app.py`)

## Cara Menjalankan

1. Ambil API key gratis di https://aistudio.google.com (menu "Get API key").
2. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
3. Salin `.env.example` menjadi `.env`, lalu isi API key kamu:
   ```
   GEMINI_API_KEY=api_key_kamu
   ```
4. Jalankan salah satu:
   ```
   python chatbot.py        # versi terminal
   streamlit run app.py     # versi web
   ```

## Kustomisasi
Edit variabel `SYSTEM_PROMPT` di `chatbot.py` untuk mengganti nama toko, produk, harga, atau gaya bicara bot.

## Catatan
- Jangan upload file `.env` ke GitHub (tambahkan ke `.gitignore`).
- Jika muncul error nama model, ganti nilai `MODEL` di `chatbot.py` sesuai model terbaru di AI Studio.
