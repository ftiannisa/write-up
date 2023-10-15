# [Bandit](https://overthewire.org/wargames/bandit/)

> ⚠️ DISCLAIMER ⚠️\
> This write-up is for archival and educational purpose. I really encourage you to try first and read any materials given in the lab. Use this write-up as your last resort.\
> Happy learning and good luck! :) –fr.🔮

![](https://progress-bar.dev/61/?title=Incomplete&width=150)

Level: 20/33

## Contents.

<details>
  <!-- <summary></summary> -->
  
  - [Level 0](#level-0)
  - [Level 0 → Level 1](#level-0--level-1)
  - [Level 1 → Level 2](#level-1--level-2)
  - [Level 2 → Level 3](#level-2--level-3)
  - [Level 3 → Level 4](#level-3--level-4)
  - [Level 4 → Level 5](#level-4--level-5)
  - [Level 5 → Level 6](#level-5--level-6)
  - [Level 6 → Level 7](#level-6--level-7)
  - [Level 7 → Level 8](#level-7--level-8)
  - [Level 8 → Level 9](#level-8--level-9)
  - [Level 9 → Level 10](#level-9--level-10)
  - [Level 10 → Level 11](#level-10--level-11)
  - [Level 11 → Level 12](#level-11--level-12)
  - [Level 12 → Level 13](#level-12--level-13)
  - [Level 13 → Level 14](#level-13--level-14)
  - [Level 14 → Level 15](#level-14--level-15)
  - [Level 15 → Level 16](#level-15--level-16)
  - [Level 16 → Level 17](#level-16--level-17)
  - [Level 17 → Level 18](#level-17--level-18)
  - [Level 18 → Level 19](#level-18--level-19)
  - [Level 19 → Level 20](#level-19--level-20)
  - [Level 20 → Level 21](#level-20--level-21)
</details>

## Level 0

Connect SSH.

commands: `ssh <username>@<remote> -p <port>`

```sh
$ ssh bandit0@bandit.labs.overthewire.org -p 2220
```

<!-- bandit0 -->
<br>

## Level 0 → Level 1

Read file.

commands: `cat <filename>`

```sh
$ cat readme
# ^D or type "exit" to exit ssh
$ ssh bandit1@bandit.labs.overthewire.org -p 2220
```

<!-- NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL -->
<br>

## Level 1 → Level 2

Read file with special characters.

commands: `cat`

```sh
$ cat ./-
```

<!-- rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi -->
<br>

## Level 2 → Level 3

Read file with spaces.

commands: `cat`

```sh
$ cat "spaces in this filename"
```

<!-- aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG -->
<br>

## Level 3 → Level 4

Change directory, see hidden files.

commands: `cd <directory>`, `ls -la`

```sh
$ cd inhere
$ ls -la # or just `la` for short
```

<!-- 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe -->
<br>

## Level 4 → Level 5

Check file types (iterable).

commands: `cd`, `file <filename>`

```sh
$ cd inhere
$ file ./*
```

<!-- lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR -->
<br>

## Level 5 → Level 6

Find file with specific properties.

commands: `find`

```sh
$ find . -size 1033c
```

<!-- P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU -->
<br>

## Level 6 → Level 7

Find file with specific properties and owner.

commands: `find`

```sh
$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

_\*) The **2>/dev/null** at the end of the find command tells your shell to redirect the standard error messages to /dev/null._ [source](httsh://exploreinformatica.com/how-to-exclude-all-permission-denied-messages-when-using-find-command)

<!-- z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S -->
<br>

## Level 7 → Level 8

Search word in file.

commands: `grep <pattern> <filename>`

```sh
$ grep millionth data.txt
```

<!-- TESKZC0XvTetK0S9xNwm25STk5iWrBvP -->
<br>

## Level 8 → Level 9

Find unique data in file.

commands: `sort`, `uniq`

```sh
$ sort data.txt | uniq -u
```

<!-- EN632PlfYiZbn3PhVK3XOGSlNInNE00t -->
<br>

## Level 9 → Level 10

Read human-readable strings, search word in file.

commands: `strings <filename>`, `grep`

```sh
$ strings data.txt | grep ==
```

<!-- G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s -->
<br>

## Level 10 → Level 11

Read file, decode base64 data.

commands: `cat`, `base64`

```sh
$ cat data.txt | base64 -d
```

<!-- 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM -->
<br>

## Level 11 → Level 12

Read file, decode ROT13.

commands: `cat`, `tr`

```sh
$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

<!-- JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv -->
<br>

## Level 12 → Level 13

- Extract files.
- Convert hexdump to binary.
- Make new directory, copy datafile, rename file.

commands: `gzip`, `bzip2 -d` or `bunzip2`, `tar -xf`, `xxd`, `mkdir`, `cp <source> <directory>`, `mv <source> <directory>`

```sh
# make new dir and change dir
$ mkdir /tmp/ur_uname
$ cd /tmp/ur_uname

# copy file to current dir
$ cp ~/data.txt .

# convert hexdump to .gz file
$ xxd -r data.txt > data.gz

# extract gzip file
$ gzip -d data.gz

# extract bzip2 file
$ bzip2 -d data

$ mv data.out data.gz   # rename file
$ gzip -d data.gz

# extract tar file
$ tar -xf data
$ tar -xf data5.bin

$ bunzip2 data6.bin     # another way to extract bzip2
$ tar -xf data6.bin.out
$ mv data8.bin data8.gz
$ gzip -d data8.gz
$ cat data8
```

_**Tips**: use `ls` to see what files have been created after extracting a file and `file` command to check the output's file type. Also use `mv` to rename the file if necessary._

<!-- wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw -->
<br>

## Level 13 → Level 14

Connect SSH using private key.

commands: `ssh -i`

```sh
$ ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
```

<!-- fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq -->
<br>

## Level 14 → Level 15

Connect and send data over a network connection.

commands: `echo`, `nc <host> <port>`

> ❗ should log into bandit13 first.

```sh
$ echo [password] | nc 127.0.0.1 30000
# or just run the `nc <host> <port>` and then paste the password
```

[source](https://askubuntu.com/questions/509629/sending-data-to-port-does-not-seem-to-be-working-on-ubuntu-linux)

<!-- jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt -->
<br>

## Level 15 → Level 16

Send data using SSL encryption.

commands: `openssl s_client`, `echo`

```sh
$ echo [password] | openssl s_client -connect 127.0.0.1:30001 -ign_eof
# or run the `openssl` with/-out -ign_eof, then paste the password
```

[source](https://stackoverflow.com/questions/23352152/how-to-send-a-string-to-server-using-s-client)

<!-- JQttfApK4SeyHwDlI9SXGR50qclOAil1 -->
<br>

## Level 16 → Level 17

Scan network within port range.

commands: `nmap`

```sh
$ nmap -sV localhost -p31000-32000 # or `nmap -A -T4`
$ echo [password] | openssl s_client -connect localhost:31790 -ign_eof

# copy the creds to a new key file then connect to bandit17
# if there's a "<key> are too open" error,
# run this and connect again
$ chmod 400 <key_filename>
```

> `nmap -sV`: determine service/version info \
> `nmap -A`: enable OS and version detection, script scanning, and traceroute \
> `nmap -T4`: (optional?) faster execution

[soure](https://manpages.ubuntu.com/manpages/lunar/en/man1/nmap.1.html)
<br>

## Level 17 → Level 18

Compare files line by line.

commands: `diff <file1> <file2>`

> ❗ should log into bandit16 first.

```sh
$ diff passwords.old passwords.new
```

> `%<` &emsp; lines from FILE1 \
> `%>` &emsp; lines from FILE2 \
> `%=` &emsp; lines common to FILE1 and FILE2

<!-- hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg -->
<br>

## Level 18 → Level 19

Read file directly through SSH login.

commands: `ssh`, `cat`

```sh
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

<!-- awhqfNnAbc1naukrpqDYcF95h7HoMTrC -->
<br>

## Level 19 → Level 20

Just use the setuid binary as told.

> 💡Hint: I figure that the binary is like the `sudo` command but for bandit20 user, not super-user 🤓

commands: `cat`

```sh
$ ./bandit20-do cat /etc/bandit_pass/bandit20
```

<!-- VxCazJaVykI6W36BkBU0mJTCM8rR95XT -->
<br>

## Level 20 → Level 21

Connect to your own network daemon. [Read this](https://stackoverflow.com/questions/51775230/what-does-connecting-to-own-network-daemon-mean)

commands: `nc -l <port>`

```sh
# You need to open 2 terminal tabs
# 00 - 1st tab
$ nc -l <port>

# 01 - 2nd tab
$ ./suconnect <port>

# 02 - paste the password on the 1st tab
```

<!-- NvEJF7oVjkddltPSrdKEFOllh9V1IBcq -->
<br>

<!-- ## Level X → Level X

DESC

commands:

```sh
$
```

<br> -->
