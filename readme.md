# Calculateur de Moyennes par Semestre

Ce projet est un outil en ligne de commande développé en Python. Il permet de calculer facilement vos moyennes par UE pour chaque semestre, en appliquant les coefficients associés à chaque Ressource et SAÉ.

## Structure du projet

Le projet est composé des fichiers suivants :

- `main.py` : Le script principal qui lance le menu interactif.
- `semestre1.py` à `semestre6.py` : Les scripts contenant les coefficients et les calculs spécifiques pour chaque semestre.

## Prérequis

Pour utiliser ce programme, vous devez avoir **Python 3** installé sur votre machine.

Le projet utilise également la bibliothèque tierce `inquirer` pour générer le menu interactif de sélection du semestre.

### Installation de la bibliothèque requise

Ouvrez votre terminal (ou invite de commande) et exécutez la commande suivante :

```bash
pip install inquirer
```

## Comment l'utiliser ?

1. Récuperez et décompressez l'archive.
2. Ouvrez votre terminal dans le dossier décompressé.
3. Lancez le programme avec la commande :

```bash
python main.py
```

4. Utilisez les **flèches directionnelles** (Haut/Bas) de votre clavier pour choisir le semestre que vous souhaitez calculer, puis appuyez sur **Entrée**.
5. Saisissez vos notes une par une lorsqu'elles vous sont demandées. 
   
> ** Important :** Si vous avez des notes avec des décimales, veillez à **utiliser un point (`.`) et non une virgule (`,`)** (par exemple : `14.5` au lieu de `14,5`).

## Résultats

Une fois toutes les notes saisies, le programme calculera et affichera automatiquement votre moyenne sur 20 pour chaque Unité d'Enseignement du semestre sélectionné.