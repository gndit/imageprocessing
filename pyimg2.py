from PIL import Image


def main():
    try:
        img = Image.open("/root/Downloads/girl.jpg")
        img2 = Image.open("/root/Downloads/horse.jpg")
        img.paste(img2, (50, 50))
        img.save("/root/Downloads/new_girl.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()