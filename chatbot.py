import time
import webbrowser
import csv



my_dict = {}

##good_expressions = ["gnarly" , "good" , "great" , "spectacular" , "amazing" , "exited"]
with open('nice_words.csv', 'r') as f:
  reader = csv.reader(f)
  good_expressions  = list(reader)

import re
list = good_expressions
good_expressions = re.sub('[\[\]]','',repr(list))



var1 = input(" hello, what is your name?: ")
my_dict['name'] = var1
time.sleep(1)
print (f"im glad to meet you {var1.title()}")
##print (f"im glad to meet you"+my_dict['name'])

var0 = input("how is your day " + my_dict['name'] + " : ")

if var0 in good_expressions:
     print(f"Im happy that you are having a {var0.title()} day ")
else:
     print("ohh thats bad :(")

var2 = input (" what is your favorite movie?: ")
my_dict['movie'] = var2
time.sleep(1)
print (f"oh i also like {var2. title()}")
time.sleep(1)

var3 = int(input ("oh i forgot to ask you, what is your age?: "))
my_dict['age'] = var3
time.sleep(1)
if var3 >= 50:
    print("you are older than me")
else: 
    print("you are younger than me")

time.sleep(1)

var4 = input (" where do you live?: ")
my_dict['address'] = var4
time.sleep(1)
print (f"i live in tampere ")
time.sleep(1)

var5 = input ("what sport do you play?: ")
my_dict['sport'] = var5
time.sleep(1)
print (f"ok")
time.sleep(1)

##summarise the users info
print (f"Ok so your name is " + my_dict['name'] 
+ " and your age is "  + str(my_dict['age']) + " and your address is " + my_dict['address'] +
" and your favorite movie is " + my_dict['movie'] + " and you play " + my_dict['sport'] + ".thats all :P")



var6 = input ("Do you want to see my girlfriend?: ")
time.sleep(1)
##print (f"is it this one?")
agree = ["yes" , "yep" , "yeah"]
if  var6 in agree:



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



var7 = input("You want me to draw something for you?: ")


if  var7 == "yes":

     print (f"ok i'll draw something, wait for me to finish!")
##draw
     from turtle import *
     color('red', 'yellow')
     begin_fill()
     while True:
         forward(290)
         left(170)
         right(80)
         if abs(pos()) < 1:
             break
     end_fill()
     done()

else:
    print("ok")


healthy = ["chicken"
          , "brocolli"
          , "beef"
          , "spinach" 
          , "almonds" 
          , "brazil nut" 
          , "lentils" 
          , "black beans" 
          , "walnuts" 
          , "beets"
          , "avocado" 
          , "dark chocolate" 
          , "raberries" 
          , "garlic" 
          , "lemons" 
          , "Qunia" 
          , "eggs" 
          , "fish"
          , "pumpkin seeeds" 
          , "chia seeds" 
          , "milk" 
          , "greek yogurt"
          , "apples" 
          , "avocadoes" 
          , "bananas" 
          , "berries" 
          , "lemons" 
          , "tomatoes" 
          , "cauliflower" 
          , "lettuce" 
          , "mushrooms" 
          , "oninons" 
          , "peppers" 
          , "spaghetti" 
          , "mint" 
          , "coffee" 
          , "green tea" 
          , "water"]

var8 = input("whats you favorite food or drink: ")
my_dict['food'] = var8
if var8 in healthy:        
      print(f"your gonna be healthy :)")
else:
      print(f"eat more healthy food!")              

var9 = int(input("how many friends do you have?: "))
if var9 >= 15:
    print("you have a lot of friends")
else: 
    print("ok")

var10 = input("do you play minecraft: ")
if var10 == ("yes"):
    
    from PIL import Image
    import urllib.request 

    URL = 'https://lh3.googleusercontent.com/yAtZnNL-9Eb5VYSsCaOC7KAsOVIJcY8mpKa0MoF-0HCL6b0OrFcBizURHywpuip-D6Y'
    with urllib.request.urlopen(URL) as url:
        with open('download.jpg' , 'wb') as f:
            f.write(url.read())

    img = Image.open('download.jpg')

    img.show()
else:
    print(f"ok")

  
var11 = input("do you still wanna talk with me?: ")
if var11 == "no":
    print(f"ok, that´s fine")
    exit()
else:
    print(f"ok, here´s my next question.")
   
var12 = input("do you want me to show you a video?: ")
if var12 == "yes":
    webbrowser.open('https://www.youtube.com/watch?v=V5ywC6nsWis&t=32s')
    
else:
    print(f"ok")
    


var14 = ("do you skate board?: ")
if var14 == ("yes"):
   print(f"ok you'll like this game:)")
   time.sleep(3)
   webbrowser.open('http://www.agame.com/game/stunt-skateboard-3d')
else:
    print(f"ok then.")

var15 = input("well i'll see you later: ")

var16 = input("do you want to talk to me -ralph the creator: ")
if var16 == ("no"):
    exit()
else:
    print(f"yay x) -ralph the creator")

var17 = input("So you name is " + my_dict['name'] + " right?- ralph the creator: ")
if var17 == "yes":
    print(f"ok")
else:
    print(f"of course thats your name!")
time.sleep(2.5)
var18 = input("and your favorite food is " + my_dict['food'] + " right?- ralph the creator: ")
if var18 == "yes":
    print(f"ok")
else:
    print(f"of course its your favorite food!")

var19 = input("and your favorite sport is " + my_dict['sport'] + " right?- ralph the creator: ")
if var19 == "yes":
    print(f"ok")
else:
    print(f"of course its your favorite sport!")

var20 = input("and finally , your address is " + my_dict['address'] + " right?- ralph the creator: ")
if var20 == "yes":
    print(f"ok")
else:
    print(f"of course its your favorite address!: ")

var21 = input("so" + my_dict['name'] + " how is your day? - ralph the creator: ")
if var21 in good_expressions:
     print(f" {var21.title()} day ")
else:
     print("ohh :(")

var22 = input("lets play some minecraft , no?: ")
if var22 == "yes":
    webbrowser.open('https://www.minecraft.net/fi-fi/')
else:
    print(f"ok , thats fine")

var23 = input("ok so lets play wolf simulator :)")
if var23 == "yes":

    webbrowser.open('https://www.crazygames.com/game/wolf-simulator-wild-animals-3d')
else:
    print(f"ok then")