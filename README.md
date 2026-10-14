# Chatbot Customer Service "Kopi Senja"

Kopi Senja adalah proyek chatbot customer service untuk toko online fiktif yang dikembangkan menggunakan Python dan Google Gemini API. Chatbot ini memiliki dua antarmuka, yaitu versi terminal melalui `chatbot.py` dan versi web menggunakan Streamlit melalui `app.py`. Asisten chatbot ini bernama **Sena**.

## Daftar Isi

- [Fitur](#fitur)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Proyek](#struktur-proyek)
- [Alur Kerja Chatbot](#alur-kerja-chatbot)
- [Persiapan dan Instalasi](#persiapan-dan-instalasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Pengujian](#pengujian)
- [Kustomisasi](#kustomisasi)
- [Keamanan API Key](#keamanan-api-key)
- [Batasan Proyek](#batasan-proyek)

## Fitur

- Menjawab pertanyaan mengenai produk, harga, jam layanan, pengiriman, pembayaran, dan retur berdasarkan instruksi toko.
- Mempertahankan riwayat percakapan agar jawaban dapat mempertimbangkan pesan sebelumnya.
- Mengarahkan pertanyaan di luar topik Kopi Senja kembali ke layanan customer service.
- Menghindari pemberian informasi yang tidak tersedia dalam instruksi toko dan mengarahkan pelanggan ke customer service jika diperlukan.
- Menyediakan dua antarmuka, yaitu terminal dan web.
- Mencoba beberapa nama model secara berurutan serta mengulangi permintaan pada kondisi tertentu, seperti layanan sibuk atau batas permintaan tercapai.

## Teknologi yang Digunakan

- **Python**: bahasa pemrograman utama untuk mengembangkan chatbot.
- **Google Gemini API (`google-genai`)**: menghasilkan jawaban berdasarkan pesan pengguna dan instruksi sistem.
- **python-dotenv**: membaca konfigurasi API key dari file `.env`.
- **Streamlit**: membangun antarmuka chatbot berbasis web.
- **Git dan GitHub**: mengelola versi kode dan menyimpan repositori proyek.

## Struktur Proyek

```text
kopi-senja-chatbot/
├── chatbot.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

Penjelasan setiap file:

- `chatbot.py`: berisi instruksi sistem toko, fungsi komunikasi dengan Gemini API, mekanisme percobaan ulang, pemilihan model cadangan, dan antarmuka terminal.
- `app.py`: menyediakan antarmuka web menggunakan Streamlit dan mengelola riwayat percakapan selama sesi berlangsung.
- `requirements.txt`: berisi daftar pustaka Python yang diperlukan untuk menjalankan aplikasi.
- `.env.example`: menyediakan contoh konfigurasi variabel lingkungan tanpa menyertakan API key asli.
- `.gitignore`: mencegah file rahasia, cache Python, dan lingkungan virtual ikut dimasukkan ke Git.
- `README.md`: berisi dokumentasi proyek, proses instalasi, cara penggunaan, dan informasi pengembangan chatbot.

## Alur Kerja Chatbot

Proses kerja chatbot Kopi Senja terdiri dari beberapa tahapan berikut.

1. **Pengguna memasukkan pesan.** Pada versi terminal, pesan dimasukkan melalui terminal. Pada versi web, pengguna mengetik pesan melalui antarmuka chat Streamlit.

2. **Aplikasi memeriksa konfigurasi.** Program membaca `GEMINI_API_KEY` dari variabel lingkungan atau file `.env`. Jika API key tidak ditemukan, aplikasi menampilkan pesan kesalahan dan tidak melanjutkan permintaan.

3. **Riwayat percakapan disiapkan.** Pesan pengguna dan jawaban sebelumnya disimpan dalam riwayat percakapan. Pada versi web, riwayat dikelola menggunakan `st.session_state` selama sesi Streamlit berlangsung.

4. **Instruksi sistem diterapkan.** Variabel `SYSTEM_PROMPT` dalam `chatbot.py` mengatur identitas Sena, informasi toko fiktif, gaya bahasa, ruang lingkup pertanyaan, dan aturan respons chatbot.

5. **Permintaan dikirim ke Gemini API.** Program mengirim pesan dan riwayat percakapan ke model Gemini menggunakan pustaka `google-genai`, disertai instruksi sistem yang telah ditentukan.

6. **Model dipilih dan permintaan ditangani.** Program menggunakan daftar `DAFTAR_MODEL` untuk mencoba model yang tersedia secara berurutan. Jika model tidak ditemukan, program dapat mencoba model berikutnya. Pada kondisi tertentu, seperti layanan sibuk atau batas permintaan tercapai, program juga dapat mencoba kembali sesuai konfigurasi.

7. **Jawaban ditampilkan.** Respons dari Gemini ditampilkan kepada pengguna melalui terminal atau antarmuka web. Respons tersebut kemudian ditambahkan ke riwayat percakapan untuk membantu menjawab pesan berikutnya.

8. **Percakapan berlanjut atau diakhiri.** Pada versi terminal, pengguna dapat mengetik `keluar`, `exit`, atau `quit` untuk mengakhiri percakapan. Pada versi web, percakapan berlangsung selama sesi aplikasi.

## Persiapan dan Instalasi

### 1. Menyiapkan Lingkungan Pengembangan

Pastikan Python sudah terpasang di komputer dan dapat dijalankan melalui terminal. Setelah itu, buka terminal di VS Code dan masuk ke folder proyek.

```powershell
cd D:\kopi-senja-chatbot
```

Sesuaikan lokasi folder jika proyek disimpan di direktori yang berbeda.

### 2. Membuat Lingkungan Virtual

Untuk memisahkan dependensi proyek dari proyek Python lainnya, buat lingkungan virtual menggunakan perintah berikut:

```powershell
python -m venv .venv
```

Aktifkan lingkungan virtual di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Langkah ini disarankan agar pengelolaan dependensi lebih teratur.

### 3. Memasang Dependensi

Pasang seluruh pustaka yang tercantum dalam `requirements.txt` menggunakan perintah:

```bash
python -m pip install -r requirements.txt
```

Dependensi proyek mencakup `google-genai`, `python-dotenv`, dan `streamlit`.

### 4. Membuat API Key Google Gemini

Buka [Google AI Studio](https://aistudio.google.com/) untuk membuat API key yang digunakan aplikasi dalam mengakses Gemini API.

Ketersediaan model, akses, dan kuota mengikuti ketentuan layanan Google yang berlaku.

### 5. Mengatur File `.env`

Salin file `.env.example` menjadi `.env` di folder utama proyek. Pada Windows PowerShell, jalankan:

```powershell
Copy-Item .env.example .env
```

Buka file `.env`, kemudian isi API key pada variabel berikut:

```env
GEMINI_API_KEY=isi_api_key_kamu
```

Ganti `isi_api_key_kamu` dengan API key milik sendiri. Pastikan nama variabel sesuai dengan yang digunakan dalam kode program.

**Penting:** Jangan mengunggah file `.env` ke GitHub karena file tersebut berisi informasi rahasia.

### 6. Memeriksa Konfigurasi Model

Program pada `chatbot.py` menggunakan daftar model yang disimpan dalam `DAFTAR_MODEL`. Nama model yang tersedia dapat berubah mengikuti layanan Google Gemini API.

Jika terjadi kesalahan karena model tidak ditemukan, periksa daftar model dan sesuaikan dengan model yang tersedia untuk API key yang digunakan.

## Menjalankan Aplikasi

Sebelum menjalankan chatbot, pastikan dependensi telah terpasang dan file `.env` sudah dikonfigurasi.

### 1. Menjalankan Versi Terminal

Jalankan perintah berikut:

```bash
python chatbot.py
```

Chatbot akan menampilkan salam pembuka dan menerima pertanyaan melalui terminal. Ketik pertanyaan pada prompt `Kamu:` untuk memulai percakapan.

Untuk mengakhiri program, ketik salah satu perintah berikut:

- `keluar`
- `exit`
- `quit`

### 2. Menjalankan Versi Web

Jalankan perintah berikut:

```bash
streamlit run app.py
```

Setelah perintah dijalankan, Streamlit akan menampilkan alamat lokal di terminal. Buka alamat tersebut melalui browser untuk menggunakan chatbot berbasis web.

## Pengujian

Pengujian dilakukan untuk memeriksa apakah chatbot dapat berjalan sesuai dengan kebutuhan yang telah ditentukan. Pengujian dapat dilakukan secara manual melalui versi terminal dan web.

Beberapa skenario pengujian yang dapat dilakukan meliputi:

1. **Pengujian informasi produk dan harga**  
   Masukkan pertanyaan mengenai produk atau harga, kemudian periksa apakah jawaban sesuai dengan informasi yang ditetapkan dalam instruksi sistem.

2. **Pengujian informasi layanan**  
   Tanyakan jam layanan, pengiriman, pembayaran, atau retur untuk memeriksa kesesuaian jawaban chatbot.

3. **Pengujian pertanyaan di luar topik**  
   Masukkan pertanyaan yang tidak berhubungan dengan Kopi Senja untuk memeriksa apakah chatbot mengarahkan percakapan kembali ke layanan toko.

4. **Pengujian informasi yang tidak tersedia**  
   Tanyakan informasi yang tidak tercantum dalam instruksi sistem untuk memeriksa apakah chatbot menghindari jawaban yang dibuat-buat.

5. **Pengujian riwayat percakapan**  
   Kirim beberapa pertanyaan yang saling berkaitan untuk memeriksa apakah chatbot mempertimbangkan pesan sebelumnya.

6. **Pengujian konfigurasi API key**  
   Jalankan aplikasi tanpa konfigurasi `GEMINI_API_KEY` untuk memeriksa apakah aplikasi menampilkan pesan kesalahan yang sesuai.

7. **Pengujian antarmuka aplikasi**  
   Jalankan versi terminal dan web untuk memastikan kedua antarmuka dapat digunakan.

8. **Pengujian penanganan kesalahan API**  
   Periksa perilaku aplikasi ketika model tidak tersedia, layanan mengalami gangguan, atau batas permintaan tercapai.

Hasil pengujian perlu dicatat berdasarkan pengujian yang benar-benar dilakukan. Jangan menyatakan seluruh pengujian berhasil sebelum setiap skenario diperiksa.

## Kustomisasi

Instruksi sistem, informasi toko, gaya bahasa, ruang lingkup pertanyaan, dan aturan respons chatbot dapat disesuaikan melalui variabel `SYSTEM_PROMPT` di `chatbot.py`.

Pengaturan model dan mekanisme percobaan ulang dapat disesuaikan melalui konstanta berikut:

- `DAFTAR_MODEL`: daftar model yang akan dicoba oleh aplikasi.
- `PERCOBAAN_PER_MODEL`: jumlah percobaan permintaan sesuai konfigurasi program.
- `JEDA_DETIK`: jeda yang digunakan dalam mekanisme percobaan ulang.

Versi web menggunakan fungsi `minta_jawaban` dari `chatbot.py`, sehingga perubahan pada logika chatbot di file tersebut dapat memengaruhi kedua antarmuka.

## Keamanan API Key

Keamanan API key perlu diperhatikan selama proses pengembangan dan pengelolaan repositori.

- Simpan API key hanya di file `.env` lokal.
- Jangan mengunggah atau melakukan commit terhadap file `.env`.
- Gunakan `.env.example` untuk mendokumentasikan nama variabel konfigurasi tanpa memasukkan nilai rahasia.
- Pastikan file `.env` tercantum dalam `.gitignore`.
- Jangan menuliskan API key secara langsung di kode sumber, README, pesan commit, atau tangkapan layar.
- Jika API key pernah terekspos, segera cabut atau ganti key melalui layanan penyedia API.

Menghapus file `.env` dari commit terbaru saja tidak menjamin API key hilang dari riwayat Git. Oleh karena itu, riwayat commit juga perlu diperiksa apabila rahasia pernah dimasukkan ke repositori.

## Batasan Proyek

Chatbot Kopi Senja memiliki beberapa batasan berikut:

- Kopi Senja merupakan toko fiktif. Informasi produk dan layanan ditentukan melalui instruksi sistem dalam program.
- Chatbot memerlukan koneksi internet dan akses ke Google Gemini API.
- Jawaban yang dihasilkan AI dapat keliru sehingga tetap perlu diperiksa.
- Riwayat percakapan disimpan selama program terminal berjalan atau selama sesi Streamlit berlangsung, bukan sebagai riwayat permanen dalam database.
- Proyek ini belum menyediakan sistem transaksi atau pemesanan, pembayaran otomatis, pengelolaan inventaris, maupun pelacakan pengiriman secara real-time.

