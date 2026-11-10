# semestre2.py - Calcul des moyennes par UE du Semestre 2

def calculer():
    print("=== SEMESTRE 2 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r201 = float(input("Note R201 - Technologies de l'Internet : "))
    r202 = float(input("Note R202 - Admin système et fondamentaux de la virtualisation : "))
    r203 = float(input("Note R203 - Bases des services réseaux : "))
    r204 = float(input("Note R204 - Initiation à la téléphonie d'entreprise : "))
    r205 = float(input("Note R205 - Signaux et systèmes pour les transmissions : "))
    r206 = float(input("Note R206 - Numérisation de l'information : "))
    r207 = float(input("Note R207 - Sources de données : "))
    r208 = float(input("Note R208 - Analyse et traitement de données structurées : "))
    r209 = float(input("Note R209 - Initiation au développement web : "))
    r210 = float(input("Note R210 - Anglais technique 2 : "))
    r211 = float(input("Note R211 - Communication : "))
    r212 = float(input("Note R212 - Projet Personnel et Professionnel : "))
    r213 = float(input("Note R213 - Mathématiques des systèmes numériques : "))
    r214 = float(input("Note R214 - Analyse mathématique des signaux : "))
    
    sae21 = float(input("Note SAE21 - Construire un réseau pour une TPE : "))
    sae22 = float(input("Note SAE22 - Mesurer et caractériser un signal ou un système : "))
    sae23 = float(input("Note SAE23 - Mettre en place une solution info d'entreprise : "))
    sae24 = float(input("Note SAE24 - Projet intégratif : "))
    sae25 = float(input("Note SAE25 - Portfolio : "))

    # Calcul des moyennes par UE
    ue1 = (r201*13 + r202*9 + r203*11 + r204*7 + r205*5 + r206*3 + r207*1 + r209*3 + r210*10 + r211*5 + r212*2 + r213*2 + r214*2 + sae21*24 + sae24*19 + sae25*7) / 123
    ue2 = (r201*5 + r204*3 + r205*9 + r206*7 + r210*4 + r211*4 + r212*2 + r213*4 + r214*8 + sae22*20 + sae24*13 + sae25*5) / 84
    ue3 = (r201*5 + r202*4 + r204*4 + r207*7 + r208*7 + r209*8 + r210*4 + r211*4 + r212*4 + r213*6 + sae23*20 + sae24*14 + sae25*6) / 93

    # Affichage des résultats
    print("\n--- Résultats Semestre 2 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")

if __name__ == "__main__":
    calculer()
