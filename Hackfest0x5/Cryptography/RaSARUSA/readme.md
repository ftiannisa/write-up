# ReSAh

### Category: Cryptography

###### author: rehan

U can do it too, right?

- rahasia.txt

```
c   : 606692285506838941840602456152941805058687761035977742885434270828366768350801130402690262903464242989622720049447625017
e   : 65537
n   : 833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019
```

<br><br>

### Solution:

Di dalam file text tersebut, disediakan nilai c sebagai ciphertext, e, dan n. Dalam RSA sendiri, dibutuhkan dua buah bilangan prima, p dan q, yang kemudian akan dikalikan untuk mendapatkan n. Oleh karena itu, untuk mendapatkan nilai p dan q tersebut, kita harus melakukan faktorisasi terhadap n. Di sini, saya menggunakan website [factordb](http://www.factordb.com/index.php) untuk faktorisasi. Selanjutnya, kita akan mencari nilai phi dan d, lalu mendekripsi ciphertext. Berikut kode program yang saya pakai:

```py
from Crypto.Util.number import *
from Crypto.PublicKey import RSA

c = 606692285506838941840602456152941805058687761035977742885434270828366768350801130402690262903464242989622720049447625017
n = 833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019
e = 65537

# factorization
p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901

phi = (p-1)*(q-1) #find phi

d = inverse(e,phi) #find d

msg = pow(c,d,n) #decrypt c -> msg = (c to the d) mod n

print(long_to_bytes(msg)) #convert to byte string and print output

```

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{aN0th3R__EZZ_Ch4lL___H4v3_fUn}
</details>

<br><br>
🏷️tags: RSA
