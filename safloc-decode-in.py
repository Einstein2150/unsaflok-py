#based on https://gitee.com/wangshuoyue/unsaflok
#modified and Python3-Port by Einstein2150

import binascii

# Lookup-Tabellen aus dem C-Code
c_aDecode = [
    234, 13, 217, 116, 78, 40, 253, 186, 123, 152, 135, 120, 221, 141, 181, 26, 14, 48, 243, 47,
    106, 59, 172, 9, 185, 32, 110, 91, 43, 182, 33, 170, 23, 68, 90, 84, 87, 190, 10, 82,
    103, 201, 80, 53, 245, 65, 160, 148, 96, 254, 36, 162, 54, 239, 30, 107, 247, 156, 105, 218,
    155, 111, 173, 216, 251, 151, 98, 95, 31, 56, 194, 215, 113, 49, 240, 19, 238, 15, 163, 167,
    28, 213, 17, 76, 69, 44, 4, 219, 166, 46, 248, 100, 154, 184, 83, 102, 220, 122, 93, 3,
    7, 128, 55, 255, 252, 6, 188, 38, 192, 149, 74, 241, 81, 45, 34, 24, 1, 121, 94, 118,
    29, 127, 20, 227, 158, 138, 187, 52, 191, 244, 171, 72, 99, 85, 62, 86, 140, 209, 18, 237,
    195, 73, 142, 146, 157, 202, 177, 229, 206, 77, 63, 250, 115, 5, 224, 75, 147, 178, 203, 8,
    225, 150, 25, 61, 131, 57, 117, 236, 214, 60, 208, 112, 129, 22, 41, 21, 108, 199, 231, 226,
    246, 183, 232, 37, 109, 58, 230, 200, 153, 70, 176, 133, 2, 97, 27, 139, 179, 159, 11, 42,
    168, 119, 16, 193, 136, 204, 164, 222, 67, 88, 35, 180, 161, 165, 92, 174, 169, 126, 66, 64,
    144, 210, 233, 132, 207, 228, 235, 71, 79, 130, 212, 197, 143, 205, 211, 134, 0, 89, 223, 242,
    12, 124, 198, 189, 249, 125, 196, 145, 39, 137, 50, 114, 51, 101, 104, 175
]

def decrypt_card(hex_string):
    data = bytearray(binascii.unhexlify(hex_string))
    decrypted_card = bytearray(len(data))

    # Schritt 1: Byte-Werte aus der Lookup-Tabelle decodieren
    for i in range(len(data)):
        num = c_aDecode[data[i]] - (i + 1)
        if num < 0:
            num += 256
        decrypted_card[i] = num

    # Bit-Manipulation für zusätzliche Entschlüsselungsschritte
    b = 0
    b2 = 0

    if len(decrypted_card) == 17:
        b = decrypted_card[10]
        b2 = b & 1

    for num2 in range(len(decrypted_card), 0, -1):
        b = decrypted_card[num2 - 1]
        for num3 in range(8, 0, -1):
            num4 = num2 + num3
            if num4 > len(decrypted_card):
                num4 -= len(decrypted_card)
            b3 = decrypted_card[num4 - 1]
            b4 = (b3 & 0x80) >> 7
            b3 = ((b3 << 1) & 0xFF) | b2
            b2 = (b & 0x80) >> 7
            b = ((b << 1) & 0xFF) | b4
            decrypted_card[num4 - 1] = b3
        decrypted_card[num2 - 1] = b

    return decrypted_card.hex()


def main():
    user_input = input("Bitte Hexwert eingeben (mit oder ohne Leerzeichen): ")
    clean_input = user_input.replace(" ", "").strip()

    if all(c in "0123456789abcdefABCDEF" for c in clean_input) and len(clean_input) % 2 == 0:
        try:
            result = decrypt_card(clean_input)
            print(f"Entschlüsselte Daten: {result}")
        except Exception as e:
            print(f"Fehler beim Entschlüsseln: {e}")
    else:
        print("Ungültiger Hexwert. Bitte eine gerade Anzahl gültiger Hex-Zeichen eingeben.")

if __name__ == "__main__":
    main()