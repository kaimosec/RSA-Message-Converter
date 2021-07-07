# RSAMessageConverter

----------
Converts strings or binary to a number and visa versa for the sake of working with RSA.

# Usage

----------------
```
python3 convertmessage.py [-h] [--cipher | --uncipher] [--message MESSAGE | --file FILE] [--binary] [--out OUT] [--encoding ENCODING]

optional arguments:
  -h, --help           show this help message and exit
  --cipher             convert from plain to cipher
  --uncipher           convert from cipher to plain
  --message MESSAGE    message to perform conversion on
  --file FILE          file to perform conversion on
  --binary             specify that the message is binary
  --out OUT            file to output to. Required when unciphering to binary
  --encoding ENCODING  default is ascii

```

# Examples

-----------------
**Convert message to number**
```
python3 convertmessage.py --cipher --message "Rosetta Code"
# Cipher: 25512506514985639724585018469

```

**Convert number to message**
```
python3 convertmessage.py --uncipher --message 25512506514985639724585018469                                                                                                                                                                                                                                       2 ⨯
# Rosetta Code
```

**Convert binary file to number**
```
python3 convertmessage.py --cipher --file pic.png --binary 
# Cipher: 14725267986073729673605561729446055850512790630226246458370820124918558223...
```

**Convert number to binary file**
```
python3 convertmessage.py --uncipher --binary --out out.png --message 14725267986073729673605561729...
```

# Todo

----------------------
- Add padding functionality