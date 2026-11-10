# semestre6.py - Calcul des moyennes par UE du Semestre 6

def calculer():
    print("=== SEMESTRE 6 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r601 = float(input("Note R601 - Anglais: insertion professionnelle 2 : "))
    r602 = float(input("Note R602 - Communication : "))
    r603 = float(input("Note R603 - Connaissance de l'entreprise : "))
    r604 = float(input("Note R604 - Pilotage de solutions cloud pour l'entreprise : "))
    
    sae61 = float(input("Note SAE61 - Gérer le pipeline d'une application orientée cloud : "))
    sae62 = float(input("Note SAE62 - Portfolio : "))
    sae63 = float(input("Note SAE63 - Stage : "))

    # Calcul des moyennes par UE
    ue1 = (r601*6 + r602*8 + r603*6 + sae62*4 + sae63*20) / 44
    ue2 = (r601*6 + r602*8 + r603*6 + sae62*4 + sae63*20) / 44
    ue3 = (r601*6 + r602*8 + r603*6 + sae62*4 + sae63*20) / 44
    ue4 = (r604*60 + sae61*26 + sae62*4 + sae63*20) / 110
    ue5 = (sae61*34 + sae62*4 + sae63*20) / 58

    # Affichage des résultats
    print("\n--- Résultats Semestre 6 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")
    print("Moyenne UE 4 :", round(ue4, 2), "/ 20")
    print("Moyenne UE 5 :", round(ue5, 2), "/ 20")

if __name__ == "__main__":
    calculer()
