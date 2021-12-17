# [Insp3ct0r](https://play.picoctf.org/practice/challenge/18?category=1&page=1)
### Category: Web (50 pts)
<!-- ###### Difficulty:  -->

Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ ([link](https://jupiter.challenges.picoctf.org/problem/41511/)) or http://jupiter.challenges.picoctf.org:41511
<br><br>
### Solution:
:indonesia: Untuk challenge ini, langsung aja dibuka link webnya. Kalo udah, klik tombol F12 atau bisa juga klik kanan > Inspect. Bisa diliat di tab Elements (atau bisa langsung cek tab Source > file (index))sudah tampil kode HTMLnya dan dari sini kita bisa dapat 1/3 flagnya
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins1.png?raw=true"/>
</p>
Flag 1/3: picoCTF{tru3_d3 <br>
Lanjut, sekarang kita pindah ke tab Source lalu klik file myjs.js. Di sini terlihat pada baris terakhir sudah ada potongan flag yang ketiga
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins2.png?raw=true"/>
</p>
Flag 3/3: _lucky?832b0699} <br>
Sekarang kita cari potongan flag yang terakhir. Klik file mycss.css dan bisa kita lihat di baris terakhir terdapat potongan flag kedua :D
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins3.png?raw=true"/>
</p>
Flag 2/3: t3ct1ve_0r_ju5t<br>
Semua potongan flagnya sudah ada, sekarang tinggal digabungin aja. Gabunginnya sesuai urutan ya, mulai dari 1/3, 2/3, lalu 3/3. Mudah kan? Selamat mencoba!
<br>
<br>
:uk: Click the website link and press F12 (or right click and then Inspect). From here, you just have to look through the HTML code and you'll find the 1/3 of the flag
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins1.png?raw=true"/>
</p>
Flag 1/3: picoCTF{tru3_d3 <br>
Now, switch to the Source tab and click myjs.js file. See the last line of the code and you'll get the 3/3 of the flag
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins2.png?raw=true"/>
</p>
Flag 3/3: _lucky?832b0699} <br>
Last, we'll search for the last piece of the flag. Click the mycss.css file and look over the last line.
<p align="center">
    <img src="https://github.com/ftiannisa/writeup/blob/main/media/pico-ins3.png?raw=true"/>
</p>
Flag 2/3: t3ct1ve_0r_ju5t<br>
Now that we get all the pieces, just put them together in order from 1/3 to 2/3 and 3/3. Easy, isn't it? ;)
<br><br>

### FLAG

<details>
  <summary></summary>
  
  picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
</details>
