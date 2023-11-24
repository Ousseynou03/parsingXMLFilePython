#!/bin/bash

# Exécuter le script Python
"/usr/local/bin/python3" "/Users/mac/Desktop/QA Testing/script test Python/parsingXML/test3.py"

# Vérifier le code de sortie du script Python
if [ $? -eq 0 ]; then
    # Le script Python s'est terminé avec succès
    echo "Le script Python s'est terminé avec succès. Arrêt du script shell."
else
    # Le script Python a rencontré une erreur
    echo "Le script Python a rencontré une erreur. Continuation du script shell."
fi
