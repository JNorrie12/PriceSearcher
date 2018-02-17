import csv
import json
import operator
import time
import sys 
import urllib


#asset sorted(data) == counting(data)

#Search is the base class and only contains methods and attributes to do with sotrinng, searching and outputting, i.e. methods common to both the csv and json imports.
class Search:
	#Params:
	# data = nested list structure of items to search.
	# iid  = id of item we wish to search.
	# output = The json 
	def __init__(self, data, iid):

		self.data = data
		self.iid = iid
		self.output = None

	#Sorts data so a more intellegent search than iterating can be carried out. The in built python sort is fairly well optimised, however for larger data sets it might be worth implementing a Radix sort for example.
	def sort(self):

		sort = sorted(self.data, key=operator.itemgetter(0));
		self.data = sort

	#Using a bisection method or 'binary algorithm' to perform a quicker search.
	def bisection(self):
		L = len(self.data)
		R = 0
		mid = len(self.data)/2 

		while mid > 1:
			mid = (L+R)/2
			bisecval = self.data[mid][0]
			if bisecval > self.iid:

				L = mid - 1

			elif bisecval < self.iid:

				R = mid + 1

			else:

				self.output = self.data[mid]
				break
		if self.data[mid][0] == self.iid:
			self.output = self.data[mid]	

	#Write to json
	def writejson(self, outputFile = "output.json" ):
	
		with open( outputFile , 'w') as outfile:
	    		json.dump(self.output, outfile)
		print "Written to JSON " + outputFile

	#Running all the methods in order to perform a standard full search.
	def fullSearch(self):
		self.sort()
		self.bisection()
		self.writejson()










#Class inheriting from Search but containing all the csv unique stuff.
class SearchCsv(Search):

	#when instane is constucted, data is retreived from filepath/url and used it init Search base class.
	#Params:
	#fileName = The path to the file or web url depending on the sencario.
	#fileOrWeb = "f" or "w" depending on import type.
	def __init__(self, fileName, fileOrWeb, iid):
		self.fileName = fileName
		self.fileOrWeb = fileOrWeb

		data = self.csvimport()
				
		Search.__init__(self, data , iid)

	#Import a csv via web or file, however the web option hasn't been tested due to lack of data, just showing how it could be implemented! 
	def csvimport(self):
		if self.fileOrWeb == "f":		
			csvData = open( self.fileName , 'r')
		elif self.fileOrWeb == "w":
			csvData = urllib.urlopen( self.fileName )
		csvList = csv.reader(csvData, delimiter = ',')
		
		return  csvList

	#Csv has loads of wierd buffer characters so we need to clean the data up. Also change yes and no to true and false.
	def parseResultCsv(self ):
		self.output[1]=self.output[1][2:-1]
		self.output[2]=self.output[2][2:-1]
		self.output[3]=self.output[3][2:-1]
		self.output[4]=float(self.output[4][2:-1])
		if "y" in self.output[5]:
			self.output[5] = True
		elif "n" in self.output[5]:
			self.output[5] = False	

	#Sincewe want to clean up the csv data before outputting, we overide the fullSearch method.
	def fullSearch(self):
		self.sort()		
		self.bisection()
		self.parseResultCsv()
		self.writejson()		

#Unique Json class, inherting Search.














class SearchJson(Search):
	#Like csv, the init imports the data which is then used to init the search intialiser.
	def __init__(self, fileName, fileOrWeb, iid):
		self.fileName = fileName
		self.fileOrWeb = fileOrWeb		
		
		data = self.importJson()

		Search.__init__(self, data , iid)
	
	#The Jsons come in a not very helpful dictionary format (Not that dictionaries aren't helpful, more the way it'set out isn't very useful) so I change it to the same format as the csv. This allows use to use the single bisection search.
	def importJson(self):
		if self.fileOrWeb == "f":
			jsonData = open( self.fileName )
		elif self.fileOrWeb == "w":
			jsonData = urllib.urlopen( self.fileName )

		jsonList = []
		t4 = time.time()
		data = json.loads(jsonData.read())
		print "Import Time: " +  str(time.time() -t4)	#I display the import time because my internet was very slow and it was taking a long time. 
								#Just showing that my search alogrithm isn't at fault!
		
		for i in data:					#Paring the data into a nested list structure/
			jsonEntry = [i.get("id"), i.get('name'), i.get("brand"), i.get("retailer"), i.get("price"), i.get("in_stock")]
			jsonList.append(jsonEntry)
		
		return jsonList


	#Change the yes and no's so trues and falses
	def parseOutput(self):
		if "y" in self.output[5]:
			self.output[5] = True
		elif "n" in self.output[5]:
			self.output[5] = False	

	#Again, override the fullSearch method.
	def fullSearch(self):
		self.sort()
		self.bisection()
		self.parseOutput()
		self.writejson()

