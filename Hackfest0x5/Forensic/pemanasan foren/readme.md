# pemanasan foren

### Category: Forensic

###### author: wisnuazfarm

pemanasan dulu biar panas

\*panas kalau lihat EX sama yang baru

- [flag.txt](/Hackfest0x5/Forensic/pemanasan%20foren/flag.txt)
  <br><br>

### Solution:

![](/media/hf05-pf1.png)

Awalnya, saya pikir ini adalah morse code, tetapi ketika saya terjemahkan, hasilnya hanya kumpulan karakter seperti berikut

![](/media/hf05-pf2.png)

Saya kira string itu harus di-decode terlebih dulu tapi tentu saja tidak berhasil. Akhirnya setelah cukup lama, saya mulai berpikir, bagaimana kalau ternyata ini bukan morse code? Lalu saya coba ganti spasinya dengan 0 dan tanda titik menjadi 1. Selanjutnya, pisahkan per 8 digit.

![](/media/hf05-pf3.png)

Kemudian, convert bilangan biner tersebut menjadi ASCII. Saya menggunakan website [ini](https://www.rapidtables.com/convert/number/binary-to-ascii.html)

![](/media/hf05-pf4.png)

Dan akhirnya kita dapat flagnya

<br><br>

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{b1n4ry_s1mpl3_p3m4n4s4n_4553} 
</details>
