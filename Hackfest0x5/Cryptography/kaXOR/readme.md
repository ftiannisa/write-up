# kaXOR

### Category: Cryptography

###### author: rehan

Just EZ chall, and I know u can do it!

- chall.py

```py
from secret import flag, key

cipher = ''
for i in range(len(flag)):
	cipher += chr(ord(flag[i]) ^ key)

a = open('cipher.txt', 'w')
a.write(cipher)
a.close()
```

- [cipher.txt](/Hackfest0x5/Cryptography/kaXOR/cipher.txt)

<br><br>

### Solution:

Diberikan 2 file, chall.py dan cipher.txt

Jika melihat isi chall.py, kita tahu bahwa file cipher.txt adalah hasil enkripsi dengan simple XOR, tetapi kita tidak tahu isi flag maupun key yang digunakan. Oleh karena itu, kita akan menggunakan teknik brute force, berikut script yang saya buat.

```py
c = open("cipher.txt", "r")
cipher = c.readline()

for key in range(255):
    msg = ''
    for i in cipher:
        msg += chr(ord(i) ^ key)
    if "hack" in msg:
        print(msg)
```

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{bRu73F0rC3_i5_th3_R1gh7_4nSweR_f0R_th1S_Ch4l1enG3}
</details>

<br><br>
🏷️tags: brute force XOR
