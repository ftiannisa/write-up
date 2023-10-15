# Privilege Escalation

### Category: Forensics

CVE and full path file that used by attackers to perform privilege escalation

Format Flag: Fostifest{CVE-XXXX-XXXX:/path/path/path/file}<br><br>

### Solution:

1. Terdapat shell yang telah ditanamkan oleh attacker ke dalam server Fostifest
2. kami coba untuk mencari dengan menggunakan tools pencarian yang ada di winscp dengan key search \*.sh

![](/media/fosti-pe1.png)

3. ditemukan beberapa file mencurigakan yang terdapat pada direktori /var/www/.,/ dan /var/www/.,/root
4. setelah itu terdapat file exp yang berada pada direktori /var/www/.,/root/ yang merupakan file privilege escalation

![](/media/fosti-pe2.png)

5. kemudian kami menemukan referensi dari google dengan link https://github.com/Al1ex/CVE-2022-0847 yang menyatakan exp merupakan file backdoor dengan teknik privilege escalation
6. kami pun mengecek file tersebut di virus total

![](/media/fosti-pe3.png)

7. dan kami menemukan flagnya

<br>
<br>

### FLAG

<details>
  <summary></summary>
  
Fostifest{CVE-2022-0847:/var/www/.,/root/exp}
</details>
