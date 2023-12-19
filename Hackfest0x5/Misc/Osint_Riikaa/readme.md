# Osint_Riikaa

### Category: Misc

###### author: Ikhari

Riikaa!!! wrong file upload!!!

## Solution:

Jika kita lihat kembali profil Rika di Twitter, di bionya terdapat tulisan "If you meet the username Riikaa_Chan or RiikaaChan, it's probably me". Maka kali ini saya mencoba mencari akun dengan nama "RiikaaChan" dengan menggunakan [sherlock](https://github.com/sherlock-project/sherlock). Salah satu hasilnya merupakan akun Github dengan nama RiikaaChan.

![](/media/hf05-or1.png)
![](/media/hf05-or2.png)

Akun tersebut dibuat sekitar tanggal 23 Desember 2021 _(catatan: screenshot di atas baru saya ambil setelah Hackfest0x5 selesai ketika menulis writeup, pada tanggal 6 Januari 2022, lalu kurangi 14 hari)_. Di sini, kita bisa lihat Rika mempunyai 1 repo bernama SmthWrong. Selanjutnya, saya coba cari flag dengan mengecek commit historynya. Saya kurang tau apakah ada cara yang lebih mudah, jadi saya mengecek secara manual:') Akhirnya saya menemukan flagnya yang terletak di branch "development" dengan commit message "Add python".

![](/media/hf05-or3.png)

## FLAG

<details>
  <summary></summary>
  
hackfest0x5{Sc4R3d_0f_c0Mm1t}

</details>

<br>

🏷️tags: OSINT, Github
