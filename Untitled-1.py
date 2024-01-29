print("Vyberte si vozoreček na obdelník/kvádr (byerte číslici)")
funkce1 = True








while funkce1 == True:
    print("1. Obsah")
    print("2. Objem")
    print("3. obvod")
    print("4. Konec programu")
    výběr = int(input("Váě výběr: "))
    
    if výběr == 1:
     a = int(input("Zvolte neznámou a: "))
     b = int(input("Zvolte neznámou b: "))
     if a >0 and b >0:   
      výsledek1 = (a * b)*2 
      výsledek2 = a *b 
      print(f"obvod obdelníka je {výsledek1}")
    
    
    
    elif výběr == 2 :
         a = int(input("Zvolte neznámou a: "))
         b = int(input("Zvolte neznámou b: "))
         c = int(input("Zvolte neznámou b: "))
         if a >0 and b >0 and c >0:   
          výpočet4 = a * b * c
          print(f"Objem kvádru je {výpočet4} ")
    elif výběr == 3:
     a = int(input("Zvolte neznámou a: "))
     b = int(input("Zvolte neznámou b: "))
     if a >0 and b >0:   
            print(f"obsah obdelníka je {výsledek2}")
    elif výběr == 4: 
       funkce1 = False
    
    else:
        print("Špatný výběr!!")
