import os

# Remplacement des espaces par des underscores dans les noms de fichier dans le dossier courant et sous-dossiers
for root, dirs, files in os.walk('.'):
    for file in files:
        if ' ' in file:
            os.rename(os.path.join(root, file), os.path.join(root, file.replace(' ', '_')))

