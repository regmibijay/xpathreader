# xPathreader
Reads xPath documents and outputs specified tags.

## Installation:
You can install xpathreader from pip directly using `pip3 install xpathreader`

Alternatively:
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
  $ python3 xpathreader.py -i filename1.xml filename2.xml filename3.xml -f .//tag1/tag2 .//tag6/tag7 -e utf-8
  ```
  Syntax explaination:
   - `-i` specfies input file path, multiple file paths are supported and seperated by space.
   - `-f` specifies tags to find, multiple tags are supported and seperated by space.
   - `-o` specifies output mode, currently list or string mode are supported. 
     -   `-o s` or `-o string` for string mode
     -   `-o l` or `-o list` for list mode (default)
   - `-e`specifies the file encoding. Input in lower case. 
2. Importing from PIP Package:
```
import xpathreader
out = xpathreader.read(filePath,findTag,outputMode,encoding) #outputMode = "list" or "string"
```

3. Search Syntax: 
  - Syntax as specified in pythons ElementTree[https://docs.python.org/2/library/xml.etree.elementtree.html#supported-xpath-syntax]
  ``` 

 tag

Selects all child elements with the given tag. For example, spam selects all child elements named spam, and spam/egg selects all grandchildren named egg in all children named spam.

*

Selects all child elements. For example, */egg selects all grandchildren named egg.

.

Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path.

//

Selects all subelements, on all levels beneath the current element. For example, .//egg selects all egg elements in the entire tree.

..

Selects the parent element.

[@attrib]

Selects all elements that have the given attribute.

[@attrib='value']

Selects all elements for which the given attribute has the given value. The value cannot contain quotes.

[tag]

Selects all elements that have a child named tag. Only immediate children are supported.

[tag='text']

Selects all elements that have a child named tag whose complete text content, including descendants, equals the given text.

[position]

Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1).
