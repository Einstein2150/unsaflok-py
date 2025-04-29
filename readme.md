# Saflok Card Tools

This repository provides three Python tools for decoding, verifying, and encoding Saflok hotel key cards.

## Demo Video

Check out the demonstration on YouTube:

[![Watch the video](https://img.youtube.com/vi/gPPiMt1yU1s/maxresdefault.jpg)](https://www.youtube.com/watch?v=gPPiMt1yU1s)

## Tools Overview

### 1. `saflok-decode-in.py`

**Purpose:**
- Decrypts a Saflok card's encrypted block data

**Main Features:**
- Decryption of encrypted Saflok data.

### 2. `saflok-checksum.py`

**Purpose:**
- Calculates the checksum for a basic access block.
- Validates the integrity of the decrypted card data.

**Main Features:**
- Manual checksum verification.
- Simple script to confirm if the card data block is correctly structured.

### 3. `saflok-encode-in.py`

**Purpose:**
- Generates an encoded Saflok card block.
- Re-encrypts structured card data to create valid Saflok key cards.

**Main Features:**
- Input structured data with checksum
- Encode back to a correctly encrypted card block.

---

## Requirements
- Python 3.7+

No external libraries are required (uses only standard Python modules).

## Example Usage
```bash
# Decrypt a block
python3 saflok-decode-in.py 

# Checksum verification
python3 saflok-checksum.py 

# Encode a new block
python3 saflok-encode-in.py
```

---

## Notes
- These tools are for educational and research purposes only.
- They are based on reverse engineering work published by researchers including Lennert Wouters, Ian Carroll, and the open-source community.
- Saflok is a registered trademark of Dormakaba.


## License
This project is licensed under the MIT License.

