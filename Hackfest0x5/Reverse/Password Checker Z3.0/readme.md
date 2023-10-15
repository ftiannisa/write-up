# Password Checker Z3.0

### Category: Reverse Engineering

###### author: kimnad

Get the correct password!

- [chall](/Hackfest0x5/Reverse/Password%20Checker%20Z3.0/chall)
  <br><br>

### Solution:

Pertama, saya coba lihat programnya menggunakan ghidra

![](/media/hf05-pc3-1.png)
![](/media/hf05-pc3-2.png)
![](/media/hf05-pc3-3.png)

Program di atas berfungsi memvalidasi password yang diinput user. Karena belum terlalu paham mengenai reverse engineering, awalnya saya mencoba metode yang sama dengan kedua challenge sebelumnya tapi tidak terlalu membuahkan hasil. Lalu seperti biasa, saya cari-cari referensi lagi dan akhirnya membuat script Python menggunakan library angr seperti berikut

![](/media/hf05-pc3-4.png)

Sebelum menjalankan program, buat virtual environment dan install angr

![](/media/hf05-pc3-5.png)

Setelah instalasi selesai, jalankan program

![](/media/hf05-pc3-6.png)

Langsung saja kita gabungkan output dengan format flag

<br><br>

### FLAG

<details>
  <summary></summary>
hackfest0x5{z3solve_your_equation}
</details>

<br><br>
🏷️tags: flag checker, z3, angr

### References

- [Google CTF - BEGINNER Reverse Engineering w/ ANGR](https://www.youtube.com/watch?v=RCgEIBfnTEI)
