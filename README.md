
# Paytm Movie Notifier  
  
This script is used for getting notified via sound whenever online ticket booking starts on **paytm.com**  
Script is pretty simple to use. Just edit the `params.ini` file and mention your desired *city*, *movie*, *date*, *theatre*, etc.

*Requirements:*  
 - [python 3.x](https://www.python.org/downloads/release/python-368/)  
 - [requests](https://2.python-requests.org/en/master/) (`pip install requests`)  
 - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (`pip install bs4`)  


I have updated the script to work based on Paytm's 2022-03-22 code. This code should work for some time. Only break point for this code is the class name of theatre div in paytm. which is '_1dNVz' right now. If you are a developer and incase code is not working, please update this and try again. 
 
