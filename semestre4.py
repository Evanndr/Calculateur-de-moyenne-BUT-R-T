# semestre4.py - Calcul des moyennes par UE du Semestre 4

def calculer():
    print("=== SEMESTRE 4 ===")
    
    # Saisie des notes des Ressources et SAÉ
    r401 = float(input("Note R401 - Infrastructures de sécurité : "))
    r402 = float(input("Note R402 - Transmissions avancées : "))
    r403 = float(input("Note R403 - Physique des Télécoms : "))
    r404 = float(input("Note R404 - Réseaux cellulaires : "))
    r405 = float(input("Note R405 - Automatisation des tâches d'administration : "))
    r406 = float(input("Note R406 - Anglais professionnel 2 : "))
    r407 = float(input("Note R407 - Communication : "))
    r408 = float(input("Note R408 - Projet Personnel et Professionnel : "))
    r409 = float(input("Note R409 - Fondamentaux de la conteneurisation : "))
    r410 = float(input("Note R410 - Développement de microservices : "))
    
    sae41 = float(input("Note SAE41 - Développer-Déployer un microservice env. virtualisé : "))
    sae42 = float(input("Note SAE42 - Portfolio : "))
    sae43 = float(input("Note SAE43 - Stage : "))

    # Calcul des moyennes par UE
    ue1 = (r401*8 + r406*4 + r407*4 + r408*2 + sae42*2 + sae43*25) / 45
    ue2 = (r401*7 + r402*11 + r403*12 + r404*13 + r406*2 + r407*3 + r408*1 + sae42*7 + sae43*27) / 83
    ue3 = (r405*14 + r406*2 + r407*3 + r408*1 + sae42*4 + sae43*25) / 49
    ue4 = (r409*9 + sae41*30 + sae42*4 + sae43*12) / 55
    ue5 = (r409*3 + r410*18 + sae41*31 + sae42*4 + sae43*12) / 68

    # Affichage des résultats
    print("\n--- Résultats Semestre 4 ---")
    print("Moyenne UE 1 :", round(ue1, 2), "/ 20")
    print("Moyenne UE 2 :", round(ue2, 2), "/ 20")
    print("Moyenne UE 3 :", round(ue3, 2), "/ 20")
    print("Moyenne UE 4 :", round(ue4, 2), "/ 20")
    print("Moyenne UE 5 :", round(ue5, 2), "/ 20")

if __name__ == "__main__":
    calculer()
