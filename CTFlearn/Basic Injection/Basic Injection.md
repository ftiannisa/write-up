# [Basic Injection](https://ctflearn.com/challenge/88)
### Category: Web
###### Difficulty: Easy - 30 pts

See if you can leak the whole database using what you know about SQL Injections. [link](https://web.ctflearn.com/web4/)

Don't know where to begin? Check out CTFlearn's [SQL Injection Lab](https://ctflearn.com/lab/sql-injection-part-1)
<br><br>
### Solution:
:indonesia: Sebelum cari flagnya, kalian bisa baca-baca dulu lab yang sudah disediakan author. Di situ isinya cukup bermanfaat dan udah ada penjelasan mengenai hal-hal basic, jadi buat yang baru banget belajar sepertinya bisa paham tentang SQL injection ini.

Di dalam web ini ada sebuah input form, yang mana hasil inputannya ini akan dimasukkan ke dalam suatu query SQL. 
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/ctfl-bi1.png?raw=true"/>
</p>
Di sini saya coba input kata 'admin' dan query SQL akan menampilkan data yang memiliki nama 'admin', tetapi hasilnya "0 results" yang berarti database tersebut tidak memiliki data dengan nama 'admin'.
Sekarang kita coba lagi menggunakan input yang sudah dicontohkan pada lab.
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/ctfl-bi-result.png?raw=true"/>
</p>
Menginput "admin' or '1' = '1" (tanpa tanda kutip ganda, ya) dan hasilnya keluar
<br>
<br>
:uk: This one is pretty simple actually. If you are new to SQL injection, you can try the lab which the author has already provided. It's pretty useful and they also explained the basics so you don't have to worry about it.

Let's try inputting a random word, in this case I input 'admin'.
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/ctfl-bi1.png?raw=true"/>
</p>
As you can see, it shows "0 results". It's because the database doesn't have any data with 'admin' as its name value. Now let's try the method that we've learned from the lab.
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/ctfl-bi-result.png?raw=true"/>
</p>
I input "admin' or '1' = '1" (without double quotes) and it works! :D
<br><br>

### FLAG

<details>
  <summary></summary>
  
  CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
</details>
