#This script opens a headless browser and plays the stream from Worldwide FM (now defunct) and The Lot Radio
#User to input the url of the website and the button as arguments for the runradio function
#Note: It might require a locally ccessible chromedriver library to work

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import numpy as np

#open browser
chrome_options = Options()
chrome_options.add_argument("--headless") #turn on to go back to headless
    # chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)


#pass the url of the radio station and the name of the button to start the radio in a headless browser
def runradio(starturl, buttonname):
    #chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    #chrome_options.add_argument("--headless") #turn on to go back to headless
    # chrome_options.headless = True # also works
    #driver = webdriver.Chrome(options=chrome_options)
    #start_url = "https://worldwidefm.net/"
    driver.get(starturl)
    driver.find_element_by_class_name(buttonname).click()
    sleep(10)
    #driver.close()

#check if function works    
runradio("https://www.thelotradio.com/", 'wf-section')
print("hello")
runradio("https://worldwidefm.net/", 'col-xs-2.col-sm-1')
driver.close()
stations = np.array([['https://www.thelotradio.com/','https://worldwidefm.net/'],['wf-section','col-xs-2.col-sm-1']])

#check if runradio works with the station array
#print(stations)
#print(stations[0,0])
#print(stations[1,0])
#runradio(stations[0,0], stations[1,0])
#runradio(stations[0,1], stations[1,1])


#check how many stations
shapearray = stations.shape

#print all stations
for i in range(shapearray[1]):
  print(stations[0,i], stations[1,i])

#runradio(stations[0,0], stations[1,0])
#runradio(stations[0,1], stations[1,1])
