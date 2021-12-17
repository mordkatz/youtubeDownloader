#importing the module 
from pytube import YouTube 

#where to save 
SAVE_PATH = "C:/Users/mordy/Desktop" #to_d

#link of the video to be downloaded 
link = input("Enter full YouTube link: ")


try: 
	#object creation using YouTube which was imported in the beginning 
	yt = YouTube(link) 
except: 
	print("Connection Error") #to handle exception 

#get the video with the extension and resolution passed in the get() function 
ys = yt.streams.get_highest_resolution()
try: 
	#downloading the video 
	ys.download(SAVE_PATH) 
except: 
	print("Some Error!") 
print('Task Completed!') 
