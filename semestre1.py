# semestre1.py - Calcul des moyennes par UE du Semestre 1

def calculer():
    print("=== SEMESTRE 1 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r101 = float(input("Note R101 - Initiation aux réseaux informatiques : "))
    r102 = float(input("Note R102 - Principes et architecture des réseaux : "))
    r103 = float(input("Note R103 - Réseaux locaux et équipements actifs : "))
    r104 = float(input("Note R104 - Fondamentaux des systèmes électroniques : "))
    r105 = float(input("Note R105 - Supports de transmission pour les réseaux : "))
    r106 = float(input("Note R106 - Architecture des systèmes numériques et informatiques : "))
    r107 = float(input("Note R107 - Fondamentaux de la programmation : "))
    r108 = float(input("Note R108 - Bases des systèmes d'exploitation : "))
    r109 = float(input("Note R109 - Introduction aux technologies web : "))
    r110 = float(input("Note R110 - Anglais technique 1 : "))
    r111 = float(input("Note R111 - Communication : "))
    r112 = float(input("Note R112 - Projet personnel et professionnel : "))
    r113 = float(input("Note R113 - Mathématiques du signal : "))
    r114 = float(input("Note R114 - Mathématiques des transmissions : "))
    r115 = float(input("Note R115 - Gestion de projet : "))
    
    sae11 = float(input("Note SAE11 - Hygiène informatique et cybersécurité : "))
    sae12 = float(input("Note SAE12 - Initiation aux réseaux informatiques : "))
    sae13 = float(input("Note SAE13 - Découvrir un dispositif de transmission : "))
    sae14 = float(input("Note SAE14 - Se présenter sur Internet : "))
    sae15 = float(input("Note SAE15 - Traiter des données : "))
    sae16 = float(input("Note SAE16 - Portfolio : "))

    # Calcul des moyennes par UE (somme des notes * coefficients / somme des coefficients)
    ue1 = (r101*10 + r102*10 + r103*7 + r104*7 + r106*5 + r108*6 + r110*5 + r111*4 + r112*2 + r113*5 + r114*5 + sae11*20 + sae12*20 + sae16*7) / 113
    ue2 = (r101*4 + r103*2 + r104*8 + r105*6 + r110*5 + r111*5 + r112*2 + r113*9 + r114*9 + r115*3 + sae13*29 + sae16*7) / 89
    ue3 = (r101*4 + r103*2 + r106*5 + r107*15 + r108*6 + r109*4 + r110*5 + r111*5 + r112*2 + r115*3 + sae14*20 + sae15*20 + sae16*7) / 98

    # Affichage des résultats
    print("\n--- Résultats Semestre 1 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")

if __name__ == "__main__":
    calculer()
