# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

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

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Insight dari data ini dapat digunakan oleh Jaya Jaya Institut untuk merancang strategi proaktif, seperti: Program bimbingan khusus bagi mahasiswa berisiko tinggi dropout dan Ekspansi program beasiswa dengan kriteria penerimaan yang lebih inklusif.
- Untuk mahasiswa dengan nilai admission grade tinggi yang terancam dropout, mentoring akademik dapat membantu mereka merencanakan jalur akademik yang lebih jelas, memberikan dukungan dalam menghadapi kesulitan belajar, dan meningkatkan keterampilan manajemen waktu.
- Mengingat mahasiswa yang dropout memiliki ibu dengan pekerjaan yang baik namun kualifikasi pendidikan yang lebih rendah, institusi pendidikan dapat menawarkan program pelatihan keterampilan atau pendidikan bagi orang tua, khususnya ibu, untuk meningkatkan kualitas pendidikan mereka. Hal ini dapat membantu menciptakan lingkungan rumah yang lebih mendukung pendidikan anak, yang pada gilirannya bisa mengurangi risiko mahasiswa untuk dropout.
