import sys
import random
import time
import os
time.sleep(1)
print"""
+=====================+=====================+
|											|
|				 CCGen v1.0					|
| 		       								|
|			 CODED BY : LilToba             |
|       E-mail : mrbarcode000@gmail.com		|
+=====================+=====================+
\n"""

with open('up1.txt') as f:
    for line in f:
        print line.strip()

time.sleep(1)
def cardgenerator():
    binn = raw_input("Enter Bin (Ex :521086) : ")
    mm = raw_input("Month (MM) : ")
    yy = raw_input("Year (YY) : ")
    i=1
    for i in range(0,100):
            i=i+1
	    geneccv = random.randint(100,999)
	    genenum = random.randint(1000000000,9999999999)
	    creditcard = (binn,genenum)
	    creditcardstr = "%s%s"%(creditcard)
	    all = creditcardstr,"|",mm,"|",yy,"|",geneccv
	    allstring = "%s%s%s%s%s%s%s"%(all)
	    print allstring

cardgenerator()
	
