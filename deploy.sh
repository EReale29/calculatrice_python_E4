#!/bin/bash

echo "Préparation du déploiement (GitHub)..."

# 1. Créer un dossier de distribution local
DIST_DIR="dist"
mkdir -p "$DIST_DIR"

# 2. Copier les fichiers nécessaires
echo "Copie des fichiers vers $DIST_DIR"
cp calculatrice.py "$DIST_DIR/"
cp test_main.py "$DIST_DIR/"
cp README.md "$DIST_DIR/" 2>/dev/null || true

# 3. Lancer les tests dans le dossier distribué
cd "$DIST_DIR"
echo "Lancement des tests dans dist/"
python3 -m unittest test_main.py

# 4. Emballer tout dans une archive zip
cd ..
ZIP_NAME="calculatrice_build.zip"
zip -r "$ZIP_NAME" "$DIST_DIR"

echo "Déploiement terminé. Archive créée : $ZIP_NAME"