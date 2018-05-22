

import string
def slidingwindowplot(dna_file,window_length):
     file1=open(dna_file,"r")#opens the file#example for a text.
     file1.readline()
     file2=open("tmp.txt","w")
     file2.write(file1.read().rstrip('\n'))
     file2.close()
     file2=open("tmp.txt","r")
     data=file2.read(window_length)
     data.lower()
     data=''.join(data.split())
     count3=1
     count2=1
     x={}
     tmp={}

     while len(data)and count3<19:
          while len(data)!=window_length:
               lenght=len(data)
               count=window_length-lenght
               data+=file2.read(count)
               data=''.join(data.split())
               for i in range (lenght-1):
                    if data[i]!="a" and data[i]!="c" and data[i]!="g" and data[i]!="t":
                         data.replace(data[i],'')
          
          
     
          tmp[count3]=data
          a,b=count2, count2+window_length-1 
          flag="{}-{}".format(a,b)
          x[count3]=flag
          count2+=window_length
          count3+=1

          data=file2.read(window_length)
          data=''.join(data.split())
          data.lower()
          
     

     

     
     tmp =  {k: v.lower() for k, v in tmp.items()}
     y={}
     
     for k in tmp:
          stri=tmp[k]
          Dictionary={}
          l=len(stri)
          i=0
          while i<l:
              word=stri[i]
              if    Dictionary.has_key(word):#if the substring already exists in the dictionary
                    Dictionary[word] += 1
              else:
                  Dictionary[word]=1
              i+=1
          frequency={}
          frequency['gc']=float((Dictionary['g']+Dictionary['c'])*100)/window_length
          y[k]=frequency['gc']/100
          y[k]= "{0:.4f}".format(y[k])

          x1=list()
          y1=list()

          for k in x:
               x1.append(x[k])
          for k in y:
               y1.append(y[k])
     
     


     return x1,y1
          
      
          
    
     
     
                      
             
    
    
     
     
   
     
output1 ,output2 =slidingwindowplot ("sample_dna1.txt", 10000)
file=open("result.txt", "w")#will write the result into a file
data=""
file.write("x values:")
file.write("\n")
for i in range(len(output1)):
     file.write(output1[i])
     file.write("   ")



file.write("\n")

file.write("y values:")
file.write("\n")
for i in range(len(output2)):
     file.write(output2[i])
     file.write("   ")
file.close
    


