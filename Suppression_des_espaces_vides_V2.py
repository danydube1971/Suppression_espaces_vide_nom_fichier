"""Ce code va parcourir tous les fichiers dans le dossier courant et les sous-dossiers, et pour chaque fichier, il va remplacer les caractères spéciaux par leurs équivalents sans accent en utilisant la fonction unidecode(), puis remplacer les espaces par des barres de soulignement en utilisant la fonction replace(). Si le nom du fichier est modifié, il sera renommé avec le nouveau nom en utilisant la fonction os.rename()."""

import os
from unidecode import unidecode

# Remplacement des caractères spéciaux et des espaces par des barres de soulignement dans les noms de fichier
for root, dirs, files in os.walk('.'):
    for file in files:
        new_file = unidecode(file).replace(' ', '_')
        if file != new_file:
            os.rename(os.path.join(root, file), os.path.join(root, new_file))

