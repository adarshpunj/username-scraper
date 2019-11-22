USER_AGENT  = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935T Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 Instagram 8.4.0 Android (23/6.0.1; 560dpi; 1440x2560; samsung; SM-G935T; hero2qltetmo; qcom; en_US"
SCRIPT_CSV_DOWNLOADER = '''usernames = document.getElementsByClassName("_7UhW9   xLCgt      MMzan  KV-D4            fDxYl     ");var data = "";for(i=0;i<usernames.length;i++){{data = data+usernames[i].textContent+'\\n'}};var file = new Blob([data], {{'text/plain': 'text/plain'}});var url=document.createElement('a');url.href=window.URL.createObjectURL(file);url.download="{}.csv";url.click();'''
SCRIPT_LIKED_BY_PAGE = 'document.getElementsByClassName("zV_Nj")[0].click();'

HEADERS = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
'cache-control': 'no-cache',
'dnt': '1',
'pragma': 'no-cache',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36'
}

#SET PATH TO CHROMEDRIVER
CHROMEDRIVER_PATH = "/path/to/chromedriver"

#INSTAGRAM LOGIN ID & PASSWORD
USERNAME = "username"
PASSWORD = "password"

INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login"
INSTAGRAM_PHOTO_URL = "https://www.instagram.com/p/{}/"
INSTAGRAM_PROFILE = "https://www.instagram.com/{}/?__a=1"
ERROR_SCROLL = "AN ERROR OCCURED WHEN SCORLLING THE LIKED_BY PAGE\n-------------------------------"
ERROR_DOWLOADING_CSV = "AN ERROR WHILE SAVING THE DATA AS CSV\n-------------------------------"
ERROR_RESPONSE = "AN ERROR WHILE GETTING TARGET_USERNAME ACCOUNT DATA\n-------------------------------"
