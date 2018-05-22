"""
Created on Thu Mar 22 20:17:29 2018

@author: Shirly
"""
#Shirly Ohanona 314793910
'''
The program print the numbers of the s-s bonds in the cys amino acids
'''
import math
import os  
import sys 


dic={}

myFile=sys.argv[1]#the output file
pdbFile=open(myFile,'r')
for line in pdbFile:
    list = line.split()
    if list[0] == 'ATOM' and list[2]=="SG" and list[3]=="CYS":
        dic[list[5]]=list[6]+","+list[7]+","+list[8]
numbers=[]
count=1
for number1 in dic:
    for number2 in dic:
        if(number1!=number2):
            coordinates_1=dic[number1].split(",")
            coordinates_2=dic[number2].split(",")
            distance=math.sqrt((float(coordinates_1[0])-float(coordinates_2[0]))**2 + (float(coordinates_1[1])-float(coordinates_2[1]))**2 + (float(coordinates_1[2])-float(coordinates_2[2]))**2)
            if distance < 3:
                numbers.append(number1+","+number2)
                if not(number2+","+number1) in numbers:
                    print(str(count)+"."+" "+str(number1)+" "+str(number2))
                    count+=1
    


