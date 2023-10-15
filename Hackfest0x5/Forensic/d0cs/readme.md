# d0cs

### Category: Forensic

###### author: wisnuazfarm

docs have more functional

\*document bukan cuman sekedar untuk baca dan nulis

- [File](https://mega.nz/file/f1FHTILQ#GmSWGwT3EwTub47PoV2MZGgtv1jUARkrZfNoKezq_Yc)
  <br><br>

### Solution:

Pertama, kita download dulu filenya. File yang disediakan dalam challenge ini adalah file dokumen berekstensi .dotm. Jika dibuka, seperti ini tampilannya

![](/media/hf05-docs1.png)
![](/media/hf05-docs2.png)

Setelah warnanya diganti, tidak ada flag yang cocok. Kemudian saya coba menggunakan binwalk dan mengekstraknya, lalu dicek menggunakan command `grep -r "hack"` tetapi yang muncul hanya flag yang sama. Setelah cari-cari referensi, akhirnya saya tahu ada tools Python bernama oletools yang bisa menganalisis dokumen dan mendeteksi virus macro. Berikut ini langkah pengerjaan yang saya lakukan

![](/media/hf05-docs3.png)
_Membuat virtual environment dan install oletools_

![](/media/hf05-docs4.png)

Selanjutnya, ekstrak source code dari VBA macro menggunakan olevba dan simpan dalam file d0cs.log. Berikut ini isi dari d0cs.log

![](/media/hf05-docs5.png)
![](/media/hf05-docs6.png)

Selanjutnya, saya copy kode tersebut ke macro, lalu jalankan

![](/media/hf05-docs7.png)

Seperti yang bisa kita lihat, outputnya berupa string panjang. Selanjutnya kita decode string tersebut

![](/media/hf05-docs8.png)

Dari hasil decode tersebut, terdapat link menuju pastebin. Setelah dibuka, akhirnya kita dapat flagnya:

![](/media/hf05-docs9.png)

<br><br>

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{de0bfuscatdd_shesss_678}
</details>

<br><br>
🏷️tags: macro analysis

### References

- [EKOPARTY CTF 2020 - Update](https://ctftime.org/writeup/23895)
