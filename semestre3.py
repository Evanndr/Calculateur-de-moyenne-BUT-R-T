# semestre3.py - Calcul des moyennes par UE du Semestre 3

def calculer():
    print("=== SEMESTRE 3 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r301 = float(input("Note R301 - Réseaux de campus : "))
    r302 = float(input("Note R302 - Réseaux opérateurs : "))
    r303 = float(input("Note R303 - Services réseaux avancés : "))
    r304 = float(input("Note R304 - Services d'annuaires : "))
    r305 = float(input("Note R305 - Chaînes de transmissions numériques : "))
    r306 = float(input("Note R306 - Fibres optiques et propagation : "))
    r307 = float(input("Note R307 - Réseaux d'accès : "))
    r308 = float(input("Note R308 - Consolidation de la programmation : "))
    r309 = float(input("Note R309 - Programmation événementielle : "))
    r310 = float(input("Note R310 - Gestion d'un système de bases de données : "))
    r311 = float(input("Note R311 - Anglais professionnel 1 : "))
    r312 = float(input("Note R312 - Communication : "))
    r313 = float(input("Note R313 - Projet Personnel et Professionnel : "))
    r314 = float(input("Note R314 - Analyse de Fourier : "))
    r315 = float(input("Note R315 - Gestion de projet 2 : "))
    r316 = float(input("Note R316 - Ecosystème Cloud : "))
    r317 = float(input("Note R317 - Virtualisation avancée : "))
    
    sae31 = float(input("Note SAE31 - Mettre en œuvre un système de transmission : "))
    sae32 = float(input("Note SAE32 - Développer des applications communicantes : "))
    sae33 = float(input("Note SAE33 - Concevoir un réseau multisites et services vir : "))
    sae34 = float(input("Note SAE34 - Mettre en place une infrastructure virtualisée : "))
    sae35 = float(input("Note SAE35 - Portfolio : "))

    # Calcul des moyennes par UE
    ue1 = (r301*8 + r302*5 + r303*8 + r304*4 + r311*4 + r312*4 + r313*2 + r315*2 + sae32*4 + sae33*17 + sae35*5) / 63
    ue2 = (r301*4 + r302*6 + r305*17 + r306*9 + r307*9 + r310*2 + r311*3 + r312*4 + r313*1 + r314*10 + r315*2 + sae31*25 + sae32*9 + sae33*7 + sae35*5) / 113
    ue3 = (r308*10 + r309*6 + r310*2 + r311*3 + r312*3 + r313*1 + r315*1 + sae32*14 + sae35*4) / 44
    ue4 = (r316*7 + r317*22 + sae33*12 + sae34*18 + sae35*2) / 61
    ue5 = (sae33*11 + sae34*6 + sae35*2) / 19

    # Affichage des résultats
    print("\n--- Résultats Semestre 3 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")
    print("Moyenne UE 4 :", round(ue4, 2), "/ 20")
    print("Moyenne UE 5 :", round(ue5, 2), "/ 20")

if __name__ == "__main__":
    calculer()
