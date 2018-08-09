from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''fills the "all of htses words" field in twitter advanced search
args can be any number of strings, uses an & operator so all of these must be present
'''
def keyWordSearch(*args):
	keyWords = driver.find_element_by_name('''ands''')
	for word in args:
		keyWords.send_keys(" \' "+str(word)+ " \' ")
		keyWords.send_keys(" ")

'''Must be a single word'''
def exactPhraseSearch(phrase):
	exactPhrase = driver.find_element_by_name('''phrase''')
	exactPhrase.send_keys(str(phrase))

def keyWordORSearch(*args):
	keyWords = driver.find_element_by_name('''ors''')
	for word in args:
		keyWords.send_keys(" \' "+str(word)+ " \' ")
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



driver = webdriver.Chrome("D:\\Programs\\chromedriver.exe")
driver.get("https://twitter.com/search-advanced?lang=en&lang=en")
#assert ("instagram" in driver.title), "are u sure this is Instagram page?"
keyWordSearch("Rideau mall")
exactPhraseSearch("lol")
keyWordORSearch("mike")
excludeSearch("mike")
hastagSearch("ok")



#exactPhraseSearch(" ")


#logIn.send_keys(Keys.RETURN)

#driver.close()

