# PriceSearcher

Hello and welcome to my searcher!
 
It consists of a library, price.py and a main in searcher.py.

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
    
    
 # Technical Explanations
 price.py  contains classes for both the json search and csv search, which inherit from a base class 'Search'.
This makes it more obvious which methods are used in which scenario, and is more general. For instance if I want to add yaml import ability I just inherit from Search and half the job is done for me!

A search with data this big takes roughly 1.5 seconds, most of which is due to python's sorting method (the actualy binary search accounts for about 0.05 seconds). This is the obvious bottle neck and in future I would concentrate on changing this to a asymptotically faster sort such as a Radix sort. I decided not to implement this here as I wanted to keep as close to the 2-3 hour guide line set out!

 And that's about it! 
 
 
 [...Oh, almost forgot the gif.](https://media.giphy.com/media/gOkawaguYNiSI/giphy.gif)
 

   
