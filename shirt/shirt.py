import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        try:
            if (
                sys.argv[1].split(".")[1] == "jpg"
                and sys.argv[2].split(".")[1] == "png"
            ):
                head_image = sys.argv[1] # input
                new_image = sys.argv[2] # output
                edit(head_image, new_image)
            else:
                sys.exit("Invalid input")
        except FileNotFoundError:
            sys.exit("Invalid  input")
    else:
        (
            sys.exit("Too few command-line arguments")
            if len(sys.argv) < 3
            else sys.exit("Too many command-line arguments")
        )

def edit(back_ground, new_image_name):
    back_img  = Image.open(back_ground)
    back_img = ImageOps.fit(back_img, back_img.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    cs50_shirt = Image.open("shirt.png")
    back_img.paste(cs50_shirt, (45, 56))
    back_img.save(new_image_name)

if __name__ == "__main__":
    main()
