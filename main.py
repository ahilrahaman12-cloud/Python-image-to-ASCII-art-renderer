from PIL import Image

path = input("enter the path of the png image\n::=")
photo = Image.open(path).convert("RGB").resize((120, 70))

for v in range(70):
    for x in range(120):
        r, g, b = photo.getpixel((x, v))  # Now safely unpacks 3 values
        
        i = (r + g + b) * 8 // 768
        color = f"\033[38;2;{r};{g};{b}m"
        print(color + ":-=+*#%@"[i], end="")
        
    print("\033[0m")