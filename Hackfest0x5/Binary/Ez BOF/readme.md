# Ez BOF

### Category: Binary Exploitation

###### author: kimnad

`nc 202.125.94.123 60901`

- [chall](/Hackfest0x5/Binary/Ez%20BOF/chall)

<br><br>

### Solution:

Pertama, buka file dengan IDA

![](/media/hf05-bof1.png)

Program memiliki variabel input (v4) dengan ukuran yang ditetapkan 44

![](/media/hf05-bof2.png)
![](/media/hf05-bof3.png)

### FLAG

<details>
  <summary></summary>
  
hackfest0x5{Buffer_0verflow_1s_Danger0us_Yo!!}
</details>

<br><br>
🏷️tags: BOF // buffer overflow
