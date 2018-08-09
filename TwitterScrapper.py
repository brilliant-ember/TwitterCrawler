from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def keyWordSeach(*args):
	keyWords = driver.find_element_by_name('''ands''')
	for word in args:
		keyWords.send_keys(word)
		keyWords.send_keys(" ")

def exactPhraseSearch(phrase):
	exactPhrase = driver.find_element_by_name('''phrase''')
	exactPhrase.send_keys(phrase)

driver = webdriver.Chrome("D:\\Programs\\chromedriver.exe")
driver.get("https://twitter.com/search-advanced?lang=en&lang=en")
#assert ("instagram" in driver.title), "are u sure this is Instagram page?"
keyWordSeach("Rideau", "police")
exactPhraseSearch("stab")


#logIn.send_keys(Keys.RETURN)

#driver.close()

'''fills the "all of htses words" field in twitter advanced search
args can be any number of strings'''
