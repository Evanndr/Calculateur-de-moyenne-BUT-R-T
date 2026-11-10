# main.py - Fichier principal avec menu Inquirer

import semestre1
import semestre2
import semestre3
import semestre4
import semestre5
import semestre6
import sys
import inquirer



print("   CALCULATEUR DE MOYENNES PAR SEMESTRE   ")
questions = [
    inquirer.List(
        'semestre',
        message="Quel semestre voulez-vous calculer ?",
        choices=[
            'Semestre 1', 
            'Semestre 2', 
            'Semestre 3', 
            'Semestre 4', 
            'Semestre 5', 
            'Semestre 6',
            'Quitter'
        ]
    )
]
answers = inquirer.prompt(questions)
if answers:
    choix = answers['semestre']
    
    if choix == 'Semestre 1':
        semestre1.calculer()
    elif choix == 'Semestre 2':
        semestre2.calculer()
    elif choix == 'Semestre 3':
        semestre3.calculer()
    elif choix == 'Semestre 4':
        semestre4.calculer()
    elif choix == 'Semestre 5':
        semestre5.calculer()
    elif choix == 'Semestre 6':
        semestre6.calculer()
    elif choix == 'Quitter':
        print("Fermeture du programme. À bientôt !")

