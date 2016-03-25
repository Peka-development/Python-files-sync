#!/usr/bin/python
#! python3

print ("\nSync folders tool by Peka-development.ink started \n")

import os
import sys

class SyncDir:
  def __init__(self, name, path, filelist):
    self.name=name
    self.path=path
    self.filelist=filelist

class ProcessedFolders():
  def __init__(self):

	args = sys.argv[1:]
	#print (args)

	#Check for invalid number of arguments:
	if not args:
		print ("Error: no input args, process terminated")
		sys.exit(1)

	if len(args) < 2:
		print ("Error: not enough args, process terminated")
		sys.exit(1)

	if len(args) > 2:
		print ("Error: too much args, process terminated")
		sys.exit(1)

	#Set class attributes:
	self.sourceFolder = args[0]
	self.targetFolder = args[1]

#GetSourceFolder:
#	Get source folder from ui or console
print ("Source folder is: %s" %(ProcessedFolders().sourceFolder))

#GetTargetFolder:
#	Get target folder from ui or console
print ("Target folder is: %s" %(ProcessedFolders().targetFolder))

#indexSourceItems:
  # Walk through source folder and create list of contained items

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.


	rootdir=ProcessedFolders().sourceFolder

	dirs=[]
	print ("\n")
	for root, Wdirs, Wfiles in os.walk(rootdir):
		a=SyncDir('name', root, Wfiles)
		dirs.append(a)

	for dir in dirs:
		print ('directory: %s. Its ready to sync. It has files: %s' %(dir.path, dir.filelist))
		print ('--')

    
if __name__ == "__main__":
	main()

#indexTargetItems:
  # Walk through target folder and create list of contained items  

#compareItems:
  # Loop through items from source and target folders, and get difference
  
#copyItems:
  # Copy items usinig difference data 

#class Item:
  # item got some properties:
  #	name
  #	path
  #	filelist if its folder
  #	sync attributes

