# Projet Cyber Sécurité 
# Script Python pour décompresser une archive sécurisée par mot de passe :
## Deux types d'attaques : 
#### Attaque par dictionnaire
#### Attaque par force brute 

## Objectif : 

L’objectif de ce projet est de décompresser deux archives (l'une dans l'autre). La première est à décompresser avec  "Attaque par dictionnaire" et la seconde archive est à décompresser avec "Attaque par force brute". 

## L'Attaque par dictionnaire : 

Pour que l'attaque par dictionnaire fonctionne, il est nécessaire de télécharger le fichier 
[rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) disponible directement en cliquant sur le lien hypertexte. 
Le fichier txt est à placer au sein du répertoire de ce projet GitHub.
L'attaque par dictionnaire utilise tous les mots présents dans la liste rockyou.txt. 
Dès que le mot est trouvé, il est print dans la console et le temps nécessaire pour trouver le mot pour effectuer la décompression est affichée. 

## L'Attaque par force brute :  

L'attaque par force brute utilise tous les caractères possible pour essayer de "cracker" l'archive. Ainsi il va utiliser tous les caractères possibles dans un mot de passe d'archive (y compris le caractère espace). L'algorithme commence à deux caractères. Dès que le mot est trouvé, il est print dans la console et le temps nécessaire pour trouver le mot pour effectuer la décompression est affichée. 

## Utilisation 

```
python UnzipCrack.py
```
Suivre ensuite les indications directement sur le terminal. 

# Exemple de la sortie console : 

![alt text](https://ibb.co/QnmvC1k)


