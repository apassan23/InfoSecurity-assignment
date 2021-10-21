class Freq_attack:
        
        def __init__(self): #### finding frequency of each letter of ciphered text and evaluating key(shift)in the constructor itself
                self.cipher=input("enter the ciphered text : ")                         
                freq_dict={}                                                            
                for i in self.cipher:                                                        
                        freq_dict[i]=0                                                       
                for j in self.cipher:
                        freq_dict[j]+=1
                self.max_freq='a'
                for k in range(len(self.cipher)-1):
                        if (freq_dict[self.cipher[k]]<=freq_dict[self.cipher[k+1]]):
                                self.max_freq=self.cipher[k+1]
                self.key=ord(self.max_freq)-ord('e')                            
                
        def display(self):          #### printing plain text after applying key in the display function
                for i in self.cipher:
                        if (i==' '):
                                print('z',end='')
                        else:
                            if (self.key<=0):
                                print(chr((((ord(i)-97)+self.key)%26)+97),end='')
                            else:
                                print(chr((((ord(i)-97)-self.key)%26)+97),end='')
                print('')

        def topten(self):   #### function for printion top ten deciphered texts
                self.key=ord(self.max_freq)-ord('e')
                self.display()
                self.key=ord(self.max_freq)-ord('a')
                self.display()
                self.key=ord(self.max_freq)-ord('r')
                self.display()
                self.key=ord(self.max_freq)-ord('i')
                self.display()
                self.key=ord(self.max_freq)-ord('o')
                self.display()
                self.key=ord(self.max_freq)-ord('t')
                self.display()
                self.key=ord(self.max_freq)-ord('n')
                self.display()
                self.key=ord(self.max_freq)-ord('s')
                self.display()
                self.key=ord(self.max_freq)-ord('l')
                self.display()
                self.key=ord(self.max_freq)-ord('c')
                self.display()

def main(): #### function to implement menu
    choice=0
    obj=Freq_attack()
    while (choice!=3):
        print("")
        print("press 1 for optimized plain text")
        print("press 2 to see top 10 plain texts")
        print("press 3 to exit")
        print("")
        try:
            choice=int(input("enter your choice : "))
            if(choice<1 or choice>3):
                print("your have entered an invalid input.... ")
                print("please try again")
                main()
        except:
            print("your have entered an invalid input.... ")
            print("please try again")
            main()    
        if (choice==1):
            obj.display()
        elif (choice==2):
            obj.topten()
        elif (choice==3):
            print("task completed.....")
            break
            
if __name__ == "__main__":
    main()
