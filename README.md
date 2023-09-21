# CapstoneProject
Build Machine Learning Models Automatically (AutoAI) Watsonx - HCAI

## Capstone Project Ideas
Prediksi Index Pencemaran Air Sumur di Provinsi DKI Jakarta.

## Latar Belakang
Mengingat kondisi air tanah yang semakin rentan terhadap pencemaran akibat pertumbuhan pesat kota dan aktivitas manusia. DKI Jakarta, sebagai salah satu wilayah dengan tingkat kepadatan penduduk tinggi, memiliki banyak sumur air tanah yang digunakan untuk memenuhi kebutuhan air bersih penduduknya. Namun, dengan urbanisasi yang cepat, pembangunan infrastruktur yang besar, dan aktivitas industri yang tinggi, risiko pencemaran air tanah semakin meningkat. Pencemaran ini dapat berasal dari berbagai sumber, termasuk limbah industri, limbah domestik, dan penggunaan pupuk berlebihan yang dapat mengganggu kualitas air tanah. Oleh karena itu, prediksi indeks pencemaran air sumur menjadi sangat penting untuk mengambil tindakan preventif yang diperlukan, mengurangi risiko kesehatan masyarakat, dan menjaga sumber daya air yang penting ini agar tetap berkelanjutan.

## Tujuan
Tujuan dari melakukan prediksi indeks pencemaran air sumur di DKI Jakarta mencakup:

1. **Pencegahan Pencemaran Air**: Melalui prediksi ini, upaya pencegahan pencemaran air dapat diterapkan lebih dini, membantu mengidentifikasi potensi risiko terhadap kualitas air tanah dan menghindari kerusakan lebih lanjut.

2. **Perlindungan Kesehatan Masyarakat**: Prediksi indeks pencemaran air memungkinkan perlindungan kesehatan warga dengan mengambil tindakan yang tepat guna menghindari konsumsi air yang tercemar, yang dapat berdampak negatif pada kesehatan.

3. **Pengelolaan Sumber Daya Air yang Berkelanjutan**: Dengan pemantauan dan prediksi pencemaran air, DKI Jakarta dapat mengambil langkah-langkah yang diperlukan untuk menjaga sumber daya air tetap berkelanjutan, mengingat pentingnya air tanah untuk memenuhi kebutuhan air bersih kota.

4. **Kesadaran Lingkungan**: Informasi mengenai indeks pencemaran air dapat meningkatkan kesadaran masyarakat dan perusahaan terkait dampak negatif aktivitas mereka pada kualitas air tanah, mendorong adopsi praktik-praktik yang lebih peduli lingkungan.

5. **Perencanaan Pembangunan yang Lebih Cerdas**: Data indeks pencemaran air dapat digunakan untuk perencanaan pembangunan yang lebih cerdas, membantu menentukan lokasi infrastruktur yang lebih strategis dan implementasi kebijakan lingkungan yang lebih efektif.

6. **Kerjasama Regional**: Prediksi indeks pencemaran air juga dapat digunakan sebagai alat untuk mendorong kerjasama regional dalam mengatasi pencemaran yang memengaruhi wilayah-wilayah tetangga dan memiliki dampak lintas batas.

## Dataset
Sumber dataset berasal dari Jakarta Open Data: https://data.jakarta.go.id/dataset/data-hasil-pengujian-kualitas-air-sumur-provinsi-dki-jakarta-tahun-2017/resource/7bddbf71dff0859907ea7819ba815779

## Included components
*	[IBM Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) - IBM Watson® Studio helps data scientists and analysts prepare data and build models at scale across any cloud.
*	[IBM Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) - IBM Watson® Machine Learning helps data scientists and developers accelerate AI and machine-learning deployment. 
*	[IBM Cloud Object Storage](https://cloud.ibm.com/catalog/services/cloud-object-storage) - IBM Cloud™ Object Storage makes it possible to store practically limitless amounts of data, simply and cost effectively.

## Hasil


## Kesimpulan
Berdasarkan hasil prediksi Indeks Pencemaran Air di DKI Jakarta menggunakan AutoAI Watsonx, dapat disimpulkan bahwa:

+ Top Rank Pipeline untuk prediksi index pencemaran adalah Pipeline 8.

+ Algoritma yang digunakan adalah XGB Regressor. Algoritma ini yang paling akurat dan efektif untuk memprediksi indeks pencemaran air sumur di DKI Jakarta.

+ Algoritma tersebut mencapai tingkat RMSE (Root Mean Square Error) sebesar 0.321. Angka ini menunjukkan bahwa algoritma memiliki kemampuan yang baik dalam mengklasifikasikan indeks pencemaran air sumur di DKI Jakarta.

+ Enhancements yang berperan dalam meningkatkan kinerja algoritma XGB Regressor dengan mengoptimalkan parameter dan mengubah fitur yang digunakan, yaitu 1st dan 2nd Hyperparameter Optimization serta Feature Engineering.

+ Feature important yang mempengaruhi indeks pencemaran air sumur di DKI Jakarta adalah lokasi pengambilan titik contoh air.

+ Indeks pencemaran air sumur di DKI Jakarta yang paling mempengaruhi sebesar 1,38 dengan parameter zat padat terlarut 254 mg/L di Bangka.

Dengan hasil tersebut, memberikan pemahaman yang lebih baik tentang seberapa besar indeks pencemaran air sumur di DKI Jakarta. Algoritma yang dikembangkan memiliki tingkat akurasi yang tinggi dan telah mengalami peningkatan melalui proses optimisasi parameter dan rekayasa fitur. Implikasinya, algoritma ini dapat digunakan sebagai alat yang berguna dalam memprediksi indeks pencemaran air sumur di DKI Jakarta.
