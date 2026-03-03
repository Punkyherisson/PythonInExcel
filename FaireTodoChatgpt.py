import pandas as pd

# Création de la To-Do List
data = [
    [1, "Lire un fichier Excel avec pandas", "Apprentissage", "Haute", "En cours", "2025-10-09", "Tester avec read_excel()"],
    [2, "Écrire un DataFrame dans Excel", "Apprentissage", "Moyenne", "À faire", "2025-10-10", "Utiliser to_excel()"],
    [3, "Créer un rapport de ventes Excel formaté", "Projet", "Haute", "À faire", "2025-10-15", "Utiliser openpyxl"],
    [4, "Automatiser un graphique Excel", "Projet", "Moyenne", "À faire", "2025-10-18", "Tester xlsxwriter"],
    [5, "Lier Excel ↔ Python en direct", "Avancé", "Basse", "À faire", "2025-10-25", "Utiliser xlwings"]
]

columns = ["ID", "Tâche", "Catégorie", "Priorité", "État", "Date limite", "Commentaire"]
df = pd.DataFrame(data, columns=columns)

# Sauvegarde dans un fichier Excel
file_path = "/mnt/data/todo_python_excel.xlsx"
df.to_excel(file_path, index=False)

file_path
