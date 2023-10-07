# Traffic Enjoyer

### Category: Forensics

###### author: deomkicer#3362

P balap first blood

- [traffic.pcap](/Gemastik%202022/Forensics/Traffic%20Enjoyer/traffic.pcap)
  <br><br>

### Solution:

Disediakan sebuah file traffic.pcap. File berekstensi .pcap ini merupakan sebuah berkas data berisi data paket jaringan yang dibuat selama penangkapan jaringan langsung. File ini dapat dibuka serta dianalisis menggunakan tools Wireshark. Ketika di import ke dalam Wireshark, terdapat banyak sekali data yang tercapture. Dari sini kita coba menggunakan filter di tab menu **Statistic > Protocol Hierarchy**. Setelah itu lakukan filter pada **Line-based text data**.

<p align="center">
    <img src="../../../media/gem22-te1.png"/>
</p>

Jika kita lihat salah satu isinya, data yang ada berupa string base64 dan bila di-decode menghasilkan hex bytes file PNG.

Maka, lakukan **Export Objects > HTTP**

<p align="center">
    <img src="../../../media/gem22-te2.png"/>
</p>

Kemudian, decode semua isi file dan simpan ke dalam file PNG. Untuk memudahkan proses ini, kami membuat kode program seperti berikut.

<p align="center">
    <img src="../../../media/gem22-te3.png"/>
</p>

Berikut hasil file PNG yang didapat

</p>
<p align="center">
    <img src="../../../media/gem22-te4.png"/>
</p>

<br>
<br>

### FLAG

<details>
  <summary></summary>
  
Gemastik2022{balapan_f1rst_bl00d_is_real_f580c176}
</details>
