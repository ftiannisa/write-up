# Osint_Riikaa\_

### Category: Misc

###### author: Ikhari

Riikaa_Chan Just created an Account!!! She has some Secrets that some people want and uploaded a photo, The original photographer of this picture commented the flag on his comment section. Find the flag.

## Solution:

Pertama, saya cari keyword "Riikaa_Chan" di Google tapi saya tidak menemukan akun apapun yang bisa menjadi petunjuk. Kemudian, saya berpikir untuk mencari akunnya di Twitter

![](/media/hf05-or_1.png)

Saya menemukan akun tersebut dan merasa ini adalah petunjuknya. Mengingat akun tersebut dibuat pada Desember 2021 dan tweet diposting sekitar tanggal 23-24 Desember 2021, menunjukkan akun relatif baru (Hackfest0x5 ini sendiri diadakan 26 Desember 2021).

Dalam akun tersebut, Rika memposting dua foto. Karena deskripsi challenge menyebutkan "original photographer", maka saya coba mencari foto asli menggunakan Google Lens, tetapi tidak membuahkan hasil. Akhirnya setelah dapat "pencerahan", saya coba cek akun Rika menggunakan [wayback machine](https://archive.org/web/)

![](/media/hf05-or_2.png)

Terlihat ada 3 snapshots yang tersimpan pada 24 Desember 2021. Kita cek dari snapshot yang paling awal, yaitu pada 06:48

![](/media/hf05-or_3.png)

Setelah dilihat, ternyata ada 1 tweet yang sudah dihapus. Dalam tweet tersebut, terdapat sebuah foto dan link menuju Pinterest. Langsung saja kita cek linknya

![](/media/hf05-or_4.png)

Isinya adalah foto yang sama dengan foto yang dipost Rika, tetapi di postingan ini tidak ada komentar apapun. Maka saya lanjut melihat-lihat akun Bali ini

![](/media/hf05-or_5.png)
![](/media/hf05-or_6.png)

Setelah dicek, akun ini memiliki 3 foto dan 1 di antaranya memiliki link yang mengarah ke Instagram, berikut profilnya

![](/media/hf05-or_7.png)

Saya melihat-lihat postingan yang ada dan menemukan 3 foto yang sama dengan postingan Rika, lalu ketika saya mengecek postingan air terjun, akhirnya saya menemukan flagnya di kolom komentar

![](/media/hf05-or_8.png)

## FLAG

<details>
  <summary></summary>
  
hackfest0x5{U_C4N_F1ND_M3_TH1S_i5_yOUr_fL@6}
</details>

<br>

🏷️tags: OSINT, social media

### References

- [Instagram & Twitter OSINT - DownUnderCTF](https://www.youtube.com/watch?v=DV8hUcdK2Bk)
