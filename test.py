import convertmessage

# Wrote these 2 function to see exactly how int.from_bytes works, used in cipher()
# def test_cipher(plaintext):
#     bytes = plaintext.encode()
#     num = 0
#     order = 0
#     for i in range(len(bytes) - 1, -1, -1):
#         byte = bytes[i]
#         for j in range(0, 8):
#             bit = get_bit_value(byte, j)
#             num += bit * pow(2, order)
#             order += 1
#     return num
#
#
# # Get the bit value of byte that is at n position from LSB. n = 0 gives LSB value
# def get_bit_value(byte, n):
#     return (byte & pow(2, n)) >> n

a = 'Rosetta Code'
print(a)

num = convertmessage.cipher(a, False)
print(num)

num_bits = convertmessage.get_num_bits(num)
print(num_bits)

num_bytes = convertmessage.get_num_bytes(num)
print(num_bytes)

decode = convertmessage.uncipher(num, True)
print(decode)