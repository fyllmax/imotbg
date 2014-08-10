#!/usr/bin/env python

import tkinter
from bs4 import BeautifulSoup
from urllib import request, error
from time import sleep
import os


def get_property_img():

    url = imot_url.get()

    pics_num = num_pics.get()

    f = request.urlopen(url)
    page = f.read()
    f.close()
    soup = BeautifulSoup(page)

    img_link = soup.findAll('img')[0]["src"]
    # print(img_link)

    cherta = img_link.rfind("/")

    imot_id = "{}".format(img_link[cherta:-5])

    for img in range(1, pics_num + 1):

        big_img_link = "{}big{}{}.pic".format(img_link[: cherta - 3], imot_id, img)

        # img_name = "img_{}.{}".format(img, img_format)
        img_name = "img_{}.jpg".format(img)

        try:

            url = request.urlopen(big_img_link)
            print("valid url")

            f = open(img_name, 'wb')
            f.write(url.read())
            f.close()

            sleep(1)

        except error.HTTPError as err:
            if err.code == 404:
                print("invalid url")

    return True


# clearing input fields
def clear_input():
    entry_box_link.delete(0, tkinter.END)
    # entry_box_num_imgs.delete(0, tkinter.END)


# deleting images in script folder
def delete_img():

    directory = os.getcwd()

    for item in os.listdir(directory):
        if item.endswith(".jpg"):
            os.remove(item)
            print("image deleted!!!")

    print("DONE :)")

if __name__ == '__main__':
    root = tkinter.Tk()

# window size
    root.geometry("400x300")

# app title
    root.title("imot.bg image downloader")

# variables
    imot_url = tkinter.StringVar()
    num_pics = tkinter.IntVar()

# input and buttons
    download_lbl = tkinter.Label(text="Enter property link").place(x=20, y=20)
    entry_box_link = tkinter.Entry(root, textvariable=imot_url)
    entry_box_link.place(x=200, y=20)

    number_lbl = tkinter.Label(text="Enter number of images").place(x=20, y=60)
    entry_box_num_imgs = tkinter.Entry(root, textvariable=num_pics)
    entry_box_num_imgs.place(x=200, y=60)

    execution_btn = tkinter.Button(root, text="download", command=get_property_img, bg="orange", fg="white")
    execution_btn.place(x=150, y=100)

    quit_btn = tkinter.Button(root, text="QUIT", command=root.quit, bg="black", fg="yellow")
    quit_btn.place(x=300, y=100)

    clear_btn = tkinter.Button(root, text="Clear", command=clear_input, bg="black", fg="yellow").place(x=20, y=100)

    delete_btn = tkinter.Button(root, text="Delete all images", command=delete_img, bg="red", fg="yellow", width=39).place(x=20, y=140)

    tkinter.mainloop()
