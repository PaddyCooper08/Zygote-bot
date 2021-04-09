import nasapy
import os
from datetime import datetime
import urllib.request
from dotenv import load_dotenv


load_dotenv()
k = os.getenv('NASA_TOKEN')
nasa = nasapy.Nasa(key = k)

#Get today's date in YYYY-MM-DD format:

d = datetime.today().strftime('%Y-%m-%d')


#Get the image data:

apod = nasa.picture_of_the_day(date=d, hd=True)
#POINT A:
#Check the media type available:
if(apod["media_type"] == "image"):
    
    #POINT B:
    #Displaying hd images only:
    if("hdurl" in apod.keys()):
        
        #POINT C:
        #Saving name for image:
        title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"
        
        #POINT D:
        #Path of the directory:
        image_dir = "./Astro_Images"

        #Checking if the directory already exists?
        dir_res = os.path.exists(image_dir)
 
        #If it doesn't exist then make a new directory:
        if (dir_res==False):
            os.makedirs(image_dir)

        #If it exist then print a statement:
        else:
            print("Directory already exists!\n")
        
        #POINT E:
        #Retrieving the image:
        urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))
        
        #POINT F:
        #Displaying information related to image:
        
        if("date" in apod.keys()):
            print("Date image released: ",apod["date"])
            print("\n")
        if("copyright" in apod.keys()):
            print("This image is owned by: ",apod["copyright"])
            print("\n")
        if("title" in apod.keys()):
            print("Title of the image: ",apod["title"])
            print("\n")
        if("explanation" in apod.keys()):
            print("Description for the image: ",apod["explanation"])
            print("\n")
        if("hdurl" in apod.keys()):
            print("URL for this image: ",apod["hdurl"])
            print("\n")
        
        #POINT G:
        #Displaying main image:
       
        #Point H:
        #Text to Speech Conversion:
        #Take input from user:
        print("\n")
        choice = input("Press * to hear the audio explanation : ")

    

#POINT I:
#If media type is not image:
else:
    print("Sorry, Image not available!")
