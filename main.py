
# Online Python - IDE, Editor, Compiler, Interpreter
#PROBLEMA II
#Definir variables

print("Help the snail who wants to get out of the well")
H=int(input("Enter the height of the well :  ")) #La distancia del pozo 
Ld=int(input("Enter as soon as the snail goes up :  ")) #La distancia que asciende el caracol 
Ln=int(input("Enter when the snail slips : ")) #La distancia que desciende el caracol
 

while Ld > Ln:
   print("The snail came out a day: " + str ((H - Ln) / (Ld - Ln)))
   
   break
   
if Ld < Ln:
     print("The snail never came out")
     
