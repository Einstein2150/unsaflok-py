#based on https://gitee.com/wangshuoyue/unsaflok
#modified and Python3-Port by Einstein2150

import binascii

def calculate_checksum(hex_string):
    data = bytearray(binascii.unhexlify(hex_string))

    # Checksumme berechnen (Summe aller Bytes modulo 256, dann invertieren)
    checksum = (255 - (sum(data) & 0xFF)) & 0xFF

    # Die Checksumme als letztes Byte hinzufügen
    data.append(checksum)

    return data.hex(), checksum

def main():
    user_input = input("Bitte Hexwert für Checksumme eingeben (mit oder ohne Leerzeichen): ")
    clean_input = user_input.replace(" ", "").strip()

    if all(c in "0123456789abcdefABCDEF" for c in clean_input) and len(clean_input) % 2 == 0:
        try:
            checksum_hex, checksum_value = calculate_checksum(clean_input)
            print(f"Checksumme: {checksum_value:02X}")
            print(f"Daten mit Checksumme: {checksum_hex}")
        except Exception as e:
            print(f"Fehler bei der Berechnung: {e}")
    else:
        print("Ungültiger Hexwert. Bitte eine gerade Anzahl gültiger Hex-Zeichen eingeben.")

if __name__ == "__main__":
    main()