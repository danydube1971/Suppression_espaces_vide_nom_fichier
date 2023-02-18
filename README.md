# Suppression_espaces_vide_nom_fichier

Ce script Bash (et python 3) pour Linux renomme tous les fichiers dans le dossier courant et les sous-dossiers en remplaçant les espaces par des underscores. 

Voici ce que fait chaque ligne du script :

1. La première ligne déclare que le script doit être exécuté dans l'interpréteur de commande Bash.
2. La deuxième ligne utilise la commande "find" pour trouver tous les fichiers (et non pas les dossiers) 
dans le répertoire courant et les sous-dossiers qui ont un nom contenant des espaces. Ces fichiers sont stockés dans la variable "find".
3. La troisième ligne utilise la commande "exec" pour exécuter une commande Bash sur chaque fichier trouvé par la commande "find". 
La commande Bash renomme chaque fichier en remplaçant les espaces par des underscores en utilisant la commande "mv".
4. La commande "bash -c" est utilisée pour permettre l'utilisation de la substitution de variable. 
La variable "$0" fait référence à chaque fichier trouvé par la commande "find".
5. La commande "${0// /_}" remplace tous les espaces dans le nom du fichier par des underscores.
6. La commande "{} ;" est utilisée pour indiquer que la commande doit être exécutée pour chaque fichier trouvé.

En résumé, ce script permet de renommer tous les fichiers dans le dossier courant et les sous-dossiers en remplaçant les espaces 
par des underscores pour faciliter leur manipulation par la suite.

