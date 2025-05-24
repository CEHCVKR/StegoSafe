# StegoSafe

**StegoSafe** is a Python-based tool for secure image steganography using the Least Significant Bit (LSB) method. It ensures format-aware encoding by avoiding lossy image formats like JPEG that may corrupt hidden data.

---

## 🔐 Features

- ✅ Encode secret text messages into images
- ✅ Decode hidden messages from stego-images
- ✅ Format-aware safety (PNG, BMP, TIFF recommended)
- ⚠️ Warns against lossy formats like JPEG
- 📷 Supports conversion to safe formats before embedding
- 🛑 Custom binary stop marker for accurate message extraction

---

## 🧠 How It Works

StegoSafe hides data in the least significant bit of each color channel (R, G, B) in the image pixels. A binary stop marker (`1111111111111110`) is used to detect the end of the secret message during decoding.

---

## 📦 Requirements

- Python 3.x
- Pillow
- NumPy

Install dependencies:

```bash
pip install pillow numpy
```

---

## 🚀 Usage

### Encode a Message

```bash
python main.py encode <image_path> "<secret_message>"
```

Example:

```bash
python main.py encode input.png "Hello, World!"
```

You'll be prompted to choose an output format:

```
1. PNG
2. BMP
3. TIFF
4. JPEG (Not recommended due to compression artifacts)
```

---

### Decode a Message

```bash
python main.py decode <stego_image_path>
```

Example:

```bash
python main.py decode output.bmp
```

---

## 🔄 Format Compatibility

| Input Format | Supported Output Formats         |
|--------------|----------------------------------|
| JPG          | PNG ✅, BMP ✅, TIFF ✅ *(after conversion)* |
| PNG          | PNG ✅, BMP ✅, TIFF ✅            |
| BMP          | BMP ✅, PNG ✅, TIFF ✅            |
| TIFF         | TIFF ✅, PNG ✅, BMP ✅            |

---

## ⚠️ Warnings

- ❌ Avoid encoding directly into `.jpg/.jpeg` – use PNG/BMP/TIFF instead.
- ✅ Always use **lossless formats** to ensure message integrity.

---

## 🛠️ Planned Features

- [ ] GUI version with drag-and-drop support
- [ ] File embedding (not just text)
- [ ] Password-protected encryption layer
- [ ] Image integrity check before decoding

---

## 📁 Project Structure

```
StegoSafe/
│
├── main.py           # Main script
├── input.png        # Input image
├── output.bmp       # Stego-image after encoding
├── README.md        # Project documentation
```

---

## 👤 Author

**CHINNAPAREDDY VENKATA KARTHIK REDDY**  
Cybersecurity Enthusiast | B.Tech in CSE (IoT & CS)  
GitHub: [@CEHCVKR](https://github.com/CEHCVKR)  
LinkedIn: [cvkr](https://www.linkedin.com/in/cvkr/)

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share with credit.

---

> StegoSafe: **Hide secrets smartly. Extract securely.**
