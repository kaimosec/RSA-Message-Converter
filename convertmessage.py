import argparse
import math
import sys


# Convert number to string or bytes
def uncipher(num: int, decode: bool, decoding=''):
    bytes = num.to_bytes(get_num_bytes(num), 'big')
    if decode:
        if len(decoding) > 0:
            return bytes.decode(decoding)
        return bytes.decode()
    return bytes


# Get the number of bits in a number
def get_num_bits(num: int):
    i = 0
    while True:
        if num <= pow(2, i):
            break
        i += 1

    return i


# Get the number of bytes in a number
def get_num_bytes(num: int):
    return int(math.ceil(get_num_bits(num) / 8.0))


# Convert a string/bytes into a number
def cipher(message, is_bytes: bool, encoding=''):
    if not is_bytes:
        if len(encoding) > 0:
            bytes = message.encode(encoding)
        else:
            bytes = message.encode()
    else:
        bytes = message
    return int.from_bytes(bytes, "big")


# Arguments
class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


if __name__ == '__main__':
    parser = Parser("convertmessage.py")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--cipher", help='convert from plain to cipher', action='store_true')
    group.add_argument('--uncipher', help='convert from cipher to plain', action='store_true')

    group_message = parser.add_mutually_exclusive_group()
    group_message.add_argument("--message", help='message to perform conversion on')
    group_message.add_argument("--file", help="file to perform conversion on")

    parser.add_argument('--binary', help='specify that the message is binary', action='store_true')
    parser.add_argument('--out', help='file to output to. Required when unciphering to binary')
    parser.add_argument('--encoding', help='default is ascii')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        exit(1)

    # Argument validation
    if not args.message and not args.file:
        print("Error: Either --message or --file must be specified")
        exit(0)
    if args.message and args.file:
        print("Error: --message and --file cannot be specified at the same time")
        exit(0)
    if args.binary and args.uncipher and not args.out:
        print("Error: When unciphering with binary, --out must be specified")
        exit(0)

    if args.cipher:
        if args.message:
            plaintext = args.message
            num = cipher(plaintext, False)
        else:
            if not args.binary:
                with open(args.file, 'r') as file:
                    plaintext = file.read()
                    num = cipher(plaintext, False)
            else:
                with open(args.file, 'rb') as file:
                    bytes = file.read()
                    num = cipher(bytes, True)

        print("Cipher: {}".format(num))
    elif args.uncipher:
        if args.message:
            num = args.message
        else:
            with open(args.file, 'r') as file:
                num = file.read()

        num = int(num)

        if not args.binary:
            string = uncipher(num, True)
            print(string)
        else:
            bytes = uncipher(num, False)
            with open(args.out, 'wb') as file:
                file.write(bytes)
