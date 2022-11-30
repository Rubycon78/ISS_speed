#imports
from os import listdir
from os.path import dirname, realpath
from functions import calculate_speed, iterator

#get the path to the folder
path = f"{dirname(realpath(__file__))}/images"

#get the list of files in the images folder
list = listdir(path)
list.sort()

#output the csv in output
iterator(list)
