#!/bin/bash

# Remplacement des espaces par des underscores dans les noms de fichier dans le dossier courant et sous-dossiers
find . -type f -name "* *" -exec bash -c 'mv "$0" "${0// /_}"' {} \;


