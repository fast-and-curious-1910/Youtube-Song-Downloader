import selenium
from selenium import webdriver
import os
import sys
import time
import random
import classes





class MainApp:

	def __init__(self):

		self.driver = webdriver.Chrome()

	def searcher(self,site):

		self.driver.get(site)

	def youtube(self, song):

		self.driver.get(f'https://www.youtube.com/results?search_query={song}')
		time.sleep(2)
		thumbnail = self.driver.find_element_by_id('thumbnail')
		link = thumbnail.get_attribute('href')
		
		return link

	def downloadproces(self, muzieklink):

		try:
			self.driver.get('https://ytmp3.cc/en13/')
			time.sleep(2)
			inputbox = self.driver.find_element_by_id('input')
			inputbox.send_keys(str(muzieklink))
			print('gelukt')
			button = self.driver.find_element_by_id('submit')
			button.click()
			time.sleep(6)
			dloadbut = self.driver.find_element_by_xpath("//*[contains(text(), 'Download')]")
			dloadbut.click()
			
		except Exception as e:

			print(e)
			pass








