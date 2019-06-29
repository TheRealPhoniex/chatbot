


# importing time module
import time


var1 = input(" hello, what is your nickname?: ")
time.sleep(1)
print (f"im glad to meet you {var1.title()}")

var2 = input (" what is your favorite movie?: ")
time.sleep(1)
print (f"oh i also like {var2. title()}")
time.sleep(1)

var3 = int(input ("oh i forgot to ask you, what is your age?: "))
time.sleep(1)
if var3 >= 50:
    print("you are older than me")
else: 
    print("you are younger than me")

time.sleep(1)

var4 = input (" where do you live?: ")
time.sleep(1)
print (f"i live in tampere ")
time.sleep(1)

var5 = input ("do you play football?: ")
time.sleep(1)
print (f"ok")
time.sleep(1)

var6 = input ("Do you want to see my girlfriend?: ")
time.sleep(1)
##print (f"is it this one?")

if  var6 == "yes":

##show pic from internet

    from PIL import Image
    import urllib.request

    URL = 'https://assets.capitalfm.com/2018/23/lilliya-scarlett-instagram-1528814125-custom-0.png'

    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())

    img = Image.open('temp.jpg')

    img.show()

else:
    print("ok")



var13 = input("You want me to draw something for you?: ")


if  var13 == "yes":

     print (f"ok i'll draw something, wait for me to finish!")

##draw
     from turtle import *
     color('red', 'yellow')
     begin_fill()
     while True:
         forward(200)
         left(170)
         if abs(pos()) < 1:
             break
     end_fill()
     done()

else:
    print("ok")