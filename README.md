# Tugas 2
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


# Tugas 3


## 1. Mengapa kita memerlukan data delivery?
Data delivery diperlukan agar backend dapat mengirimkan data ke konsumen (frontend, mobile app, service lain) dalam format yang terstruktur dan dapat di-parse (mis. JSON, XML). Manfaatnya:
- **Interoperabilitas**: berbagai client / language dapat mengonsumsi data yang sama.  
- **Decoupling**: frontend dan backend bisa dikembangkan terpisah.  
- **Automasi & integrasi**: microservice, webhook, atau sistem pihak ketiga dapat mengakses data secara otomatis.  
- **Efisiensi**: format seperti JSON biasanya lebih ringkas sehingga mengurangi latensi / ukuran payload.


## 2. XML vs JSON, mana yang lebih baik? Mengapa JSON lebih populer dibandingkan XML?
- **JSON** lebih populer untuk web API modern karena:
  - Sintaks lebih ringkas (less verbose) -> bandwidth lebih hemat.
  - Native di JavaScript -> parsing/serialisasi mudah (`JSON.parse` / `JSON.stringify`).
  - Umumnya lebih cepat dan lebih sederhana untuk dipakai di REST API.
- **XML** masih berguna jika butuh fitur-fitur tertentu seperti namespace, XSD/schema validation, transformasi XSLT, atau kompatibilitas dengan sistem lama (legacy).
- **Kesimpulan**: untuk kebanyakan aplikasi web/mobile saat ini JSON lebih praktis, pilih XML hanya bila butuh fitur spesifik XML.


## 3. Fungsi `is_valid()` pada Django Form dan mengapa diperlukan
- `form.is_valid()` menjalankan validasi semua field, memanggil `clean_field()` dan `clean()` (jika ada), serta validator field.  
- Jika `is_valid()` mengembalikan `True`, data aman diakses lewat `form.cleaned_data`. Jika `False`, `form.errors` berisi pesan error.  
- **Kenapa penting**: mencegah data invalid/berbahaya tersimpan ke database, memastikan integritas data sebelum `form.save()` atau operasi lain.


Contoh pemakaian:
```python
form = ProductForm(request.POST)
if form.is_valid():
    form.save()
else:
    # tampilkan form.errors ke user


# 4. Mengapa perlu csrf_token di form Django? Risiko jika tidak ada?
- csrf_token mencegah Cross-Site Request Forgery (CSRF): serangan yang memaksa browser user (yang sudah login) mengirim request (biasanya POST) ke situs kita melalui halaman jahat.
- Tanpa CSRF protection, penyerang bisa membuat form di situs lain yang mengirim POST ke endpoint internal (mis. hapus/ubah data) atas nama user yang sedang login.
- csrf_token memastikan request POST berasal dari template/form yang valid dari domain kita — server memverifikasi token tersebut.
- Contoh:
<form method="POST">
  {% csrf_token %}
  <!-- fields -->
</form>

# 5. Langkah implementasi checklist (step-by-step, bukan sekadar copi dari tutorial)
1. **Menambahkan 4 fungsi views baru**  
   - `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` ditambahkan pada `views.py` menggunakan `serializers.serialize()`.

2. **Membuat routing URL untuk tiap view**  
   - Menambahkan path baru di `main/urls.py` untuk mengakses masing-masing fungsi (`/xml/`, `/json/`, `/xml/<id>/`, `/json/<id>/`).

3. **Membuat halaman list produk (main.html)**  
   - Menampilkan semua objek `Product`.
   - Ditambahkan tombol **Add** yang mengarah ke form tambah produk.
   - Ditambahkan tombol **Detail** di tiap produk untuk melihat detail.

4. **Membuat halaman form tambah produk**  
   - Membuat `forms.py` dengan `ProductForm` (berbasis `ModelForm`).
   - Membuat view `add_product` untuk menampilkan form dan menyimpan data jika valid.
   - Membuat template `add_product.html` berisi form dengan `{% csrf_token %}`.

5. **Membuat halaman detail produk**  
   - View `product_detail` menampilkan detail produk berdasarkan ID.
   - Template `product_detail.html` dibuat untuk menampilkan informasi detail produk.

## Hasil Pengujian dengan Postman

### 1. Endpoint XML (All Objects)
![XML All](assets/xml_all.png)

### 2. Endpoint JSON (All Objects)
![JSON All](assets/json_all.png)

### 3. Endpoint XML by ID
![XML by ID](assets/xml_by_id.png)

### 4. Endpoint JSON by ID
![JSON by ID](assets/json_by_id.png)

### Feedback untuk Asdos
Tutorial 2 sudah jelas dan membantu memahami konsep dasar. 