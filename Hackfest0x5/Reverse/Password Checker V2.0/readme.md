# Password Checker V2.0

### Category: Reverse Engineering

###### author: kimnad

Get the correct password!

- [chall](/Hackfest0x5/Reverse/Password%20Checker%20V2.0/chall)
  <br><br>

### Solution:

Tahap awal analisis kurang lebih sama seperti challenge sebelumnya. Pertama, saya coba jalankan command `strings` lalu saya menemukan string yang unik

![](/media/hf05-pc2-1.png)

Selanjutnya, saya buka program chall tersebut di ghidra.

![](/media/hf05-pc2-2.png)

Jika dilihat pada baris 25, program melakukan operasi XOR terhadap input user, yaitu local_a8 dengan nilai hex 0x1c dan kemudian disimpan pada variabel baru, local_68. Selanjutnya, pada baris 29 terlihat program membandingkan local_68 dengan encrypt3d_s3re3t. Dari sini, saya membuat kode program dengan bahasa C. Caranya kurang lebih mirip dengan penjelasan pada challenge [keXOxoR](/Hackfest0x5/Cryptography/keXOxoR/), yaitu dengan memanfaatkan sifat XOR yang dapat dipertukarkan. Bedanya, kali ini kita sudah mengetahui key (0x1c) dan ciphertextnya (string unik yang tadi didapat dengan `strings`). Berikut kode program yang saya buat:

![](/media/hf05-pc2-3.png)

Selanjutnya, cukup gabungan string tersebut dengan format flag

<br><br>

### FLAG

<details>
  <summary></summary>
hackfest0x5{Jus7_4n_34zzy_p34zzy_l3m0nn_squ1zzy!!}
</details>
