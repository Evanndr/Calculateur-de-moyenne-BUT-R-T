# semestre5.py - Calcul des moyennes par UE du Semestre 5

def calculer():
    print("=== SEMESTRE 5 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r501 = float(input("Note R501 - Wi-Fi avancé : "))
    r502 = float(input("Note R502 - Supervision des réseaux : "))
    r503 = float(input("Note R503 - Ingénierie de systèmes télécoms : "))
    r504 = float(input("Note R504 - Cycle de vie d'un projet informatique : "))
    r505 = float(input("Note R505 - Anglais: insertion professionnelle 1 : "))
    r506 = float(input("Note R506 - Communication : "))
    r507 = float(input("Note R507 - Projet Personnel et Professionnel : "))
    r508 = float(input("Note R508 - Gestion de projet 3 : "))
    r509 = float(input("Note R509 - Outils et méthodes du DevOps : "))
    r510 = float(input("Note R510 - Infrastructures conteneurisées : "))
    r511 = float(input("Note R511 - Programmer son infrastructure : "))
    r512 = float(input("Note R512 - Solutions Cloud : "))
    
    sae51 = float(input("Note SAE51 - Concevoir réaliser présenter une solution technique : "))
    sae52 = float(input("Note SAE52 - Piloter un projet informatique : "))
    sae53 = float(input("Note SAE53 - Orchestrer la conteneurisation d'une application : "))
    sae54 = float(input("Note SAE54 - Portfolio : "))

    # Calcul des moyennes par UE
    ue1 = (r501*5 + r502*5 + r503*8 + r504*3 + r505*5 + r506*8 + r507*2 + r508*5 + sae51*18 + sae52*6 + sae54*4) / 69
    ue2 = (r501*9 + r503*7 + r505*2 + r506*2 + r507*2 + r508*2 + sae51*15 + sae52*1 + sae54*4) / 44
    ue3 = (r502*10 + r504*3 + r505*5 + r506*8 + r507*2 + r508*2 + sae51*17 + sae52*8 + sae54*4) / 59
    ue4 = (r510*18 + r511*14 + r512*17 + sae53*30 + sae54*4) / 83
    ue5 = (r509*18 + r511*5 + sae53*18 + sae54*4) / 45

    # Affichage des résultats
    print("\n--- Résultats Semestre 5 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")
    print("Moyenne UE 4 :", round(ue4, 2), "/ 20")
    print("Moyenne UE 5 :", round(ue5, 2), "/ 20")

if __name__ == "__main__":
    calculer()
