newmap = {
2: "\nPostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "\n",
41: "\nESC",
42: "\nDEL",
43: "\t",
44: " ",
45: "-",
47: "[",
48: "]",
51: [";", ":"],
54: ",",
55: ".",
56: "/",
57: "\nCAPS",
79: "\nRightArrow",
80: "\nLetfArrow"
}

myKeys = open('hexoutput.txt')

shift = False
for line in myKeys:
    bytesArray = bytearray.fromhex(line.strip())

    for byte in bytesArray:
        if byte != 0:
            keyVal = int(byte)

            if keyVal in newmap:
                if keyVal == 2:
                    shift = True
                    continue
                if keyVal == 51:
                    if shift:
                        print(newmap[keyVal][1], end="")
                        shift = False
                        continue
                    else:
                        print(newmap[keyVal][0], end="")
                        continue
                
                print(newmap[keyVal], end="")
            else:
                print("\nNo map found for this value: " + str(keyVal))

print()