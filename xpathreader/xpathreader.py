import os,sys
from io import open
from xml.etree import ElementTree as ET
from argparse import ArgumentParser
def read(inputPath,findTag,outputMode = "list",encoding = "utf-8"):
 xmlString  = ""
 with open(inputPath,mode = "r",encoding = encoding) as f:
  xmlString = f.read()
 if not encoding == "utf-8":
  xmlString = xmlString.encode("utf-8")
 tree = ET.fromstring(xmlString)
 tags = tree.findall(findTag)
 n = len(tags)
 if outputMode == "s" or outputMode == "string" or outputMode == 1:
  return " ".join(str(x.text) for x in tags),n
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
 p.add_argument("-e", help = "Encoding of files, default is UTF-8",default = "utf-8")
 arg = p.parse_args()
 if arg.i is None or arg.f is None:
  print ("Please specify at least one valid xPath file URL and a tag to search for")
  return 1
 out = ""
 for path in arg.i:
  print ("Reading: ",path)
  if not checkURL(path):
     print ("-> Does not seem to be a valid/existing file, skipping")
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
