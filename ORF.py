#Shirly Ohanona 314793910

import string
def protein(seq):#function to convert the DNA seq to protein #code: dictionary to convert the DNA codes to amino acids
    code = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L","TCT":"S", "TCC":"s", "TCA":"S", "TCG":"S","TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP","TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W","CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L","CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P","CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q","CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R","ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T","AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K","AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R","GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V","GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A","GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E","GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    i=0
    length=len(seq)
    while i <=length:
        for k in code:
            if seq[i:i+3]==k:
                print code[k],
                break;
        i+=3

def splitCodons(orf,flag):#function to find the codon list of the orf.
    codonList = []
    length=len(orf)
    i=flag
    count=flag
    while count<=length:
        codon = orf[i:i+3]#each codon will be 3 bases from the seq
        i+=3
        count+=3
        codonList.append(codon)
    return codonList
def findOrf(listCodon):#function to find the orf in the six reading frame
    dictionary={}
    stops =["TAA", "TGA", "TAG"]#dictionary of the stop codons
    start=["ATG"]#the start codon
    length=len(listCodon)
    i=0
    k=0
    b=len(listCodon)

    
    while i <b:
        
        count=0
        tmp=""
        if listCodon[i]==start[0]:#we found the start of orf
            k=i
            while listCodon[i]!=stops[0] and listCodon[i]!=stops[1]and listCodon[i]!=stops[2]and i<length-1 :#we search for the end of the orf
                count+=3
                tmp+=listCodon[i]
                i+=1
                
    
            if listCodon[i]==stops[0] or listCodon[i]==stops[1]or listCodon[i]==stops[2]:
                count+=3
                tmp+=listCodon[i]
                
            
                
            
            lenth=len(tmp)
            a=tmp[lenth-3:lenth]
            if a==stops[0]or a==stops[1]or a==stops[2]:
                dictionary[count]=tmp
                i=(k+(count/3)+1)
        else:
            i+=1
    
            
        
           

    return dictionary#return the orfs that were found
        
                
                
def orf(sequence):#function to find the six orf
    file=open(sequence,"r")
    seq=file.read()
    seq="\n".join(seq.split("\n")[1:])
    seq=seq.replace("\n","")
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}#find the complement seq
    reverseCom = "".join([complement.get(c,c) for c in reversed(seq)])#reverse the complement seq to find the reverse complement
    posONE=splitCodons(seq,0)#find the codon list. start with the first base
    posTwo=splitCodons(seq,1)#find the codon list. start with the second base
    posThree=splitCodons(seq,2)#find the codon list. start with the third base
    negONE=splitCodons(reverseCom,0)
    negTwo=splitCodons(reverseCom,1)
    negThree=splitCodons(reverseCom,2)
    output1=findOrf(posONE)
    solution(output1,"+",seq,reverseCom)
    output2=findOrf(posTwo)
    solution(output2,"+",seq,reverseCom)
    output3=findOrf(posThree)
    solution(output3,"+",seq,reverseCom)
    output4=findOrf(negONE)
    solution(output4,"-",seq,reverseCom)
    output5=findOrf(negTwo)
    solution(output5,"-",seq,reverseCom)
    output6=findOrf(negThree)
    solution(output6,"-",seq,reverseCom)
def solution(output,status,seq,reverseCom):#prints the solutions
    for k in output:
        if k>=300:#will print the orfs in this frame, that have at list 300 bases
            if status=="+":
                start= seq.find(output[k])+1
                end=start+len(output[k])-1
            else:
                start= (len(seq)-reverseCom.find(output[k]))
                end=start-len(output[k])+1
            length=len(output[k])
            print "start: ",start," end: ",end," length: ",length," ",output[k][0:6].lower()," ",output[k][length-6:length].lower()
            print output[k].lower()
            print "\n"
            print" protein:"
            protein(output[k])
            print "\n"
            print "\n"
    
    
    
  
    
    
orf("Cloning vector pACYC184.txt")#getting the DNA seq file 
