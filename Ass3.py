import pandas as pd

class Customer:
    def GetDetails(self):
        self.CustomerName=input("Enter the customer Name : ")
        self.NoofIce=input("Enter the No.of Ice Creams : ")
        return self.CustomerName,self.NoofIce
    

class IceCream:
   
    
    def __init__(self):
        ConeData = [['Plain Cone',1.5],['Waffle Cone',2],['Cup',1]]
        self.ConeDF = pd.DataFrame(ConeData,columns=['Cone','Price'])

        ToppingsData = [['Peanuts',0.75],['Caramel Sauce',0.5],['Rainbow Sprinkles',0.5],['Pecan',1],['Chocolate Sprinkles',0.5]]
        self.ToppingDF = pd.DataFrame(ToppingsData,columns=['Toppings','Price'])

        ScoopData = [['Vanilla',0.5],['Strawberry',0.5],['Chocolate',0.5],['Caramel',0.5],['Mint',0.5],['Rainbow',0.5],['Coffee',0.5],['Bubble gum',0.5]]
        self.ScoopDF = pd.DataFrame(ScoopData,columns=['Scoop','Price'])

        

        

    def getCone(self,ConeName):
        print(self.ConeDF)
        return self.ConeDF.loc[self.ConeDF['Cone']==ConeName]
        
    def GetScoop(self,ScoopName):
        print(self.ScoopDF)


    def GetTopping(self,ToppingName):    
        print(self.ToppingDF)




if __name__=='__main__':

    Cust=Customer()
    name,count=Cust.GetDetails()
    print(name,count)
   ''' IC=IceCream()
    print('Cone : ',IC.getCone('Plain Cone'))
    IC.GetScoop('Plain Cone')
    IC.GetTopping('Plain Cone')
'''
