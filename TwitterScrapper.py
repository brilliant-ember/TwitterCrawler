from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

'''fills the "all of htses words" field in twitter advanced search
args can be any number of strings, uses an & operator so all of these must be present
'''
def sleep(x):
	time.sleep(x)
def keyWordSearch(*args):
	keyWords = driver.find_element_by_name('''ands''')
	for word in args:
		keyWords.send_keys(str(word))
		keyWords.send_keys(" ")

'''Must be a single word'''
def exactPhraseSearch(phrase):
	exactPhrase = driver.find_element_by_name('''phrase''')
	exactPhrase.send_keys(str(phrase))

def keyWordORSearch(*args):
	keyWords = driver.find_element_by_name('''ors''')
	for word in args:
		keyWords.send_keys(str(word))
		keyWords.send_keys(" ")

def excludeSearch(*args):
	keyWords = driver.find_element_by_name('''nots''')
	for word in args:
		keyWords.send_keys(" \' "+str(word)+ " \' ")
		keyWords.send_keys(" ")
def hastagSearch(*args):
	keyWords = driver.find_element_by_name('''tag''')
	for word in args:
		keyWords.send_keys(" \' "+str(word)+ " \' ")
		keyWords.send_keys(" ")

def locationSearch(place):
	keyWords = driver.find_element_by_name('''near''')
	keyWords.send_keys(str(place))





driver = webdriver.Chrome("D:\\Programs\\chromedriver.exe")
driver.get("https://twitter.com/search-advanced?lang=en&lang=en")
#assert ("instagram" in driver.title), "are u sure this is Instagram page?"
keyWordSearch("Rideau")
keyWordORSearch("stab", "stabbing","police")
locationSearch("Rideau Street")
driver.find_element_by_xpath('''//*[@id="page-container"]/div/div[1]/form/button''').click()
#for the photos
sleep(2)
elems = driver.find_elements_by_tag_name('a')
for e in range(len(elems)):
	if (elems[e].text == "Photos"):
		print("Found the photos nav thing")
		elems[e].click()
		break

sleep(2)
elems = driver.find_element_by_id("stream-items-id")
elems = elems.find_elements_by_tag_name("span")
for x in elems:
	try:
		x.click()
		sleep(2)
		driver.find_element_by_xpath('''/html/body/div[5]/div[2]/div[4]/div/div[2]/div[4]/div[2]/div[4]/div/button/div/span[1]''').click()
		sleep(2)
		r = driver.find_element_by_xpath('''/html/body/div[5]/div[2]/div[4]/div/div[2]/div[4]/div[2]/div[4]/div/div/ul/li[2]/button''').click()
		print(x.text)
		x.Select()
		driver.find_element_by_link_text('''Embed Tweet''').click()
	except:
		print("E")




#exactPhraseSearch(" ")


#logIn.send_keys(Keys.RETURN)
time.sleep(3)
#driver.close()

