'''
 you should write a Python script for the ice cream ordering system. Your program must store the prices of the individual items (cones, scoop flavours and toppings). Specifically, the program should do the following:
• At the start, the program should ask for the customer’s name to personalise and track the order and then get the number of ice creams from the customer.
• For each ice cream, the cone type, scoop amount, scoop flavour, number and type of toppings should be taken from the customer.
• At the end the program should display the itemised order with the total price.
• The program should be able to handle invalid entries inputted (such as incorrect cone type, or invalid number of toppings)
'''


import pandas as pd

class Customer:
    def GetDetails(self):
        self.CustomerName=input("\nEnter the customer Name : ")
        self.NoofIce=input("\nEnter the No.of Ice Creams : ")
        return self.CustomerName,self.NoofIce


class IceCream:

    #Constructor to Initialize the Cone, Topping and Scoop types
    def __init__(self):
        ConeData = [['Plain Cone',1.5],['Waffle Cone',2],['Cup',1]]
        self.ConeDF = pd.DataFrame(ConeData,columns=['Cone','Price'])

        ToppingsData = [['Peanuts',0.75],['Caramel Sauce',0.5],['Rainbow Sprinkles',0.5],['Pecan',1],['Chocolate Sprinkles',0.5]]
        self.ToppingDF = pd.DataFrame(ToppingsData,columns=['Topping','Price'])

        ScoopData = [['Vanilla',0.5],['Strawberry',0.5],['Chocolate',0.5],['Caramel',0.5],['Mint',0.5],['Rainbow',0.5],['Coffee',0.5],['Bubble gum',0.5]]
        self.ScoopDF = pd.DataFrame(ScoopData,columns=['Scoop','Price'])

    #Get Cone type and validating
    def getCone(self,ConeName):
        self.res=self.ConeDF.loc[self.ConeDF['Cone']==ConeName]
        if self.res.empty:
            return 'N',[]
        else:
            return 'Y',self.res
        
    #Get Scoop type and validating
    def getScoop(self,ScoopName):
        self.res=self.ScoopDF.loc[self.ScoopDF['Scoop']==ScoopName]
        if self.res.empty:
            return 'N',[]
        else:
            return 'Y',self.res

    #Get Topping type and validating
    def getTopping(self,ToppingName):
        self.res=self.ToppingDF.loc[self.ToppingDF['Topping']==ToppingName]
        if self.res.empty:
            return 'N',[]
        else:
            return 'Y',self.res

    #Get All Scoop type 
    def getScoops(self):
        return self.ScoopDF

    #Get All Toppings type 
    def getToppings(self):
        return self.ToppingDF

    #Get All Cone type
    def getCones(self):
        return self.ConeDF

#Main Function
if __name__=='__main__':

    #Intiating Objects
    Cust=Customer()
    IC=IceCream()
    while True:
        CName,ICount=Cust.GetDetails()
        ListScoops=[]
        ListToppings=[]

        for n in range(int(ICount)):
            LScoops=[]
            LToppings=[]
            print("\n IceCream ",(n+1))
            print('\n',IC.getCones().to_string(index=False))

            while True:
                #Getting Cone type from user
                TCone=input("\nSelect Type of Cone for IceCream "+str(n+1)+" :")
                f,item=IC.getCone(TCone)
                if f=='Y':
                    TCone=item.Cone.to_string(index=False)
                    break
                else:
                    print("\nNo Cones Available with this name")
            #Getting No.of Scoops and Scoop types from user
            NScoops=input("\nSelect Number of Scoops for IceCream "+str(n+1)+" :")
            print('\n',IC.getScoops().to_string(index=False))

            for NS in range(int(NScoops)):
                while True:
                    TScoop=input("\nSelect Type of Scoop "+str(NS+1)+" for IceCream "+str(n+1)+" :")
                    f,item=IC.getScoop(TScoop)
                    if f=='Y':
                        if item.Scoop.to_string(index=False) in LScoops:
                            print("\nAlready Selected this Scoop. Please select Different One..")
                            continue
                        else:
                            LScoops.append(item.Scoop.to_string(index=False))
                            break
                    else:
                        print("\nNo Scoop Available with this name")

            #Getting No.of Toppings and Topping types from user
            print('\n',IC.getToppings().to_string(index=False))
            NToppings=input("\nSelect Number of Toppings for IceCream "+str(n+1)+" :")

            for NT in range(int(NToppings)):
                while True:
                    TTopping=input("\nSelect Type of Topping "+str(NT+1)+" for IceCream "+str(n+1)+" :")
                    f,item=IC.getTopping(TTopping)
                    if f=='Y':
                        if item.Topping.to_string(index=False) in LToppings:
                            print("\nAlready Selected this Topping. Please select Different One..")
                            continue
                        else:
                            LToppings.append(item.Topping.to_string(index=False))
                            break
                    else:
                        print("\nNo Scoop Available with this name")
            ListScoops.append(LScoops)
            ListToppings.append(LToppings)
            
        
        line=75
        TotalPrice=0.00 #Total price of Eace Ice Cream
        Tot=0.00 #Total Price of No.Of Ice Creams
        PTopping=0.00
        PScoop=0.00

        print("="*line)
        print("\nCustomer Name : ",CName,"\t\t\tNo.Of IceCreams : ", ICount)
        print("="*line)
        

        for i in range(int(ICount)):
            print("\nIce Cream ",i+1)
            f,PCone=IC.getCone(TCone)
            TotalPrice+=float(PCone.Price.to_string(index=False))
            print("\n Cone - ",TCone," Price : ",PCone.Price.to_string(index=False))

            for ls in ListScoops[i]:
                f,TPScoop=IC.getScoop(ls)
                PScoop+=float(TPScoop.Price.to_string(index=False))
                TotalPrice+=float(TPScoop.Price.to_string(index=False))
            print("\n Scopes - ",",".join(LScoops)," Price : ",PScoop)

            for ts in ListToppings[i]:
                f,TPTopping=IC.getTopping(ts)
                PTopping+=float(TPTopping.Price.to_string(index=False))
                TotalPrice+=float(TPTopping.Price.to_string(index=False))
                
            print("\n Toppings - ",",".join(LToppings)," Price : ",PTopping)
            print("="*line)
            Tot+=TotalPrice
            print("\t\t\t\t\t\t\t Price : ",TotalPrice)
            print("="*line)

            
        print("\t\t\t\t\t\tTotal Price : ",Tot)
        exit=input("Want to continue Y/N : ")
        if exit=='N' or exit=='n':
            break
