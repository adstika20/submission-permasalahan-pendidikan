# Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan perguruan tinggi yang berdiri sejak tahun 2000, telah berhasil mencetak banyak lulusan dengan reputasi baik. Namun, tingginya tingkat dropout menjadi tantangan besar bagi institusi ini, yang berpotensi memengaruhi reputasi, akreditasi, dan keberlanjutan institusi. Menurunnya jumlah siswa yang menyelesaikan pendidikan juga berdampak pada stabilitas keuangan dan kepercayaan masyarakat terhadap institusi ini. Oleh karena itu, diperlukan solusi berbasis data untuk mengidentifikasi siswa yang berisiko dropout agar dapat diberikan bimbingan khusus secara dini.

### Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang akan diselesaikan:
- Prediksi Tingkat Risiko Dropout: Mengidentifikasi siswa yang memiliki kemungkinan tinggi untuk tidak menyelesaikan pendidikan mereka.
- Analisis Faktor Penyebab: Menentukan faktor-faktor utama yang memengaruhi risiko dropout, seperti performa akademik, kehadiran, atau kondisi sosial-ekonomi.
- Efektivitas Bimbingan: Memberikan rekomendasi strategi intervensi untuk mendukung siswa berisiko agar tetap melanjutkan pendidikan.
- Monitoring Performa Siswa: Membuat sistem visualisasi data yang mudah dipahami untuk memantau performa siswa secara real-time.

### Cakupan Proyek
1. Persiapan Data: Mengunduh dan membersihkan dataset "students' performance" agar siap untuk dianalisis.
2. Analisis Data: Mengidentifikasi tren dan faktor-faktor utama yang memengaruhi risiko dropout.
3. Prediksi Risiko Dropout: Membuat model sederhana untuk memprediksi siswa yang berisiko tinggi dropout.
4. Dashboard Visualisasi: Menyusun dashboard interaktif untuk memantau performa siswa dan hasil prediksi risiko dropout.

### Persiapan

Sumber data: [Github Page](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment:
### 1. Clone Repository
```bash
git clone https://github.com/adstika20/submission-permasalahan-pendidikan.git
cd submission-permasalahan-pendidikan
```

### 2️⃣ **Membuat Virtual Environment**  
Buat dan aktifkan lingkungan virtual untuk memastikan dependensi tidak bentrok:  
```bash
python -m venv env
```
#### Aktifkan lingkungan virtual:
```bash
.\env\Scripts\activate
```
### 3️⃣ Instal Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Jalankan Aplikasi Streamlit
```bash
streamlit run main.py
```

## Business Dashboard 
Dashboard ini dibuat menggunakan tools Tableau dengan tujuan untuk mendeteksi siswa yang berisiko tinggi melakukan dropout sedini mungkin. Dengan informasi ini, pihak terkait dapat memberikan bimbingan khusus secara proaktif untuk mencegah siswa tersebut berhenti dari pendidikan.

Link Akses Dashboard:[Dashboard Tableau Public](https://public.tableau.com/views/Performasiswa/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Bagaimana tingkat pemberian beasiswa terhadap keputusan dropout siswa ?
Mayoritas mahasiswa penerima beasiswa berhasil lulus (2.209), yang menunjukkan bahwa dukungan finansial membantu mahasiswa menyelesaikan studi mereka dengan lebih baik. Sebaliknya, sebagian besar mahasiswa yang dropout (1.421) tidak menerima beasiswa, mengindikasikan bahwa ketiadaan bantuan finansial berpotensi menjadi faktor utama yang mempengaruhi keputusan untuk keluar dari perguruan tinggi. Meskipun demikian, ada 794 mahasiswa yang menerima beasiswa namun masih terdaftar, menunjukkan bahwa selain faktor finansial, aspek lain seperti motivasi dan dukungan akademik juga memainkan peran penting.

### Bagaimana tingkat Displaced terhadap keputusan dropout siswa ?
Mahasiswa yang Displaced (1) justru menunjukkan tingkat kelulusan yang lebih tinggi (1.324) dibandingkan dengan mahasiswa yang Non-Displaced (0) yang hanya mencatatkan 885 kelulusan. Di sisi lain, meskipun mahasiswa Non-Displaced memiliki angka dropout yang lebih tinggi (752) dibandingkan mahasiswa Displaced (669), kelompok Displaced juga memiliki lebih banyak mahasiswa yang masih terdaftar (433) dibandingkan kelompok Non-Displaced (361).

### Bagaimana Admission Grade mempengaruhi keputusan dropout siswa ?
Berdasarkan grafik garis yang menunjukkan hubungan antara status dan admission grade, dapat disimpulkan bahwa terdapat pola menarik yang perlu diperhatikan. Mahasiswa yang lulus (status 2) memiliki nilai admission grade tertinggi, yaitu 519, yang menunjukkan bahwa mereka mungkin memiliki kemampuan akademik yang lebih baik pada awalnya. Namun, yang cukup mengejutkan adalah mahasiswa yang dropout (status 0) justru memiliki nilai admission grade yang lebih tinggi (437) dibandingkan mahasiswa yang masih terdaftar (status 1) dengan rata-rata nilai admission grade 336. Hal ini mungkin mengindikasikan bahwa meskipun mahasiswa dengan nilai admission grade lebih tinggi memiliki potensi yang lebih baik, faktor lain di luar nilai akademik (seperti motivasi, dukungan, atau kondisi pribadi) dapat memengaruhi keputusan mereka untuk keluar dari perguruan tinggi.

### Bagaimana Father qualification mempengaruhi keputusan dropout siswa ?
Berdasarkan grafik mengenai rata-rata kualifikasi ayah (Father's qualification) dan status mahasiswa, dapat disimpulkan beberapa hal penting. Mahasiswa yang berhasil lulus (status 2) cenderung memiliki ayah dengan tingkat pendidikan tertinggi, dengan rata-rata kualifikasi ayah sebesar 10.374, menunjukkan bahwa pendidikan orang tua, khususnya ayah, dapat berperan dalam mendukung keberhasilan akademik anak. Namun, menariknya, mahasiswa yang dropout (status 0) memiliki rata-rata kualifikasi ayah yang hanya sedikit lebih rendah (10.141), yang mengindikasikan bahwa faktor pendidikan ayah bukanlah satu-satunya penentu antara mahasiswa yang lulus dan yang dropout. Selain itu, mahasiswa yang masih terdaftar (status 1) justru memiliki rata-rata kualifikasi ayah terendah (14.458), meskipun mereka masih bertahan dalam studi mereka.

### Bagaimana Mother qualification dan occupation mempengaruhi keputusan dropout siswa ?
Mahasiswa yang masih terdaftar (status 1) memiliki rata-rata kualifikasi ibu tertinggi (17.622) dan rata-rata pekerjaan ibu sebesar 11.688, yang menunjukkan bahwa mereka cenderung berasal dari latar belakang keluarga dengan ibu yang memiliki pendidikan yang baik dan pekerjaan yang stabil. Di sisi lain, mahasiswa yang berhasil lulus (status 2) memiliki kualifikasi ibu yang lebih tinggi lagi (22.428) dan rata-rata pekerjaan ibu yang juga lebih baik (19.311), menunjukkan bahwa dukungan dari ibu dengan pekerjaan yang lebih baik dan pendidikan yang lebih tinggi berperan positif dalam kesuksesan akademik mahasiswa. Namun, yang menarik adalah mahasiswa yang dropout (status 0) justru memiliki rata-rata pekerjaan ibu tertinggi (21.035), meskipun kualifikasi ibu mereka lebih rendah (14.375). Hal ini menunjukkan bahwa meskipun ibu mahasiswa dropout memiliki pekerjaan dengan penghasilan yang lebih tinggi, faktor lain seperti kualitas pendidikan ibu atau dukungan sosial dan emosional yang lebih rendah dapat berperan dalam keputusan mahasiswa untuk keluar dari perguruan tinggi. Pola ini mengindikasikan bahwa meskipun pekerjaan ibu dapat memberikan keuntungan finansial, kualifikasi pendidikan dan dukungan yang diberikan oleh orang tua, khususnya ibu, tetap mempengaruhi keberlanjutan studi mahasiswa.

### Bagaimana pengaruh rata-rata Curricular_units_1st_sem_enrolled dan Curricular_units_1st_sem_evaluations terhadap keputusan dropout siswa ?
- Mahasiswa Dropout (Status 0)
Mahasiswa yang dropout cenderung memiliki nilai Curricular_units_1st_sem_enrolled dan Curricular_units_1st_sem_evaluations yang lebih rendah, terutama ketika nilai Curricular_units_1st_sem_grade mendekati atau di bawah rata-rata. Meskipun ada penurunan angka dropout seiring meningkatnya jumlah unit yang diambil dan dievaluasi, masih ada mahasiswa yang dropout meskipun telah mengambil unit lebih banyak.
- Mahasiswa Graduate (Status 2)
Mahasiswa yang lulus memiliki Curricular_units_1st_sem_enrolled dan Curricular_units_1st_sem_evaluations yang lebih tinggi, menunjukkan bahwa mahasiswa yang lebih berkomitmen terhadap jumlah unit yang mereka ambil dan evaluasi, terutama dengan nilai semester yang lebih baik, lebih cenderung lulus.
- Mahasiswa Enrolled (Status 1)
Mahasiswa yang masih terdaftar menunjukkan pola yang berada di antara mahasiswa yang dropout dan graduate. Mereka memiliki jumlah unit yang cukup signifikan, tetapi tidak setinggi mahasiswa yang graduate.

### Bagaimana pengaruh rata-rata Curricular_units_1st_sem_approved dan Curricular_units_1st_sem_credited terhadap keputusan dropout siswa ?
- Mahasiswa Dropout (Status 0)
Mahasiswa dengan status dropout cenderung memiliki nilai Curricular_units_1st_sem_approved dan Curricular_units_1st_sem_credited yang rendah, berkisar antara 0-0.4. Hal ini menunjukkan bahwa performa akademik yang buruk di semester pertama, dengan nilai yang rendah untuk kedua variabel tersebut, berkorelasi dengan kemungkinan mahasiswa untuk mengalami dropout.
- Mahasiswa Graduate (Status 2)
Mahasiswa yang berhasil lulus memiliki distribusi nilai yang lebih tinggi untuk kedua variabel tersebut, berkisar antara 0.6-1.0. Ini menunjukkan bahwa keberhasilan akademis di semester pertama, tercermin dari nilai approved dan credited yang tinggi, berhubungan positif dengan kelulusan mahasiswa.
- Mahasiswa Enrolled (Status 1)
Mahasiswa yang masih terdaftar menunjukkan nilai Curricular_units_1st_sem_approved dan Curricular_units_1st_sem_credited yang berada di antara nilai mahasiswa dropout dan graduate. Dengan kata lain, performa akademik mereka moderat, dengan nilai approved dan credited di rentang menengah, menunjukkan bahwa mereka belum mengalami dropout namun belum mencapai tingkat performa yang setinggi mahasiswa yang lulus.


### Bagaimana pengaruh rata-rata Curricular_units_2st_sem_enrolled dan Curricular_units_2st_sem_evaluations terhadap keputusan dropout siswa ?

- Curricular_units_2nd_sem_approved dan Curricular_units_2nd_sem_credited terhadap keputusan dropout mahasiswa menunjukkan pola yang serupa dengan semester pertama. Untuk mahasiswa dengan status dropout (0), mayoritas memiliki nilai yang rendah untuk kedua variabel tersebut, berkisar antara 0.2-0.4. Hal ini menunjukkan bahwa mahasiswa yang mengalami dropout cenderung memiliki performa akademik yang rendah yang berlanjut hingga semester kedua, dengan jumlah unit yang diambil dan dievaluasi yang juga lebih rendah.
- mahasiswa dengan status graduate (2) memiliki distribusi nilai yang lebih tinggi dibandingkan dengan kelompok lainnya. Mayoritas nilai untuk kedua variabel tersebut berada pada rentang 0.6-1.0, dengan beberapa puncak tertinggi dalam grafik yang menunjukkan performa yang sangat baik. Hal ini mengindikasikan bahwa mahasiswa yang lulus cenderung memiliki jumlah unit yang diambil dan dievaluasi lebih tinggi, serta menunjukkan konsistensi performa akademik yang baik dari semester pertama ke semester kedua.
- dan yang graduate. Distribusi nilai untuk kedua variabel tersebut cenderung moderat, menunjukkan bahwa mahasiswa ini memiliki performa akademik yang cukup baik namun tidak setinggi mahasiswa yang lulus. Jumlah unit yang diambil dan dievaluasi juga berada pada level menengah, mengindikasikan bahwa mahasiswa yang masih terdaftar memiliki tingkat komitmen yang lebih rendah dibandingkan dengan mahasiswa yang berhasil lulus, meskipun mereka tetap menunjukkan keberlanjutan dalam studi mereka.

### Bagaimana pengaruh rata-rata Curricular_units_2st_sem_approved dan Curricular_units_2st_sem_credited terhadap keputusan dropout siswa ?
mahasiswa dengan status dropout (status 0) cenderung memiliki rata-rata unit kurikuler semester kedua yang lebih rendah, baik yang disetujui maupun yang dikreditkan, dengan kisaran 0-5 unit. Sebaliknya, mahasiswa yang bertahan atau lulus (status 2) menunjukkan nilai rata-rata yang lebih tinggi, dengan banyak yang mencapai 10-20 unit, sedangkan mahasiswa yang masih terdaftar (status 1) berada di tengah-tengah. Pada grafik atas, mahasiswa yang dropout memiliki jumlah unit yang disetujui lebih rendah, menunjukkan bahwa keberhasilan dalam mendapatkan persetujuan unit kurikuler berkorelasi negatif dengan kemungkinan dropout. Pola serupa terlihat pada grafik bawah, di mana mahasiswa dropout memiliki jumlah unit yang dikreditkan lebih sedikit, sedangkan mahasiswa bertahan memiliki lebih banyak unit yang dikreditkan. Distribusi serupa antara unit yang disetujui dan dikreditkan menunjukkan korelasi yang kuat antara keduanya dalam memengaruhi keputusan dropout siswa.



## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

### 1. Pastikan Prasyarat Terpenuhi
```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi Streamlit Buka terminal atau Command Prompt  

```bash
streamlit run app.py
```
Akses Prototype : [Streamlite](https://submission-permasalahan-pendidikan-jxvugfktfifyykpomgy8zw.streamlit.app/)

#### Penjelasan Cara Prediksi Setelah Menjalankan Streamlit
- Input data menggunakan formulir sederhana.
  Setelah aplikasi berjalan, pengguna diminta untuk memasukkan nilai variabel-variabel yang tersedia di aplikasi. Setiap variabel memiliki rentang nilai tertentu, yang dijelaskan di aplikasi untuk memastikan validitas data yang dimasukkan.
- Validasi dan Transformasi data
  Data yang dimasukkan akan diproses menggunakan fungsi clip_values() untuk memastikan nilainya berada dalam rentang yang diperbolehkan.
- Prediksi Status Mahasiswa
  Setelah semua data diinput, pengguna dapat menekan tombol "Predict" untuk menjalankan prediksi. Aplikasi akan menampilkan hasil prediksi dengan label berikut:
- Graduate 🎓: Mahasiswa diprediksi lulus.
- Dropout ❌: Mahasiswa diprediksi berhenti.
- Enrolled 📘: Mahasiswa diprediksi masih terdaftar.
  

## Conclusion
Solusi berbasis data yang dikembangkan untuk mengatasi tingginya tingkat dropout di Jaya Jaya Institut mencakup integrasi teknologi analitik dan machine learning. Dashboard interaktif menggunakan Tableau memberikan wawasan real-time terkait performa siswa, sementara model prediksi berbasis algoritma gradient boosting yang di-deploy melalui Streamlit memungkinkan institusi mengidentifikasi siswa berisiko tinggi secara akurat. Dengan pendekatan ini, institusi dapat menerapkan intervensi yang lebih efektif, meningkatkan keberlanjutan studi mahasiswa, dan memperkuat reputasi serta stabilitasnya secara menyeluruh.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Insight dari data ini dapat digunakan oleh Jaya Jaya Institut untuk merancang strategi proaktif, seperti: Program bimbingan khusus bagi mahasiswa berisiko tinggi dropout dan Ekspansi program beasiswa dengan kriteria penerimaan yang lebih inklusif.
- Untuk mahasiswa dengan nilai admission grade tinggi yang terancam dropout, mentoring akademik dapat membantu mereka merencanakan jalur akademik yang lebih jelas, memberikan dukungan dalam menghadapi kesulitan belajar, dan meningkatkan keterampilan manajemen waktu.
- Mengingat mahasiswa yang dropout memiliki ibu dengan pekerjaan yang baik namun kualifikasi pendidikan yang lebih rendah, institusi pendidikan dapat menawarkan program pelatihan keterampilan atau pendidikan bagi orang tua, khususnya ibu, untuk meningkatkan kualitas pendidikan mereka. Hal ini dapat membantu menciptakan lingkungan rumah yang lebih mendukung pendidikan anak, yang pada gilirannya bisa mengurangi risiko mahasiswa untuk dropout.
-  Identifikasi mahasiswa yang memiliki kombinasi nilai rendah pada Curricular_units_1st_sem_grade dan jumlah unit yang diambil serta dievaluasi rendah. Tawarkan mereka program intervensi seperti workshop manajemen waktu, kelas tambahan, atau mentor dari mahasiswa senior. Membantu mahasiswa yang berisiko dropout untuk meningkatkan performa akademiknya.
-  Mahasiswa yang memiliki performa rendah di semester kedua (status dropout) perlu mendapatkan perhatian khusus lebih awal. Langkah yang dapat diambil adalah memberikan bimbingan akademik yang lebih intensif, menyesuaikan beban studi mereka, serta menyediakan lebih banyak akses ke tutor atau materi pendukung. Intervensi ini dapat membantu mencegah mereka jatuh lebih dalam ke dalam masalah akademik dan meningkatkan peluang mereka untuk tetap terdaftar atau lulus.
