import os,sys
from xml.etree import ElementTree as ET
from argparse import ArgumentParser
def read(inputPath,findTag,outputMode):
 xmlString  = ""
 with open(inputPath,"r") as f:
  xmlString = f.readlines()
 tree = ET.fromstring(xmlString)
 tags = tree.findall(findTag)
 n = len(tags)
 if outputMode == "s" or outputMode == "string" or outputMode == 1:
  return " ".join(str(x) for x in tags)
 return tags,n
def checkURL(path):
 if os.path.isfile(path):
  return True
 return False
def main(argv):
 p = ArgumentParser()
 p.add_argument("-i",help = "Input File, supports multiple file input", nargs = "+")
 p.add_argument("-f", help = "Tag as string, supports multiple tags", nargs = "+")
 p.add_argument("-o", help = "Output mode, list(l) or string(s)", default = "list")
 arg = p.parse_args()
 if arg.i is None or arg.f is None:
  print ("Please specify at least one valid xPath file URL and a tag to search for")
  return 1
 out = ""
 for path in arg.i:
  print ("Reading: ",path)
  if not checkURL(path):
     print ("-> Does not seem to be a valid URL, skipping")
     continue  
  for tag in arg.f:
    print ("-> Searching for ",tag)
    if arg.o == "l" or arg.o == "list":
      o,n = read(path,tag,"l")
      print("--> ",n," Tags found")
      print (*o)  
    if arg.o == "s" or arg.o == "string":
      o,n = read(path,tag,"s")
      print("--> ",n," Tags found")
      print (o)
if __name__ == "__main__":
 main(sys.argv[1:])
