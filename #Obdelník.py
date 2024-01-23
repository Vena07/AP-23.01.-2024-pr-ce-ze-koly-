#Obdelník
print("Obdelník:")
a = int(input("Zadejte hondotu strany a: "))
b = int(input("Zadejte hondotu strany b: "))
if a >0 and b >0:   
    výsledek1 = (a * b)*2 
    výsledek2 = a *b 
    print(f"obvod obdelníka je {výsledek1} a obsah obdelníka je {výsledek2}")
else:
    print("tak ty jis kokot!!!")