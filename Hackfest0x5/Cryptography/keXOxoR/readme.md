# keXOxoR

### Category: Cryptography

###### author: rehan

No Messages

- chall.py

```py
from secret import flag
import random

key = ''
for i in range(11):
    key += chr(random.randrange(0, 256))

cipher = ''
for j in range(len(flag)):
    cipher += chr(ord(flag[j]) ^ ord(key[j%len(key)]))

w = open('cipher.txt', 'w', encoding='utf-8')
w.write(cipher)
w.close()
```

- [cipher.txt](/Hackfest0x5/Cryptography/keXOxoR/cipher.txt)
  <br><br>

### Solution:

Dilihat dari file chall.py tersebut, key terdiri dari 11 karakter dan setiap karakternya didapat secara acak. Kemudian key tersebut digunakan untuk meng-enkripsi flag. Sekarang, untuk mendekripsi ciphertext, kita perlu memanfaatkan sifat XOR yang dapat dipertukarkan, contohnya jika kita melakukan operasi “X ^ key = Y”, maka kita bisa mendapatkan nilai key dengan melakukan operasi “X ^ Y = key”. Anggaplah X adalah flag dan Y adalah ciphertext. Sebelumnya karena kita sudah tahu format flag, maka 11 karakter pertama dari flag tersebut adalah “hackfest0x5”. Selanjutnya, lakukan operasi XOR antara potongan flag yang sudah diketahui dengan ciphertext. Berikut kode lengkapnya

```py
c = open("cipher.txt", "r", encoding="utf8")
cipher = c.readline()

flag = 'hackfest0x5'

key = ''
for i in range(len(flag)):
    key += chr(ord(cipher[i]) ^ ord(flag[i]))

flag = ''
for i in range(len(cipher)):
    flag += chr(ord(cipher[i]) ^ ord(key[i%len(key)]))

print(flag)
```

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{Us3_uR_L0g1c_anD_A_l1t7L3_b1t_M4g1c_T0_g3T_Fl4G}
</details>

<br><br>
🏷️tags: brute force XOR, knownplain attack
