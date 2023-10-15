# Password Checker V1.0

### Category: Reverse Engineering

###### author: kimnad

Get the correct password!

- [chall](/Hackfest0x5/Reverse/Password%20Checker%20V1.0/chall)
  <br><br>

### Solution:

![](/media/hf05-pc1-1.png)

File chall pada challenge ini adalah program executable dan ketika dijalankan, program tersebut meminta input password. Sebenarnya saya kurang paham mengenai reverse engineering tapi akhirnya saya coba untuk melihat programnya menggunakan ghidra.

![](/media/hf05-pc1-2.png)

Jika dilihat di baris 20, program membandingkan input user dengan supah_s3cret. Jika nilainya sama, maka program akan mencetak nilai dari supah_s3cret tersebut. Saya sempat kebingungan untuk mencari nilai supah_s3cret tersebut dan setelah mencari-cari referensi, saya coba menjalankan command `strings` seperti berikut

![](/media/hf05-pc1-3.png)

Dan akhirnya saya menemukan suatu string dan langsung saja gabungkan dengan format flag yang ada dan ternyata benar itu flagnya

<br><br>

### FLAG

<details>
  <summary></summary>
hackfest0x5{the_strings_command_can_be_U5eful_but_dont_R3ly_0n_1t}
</details>

<br><br>

### References

- [Reverse Engineering - CTF Playbook](https://fareedfauzi.gitbook.io/ctf-playbook/reverse-engineering)
