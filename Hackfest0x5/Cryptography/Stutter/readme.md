# Stutter

### Category: Cryptography

###### author: twistbil

looks simple, but i stuttered when i saw this. Can you help me please :(

- chall.py

```py
from secret import flag
import hashlib

lis = []
for i in range(0, len(flag)):
	a = flag[i:i+3]
	lis.append(hashlib.md5(a.encode()).hexdigest())

w = open('cipher.txt', 'w')

for i in lis:
	w.write(i+'\n')

w.close()
```

- [cipher.txt](/Hackfest0x5/Cryptography/Stutter/cipher.txt)
  <br><br>

### Solution:

Dilihat dari source codenya, flag pada challenge ini di-enkripsi dengan md5. Hash tidak bisa didekripsi, kecuali kita tahu inputnya. Maka, untuk challenge ini saya menggunakan brute force. Berikut kode programnya:

```py
import hashlib

hashed = open("cipher.txt", "r")
lines = hashed.readlines()
get_lines = lines[0::3]

flag = ''
for line in get_lines:
    ch = ''
    for i in range(32, 127):
        for j in range(32,127):
            for k in range(32, 127):
                ch = chr(i) + chr(j) + chr(k)
                f = hashlib.md5(ch.encode()).hexdigest()
                if f == line.rstrip():
                    flag += ch

print(flag)
```

### FLAG

<details>
  <summary></summary>
  
 hackfest0x5{s1mple_cr4cking_the_sststustuttutterterieringinging_hash}

</details>

<br><br>
🏷️tags: brute force hash
