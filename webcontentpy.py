from bs4 import BeautifulSoup
import urllib2
import re

def loadlocalwords(path):
	def loadlocalfile(path):
		return open(path, 'r')
	return {i.strip().lower(): i.strip().lower() for i in loadlocalfile(path).readlines()} 

def getsoup(url):
	if url[:7] != "http://":
		url = "http://" + url
	html = urllib2.urlopen(url).read()
	return BeautifulSoup(html)

def get_website_words(soup):
	word_list = []
	for i in soup.stripped_strings:
		words = i.replace("\n", " ").split(" ")
		for x in words:
			word_list.append(re.sub(r'\W+','',x.lower()))
	return word_list

def main():
	right_words = loadlocalwords("words.txt")
	try:
		url = raw_input("Enter a url: ") 
		soup = getsoup(url)
	except:
		print "Url does is not there"
		main()	
	website_words = get_website_words(soup)
	correct_word_cnt = {}
	wrong_word_cnt = {}
	for i in website_words:
		if i in right_words and i in correct_word_cnt:
			correct_word_cnt[i] += 1
		elif i in right_words and i not in correct_word_cnt:
			correct_word_cnt.update({i:1})
		elif i not in right_words and i in wrong_word_cnt:
			wrong_word_cnt[i] += 1
		elif i not in right_words and i not in wrong_word_cnt:
			wrong_word_cnt.update({i:1})
	filename = raw_input("Enter file name: ")
	with open(filename, "a") as document:
		document.write("Correct Words")
 		for key, value in correct_word_cnt.iteritems():
			 document.write("%s"% str(value))			 
			 document.write('{:>30}'.format("%s\r\n"%(key)))
		document.write("Wrong Words")
 		for key, value in wrong_word_cnt.iteritems():
			 document.write("%s"% str(value))			 
			 document.write('{:>30}'.format("%s\r\n"%(key)))
if __name__ == "__main__":
	main()









