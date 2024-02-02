import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localHost",
    user="root",
    password="Nninjah",
    database="store"
)
cursor = conn.cursor()

# Fonctions pour interagir avec la base de données
def fetch_products():
    cursor.execute("SELECT * FROM product")
    return cursor.fetchall()

def add_product(name, description, price, quantity, category):
    cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (name, description, price, quantity, category))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    conn.commit()

# Interface graphique
class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")

        # Tableau de bord
        self.tree = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"))
        self.tree.heading("#0", text="")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Quantité", text="Quantité")
        self.tree.heading("Catégorie", text="Catégorie")

        # Ajouter des données à la table
        products = fetch_products()
        for product in products:
            self.tree.insert("", "end", values=product)

        # Boutons d'action
        self.add_button = tk.Button(root, text="Ajouter Produit", command=self.add_product)
        self.delete_button = tk.Button(root, text="Supprimer Produit", command=self.delete_product)

        # Placement des éléments
        self.tree.pack(pady=10)
        self.add_button.pack(pady=5)
        self.delete_button.pack(pady=5)

    def add_product(self):
        # Fonction pour ajouter un produit
        # Implémentez cette fonction selon vos besoins
        pass

    def delete_product(self):
        # Fonction pour supprimer un produit
        # Implémentez cette fonction selon vos besoins
        pass

# Exécution de l'application
root = tk.Tk()
app = StockManagementApp(root)
root.mainloop()
