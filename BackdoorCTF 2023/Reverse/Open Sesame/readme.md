# Open Sesame

### Category: Reverse Engineering

###### author: Sl4y3r_07 - [ 192 solves / 358 pts ]

Whisper the phrase, unveil with 'Open Sesame

Attachments:

- [opensesame.zip](/BackdoorCTF%202023/Reverse/Open%20Sesame/opensesame.zip)

## Solution:

Extract the zip and we will get `open_sesame.apk`. I use [decompiler.com](https://www.decompiler.com/) to decompile the apk (or you can use jd-gui, jadx, apktool, etc.)

Open the `AndroidManifest.xml` on resources directory, we can see that the Main Activity is located in `com.example.open_sesame` package.

```xml
<activity android:name="com.example.open_sesame.MainActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
</activity>
```

Next, open `sources/com/example/open_sesame/MainActivity.java`. This is what it looks like.

<details>
<summary>📄 MainActivity.java</summary>

```java
package com.example.open_sesame;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;

public class MainActivity extends AppCompatActivity {
    private static final int[] valid_password = {52, AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR, 49, 98, 97, 98, 97};
    private static final String valid_user = "Jack Ma";
    private Button buttonLogin;
    private EditText editTextPassword;
    private EditText editTextUsername;

    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        this.editTextUsername = (EditText) findViewById(R.id.editTextUsername);
        this.editTextPassword = (EditText) findViewById(R.id.editTextPassword);
        Button button = (Button) findViewById(R.id.buttonLogin);
        this.buttonLogin = button;
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                MainActivity.this.validateCredentials();
            }
        });
    }

    /* access modifiers changed from: private */
    public void validateCredentials() {
        String trim = this.editTextUsername.getText().toString().trim();
        String trim2 = this.editTextPassword.getText().toString().trim();
        if (!trim.equals(valid_user) || !n4ut1lus(trim2)) {
            showToast("Invalid credentials. Please try again.");
            return;
        }
        "flag{" + flag(Integer.toString(sl4y3r(sh4dy(trim2))), "U|]rURuoU^PoR_FDMo@X]uBUg") + "}";
    }

    private boolean n4ut1lus(String str) {
        int[] it4chi = it4chi(str);
        if (it4chi.length != valid_password.length) {
            return false;
        }
        for (int i = 0; i < it4chi.length; i++) {
            if (it4chi[i] != valid_password[i]) {
                return false;
            }
        }
        return true;
    }

    private int[] it4chi(String str) {
        int[] iArr = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            iArr[i] = str.charAt(i);
        }
        return iArr;
    }

    private String sh4dy(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char charAt = str.charAt(i);
            if (Character.isDigit(charAt)) {
                sb.append(charAt);
            }
        }
        return sb.toString();
    }

    private int sl4y3r(String str) {
        return Integer.parseInt(str) - 1;
    }

    private String flag(String str, String str2) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str2.length(); i++) {
            sb.append((char) (str2.charAt(i) ^ str.charAt(i % str.length())));
        }
        return sb.toString();
    }

    private void showToast(String str) {
        Toast.makeText(this, str, 0).show();
    }
}
```

</details>

_whew_, that's kinda long isn't it? let's break it down.

> 🐣 **TL;DR**
>
> - initialization of 2 variables, int array `valid_password` and string `valid_user`
>   - `valid_password` = {52, 108, 49, 98, 97, 98, 97} which equal to "4l1baba"
>   - `valid_user` = "Jack Ma"
> - get value of username and password
> - check whether username is equal to `valid_user`
> - convert password to an int array and check whether it has the same value as `valid_password`
> - get **only** the digits from the password strings (which equal to "41")
> - parse it into int and subtract by 1 --> `41 - 1 = 40`
> - convert the value back to string and use it as key for xor
>   ```
>   ciphertext = "U|]rURuoU^PoR_FDMo@X]uBUg"
>   key = "40"
>   ```
>   solver script is [here](#solver)

### Variable initialization

```java
private static final int[] valid_password = {52, AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR, 49, 98, 97, 98, 97};
private static final String valid_user = "Jack Ma";
```

on the top of `class MainActivity`, you can see there are 2 variable initialization, an integer array `valid_password` and a string `valid_user`

_wait a sec, what's AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR?_

Well, according to the [official docs](<https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#FEATURE_SUPPORT_ACTION_BAR()>), it has an int value of 108. So now we know the actual value or elements of `valid_password` is {52, 108, 49, 98, 97, 98, 97} and if we convert it to characters, the result will be "4l1baba".

### validateCredentials()

the onCreate() function is used to render layout and we can see there are 3 objects: 2 text field to input username and password and 1 button that will run `validateCredentials()` when clicked.

```java
public void validateCredentials() {
    String trim = this.editTextUsername.getText().toString().trim();
    String trim2 = this.editTextPassword.getText().toString().trim();
    if (!trim.equals(valid_user) || !n4ut1lus(trim2)) {
        showToast("Invalid credentials. Please try again.");
        return;
    }
    "flag{" + flag(Integer.toString(sl4y3r(sh4dy(trim2))), "U|]rURuoU^PoR_FDMo@X]uBUg") + "}";
}
```

what this function do is:

- get the username and password
- check if the value of username is equal to `valid_user`
- passed the value of password as an argument for `n4ut1lus()` function (which will be covered after this)
- if both conditions are true, the password will be processed through several functions (`sh4dy()` and `sl4y3r()`), then the result will be passed along with another random string as arguments for `flag()` function. (confused? it's ok, take your time lol)

### n4ut1lus() and it4chi()

These two functions are connected to each other and I will break `it4chi()` first to make it easier to understand the flow.

```java
private boolean n4ut1lus(String str) {
    int[] it4chi = it4chi(str);
    if (it4chi.length != valid_password.length) {
        return false;
    }
    for (int i = 0; i < it4chi.length; i++) {
        if (it4chi[i] != valid_password[i]) {
            return false;
        }
    }
    return true;
}

private int[] it4chi(String str) {
    int[] iArr = new int[str.length()];
    for (int i = 0; i < str.length(); i++) {
        iArr[i] = str.charAt(i);
    }
    return iArr;
}
```

`it4chi()` function gets the int value of each char and store in to an int array. Then inside `n4ut1lus()`, it checks whether this int array has the same length and the same value as `valid_password` or not.

### sh4dy(), sl4y3r(), and flag()

```java
private String sh4dy(String str) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < str.length(); i++) {
        char charAt = str.charAt(i);
        if (Character.isDigit(charAt)) {
            sb.append(charAt);
        }
    }
    return sb.toString();
}

private int sl4y3r(String str) {
    return Integer.parseInt(str) - 1;
}

private String flag(String str, String str2) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < str2.length(); i++) {
        sb.append((char) (str2.charAt(i) ^ str.charAt(i % str.length())));
    }
    return sb.toString();
}
```

- `sh4dy()` gets every characters of a string that is a digit.
- `sl4y3r()` parse a string to integer and subtract the number by 1
- `flag()` xor the first string with the second string

### Solver!

So now you already know what each function do, you can made a script to solve it. This is the simple script I used.

```py
pwd = [52, 108, 49, 98, 97, 98, 97]
pwd = ''.join([chr(i) for i in pwd if chr(i).isdigit()])
pwd = str(int(pwd)-1)
# print(pwd)

enc = "U|]rURuoU^PoR_FDMo@X]uBUg"

for idx in range(len(enc)):
    print(chr(ord(enc[idx]) ^ ord(pwd[idx % len(pwd)])), end='')
```

## FLAG

<details>
  <summary></summary>
  
flag{aLiBabA_and_forty_thiEveS}

</details>
<br><br>

🏷️tags: Android
