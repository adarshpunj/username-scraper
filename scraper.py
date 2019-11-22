#!/usr/bin/python3

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import settings
import random
import json
import time
import sys
import os

"""
This is a Selenium version
of Instagram username-scraper

A settings.py is required to
run this file

Example:
scraper = InstagramUsernameScraper()
scraper.configureDriver('incognito','headless')
scraper.login(username='jondoe', passowrd='jon@123')
scraper.scrapeBy_shortcode(duration=10)
"""

class InstagramUsernameScraper():
	def __init__(self):
		self.target_username = sys.argv[1]

	def configureDriver(self, *args
		, window_size='300,800', download_directory=None):

		"""
		Configures selenium webdriver

		Parameters:
		*args (string) : these arguments are added as
				 chrome options arguments

		window_size (string) : size of chromium window
		download_directory : Files will be downloaded to this
				     directory
		"""

		# Setting download location
		if download_directory==None:
			download_directory = os.getcwd()+'/{}'.format(self.target_username)

		options = Options()
		prefs = {'download.default_directory':download_directory}

		# Adding chrome options
		for arg in args:
			try:
				options.add_argument('--{}'.format(arg))
			except Exception as e:
				print(e)
				pass

		options.add_argument(
			'--user-agent={}'.format(settings.USER_AGENT))

		options.add_argument(
			'--window-size={}'.format(window_size))

		options.add_experimental_option('prefs'
			,prefs)

		self.driver = webdriver.Chrome(settings.CHROMEDRIVER_PATH
			,chrome_options=options)

	def login(self, username=settings.USERNAME
		, password=settings.PASSWORD):

		"""
		Logs into Instagram

		Parameters:
		username (string)
		password (string)
		(Default value of args is stored in settings.py)
		"""


		self.driver.get(settings.INSTAGRAM_LOGIN_URL)
		# Login credentials text field		
		creds = self.driver.find_elements_by_css_selector("._2hvTZ.pexuQ.zyHYP")
		creds[0].send_keys(username)
		creds[1].send_keys(password)

		# Click 'Login' button
		btn_Login = self.driver.find_elements_by_css_selector(
			".sqdOP.L3NKy.y3zKF")[1]
		btn_Login.click()

		print("LOGGED INTO INSTAGRAM")
		time.sleep(5)

	def scrapeBy_shortcode(self, shortcode, duration=60):
		"""
		Downloads a CSV file loaded
		with Instagram usernames which
		have liked a post

		Parameters:
		shortcode (string) : Photo ID
		duration (int)     : Seconds for which liked_by
				     box is to be scrolled
	    	"""

		self.driver.get(settings.INSTAGRAM_PHOTO_URL.format(shortcode))
		# This script will open mobile version 
		# of /liked_by webpage
		self.driver.execute_script(
				settings.SCRIPT_LIKED_BY_PAGE)

		# Scrolling down the list
		init_time = time.time()
		while time.time()-init_time<duration:
			try:
				ActionChains(self.driver).send_keys(Keys.DOWN).perform()
			except:
				print(settings.ERROR_SCROLL)
				print(e)

		# This script downloads CSV file
		try:
			self.driver.execute_script(
				settings.SCRIPT_CSV_DOWNLOADER.format(shortcode))
		except Exception as e:
			print(settings.ERROR_DOWNLOADING_CSV)
			print(e)

		time.sleep(5)

		self.driver.quit()

	def scrapeBy_RecentMedia(self, duration=60):
		"""
		Downloads 12 CSV
		
		Calls scrapeBy_shortcode function on latest
		Instagram posts by the target account
		"""

		#Get Instagram account details in JSON format
		try:
			response = json.loads(
				requests.get(INSTAGRAM_PROFILE_URL.format(
					'edsheeran'), headers=HEADERS
					).text)

			recent_media = response['graphql']['user']['edge_owner_to_timeline_media']['edges']

		except Exception as e:
			print(settings.ERROR_RESPONSE)
			print(e)
			return

		for post in recent_media:
			shortcode = post['node']['shortcode']
			time.sleep(randint(3,7))
			scrapeBy_shortcode(shortcode)
