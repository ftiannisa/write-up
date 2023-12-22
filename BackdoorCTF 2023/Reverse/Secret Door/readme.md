# Secret Door

### Category: Reverse Engineering

###### author: it4ch1 - [ 117 solves / 424 pts ]

Sorry to have lost the key of the secret Gate like this... But believe me there is a way if you follow the Right Path..

Attachments:

- [public.zip](/BackdoorCTF%202023/Reverse/Secret%20Door/public.zip)

## Solution:

Inside the zip file, there are 2 files: `encoded.bin` and `chall.out`

`encoded.bin` is a data file that contains random unreadable strings and `chall.out` is a non-stripped, 64-bit ELF.

```console
$ file chall.out
chall.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=482f71c02048b82f3f4d68962f3f99e6c33aba16, for GNU/Linux 3.2.0, not stripped
```

Next, I load the ELF into IDA and analyze the main function.

![](/media/bd23-sd.png)

In main(), it checks the length of input, intialize an int array, do some xor operation, and call bunch of other functions, but _Spoiler alert: most of this code is not that important_

Why? because the **key** function to get the flag is `func_1()` and that's it.

Here's the code for `func_1()`.

```cpp
__int64 __fastcall func_1(char a1, char a2)
{
  _BYTE *v2; // rax
  _BYTE *v3; // rax
  __int64 v4; // rbx
  const char *v5; // rsi
  char v7; // [rsp+1Bh] [rbp-485h] BYREF
  int i; // [rsp+1Ch] [rbp-484h]
  __int64 v9[2]; // [rsp+20h] [rbp-480h] BYREF
  __int64 v10[2]; // [rsp+30h] [rbp-470h] BYREF
  char v11[32]; // [rsp+40h] [rbp-460h] BYREF
  char v12[32]; // [rsp+60h] [rbp-440h] BYREF
  char v13[512]; // [rsp+80h] [rbp-420h] BYREF
  char v14[520]; // [rsp+280h] [rbp-220h] BYREF
  unsigned __int64 v15; // [rsp+488h] [rbp-18h]

  v15 = __readfsqword(0x28u);
  std::allocator<char>::allocator(v11);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string<std::allocator<char>>(
    v12,
    "encoded.bin",
    v11);
  std::allocator<char>::~allocator(v11);
  std::ifstream::basic_ifstream(v14, v12, 4LL);
  std::allocator<char>::allocator(&v7);
  std::istreambuf_iterator<char>::istreambuf_iterator(v10);
  std::istreambuf_iterator<char>::istreambuf_iterator(v9, v14);
  std::vector<char>::vector<std::istreambuf_iterator<char>,void>(v11, v9[0], v9[1], v10[0], v10[1], &v7);
  std::allocator<char>::~allocator(&v7);
  for ( i = 0; i <= 90245; ++i )
  {
    if ( (i & 1) != 0 )
    {
      v3 = (_BYTE *)std::vector<char>::operator[](v11, i);
      *v3 ^= a2;
    }
    else
    {
      v2 = (_BYTE *)std::vector<char>::operator[](v11, i);
      *v2 ^= a1;
    }
  }
  std::ofstream::basic_ofstream(v13, "the_door.jpg", 4LL);
  v4 = std::vector<char>::size(v11);
  v5 = (const char *)std::vector<char>::data(v11);
  std::ostream::write((std::ostream *)v13, v5, v4);
  std::ofstream::close(v13);
  std::ofstream::~ofstream(v13);
  std::vector<char>::~vector(v11);
  std::ifstream::~ifstream(v14);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v12);
  return 0LL;
}
```

What it does:

- get the content of `encoded.bin`
- do iteration `i` from 0 to 90245 (which is the length of encoded.bin)
  - if `i` is odd, xor the element-i of encoded.bin with `a2`
  - if `i` is even, xor the element-i of encoded.bin with `a1`
- save the result as `the_door.jpg`

Now, let's back to the main() function. If we look at the line 66, we can see the code passed 2 arguments to func_1(): `*v7` and `v7[16]`. While v7 get its value from func_3(), we don't really need to break it down because there's `func_2()` that checks the value of v7.

```cpp
_BOOL8 __fastcall func_2(int *a1)
{
  return *a1 == 78
      && a1[1] != (*a1 == 15)
      && a1[2] == 120
      && a1[3] != (a1[2] == 31)
      && a1[4] == 120
      && a1[5] != (a1[4] == 11)
      && a1[6] == 116
      && a1[6] != (a1[7] == 6)
      && a1[8] == 100
      && a1[9] != (a1[8] == 33)
      && a1[10] == 99
      && a1[11] != (a1[10] == 34)
      && a1[12] == 120
      && a1[13] == a1[12]
      && a1[14] == 114
      && a1[15] == a1[14] + 1
      && a1[16] == 33;
}
```

and since we only need two values, we don't have to copy all that. Just get the first value and the last one, which is 78 and 33.

Now I already get what I need, it's time to write the solver. I use Python and this is my script.

```py
v12 = open("encoded.bin", "rb").read()

a1 = 78
a2 = 33

img = open("the_door.jpg", "wb")
for idx, v in enumerate(v12):
    if (idx & 1) != 0:
        v ^= a2
    else:
        v ^= a1
    img.write(v.to_bytes(1, "big"))

img.close()
```

## FLAG

<details>
  <summary></summary>

![](/BackdoorCTF%202023/Reverse/Secret%20Door/the_door.jpg)

flag{0p3n3d_7h3_s3cr3t_r3d_d00r}

</details>
<br><br>
