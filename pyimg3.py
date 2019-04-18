from PIL import Image
def main():
    try:
        img=Image.open("/root/Downloads/monkey.jpg")
        print img.histogram()
        #nw.save("/root/Downloads/n_moky.jpg")

    except IOError:
        pass
if __name__ == "__main__":
    main()
