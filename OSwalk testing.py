#!/usr/bin/python
import os
import sys

"""os.walk() testing

debug
"""
class SyncDir:
  # SyncDir got some properties:
  #	name
  #	path
  #	filelist
  #	sync attributes
  def __init__(self, name, path, filelist):
    self.name=name
    self.path=path
    self.filelist=filelist


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: no args")
    sys.exit(1)

  rootdir=args[0]
  dirs=[]
  for root, Wdirs, Wfiles in os.walk(rootdir):
    a=SyncDir('name',root,Wfiles)
    dirs.append(a)
  for dir in dirs:
    print ('directory', dir.path, 'is ready to sync. It has files:', dir.filelist)
    print ('--')
  
    
if __name__ == "__main__":
  main()
