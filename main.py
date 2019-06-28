import socket
import math, colorsys
from random import randint
from PIL import Image

HOST = ''
PORT = 1234
# PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send
sizex = 1000
sizey = 1000


def pixel(x, y, r, g, b, a=255):
    if a == 255:
        send('PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
    else:
        send('PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))


def getsize():
    send('size\n')
    info = sock.recv(80)
    a, sizex, sizey = info.replace("\n", "").split(" ")


def rect(x, y, w, h, r, g, b):
    for i in xrange(x, x + w):
        for j in xrange(y, y + h):
            pixel(i, j, r, g, b)


def printImg(file, n):
    im = Image.open(file).convert('RGB')
    im.thumbnail((400, 500), Image.ANTIALIAS)
    _, _, w, h = im.getbbox()
    while n:
        a = 900#randint(100, 500)

        for x in xrange(w):
            for y in xrange(h):
                r, g, b = im.getpixel((x, y))
                pixel(x + a, y + a, r, g, b)
    n -= 1


def worm2(x, y, n, s=15, sp=20, color=10):
    while n:
        # newcolor = hex2rgb('#00FF00')
        # newcolor = hex2rgb(hex2)
        newcolor = colorsys.hsv_to_rgb(color, 1, 1)
        # print newcolor[0] * 255
        # print newcolor[1]*255
        # print newcolor[2]*255
        rect(x, y, s, s, newcolor[0] * 255, newcolor[1] * 255, newcolor[2] * 255)

        r = randint(1, 4)
        if r == 1:
            x += sp
        if r == 2:
            y += sp
        if r == 3:
            x -= sp
        if r == 4:
            y -= sp

        if x < 0 or x > sizex:
            x = 50
        if y < 0 or y > sizey:
            y = 50
        n -= 1


# getsize()
color = 0.01

while True:
    # worm(500,500,1000000,random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #if color > 1:
    #    color = 0.01
    #color += 0.01
    #worm2(0, 0, 1000, 18, 20, color)
 printImg('c3re.png', 10)
