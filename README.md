# Football Shop

## Identitas
- Nama: Khalisa Adzkiyah  
- NPM: 2406418995  
- Kelas: A  

## Link PWS
[https://khalisa-adzkiyah-footballshop.pbp.cs.ui.ac.id/](https://khalisa-adzkiyah-footballshop.pbp.cs.ui.ac.id/)

## Cara Menjalankan (Lokal)
1. `python -m venv env`
2. `.\env\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`
6. Buka [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Implementasi (Step-by-Step)
1. Membuat project Django `football-shop` dengan `django-admin startproject football-shop .`
2. Membuat aplikasi `main` dengan `python manage.py startapp main` dan mendaftarkannya di `INSTALLED_APPS`
3. Mendefinisikan model `Product` di `main/models.py` dengan field:
   - `name`, `price`, `description`, `thumbnail`, `category`, `is_featured`
4. Menjalankan `makemigrations` dan `migrate`
5. Register model di `main/admin.py`
6. Membuat view `show_main` di `main/views.py` dan template `main/templates/main/main.html`
7. Membuat `main/urls.py`, lalu include ke `football_shop/urls.py`
8. Menambahkan files untuk deploy (`requirements.txt`, `.env.prod`), commit & push, lalu deploy ke PWS

## Bagan Request–Response
Client (browser) -> `football_shop/urls.py` -> include(`main.urls`) -> `main/urls.py` -> `views.show_main` -> 
query ke `Product` model (`models.py`) -> render `main/templates/main/main.html` -> response HTML → Client  

**Kaitan file**:
- `urls.py` -> menerima request & arahkan ke view
- `views.py` -> ambil data dari model & render template
- `models.py` -> definisi struktur data (ORM)
- `settings.py` -> konfigurasi global (DB, ALLOWED_HOSTS, static, dll)

## Peran settings.py
File konfigurasi utama: menyimpan `INSTALLED_APPS`, database, flag `DEBUG/PRODUCTION`, `ALLOWED_HOSTS`, static files, SECRET_KEY, dsb.

## Cara Kerja Migrasi
- `makemigrations` -> membuat file migration berdasarkan perubahan di model
- `migrate` -> menerapkan perubahan schema ke database (buat/ubah tabel)

## Kenapa Django Diajarkan Awal
- "Batteries-included" -> banyak fitur bawaan (ORM, admin, auth)
- Struktur MVT jelas -> memisahkan logic, data, dan UI
- Dokumentasi lengkap & banyak contoh -> cocok untuk pemula

## Feedback untuk Asdos
Tutorial jelas dan membantu.
