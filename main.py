import selenium
from selenium import webdriver
import os
import sys
import time
import random
import classes

with open('songs.txt', 'r') as reader:

	songslist = reader.readlines()

for choice in songslist:
	
	app = classes.MainApp()
	link_songs = app.youtube(choice)
	app.downloadproces(link_songs)
	time.sleep(10)
	app.driver.close()

print('I have finished downloading your songs')
