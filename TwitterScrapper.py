from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import urllib
import sys

def stringDoubleQuoted(arg):
	return '\"' + str(arg) + '\"'

def sleep(x):
	time.sleep(x)

'''fills the "all of htses words" field in twitter advanced search
args can be any number of strings, uses an & operator so all of these must be present
'''
def keyWordSearch(*args):
	result = ''
	for word in args:
		result = result + str(word) + ' '
	return result

'''Must be a single word'''
def exactPhraseSearch(phrase):
	return stringDoubleQuoted(phrase) + ' '

def keyWordORSearch(*args):
	result = ''
	if len(args) == 1: args = args[0].split()
	count = 1
	for word in args:
		if(count > 1): result = result + 'OR '
		result = result + str(word) + ' '
		count = count + 1
	return result

def excludeSearch(*args):
	result = ''
	if len(args) == 1: args = args[0].split()
	for word in args:
		result = result + '-' + str(word) + ' '
	return result

def hastagSearch(*args):
	result = ''
	if len(args) == 1: args = args[0].split()
	for word in args:
		result = result + '#' + str(word) + ' '
	return result

def locationSearch(place):
	return 'near:' + stringDoubleQuoted(place) + ' ' + 'within:15km' + ' '

def sinceDate(fromDate):
	return 'since:' + fromDate + ' '
	
def untilDate(toDate):
	return 'until:' + toDate

def clickSearch():
	driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/form/button').click()


def buildTestURL():
	# Build the search url
	url = ''
	url = url + keyWordSearch("Rideau")
	url = url + keyWordORSearch("stab", "stabbing","police")
	#url = url + excludeSearch("lol")
	#url = url + hastagSearch("ott")
	url = url + locationSearch("Rideau Street")
	url = url + sinceDate('2018-06-02')
	#url = url + untilDate('2018-07-08')

	url = url.strip()
	url = urllib.parse.quote(url)
	url = 'https://twitter.com/search?l=&q=' + url
	url = url + '&src=typd'
	return url
	
def doSearch(driverPath, url): 
	# Chrome requires the complete path with the executable
	driver = webdriver.Chrome(driverPath)
	# Firefox requires only the directory path to the gecko driver
	# "D:\soft\Python\python35-ws"
	#driver = webdriver.Firefox(sys.argv[1])
	#driver.get("https://twitter.com/search-advanced?lang=en")

	driver.get(url)

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
	list_of_photos = []
	for x in elems:
		if len(list_of_photos) >= 25:
			break
		try:
			x.click()
			sleep(2)
			driver.find_element_by_xpath('''/html/body/div[5]/div[2]/div[4]/div/div[2]/div[4]/div[2]/div[4]/div/button/div/span[1]''').click()
			elem = driver.find_element_by_xpath('''/html/body/div[5]/div[2]/div[4]/div/div[2]/div[1]/small/a''')
			list_of_photos.append(elem.get_attribute('href'))
			driver.find_element_by_xpath('''/html/body/div[5]/div[2]/button/span''').click()

		except:
			pass

	driver.close()
	return list_of_photos

def main():
	if len(sys.argv) != 2:
		print ('''\
		The path to the Gecko driver have to be passed
		Usage: python TwitterScrapper.py D:\\Programs\\chromedriver.exe
		''')
		sys.exit(1)
	url = buildTestURL()
	doSearch(sys.argv[1], url)

def performSeach(driver, keyWordSearchStr, keyWordORSearchStr, excludeSearchStr, hastagSearchStr, locationSearchStr, sinceDateStr, untilDateStr):
	# Build the search url
	url = ''
	if keyWordSearchStr:
		url = url + keyWordSearch(keyWordSearchStr)
	if keyWordORSearchStr:
		url = url + keyWordORSearch(keyWordORSearchStr)
	if excludeSearchStr:
		url = url + excludeSearch(excludeSearchStr)
	if hastagSearchStr:
		url = url + hastagSearch(hastagSearchStr)
	if locationSearchStr:
		url = url + locationSearch(locationSearchStr)
	if sinceDateStr:
		url = url + sinceDate(sinceDateStr)
	if untilDateStr:
		url = url + untilDate(untilDateStr)

	print ("url:" + url)
	url = url.strip()
	url = urllib.parse.quote(url)
	url = 'https://twitter.com/search?l=&q=' + url
	url = url + '&src=typd'
	print ("url:" + url)
	return doSearch(driver, url)
	
if __name__ == '__main__':
	print ('This program is being run by itself')
	main()
#else:
	#print ('I am being imported from another module')
	