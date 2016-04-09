########################################################################
#                                                                                                                
#     ,ad8888ba,                                                                                                      
#    d8"'    `"8b                                                                                                     
#   d8'                                                                                                               
#   88             ,adPPYYba,  ,adPPYYba,  8b,dPPYba,   ,adPPYYba,        ,adPPYba,   ,adPPYba,   88,dPYba,,adPYba,   
#   88      88888  ""     `Y8  ""     `Y8  88P'   `"8a  ""     `Y8       a8"     ""  a8"     "8a  88P'   "88"    "8a  
#   Y8,        88  ,adPPPPP88  ,adPPPPP88  88       88  ,adPPPPP88       8b          8b       d8  88      88      88  
#    Y8a.    .a88  88,    ,88  88,    ,88  88       88  88,    ,88  888  "8a,   ,aa  "8a,   ,a8"  88      88      88  
#     `"Y88888P"   `"8bbdP"Y8  `"8bbdP"Y8  88       88  `"8bbdP"Y8  888   `"Ybbd8"'   `"YbbdP"'   88      88      88  
#                                                                                                                  
#                                                                                                                  
#                                                                                                                  
#                88                           88  88                                                                  
#                88                           88  ""               ,d                                                 
#                88                           88                   88                                                 
#   8b,dPPYba,   88  ,adPPYYba,  8b       d8  88  88  ,adPPYba,  MM88MMM                                              
#   88P'    "8a  88  ""     `Y8  `8b     d8'  88  88  I8[    ""    88                                                 
#   88       d8  88  ,adPPPPP88   `8b   d8'   88  88   `"Y8ba,     88                                                 
#   88b,   ,a8"  88  88,    ,88    `8b,d8'    88  88  aa    ]8I    88,                                                
#   88`YbbdP"'   88  `"8bbdP"Y8      Y88'     88  88  `"YbbdP"'    "Y888                                              
#   88                               d8'                                                                              
#   88                              d8'                                                                               
#                                                                                                                  
#            88                                                88                                    88               
#            88                                                88                                    88               
#            88                                                88                                    88               
#    ,adPPYb,88   ,adPPYba,   8b      db      d8  8b,dPPYba,   88   ,adPPYba,   ,adPPYYba,   ,adPPYb,88               
#   a8"    `Y88  a8"     "8a  `8b    d88b    d8'  88P'   `"8a  88  a8"     "8a  ""     `Y8  a8"    `Y88               
#   8b       88  8b       d8   `8b  d8'`8b  d8'   88       88  88  8b       d8  ,adPPPPP88  8b       88               
#   "8a,   ,d88  "8a,   ,a8"    `8bd8'  `8bd8'    88       88  88  "8a,   ,a8"  88,    ,88  "8a,   ,d88               
#    `"8bbdP"Y8   `"YbbdP"'       YP      YP      88       88  88   `"YbbdP"'   `"8bbdP"Y8   `"8bbdP"Y8
#
########################################################################

########################################################################
#Headers
########################################################################
from selenium import webdriver
import time

########################################################################
#Initialise
########################################################################
chromeOptions = webdriver.ChromeOptions()
pref = {"download.default_directory" : "C:\\CarMusic"}                                                                            #Change default download folder
chromeOptions.add_experimental_option("prefs",pref)
browser=webdriver.Chrome(executable_path="C:\\chromedriver.exe",chrome_options=chromeOptions)
browser.get("http://gaana.com/playlist/neemabhasi-bxxha-carmusic")                                                                #Link to playlist

########################################################################
#Generates a list of all the songs in provided Gaana playlist.
########################################################################
def get():
    song_elem=browser.find_elements_by_class_name("playlisttrack")
    song_list=[]
    for x in range(0,len(song_elem)):
        song_list.append(song_elem[x].text.split("\n")[0])
    song_list.pop(0)
    return song_list

########################################################################
#Finds the corresponding music video and downloads it as mp3.
########################################################################
def download(s):
    link="https://www.youtube.com/results?search_query="+s
    browser.get(link)
    browser.execute_script("document.cookie=\"VISITOR_INFO1_LIVE=oKckVSqvaGw; path=/; domain=.youtube.com\";window.location.reload();")  #Disable ads
    browser.find_elements_by_class_name("yt-ui-ellipsis")[0].click()
    be=browser.current_url
    browser.get("https://www.youtube2mp3.cc/")
    t=browser.find_element_by_id("input")
    t.send_keys(be)
    browser.find_element_by_id("button").click()
    time.sleep(5)                                                                                                                 #Wait for dynamically generated download button to load
    browser.execute_script("document.getElementById(\"download\").click()")
    print(s+" downloaded!")

########################################################################
#Function calls
########################################################################
songs=get()
for x in range(0,len(songs)):
    download(songs[x])


