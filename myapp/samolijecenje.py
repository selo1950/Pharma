import json

with open('samolijecenje.json', 'r') as samolijecenje:
    medicine_clean = json.load(samolijecenje)

medicine_clean =json.loads(medicine_clean)



class Patient():
    
    def __init__(self):
        self.prob = input('Izaberite vašu indikaciju: ')
        self.age = int(input('Koliko imate godina? '))
        self.sex = input('Spol : (M/Ž)')

        if self.sex == 'Ž' and self.age > 14:
            self.pregnancy = input('Jeste li trudni? (DA/NE)')
        
        #self.get_advice()
   
        
    def get_advice(self):
        for x in range(len(medicine_clean['Lijek'])):    
            if self.prob in medicine_clean['Indikacija'][str(x)]:
                name = medicine_clean['Lijek'][str(x)]
                if self.pregnancy == 'DA' and medicine_clean['Trudnoca'][str(x)] == 'Ne':
                    print(f'Lijek {name} se ne preporučuje trudnicama.')
                else:
                    if self.age < 12:
                        doza = medicine_clean['Doza-djeca'][str(x)]
                    else:
                        doza = medicine_clean['Doza-odrasli'][str(x)]
                    print(f'Lijek {name} možete koristiti za {self.prob} u dozi od {doza}.')
                    
#Ivo = Patient()
            
            
        
        

    

        
    

 
             

             
                      


    
    