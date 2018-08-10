import TwitterScrapper

list = TwitterScrapper.performSeach("D:\soft\Python\python35-ws\chromedriver.exe", "Rideau", "stab stabbing police", None, "", "Rideau Street", '2018-06-02', None)
print(list)

'''
Sample result:
['https://twitter.com/OJEN_ROEJ/status/1026907686024048640', 'https://twitter.com/avocat_93/status/1025318200366510081', 'https://twitter.com/avocat_93/status/1025318200366510081', 'https://twitter.com/OttawaPoliceGS/status/1024626930413436928', 'https://twitter.com/OttawaPoliceGS/status/1024626930413436928', 'https://twitter.com/OttawaPoliceGS/status/1024626930413436928', 'https://twitter.com/OttawaPoliceGS/status/1024626930413436928', 'https://twitter.com/CFRAOttawa/status/1022778972835393536', 'https://twitter.com/OttawaCitizen/status/1022346545948254208', 'https://twitter.com/OttawaCitizen/status/1022166500201979904', 'https://twitter.com/1tvchannel/status/1019211878759829504', 'https://twitter.com/OttawaCitizen/status/1018950736510619648', 'https://twitter.com/cbcotttraffic/status/1017742138560450561', 'https://twitter.com/CBCOttawa/status/1015240239290384385', 'https://twitter.com/ctvottawa/status/1015226017445793797', 'https://twitter.com/OttawaCitizen/status/1014490632746872832', 'https://twitter.com/OttawaCitizen/status/1014468806599696385', 'https://twitter.com/MidouLii/status/1013469707784028161', 'https://twitter.com/1310NEWS/status/1013097109745045512', 'https://twitter.com/CBCOttawa/status/1012291993463066625']
'''