# This script will open a headless Chromium browser on a Rapberry Pi (running headless also) and play whatever is streaming from The Lot Radio (https://www.thelotradio.com/)
# Libraries required: chromium-chromedriver, python3-pip, selenium, 
#.                    pyvirtualdisplay, 
#.                    xvfb xserver-xephyr tigervnc-standalone-server xfonts-base (prefix for this last one is 'sudo apt-get install')


from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.thelotradio.com/')
driver.find_element_by_class_name("wf-section").click()

