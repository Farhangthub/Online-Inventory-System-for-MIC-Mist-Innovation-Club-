class MIC_Inventory:
    __items={}

    def __init__(self,equip):
        for i in equip:
            self.__items[i] = 0


    def DisplayEquipment(self) : 
        for i,j in self.__items.items():
            print(f"{i} : {j}")
       

    def LendEquipment(self,itm): 
        if itm not in self.__items:
            print("There is no equipment in this name")
        elif self.__items[itm]==0:
            print("This equipment is not available now.")
        else:
            self.__items[itm] -=1
            print(f"{itm} was lended now.")

    def AddEquipment(self,itm,quantity): 
        if itm not in self.__items:
            self.__items[itm]=quantity
            print(f"New equipment is added.\n Now {itm} is available:{self.__items[itm]}")
        else:
            self.__items[itm] +=quantity
            print(f"{itm} is added to MIC inventory.\n Now {itm} is available:{self.__items[itm]}")
        
    def ReturnEquipment(self,itm): 
        self.__items[itm] +=1
        print(f"Thank you for returning this equipment.\n Now {itm} is available:{self.__items[itm]}")

        

MIC_invetory_2022=MIC_Inventory(['Arduino_uno', 'Motor', 'Ir_module', 'ECG sensor'])

while 1:
    print("Select from below:\n1)Display \n2)Lend \n3)Add \n4)Return")
    x =int(input("Enter your choice:"))
    if x==1:
        MIC_invetory_2022.DisplayEquipment()
    elif x == 2:
        itm = input("Enter the name of the equuipment you want to lend:")
        MIC_invetory_2022.LendEquipment(itm)
    elif x == 3:
        itm=input("Enter the name of the equipment you want to add:")
        quantity=int(input("Enter the quantity of the equipment:"))
        MIC_invetory_2022.AddEquipment(itm,quantity)
    elif x== 4:
        itm = input("Enter the name of the equuipment you want to return:")
        MIC_invetory_2022.LendEquipment(itm)
    else:
        break




        
