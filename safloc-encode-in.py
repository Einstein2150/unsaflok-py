#based on https://gitee.com/wangshuoyue/unsaflok
#modified and Python3-Port by Einstein2150

import binascii

# Lookup-Tabelle zum Codieren (c_aEncode aus dem C-Code)
c_aEncode = [
    236, 116, 192, 99, 86, 153, 105, 100, 159, 23,
    38, 198, 240, 1, 16, 77, 202, 82, 138, 75,
    122, 175, 173, 32, 115, 162, 15, 194, 80, 120,
    54, 68, 25, 30, 114, 210, 50, 183, 107, 248,
    5, 174, 199, 28, 85, 113, 89, 19, 17, 73,
    250, 252, 127, 43, 52, 102, 69, 165, 185, 21,
    169, 163, 134, 150, 219, 45, 218, 208, 33, 84,
    189, 227, 131, 141, 110, 155, 83, 149, 4, 228,
    42, 112, 39, 94, 35, 133, 135, 36, 209, 237,
    34, 27, 214, 98, 118, 67, 48, 193, 66, 132,
    91, 253, 95, 40, 254, 58, 20, 55, 176, 184,
    26, 61, 171, 72, 251, 152, 3, 166, 119, 201,
    11, 117, 97, 8, 241, 245, 217, 121, 101, 172,
    229, 164, 223, 191, 235, 10, 204, 249, 125, 195,
    136, 13, 142, 232, 220, 247, 143, 156, 47, 109,
    161, 65, 9, 188, 92, 60, 57, 144, 124, 197,
    46, 212, 51, 78, 206, 213, 88, 79, 200, 216,
    31, 130, 22, 62, 215, 255, 190, 146, 157, 196,
    211, 14, 29, 181, 93, 24, 7, 126, 106, 243,
    37, 128, 108, 203, 70, 140, 246, 231, 242, 177,
    187, 41, 145, 158, 205, 233, 148, 224, 170, 137,
    221, 234, 230, 81, 168, 71, 63, 2, 59, 87,
    96, 12, 207, 238, 154, 160, 179, 123, 225, 147,
    186, 178, 182, 222, 0, 226, 167, 139, 76, 53,
    74, 111, 239, 18, 129, 44, 180, 56, 90, 244,
    151, 64, 104, 6, 49, 103
]

def encrypt_card(hex_string):
    data = bytearray(binascii.unhexlify(hex_string))
    encrypted_card = bytearray(len(data))

    # Initial Bit-Manipulation
    b = 0
    for i in range(len(data)):
        b2 = data[i]
        num2 = i
        for j in range(8):
            num2 += 1
            if num2 >= len(data):
                num2 -= len(data)
            b3 = data[num2]
            b4 = b2 & 1
            b2 = (b2 >> 1) | (b << 7)
            b = b3 & 1
            b3 = (b3 >> 1) | (b4 << 7)
            data[num2] = b3
        data[i] = b2

    if len(data) == 17:
        b2 = data[10]
        b2 |= b
        data[10] = b2

    # Anwendung der Encode-Tabelle
    for i in range(len(data)):
        j = data[i] + (i + 1)
        if j > 255:
            j -= 256
        encrypted_card[i] = c_aEncode[j]

    return encrypted_card.hex()

def main():
    user_input = input("Bitte Hexwert zum Verschlüsseln eingeben (mit oder ohne Leerzeichen): ")
    clean_input = user_input.replace(" ", "").strip()

    if all(c in "0123456789abcdefABCDEF" for c in clean_input) and len(clean_input) % 2 == 0:
        try:
            encrypted = encrypt_card(clean_input)
            print(f"Verschlüsselte Daten: {encrypted}")
        except Exception as e:
            print(f"Fehler bei der Verschlüsselung: {e}")
    else:
        print("Ungültiger Hexwert. Bitte eine gerade Anzahl gültiger Hex-Zeichen eingeben.")

if __name__ == "__main__":
    main()