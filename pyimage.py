from PIL import Image as img
def main():
    try:
        immg=img.open("/root/Downloads/horse.jpg")
        immg=immg.rotate(180)
        immg.save("/root/Downloads/rotate_horse.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()