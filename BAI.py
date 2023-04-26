#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
#import pickle
import speech_recognition as sr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import clipboard
import os
from selenium import webdriver
options = Options()

#options.headless = True
# Start a Selenium driver 
driver_path='/usr/local/bin/chromedriver'

from gtts import gTTS
import os
#import sys
#import re
#import importlib
#reload(sys)
#sys.setdefaultencoding('utf8')

#open_file = open("sjp.pkl", "rb")
#lista = pickle.load(open_file)
#open_file.close()
#def redukcja(x):
#  return list(dict.fromkeys(x))

#def rhyme(word):
#    wynik = []
#    if len(word) >= 7:
#       for x in lista:
#           if word[-5:] in x[-5:]:
#              wynik.append(x)
#    elif len(word) <=6:
#       for x in lista:
#           if word[-4:] in x[-4:]:
#              wynik.append(x)
#    final = redukcja(wynik)
#    print("Dostępne rymy do "+word+": "+str(final))
driver = webdriver.Chrome(driver_path, options=options)
time.sleep(2)
driver.get("https://chatbot.theb.ai/")
driver.get("https://fastgpt.app/")

time.sleep(2)
driver.delete_all_cookies()


def pentacostal(macaria):
   tts = gTTS(macaria, lang='en')
   tts.save("thus_spoke_ahriman.mp3")
   os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")


def septuaginta(macaria):
    milton = open(macaria,'r')
    satan = milton.readlines()
    pure_satan = re.sub(r"('|\\n|;)","", satan)
    tts = gTTS(pure_satan, lang='en')
    tts.save("thus_spoke_ahriman.mp3")
    os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")


def pentacostal_pl(macaria):
  tts = gTTS(macaria, lang='pl')
  tts.save("thus_spoke_ahriman.mp3")
  os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")

def polak(macaria):
  tts = gTTS(macaria, lang='pl')
  tts.save("thus_spoke_polaczek.mp3")
  os.system("play thus_spoke_polaczek.mp3")



def septuaginta_pl(macaria):
    milton = open('macaria','r')
    satan = milton.readlines()
    pure_satan = re.sub(r"('|\\n|;)","", satan2)
    tts = gTTS(pure_satan, lang='pl')
    tts.save("thus_spoke_ahriman.mp3")
    os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")


def clear_chat():
 driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div/div/footer/div/div/div[1]/button").click()
 time.sleep(2)
 b = driver.find_elements(By.XPATH, "//button")
 b[-1].click()
 time.sleep(3)

def pytaj(a):
 driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div/div/div/div/footer/div/div/div[2]/div/div[1]/div[1]/textarea").send_keys(a+"\n")

def odp(): 
 a = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div").text
 print(a)
 return a
def odp1(): 
 a = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div").text
 return a

  






# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
         print("Co chcesz powiedzieć?")
         audio = r.listen(source)
# Speech recognition using Google Speech Recognition
         try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
             # print("Powiedziałeś: " + r.recognize_google(audio,language="pl-PL"))
             words = r.recognize_google(audio,language="pl-PL")
    #         rhyme(word)
             print(words)
             clear_chat()
             time.sleep(1)
             pytaj(words)
             time.sleep(1)
             time.sleep(30)
             lancuch = odp()
             pentacostal_pl(lancuch)
    #        print("You said: " + r.recognize_google(audio))
         except sr.UnknownValueError:
             print("Google Speech Recognition nie kmini tego co nawijasz")
         except sr.RequestError as e:
             print("Could not request results from Google Speech Recognition service; {0}".format(e))
