# CodeJugling

### Category: Reverse Engineering

Find the flag!

- [reversing-itu-mudah](/Gemastik%202022/Reverse/CodeJugling/reversing-itu-mudah)
  <br><br>

### Solution:

Diberikan sebuah stripped binary file yang berarti informasi debugging dari program tersebut sudah dihilangkan, termasuk nama-nama fungsi yang digunakan.

![](/media/gem22-cj1.png)

Selanjutnya, disassembly file menggunakan Ghidra dan cek fungsi-fungsi yang ada. Terlihat ada salah satu fungsi yang melakukan pengecekan input dengan memanggil fungsi lain. Jika inputan benar, maka program akan menampilkan flag (yang tak lain dan tak bukan adalah inputan itu sendiri)

![](/media/gem22-cj2.png)

![](/media/gem22-cj3.png)

Nah sekarang kita lihat fungsi-fungsi yang digunakan untuk mengecek input tadi. Setiap fungsi tersebut ternyata melakukan perbandingan tiap karakter dari inputan dengan sebuah karakter. Kita susun saja setiap karakter yang dibandingkan tersebut dan flag pun berhasil didapatkan

\*_) karena fungsinya cukup banyak, jadi kami hanya menampilkan 8 fungsi pertama saja yang membentuk potongan kata “Gemastik” sebagai contoh✌️_

![](/media/gem22-cj-f1.png)
![](/media/gem22-cj-f2.png)
![](/media/gem22-cj-f3.png)
![](/media/gem22-cj-f4.png)
![](/media/gem22-cj-f5.png)
![](/media/gem22-cj-f6.png)
![](/media/gem22-cj-f7.png)
![](/media/gem22-cj-f8.png)
<br>
<br>

### FLAG

<details>
  <summary></summary>
  
Gemastik2022{st45iUn_MLG_k07a_b4rU}
</details>
