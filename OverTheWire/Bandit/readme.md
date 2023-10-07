# [Bandit](https://overthewire.org/wargames/bandit/)

> ⚠️ DISCLAIMER ⚠️\
> This write-up is for archival and educational purpose. I really encourage you to try first and read any materials given in the lab. Use this write-up as your last resort.\
> Happy learning and good luck! :) –fr.🔮

Status: Incomplete, Current Level: 10

## Contents.

<details>
  <!-- <summary></summary> -->
  
  - [Level 0](#level-0)
  - [Level 0 → Level 1](#level-0-→-level-1)
  - [Level 1 → Level 2](#level-1-→-level-2)
  - [Level 2 → Level 3](#level-2-→-level-3)
  - [Level 3 → Level 4](#level-3-→-level-4)
  - [Level 4 → Level 5](#level-4-→-level-5)
  - [Level 5 → Level 6](#level-5-→-level-6)
  - [Level 6 → Level 7](#level-6-→-level-7)
  - [Level 7 → Level 8](#level-7-→-level-8)
  - [Level 8 → Level 9](#level-8-→-level-9)
  - [Level 9 → Level 10](#level-9-→-level-10)
  - [Level 10 → Level 11](#level-10-→-level-11)
  <!-- - [Level 11 → Level 12](#level-11-→-level-12) -->
</details>

## Level 0

Connect SSH.

commands: `ssh <username>@<remote> -p <port>`

```ps
$ ssh bandit0@bandit.labs.overthewire.org -p 2220
```

<!-- bandit0 -->
<br>

## Level 0 → Level 1

Read file.

commands: `cat <filename>`

```ps
$ cat readme
# ^D or type "exit" to exit ssh
$ ssh bandit1@bandit.labs.overthewire.org -p 2220
```

<!-- NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL -->
<br>

## Level 1 → Level 2

Read file with special characters.

commands: `cat`

```ps
$ cat ./-
```

<!-- rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi -->
<br>

## Level 2 → Level 3

Read file with spaces.

commands: `cat`

```ps
$ cat "spaces in this filename"
```

<!-- aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG -->
<br>

## Level 3 → Level 4

Change directory, see hidden files.

commands: `cd <directory>`, `ls -la`

```ps
$ cd inhere
$ ls -la # or just `la` for short
```

<!-- 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe -->
<br>

## Level 4 → Level 5

Check file types (iterable).

commands: `cd`, `file <filename>`

```ps
$ cd inhere
$ file ./*
```

<!-- lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR -->
<br>

## Level 5 → Level 6

Find file with specific properties.

commands: `find`

```ps
$ find . -size 1033c
```

<!-- P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU -->
<br>

## Level 6 → Level 7

Find file with specific properties and owner.

commands: `find`

```ps
$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

_\*) The **2>/dev/null** at the end of the find command tells your shell to redirect the standard error messages to /dev/null._ [source](https://exploreinformatica.com/how-to-exclude-all-permission-denied-messages-when-using-find-command)

<!-- z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S -->
<br>

## Level 7 → Level 8

Search word in file.

commands: `grep <pattern> <filename>`

```ps
$ grep millionth data.txt
```

<!-- TESKZC0XvTetK0S9xNwm25STk5iWrBvP -->
<br>

## Level 8 → Level 9

Find unique data in file.

commands: `sort`, `uniq`

```ps
$ sort data.txt | uniq -u
```

<!-- EN632PlfYiZbn3PhVK3XOGSlNInNE00t -->
<br>

## Level 9 → Level 10

Read human-readable strings, search word in file.

commands: `strings`, `grep`

```ps
$ strings data.txt | grep ==
```

<!-- G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s -->
<br>

## Level 10 → Level 11

Read file, decode base64 data.

commands:

```ps
$ cat data.txt | base64 -d
```

<!-- 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM -->
<br>

<!-- ## Level X → Level X

DESC

commands:

```ps
$
```

<br> -->
