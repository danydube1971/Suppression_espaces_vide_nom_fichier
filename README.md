# Suppression_espaces_vide_nom_fichier

Ce code va parcourir tous les fichiers dans le dossier courant et les sous-dossiers, et pour chaque fichier, il va remplacer les caractères spéciaux par leurs équivalents sans accent en utilisant la fonction **unidecode()**, puis remplacer les espaces par des barres de soulignement en utilisant la fonction **replace()**. Si le nom du fichier est modifié, il sera renommé avec le nouveau nom en utilisant la fonction **os.rename()**.

**Comment utiliser le script**

1. Placez-y le script au même emplacement que les fichiers à renommer.
2. Exécuter le script dans un terminal Linux: **python3 "Suppression_des_espaces_vides_V2.py"**
