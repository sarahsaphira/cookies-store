# TUGAS INDIVIDU 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

2. Jelaskan cara kerja penghubungan model MoodEntry dengan User!

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.


4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- Tambahkan kode berikut ke main/views.py
```html
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- response.setcookie('last_login', str(datetime.datetime.now())) digunakan untuk menyimpan waktu terakhir user yang bersangkutan login pada cookie
- Tambahkan 'last_login': request.COOKIES['last_login'], pada context di views.py untuk mengakses cookie last_login
- Tambahkan @login_required(login_url='/login') di atas function show_main pada views.py untuk memastikan hanya logged in user yang bisa akses
- Tambahkan potongan kode berikut pada urls.py untuk handle routing:
```html
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```
- Buat template yang akan digunakan untuk masing-masing routing dari views.py (klik untuk mengakses):
[register.html]()
[main.html]()
[login.html]()
- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- Buka localhost:8000 dan register untuk 2 username dengan username yang berbeda dan password
- Login ntuk kedua user tersebut, kemudian buat 3 product/item baru dengan klik tombol Add New Product dan isi seluruh detail product yang diinginkan
- Setelah selesai coba cek apakah product yang ditambahkan sudah ada di tabel
- Apabila sudah benar, seharusnya setiap user memiliki tabel dengan isi product yang berbeda-beda
-  Menghubungkan model Item dengan User.
- Tambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) pada class Product di models.py untuk initiate Many to One relationship (karena menggunakan ForeignKey) pada User dengan Product/Item.
- Ubah views.py pada bagian:
```html
def create_product(request):
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return redirect('main:show_main')
```
- Tambahkan products = Product.objects.filter(user=request.user) dan ubah context untuk key 'name'
```html
def show_main(request):
products = Product.objects.filter(user=request.user)

context = {
    'name': request.user.username,
    ...
}
```
- Lakukan migration untuk menyimpan perubahan
- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Untuk menampilkan username dapat menggunakan potongan kode berikut pada main.html:
```html
<p>{{ name }}</p>
```
- Untuk menampilkan data last login user dapat memanfaatkan Cookies dengan menggunakan potongan kode berikut pada main.html:
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
- Untuk mengimplementasikan cookiesnya sebagai berikut:
- response.set_cookie('last_login', str(datetime.datetime.now())) pada function login_user di views.py untuk set cookie kapan user login terakhir kali
- response.delete_cookie('last_login') pada function logout_user di views.py untuk menghapus cookie
- 'last_login': request.COOKIES['last_login'], pada context function show_main di views.py

# TUGAS INDIVIDU 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery sangat penting dalam pengimplementasian sebuah platform karena berperan dalam memastikan ketersediaan layanan. Tanpa mekanisme pengiriman data yang tepat, pengguna mungkin mengalami keterlambatan atau bahkan kehilangan akses terhadap informasi yang diperlukan. Ini bisa berdampak negatif pada pengalaman pengguna dan kinerja platform secara keseluruhan. Selain itu, data delivery yang efisien memungkinkan integrasi antara berbagai sistem dan aplikasi di dalam platform, memastikan bahwa data dapat dikirim dan diterima tanpa hambatan. Hal ini juga mendukung konsistensi data, yang penting untuk menjaga integritas informasi antar sistem. 

Di samping itu, platform yang memiliki data delivery yang baik lebih mampu beradaptasi dengan pertumbuhan pengguna dan peningkatan volume data, sehingga memastikan skalabilitas yang dibutuhkan seiring perkembangan platform. Mekanisme ini juga memungkinkan keamanan data yang lebih kuat dengan memastikan bahwa data hanya diakses oleh pihak yang berwenang, melindungi informasi sensitif dari potensi ancaman.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON secara umum lebih baik untuk kebanyakan kasus penggunaan modern, terutama dalam pengembangan aplikasi web dan komunikasi data yang membutuhkan kecepatan dan efisiensi. JSON lebih ringan, lebih mudah dibaca, dan lebih cepat diproses dibandingkan XML. Selain itu, JSON memiliki integrasi yang sangat baik dengan bahasa pemrograman seperti JavaScript, yang membuatnya lebih populer dalam pengembangan aplikasi berbasis web.

Namun, jika memerlukan validasi skema yang kuat atau bekerja dengan data yang kompleks dan terstruktur (misalnya, dengan metadata atau atribut), XML bisa menjadi pilihan yang lebih tepat karena dukungan untuk skema yang lebih formal.

Secara keseluruhan, untuk penggunaan umum yang melibatkan pertukaran data sederhana, JSON biasanya merupakan pilihan yang lebih baik.

JSON lebih populer dibandingkan XML karena :
- Tingkat simplicity dan readability yang tinggi karena syntax dan indentasinya yang ringkas
- Memiliki banyak method yang dapat mempercepat proses penyusunan program (contoh: JSON.parse() untuk mengubah JSON string menjadi Object dengan atribut-atributnya)
- Dapat merepresentasikan data dengan ukuran file yang kecil karena syntaxnya ringkas (seperti tidak menggunakan tag, etc.)
- Dapat melakukan transfer/pertukaran data dengan sangat cepat (tidak perlu banyak parse karena syntaxnya juga singkat)
- Sangat compatible dengan berbagai teknologi web, seperti JavaScript dan lain-lain.
- Mendukung tipe data native, seperti numbers, booleans, null, etc.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua validasi yang telah ditentukan, baik dari validasi bawaan Django maupun validasi custom. Method ini akan mengembalikan nilai True jika data valid, dan False jika tidak.

Kita membutuhkan method ini untuk memastikan bahwa data yang diolah sudah benar sebelum disimpan ke database atau diproses lebih lanjut, sehingga mencegah kesalahan atau data yang tidak sesuai.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Dalam Django, kita membutuhkan csrf_token untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Serangan ini terjadi ketika penyerang mencoba mengirimkan permintaan berbahaya atas nama pengguna tanpa izin mereka. Misalnya, jika pengguna sedang login ke suatu aplikasi, penyerang bisa memanfaatkan celah ini untuk melakukan aksi seperti mengubah data atau menjalankan transaksi tanpa sepengetahuan pengguna.

Dengan menambahkan csrf_token pada form, Django memastikan bahwa setiap permintaan yang dikirim benar-benar berasal dari sumber yang sah (form asli di situs), bukan dari halaman eksternal yang dibuat oleh penyerang. Tanpa csrf_token, aplikasi rentan terhadap serangan ini, yang bisa berdampak pada keamanan dan integritas data.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat base.html pada root/templates dan mengisinya dengan:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Membuat forms.py pada main dan mengisinya dengan:
```html
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
```
- Ubah function show_main pada views.py menjadi sebagai berikut:
```html
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Sarah Saphira Setiawan',
        'npm' : '2306240093',
        'class': 'PBP A',
        'products': products
    }

    return render(request, "main.html", context)
```
- Buat create_product.html pada main/templates/ dan isi sebagai berikut:
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>
```
- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

- create_product untuk menerima input user, dapat diakses ketika user klik button "Add New Product"
```html
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- show_xml untuk menampilkan representasi seluruh products dalam format XML
```html
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- show_json untuk menampilkan representasi seluruh products dalam format JSON,
```html
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- show_xml_by_id untuk menampilkan representasi product dengan id yang diinginkan dalam format XML
```html
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- show_json_by_id untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON
```html
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Membuat routing URL untuk masing-masing views

- Isi urls.py dengan:
```html
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
- urlpatterns digunakan agar function-function yang telah dicantumkan pada views.py dapat diakses dengan url yang diinginkan.

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman

- XML: (url)/xml: Untuk menampilkan representasi seluruh products dalam format XML
![](https://github.com/sarahsaphira/cookies-store/blob/fa5ccb3d9a3fbbc8417ffb8a28bca29d71c718f4/xml.png)

- JSON: (url)/json: Untuk menampilkan representasi seluruh products dalam format JSON
![](https://github.com/sarahsaphira/cookies-store/blob/fa5ccb3d9a3fbbc8417ffb8a28bca29d71c718f4/json.png)

- XML by ID: (url)/xml/(desired_id): Untuk menampilkan representasi product dengan id yang diinginkan dalam format XML
![](https://github.com/sarahsaphira/cookies-store/blob/fa5ccb3d9a3fbbc8417ffb8a28bca29d71c718f4/XMLbyID.png)

- JSON by ID: (url)/xml/(desired_id): Untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON
![](https://github.com/sarahsaphira/cookies-store/blob/fa5ccb3d9a3fbbc8417ffb8a28bca29d71c718f4/JSONbyID.png)

# TUGAS INDIVIDU 2
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
```html
urlpatterns = [
    path('', include('main.urls')),
]
```

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

- membuka models.py dan mengisinya dengan attributes/fields yang diperlukan. Pada kasus ini, saya menggunakan 3 attributes, yakni name (CharField), price (IntegerField), description (TextField). Isi file models.py adalah sebagai berikut:
```html
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

- Membuka views.py dan menambahkan potongan kode di bawah ini untuk menghubungkan Views dan Templates. Sehingga, isi views.py sebagai berikut:
```html
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
```

- Menjalankan git push origin main, git add . , git commit -m "message", dan git push -u origin main untuk update github repository agar sesuai dengan local repository

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/sarahsaphira/cookies-store/blob/1b0f33067c635ff55e09f6e077944304a335bbb5/BaganNomor2.png)

Client mengirim request ke Internet -> forward ke Python/Django -> forward ke urls.py -> forward ke views.py untuk memproses url -> read/write data dari/ke models.py dan database -> input/display data dari/ke templates -> return html file yang telah dimerge dengan value-value yang diinginkan -> proses ke internet -> display ke client's device

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git berfungsi sebagai alat penting dalam pengembangan perangkat lunak karena membantu tim pengembang mengelola perubahan pada kode. Dengan Git, setiap perubahan yang dilakukan dicatat, sehingga pengembang bisa melihat versi-versi sebelumnya, siapa yang melakukan perubahan, dan alasan perubahan tersebut.

Git juga memudahkan kerja sama tim. Beberapa orang bisa bekerja di proyek yang sama tanpa perlu khawatir akan mengganggu pekerjaan satu sama lain. Mereka bisa membuat cabang (branch) dari kode utama untuk mengembangkan fitur baru atau memperbaiki masalah, lalu menggabungkannya kembali setelah selesai.

Selain itu, Git memungkinkan kita untuk kembali ke versi kode yang stabil jika terjadi kesalahan. Ini memberikan rasa aman karena kita selalu bisa memulihkan kode yang sudah bekerja dengan baik. Jika ada konflik ketika beberapa orang mengubah bagian kode yang sama, Git juga membantu menyelesaikan masalah ini.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dipilih sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena memiliki beberapa keunggulan yang membuatnya cocok untuk pemula. Pertama, Django sudah dilengkapi dengan banyak fitur bawaan, seperti autentikasi pengguna, manajemen database, dan URL routing, sehingga kita tidak perlu membangun semuanya dari nol. Ini membantu pengembang baru untuk lebih fokus pada logika aplikasi daripada hal-hal teknis yang rumit.

Selain itu, Django mengikuti prinsip "batteries included", yang berarti banyak kebutuhan pengembangan umum sudah tersedia dan siap pakai. Ini membuat proses belajar lebih mudah karena pengembang tidak harus mencari atau mengatur banyak alat tambahan.

Django juga mengedepankan praktik pengembangan yang baik, seperti pembagian tugas antara bagian yang mengatur logika (views), data (models), dan tampilan (templates) melalui arsitektur Model-View-Template (MVT). Dengan pendekatan ini, pengembang belajar cara mengorganisasi kode dengan baik dari awal.

5. Mengapa model pada Django disebut sebagai ORM?

Model dalam Django disebut ORM (Object-Relational Mapping) karena memungkinkan kita bekerja dengan data di database menggunakan objek Python, tanpa harus menulis perintah SQL secara langsung. Django ORM menghubungkan objek Python dengan tabel di database relasional.

Jadi, saat kita membuat model di Django, misalnya model Product, Django akan mengubahnya menjadi tabel product di database, dan setiap atribut dari model tersebut akan menjadi kolom di tabel. ORM mempermudah kita untuk mengambil, menyimpan, atau mengubah data hanya dengan menggunakan metode pada objek Python, tanpa perlu berurusan dengan query SQL yang kompleks.

ORM juga memastikan agar struktur kode dan database tetap konsisten. Jika ada perubahan pada model, Django bisa otomatis menyesuaikan perubahan tersebut ke dalam database melalui fitur migrasi. Ini membantu kita menghindari pengelolaan database secara manual, membuat pengembangan lebih cepat dan mudah.

Intinya, Django menggunakan ORM untuk memetakan objek Python ke tabel database, sehingga kita bisa bekerja dengan database secara lebih sederhana dan efisien.