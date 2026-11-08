# 🎨 Image to ASCII Art Renderer

A lightweight Python script that converts any PNG image into vibrant, colored ASCII art directly in your terminal using true-color ANSI escape sequences.

---

## ✨ Features

- **True-Color Support:** Preserves the original RGB colors of your image using ANSI 24-bit true-color terminal codes.
- **Custom Resolution Scaling:** Automatically resizes input images to `120x70` pixels for optimal terminal display.
- **Simple & Dependency-Light:** Built entirely using Python's standard library and the popular `Pillow` (PIL) library.

---

## 🛠️ Prerequisites

Make sure you have Python installed along with the Pillow library. You can install Pillow via pip:

```bash
pip install Pillow
```

---

## 🚀 How to Use

1. Save your Python script (e.g., as `main.py`).
2. Run the script from your terminal:
   ```bash
   python main.py
   ```
3. When prompted, enter the file path to your target PNG image:
   ```text
   enter the path of the png image
   ::= path/to/your/image.png
   ```
4. Watch your terminal transform the image into colorful ASCII art!

---

## ⚙️ How It Works

- **Resizing:** The script loads the image, converts it to RGB mode, and scales it down to a grid of 120 columns by 70 rows.
- **Brightness Mapping:** It calculates the average brightness of each pixel and maps it to a character gradient (`:-=+*#%@`).
- **Color Rendering:** It extracts the individual `R`, `G`, and `B` values to apply matching terminal text colors (`\033[38;2;r;g;bm`) for every character printed.
