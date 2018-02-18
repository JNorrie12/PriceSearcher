#!/usr/bin/python
import time
from price import SearchCsv, SearchJson



def main():
	x = raw_input("Welcome to my search! Would you like to run the Json or Csv example?")
	if x.lower() == "csv" :

		s = SearchCsv( "products.csv", "f" ,"5860865")


		t1 = time.time()
		s.fullSearch()
		t2 = time.time()
		print "Full sort and search took: " + str(t2 -t1)

	elif x.lower() == "json" :
	


		p = SearchJson( "https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json",  'w' ,"149136f7ff3c4de89")
	
		t1 = time.time()	
		p.fullSearch()
		t2 = time.time()
		print "Full sort and search took: " + str(t2 -t1)

	else:
		print "Input Error!"

main()
