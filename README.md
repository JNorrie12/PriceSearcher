# PriceSearcher

Hello and welcome to my searcher!
 
It consists of a library containing classes for both the json search and csv search, which inherit from a base class 'Search'. 
This makes it more obviously which methods are used in which secnario, and is better for future proofing!

# Set up and Running
Clone the repo, then in a terminal, cd to the directory and run ./searcher.py. 
At which point you will be prompted for csv or json, choose an option and you're away!

By default the porgram looks for the csv file in the it's directory, however in search.py you can change this to a path of your choosing. You can also change the id you'd like to search and whether it is from the a file or a url.
The can be done by changing the parameter where the search instances are made, e.g:

		s = SearchCsv( x , y , z)
    
    x = "file path + name" the data is from a file, otherwise this can be a string of a url address.
    y = This tells us whether to look for a file("f") or for a wed address ("w")
    z = The id we'd like to search
  
    the instance p = Search.Json(...) follows the same format.
    
 And that's about it! 
 
 
 ...Oh, almost forgot the gif.
 
 [Alt Text](https://media.giphy.com/media/gOkawaguYNiSI/giphy.gif)
 

   
