from time import time
cvf=0
import os
import binascii
import math
import os.path

lenf=0
name=""
szx=""
wer=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        Deep = str(input("Please, enter Deep? "))

                        x = Deep.isnumeric()
                        if x==False:
                                print("Sorry this not whole number")
                                raise SystemExit
                        
                        if x==True:
                                Deep=int(Deep)
                                Deep6=65535-25-2

                                if Deep>Deep6:
                                        Deep=Deep6

                                if Deep<1:
                                        Deep=26
                                                
                                Deep=Deep+25
                                Deep2=Deep+2
                                Deep3=Deep*2
                                print(Deep-25)

                        i=1

                    if namez=="e":
                        i=2
                 
                    sda4=""
                    sda5=""
                    sda6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    ccc=1

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""

                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""

                    sda11=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        sda23=""
 
                        sda18=""
                        sda29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(sda2)

                                    sda3=sda2
                                 
                                    lenf5=len(sda3)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                  
                                    sda17=""
                   
                                    g=0

                                    sda3=sda2

                                    lenf6=len(sda3)                      
                                    sda17=""
                                
                                    sda3=sda2
                                    
                                    lenf6=len(sda3)
                                
                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda10=""
                                    sda11=""
                                    
                                    sda17=""
                 
                                    if   Circle_times2==0 and SpinS==0:
                                    	sda3="1"+sda3
                                    	SpinS=1

                                    if Circle_times2>=(2**48)-3:
                                            ccc=2
                                            
                                    T7 = int(sda3, 2)
                                    
                                    nameas=name+".bin" 
                                    
                                    bit=""
                                    e=0
                                    De=(e+((2**Deep2)-1)+(2**Deep)-1)
                                    e=De
                                    while f!=1:
                                        T1=T7%e
                                        if T1==0:
                                                T7=T7//e
                                                f=1
                                                bit="1"
                                        else:
                                                e=e-1
                                                g=g+1
                                        if g>(2**(Deep+2))-1:
                                                ccc=2
                                                bit=""
                                                f=1       
                                               
                                    if ccc==1:
                                    		nameas=name+".bin" 
                                    
                                  
                                    if ccc==1:
                                    	
                                    	    sda17=bin(T7)[2:]
                                   
                                    if ccc==1:
                                    	                          
                                            sda23=bin(g)[2:]
                                            hr=Deep+2
                                            
                                        	
                                            lenf=len(sda23)
                                            if lenf>Deep+2:
                                            	ccc=2

                                            if ccc==1:
                                                    
                                                    szx4=""
                                                    xc=hr-lenf%hr
                                                    z=0
                                                    if xc!=0:
                                                        if xc!=hr:
                                                                while z<xc:
                                                                        szx4="0"+szx4
                                                                        z=z+1
     
                                    if ccc==1:
                                           
                                            sda17=sda17+szx4+sda23
                                            sda18=sda3
                                            #print(len(sda17))
                              
                                    
                                    lenfS=len(sda17)
                                    #print(lenfS)

                                    if ccc==2 and Circle_times2==0:
                                                    sda3=sda3[1:]
                                    
                                   
                                    Circle_times2=Circle_times2+1
                          
                                    sda2=sda17

                                    if ccc==2:
                                            
                                            sda17=sda3
                                   
                                    
                                    if   lenfS<=Deep3 or ccc==2:
                                        Circle_times3=Circle_times2
                                        
                                        if ccc==2:
                                        	Circle_times3=Circle_times2-1


                                    if   lenfS<=Deep3 or ccc==2:
                                            Deep=Deep+2
                                    	   
                                            sda30=bin(Deep)[2:]
                                            lenf=len(sda30)

                                            szx8=""
                                            xc=16-lenf%16
                                            z=0
                                            if xc!=0:
                                                if xc!=16:
                                                        while z<xc:
                                                         	szx8="0"+szx8
                                                         	z=z+1
                                                
                                    if   lenfS<=Deep3 or ccc==2:
                                    	   
                                            sda29=bin(Circle_times3)[2:]
                                            lenf=len(sda29)

                                            szx7=""
                                            xc=48-lenf%48
                                            z=0
                                            if xc!=0:
                                                if xc!=48:
                                                        while z<xc:
                                                         	szx7="0"+szx7
                                                         	z=z+1
                                            		

                                    if   lenfS<=Deep3 or ccc==2:

                                                lenf=len(sda17)
                                                szx=""
                                                xc=8-lenf%8
                                                if xc==8:
                                                	xc=0
                                                xc2=xc
                                                z=0
                                                if xc!=0:
                                                        if xc!=8:
                                                                while z<xc:
                                                                        szx="0"+szx
                                                                        z=z+1

                                    if   lenfS<=Deep3 or ccc==2:
                                    	   


                                            sda31=bin(xc2)[2:]
                                            lenf=len(sda31)

                                            szx9=""
                                            xc=8-lenf%8
                                            z=0
                                            if xc!=0:
                                                if xc!=8:
                                                        while z<xc:
                                                         	szx9="0"+szx9
                                                         	z=z+1       

                                    if   lenfS<=Deep3 or ccc==2:
                                            lenf=len(sda17)                                           
                                            sda17=szx9+sda31+szx8+sda30+szx7+sda29+szx+sda17

                                    if   lenfS<=Deep3 or ccc==2:
                                                
                                    		L=len(sda17)
                                    		n = int(sda17, 2)
                                    		qqwslenf=len(sda17)
                                    		qqwslenf=(qqwslenf//8)*2
                                    		qqwslenf=str(qqwslenf)
                                    		qqwslenf="%0"+qqwslenf+"x"
                                    		jl=binascii.unhexlify(qqwslenf % n)
                                    		sssssw=len(jl)
                                    		szxzzza=""
                                    		szxzs=""
                                    		sda2=sda6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(jl)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    sda17=""
                              
                                    sda3=sda2
                                    
                                    lenf6=len(sda3)

                                    szx=""

                                    sda6=""

                                    #Extract

                                    sda10=""
                                    sda11=""
                                  
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                
                                    T7=0
                                    T9=0
                                 
                                    if C==1:
                                        if   Circle_times2==0:

                                                sda11=sda3[0:8]
                                                xc3 = int(sda11, 2)
                                                if xc3>7:
                                                        Corrupted=1
                                                sda3=sda3[8:]
                                                lenf6=len(sda3)

                                                sda10=sda3[0:16]
                                                Deep5 = int(sda10, 2)
                                                Deep5=Deep5
                                                Deep8=Deep5-2
                                                Deep4=Deep5
                                                sda3=sda3[16:]
                                                lenf6=len(sda3)
                                                Deep7=Deep5-2
                                                
                                                sda6=sda3[0:48]
                                                T = int(sda6, 2)
                                                sda3=sda3[48:]
                                                lenf6=len(sda3)
                                                print("Deep: ")
                                                print(Deep7-25-2)
                                                
                                        if   Circle_times2>0:
                                        	xc3=0
                                        
                                        	
    
                                        if C==1 and T!=0:
                                                sda3=sda3[xc3:]
                                                lenf6=len(sda3)
                                                sda3=sda3[0:lenf6-Deep4]
                                                lenf6=len(sda3)
                                                if lenf6==0:
                                                        Corrupted==1
                                                        
                                                if lenf6!=0:
                                                
                                                        T8 = int(sda4, 2)
                                                       
                                                        e=0
                                                        
                                                        De=(e+((2**Deep5)-1)+(2**Deep8)-1)
                                                        e=De
                                                        j=e-T8
                                                        T7=T7*j
                                               
                                       
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                   
                                    sda5=""
                                    
                                    
                                    sda17=bin(T7)[2:]
                                     
                                    sda2=sda17
                                   

                                    if i==2:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            if C==1 and T==0:
                                            	sda17=sda3
                                            	lenf=len(sda17)
                                            	szx=""
                                            	xc=8-lenf%8
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda17=szx+sda17
                                        
                                            if C==1 and T!=0:
 
                                            	sda17=bin(T7)[3:]
                                            	lenf14=len(sda17)
                                            	#print(lenf14)
                                            	lenf16=lenf14%8
                                            	if lenf16!=0 or lenf14>=((2**40)-1)*8 or Corrupted==1:

                                            		print("file corrupted")
                                            		raise SystemExit
                                            		
                                            	
                                            	lenf=len(sda17)
                                            	szx=""
                                            	xc=8-lenf%8
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda17=szx+sda17

                                            L=len(sda17)
                                         
                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
