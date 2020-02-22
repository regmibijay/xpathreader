# xPathreader
Reads xPath document and outputs tags specified

## Installation:
1. Cloning this repository:
  - `git clone https://github.com/regmibijay/xpathreader`
2. Building a pip wheel:
  - `cd xpathreader`
  - `python3 setup.py bdist_wheel`
3. Installing PIP Wheel:
  - `pip3 install dist/xpathreader-x.x-pyx-xxxx-xxx.whl` #replace x's with respective version name
 
  
## Usage: 
1. Command line: 
  ``` 
  $ python3 xpathreader.py -i filename1.xml filename2.xml filename3.xml -f .//tag1/tag2 .//tag6/tag7 
  ```
  Syntax explaination:
   - `-i` specfies input file path, multiple file paths are supported and seperated by space.
   - `-f` specifies tags to find, multiple tags are supported and seperated by space.
   - `-o` specifies output mode, currently list or string mode are supported. 
     -   `-o s` or `-o string` for string mode
     -   `-o l` or `-o list` for list mode (default)
2. Importing from PIP Package:
```
import xpathreader
out = xpathreader.read(filePath,findTag,outputMode) #outputMode = "list" or "string"
```

   
