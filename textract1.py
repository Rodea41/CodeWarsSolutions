
import re 
import textract


textobj = textract.process('C:/Users/crodea/Desktop/doc2.docx') ##opens doc2 and stores as an object
                        
                                       
text = str(textobj) ## converts object to a string               

productCodeRegex = re.compile(r'([W0-2][A0-9]\d\d\d\d)') #### Regex searches for 6 digits patterm . 1 digit can start with letter 'W' or the number 1 or 2. Rest can be any digit
                                                         ##### Need to find way to filter our digits that are not product code

codeDateRegex = re.compile(r'(\d?\d\/\d?\d\/[2][1-4])')  ## Finds code date 1/10/22

#quantityRegex = re.compile(r'(\d\d\d\d\d)') 

#weightRegex = re.compile(r'(\d\d\d\d\d)')



##to = textRegex.search(text)  ## search through text string for pattern defined in textRegex

findpCode = re.findall(productCodeRegex, text)

findCodeDate = re.findall(codeDateRegex, text)


print(findpCode)
## print(findCodeDate)





            ####Example format of what to search for

##W00044 - BEEF BONES 3PC CUT\n\n1/10/22\n\n209\n\n13,216.05\n\n5,994.761\

## W77304 - Beef HIND TENDON\n\n1/10/22\n\n19\n\n565.10\n\n256.328
