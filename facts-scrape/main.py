import requests
from BeautifulSoup import BeautifulSoup
import unidecode
import json

lfacts = []

# sex facts
def sfacts():
	url = 'http://www.hexjam.com/uk/sex-relationships/40-interesting-things-you-never-knew-about-sex'
	r = requests.get(url).content;
	soup = BeautifulSoup(r);
	all_p = soup.findAll('p')
	fres = []
	# logic to get all facts
	for x in all_p:
		if x.findChildren('strong') != 0:
			try:
				v = x.text.split(".")
				k = int(v[0])
				s = ''.join(v[1:])
				fres.append(unidecode.unidecode(s))
			except:
				pass
	return fres

# random facts
def rfacts():
	url = "http://hubpages.com/education/Very-Interesting-Facts"
	r = requests.get(url).content
	soup = BeautifulSoup(r);
	k = soup.findChildren('div', {'id': 'txtd_3703576'});
	k = k[0]
	k = k.findChildren("p")
	k = k[0]
	j = k.__str__().split("<br /><br /><br />")
	fres = []
	for x in j:
		fres.append(unidecode.unidecode(BeautifulSoup(x).text))
	return fres

# useless facts
def usfacts():
	url = "http://www.djtech.net/humor/useless_facts.htm"
	r = requests.get(url).content
	soup = BeautifulSoup(r)
	k = soup.findAll('li');
	fres = []
	for x in k:
		fres.append(unidecode.unidecode(BeautifulSoup(' '.join(x.text.split('\n\t\t')), convertEntities=BeautifulSoup.HTML_ENTITIES).text))
	return fres

# more facts
def mfacts():
	url = "http://www.spinfold.com/35-unknown-facts-about-universe/"
	r = requests.get(url).content;
	soup = BeautifulSoup(r)
	fres = []
	for x in soup.findAll('p'):
		try:
			x = x.text
			x = x.split(".")
			v = int(x[0])
			fres.append('.'.join(x[1:]))
		except:
			pass

	url = "http://www.spinfold.com/30-amazing-facts-about-pi/"
	r = requests.get(url).content;
	soup = BeautifulSoup(r);
	fres = []
	for x in soup.findAll('p'):
		try:
			x = x.text
			x = x.split(".")
			v = int(x[0])
			fres.append(unidecode.unidecode('.'.join(x[1:])))
		except:
			pass

	return fres

# about numbers
def nfacts():
	url = "http://www.spinfold.com/amazing-facts-about-numbers/"
	r = requests.get(url).content
	fres = []
	soup = BeautifulSoup(r)
	k = soup.findAll('div', {'class': 'entry'})
	k = k[0]
	for x in k.findAll('li'):
		fres.append(unidecode.unidecode(BeautifulSoup(x.text, convertEntities=BeautifulSoup.HTML_ENTITIES).text))
	return fres

lfacts += sfacts()
lfacts += rfacts()
lfacts += usfacts()
lfacts += mfacts()
# lfacts += nfacts()
d = {}
d["amt"] = len(lfacts)
d["datas"] = lfacts
with open('../data.json', "w") as f:
	json.dump(d, f)
print "process completed"