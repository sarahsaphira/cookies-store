# cookies-store
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Cara Pengerjaan Checklist
- Membuat sebuah proyek Django baru.
- Membuat direktori baru bernama cookies-store yang akan dijadikan local directory
- Membuat repository github baru bernama cookies-store
- Membuat file README.md dan mengeditnya melalui VSCODE
- Membuka CMD pada directory cookies-store dan menjalankan git init, git branch -M main, git remote add origin https://github.com/sarahsaphira/cookies-store.git, dan git push -u origin main untuk membuat main branch dengan nama main, menghubungkan local directory/repository dengan repository github, dan push/update semua perubahan ke github
- Menjalankan python3 -m venv env untuk membuat virtual environment untuk directory agar dapat maintain versi-versi django dan lain sebagainya yang dipakai di device
- Menjalankan source env/bin/activate untuk mengaktifkan virtual environment
- Membuat file baru bernama requirements.txt dan mengisinya dengan hal-hal yang ingin diinstall agar tidak terlalu banyak menjalankan command pip install, saya mengisinya dengan:
- Menjalankan pip install -r requirements.txt untuk install hal-hal yang telah ditambahkan pada requirements.txt tadi
- Menjalankan django-admin startproject cookies_store .
- Membuka file settings.py dan ubah ALLOWED_HOSTS = [] menjadi ALLOWED_HOSTS = ["localhost", "127.0.0.1"] karena akan diperlukan untuk proses deployment
- Membuat file baru bernama .gitignore untuk memberikan informasi mengenai berkas yang perubahannya tidak perlu ditrack oleh Git,
- Membuat aplikasi dengan nama main pada proyek tersebut.
- Masih pada CMD yang sama, jalankan python3 manage.py startapp main untuk membuat django app baru bernama main pada django project bernama cookies_store
- Membuka file settings.py dan tambahkan 'main' pada variabel INSTALLED_APPS
- Membuka directory main dan buat directory baru bernama templates untuk menyimpan file main.html yang akan digunakan karena django menggunakan Model-View-Template (MVT)
- Membuat file baru bernama main.html pada directory templates dan mengisinya dengan konten-konten yang diperlukan. 
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Membuka file urls.py pada directory cookies_store
- Menambahkan from django.urls import path, include
- Mengubah urlpatterns menjadi:
urlpatterns = [
    path('', include('main.urls')),
]

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

- membuka models.py dan mengisinya dengan attributes/fields yang diperlukan. Pada kasus ini, saya menggunakan 3 attributes, yakni name (CharField), price (IntegerField), description (TextField). Isi file models.py adalah sebagai berikut:
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

- Membuka views.py dan menambahkan potongan kode di bawah ini untuk menghubungkan Views dan Templates. Sehingga, isi views.py sebagai berikut:
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306240093',
        'name': 'Sarah Saphira Setiawan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

- ubah urlpatterns menjadi seperti ini:
urlpatterns = [
    path('', show_main, name='show_main'), 
]

- Menjalankan git push origin main, git add . , git commit -m "message", dan git push -u origin main untuk update github repository agar sesuai dengan local repository

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/sarahsaphira/cookies-store/blob/1b0f33067c635ff55e09f6e077944304a335bbb5/BaganNomor2.png)

- Client mengirim request ke Internet -> forward ke Python/Django -> forward ke urls.py -> forward ke views.py untuk memproses url -> read/write data dari/ke models.py dan database -> input/display data dari/ke templates -> return html file yang telah dimerge dengan value-value yang diinginkan -> proses ke internet -> display ke client's device

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

- Git berfungsi sebagai alat penting dalam pengembangan perangkat lunak karena membantu tim pengembang mengelola perubahan pada kode. Dengan Git, setiap perubahan yang dilakukan dicatat, sehingga pengembang bisa melihat versi-versi sebelumnya, siapa yang melakukan perubahan, dan alasan perubahan tersebut.

- Git juga memudahkan kerja sama tim. Beberapa orang bisa bekerja di proyek yang sama tanpa perlu khawatir akan mengganggu pekerjaan satu sama lain. Mereka bisa membuat cabang (branch) dari kode utama untuk mengembangkan fitur baru atau memperbaiki masalah, lalu menggabungkannya kembali setelah selesai.

- Selain itu, Git memungkinkan kita untuk kembali ke versi kode yang stabil jika terjadi kesalahan. Ini memberikan rasa aman karena kita selalu bisa memulihkan kode yang sudah bekerja dengan baik. Jika ada konflik ketika beberapa orang mengubah bagian kode yang sama, Git juga membantu menyelesaikan masalah ini.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

- Django sering dipilih sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena memiliki beberapa keunggulan yang membuatnya cocok untuk pemula. Pertama, Django sudah dilengkapi dengan banyak fitur bawaan, seperti autentikasi pengguna, manajemen database, dan URL routing, sehingga kita tidak perlu membangun semuanya dari nol. Ini membantu pengembang baru untuk lebih fokus pada logika aplikasi daripada hal-hal teknis yang rumit.

- Selain itu, Django mengikuti prinsip "batteries included", yang berarti banyak kebutuhan pengembangan umum sudah tersedia dan siap pakai. Ini membuat proses belajar lebih mudah karena pengembang tidak harus mencari atau mengatur banyak alat tambahan.

- Django juga mengedepankan praktik pengembangan yang baik, seperti pembagian tugas antara bagian yang mengatur logika (views), data (models), dan tampilan (templates) melalui arsitektur Model-View-Template (MVT). Dengan pendekatan ini, pengembang belajar cara mengorganisasi kode dengan baik dari awal.

5. Mengapa model pada Django disebut sebagai ORM?
- Model dalam Django disebut ORM (Object-Relational Mapping) karena memungkinkan kita bekerja dengan data di database menggunakan objek Python, tanpa harus menulis perintah SQL secara langsung. Django ORM menghubungkan objek Python dengan tabel di database relasional.

- Jadi, saat kita membuat model di Django, misalnya model Product, Django akan mengubahnya menjadi tabel product di database, dan setiap atribut dari model tersebut akan menjadi kolom di tabel. ORM mempermudah kita untuk mengambil, menyimpan, atau mengubah data hanya dengan menggunakan metode pada objek Python, tanpa perlu berurusan dengan query SQL yang kompleks.

- ORM juga memastikan agar struktur kode dan database tetap konsisten. Jika ada perubahan pada model, Django bisa otomatis menyesuaikan perubahan tersebut ke dalam database melalui fitur migrasi. Ini membantu kita menghindari pengelolaan database secara manual, membuat pengembangan lebih cepat dan mudah.

- Intinya, Django menggunakan ORM untuk memetakan objek Python ke tabel database, sehingga kita bisa bekerja dengan database secara lebih sederhana dan efisien.