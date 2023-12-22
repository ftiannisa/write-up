# Sonic-Hide_and-Seek

### Category: Forensics

###### author: 7π4nd5R_G0d - [ 57 solves / 468 pts ]

From the apollo moon landing in 1969 to people using Deepfake to fool others, the use of technology has changed. Anyways, use your skills to uncover the deep secrets of the moon landing from the given data. Adios amigo.

Attachments:

- [hideandseek.wav](/BackdoorCTF%202023/Forensics/hideandseek.wav)

## Solution:

We're given an audio file, a .wav file to be exact. At first, I checked the file using `file`, `binwalk`, and `exiftool` commands but nothing interesting. Then, my first _instinct_ (lol) was to use DeepSound. Turned out I was right, we get a text file that says:

```
PART3: 4r5n't_th3y?}
```

Next step, I opened the audio on Sonic Visualiser (or Audacity, both are fine), checked for spectrogram and saw a text. We get the first part of the flag.

![sonic](/media/bd23-sonic.png) <br>
text from the spectrogram: `Part1: flag{aud105`

Then I got stuck but one of my teammates suggested to use sstv decoder using Robot36. It's an Android app but since I'm too lazy to grab my phone, I look for an alternative instead and found this [repo / tools](https://github.com/colaclanth/sstv) which do the same job. The installation and usage is pretty easy too, just follow the guide. Use this command to extract an image:

```console
$ sstv -d hideandseek.wav -o sstv.png
[sstv] Searching for calibration header... Found!
[sstv] Detected SSTV mode Robot 36
[sstv] Decoding image...   [####################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
```

Final result: `Part2: _4r3_c00l_`

![](/BackdoorCTF%202023/Forensics/sstv.png)

Last, just combine all parts and submit!

## FLAG

<details>
  <summary></summary>
  
flag{aud105_4r3_c00l_4r5n't_th3y?}

</details>
<br><br>

🏷️tags: DeepSound, spectrogram, SSTV, steganography on audio wav

### References

- [SSTV Decoder](https://github.com/colaclanth/sstv)
