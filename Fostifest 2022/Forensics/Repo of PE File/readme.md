# Repo of PE File

### Category: Forensics

Original Repository of files used for privilege escalation

Format Flag: Fostifest{url}<br><br>

### Solution:

1. setelah menemukan direktori yang terdapat backdoor privilege escalation, kami analisa lagi pada folder root pada direktori /var/www/.,/root/ dengan menggunakan perintah
`ls -a`
<p align="center">
    <img src="../../../media/fosti-rpe1.png"/>
</p>

2. setelah kami enter dan menemukan adanya folder .git setelah kami buka dan mengecek file nya satu persatu dan di file config kami menemukan repositori yang digunakan untuk privilege escalation yaitu dengan link https://github.com/Al1ex/CVE-2022-0847
<p align="center">
    <img src="../../../media/fosti-rpe2.png"/>
</p>

3. dan kami menemukan flag nya

<br>
<br>

### FLAG

<details>
  <summary></summary>
  
Fostifest{https://github.com/Al1ex/CVE-2022-0847}
</details>
