import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Fonction pour calculer et afficher le prix du café sélectionné
def choisir():
    choix = selection.get()
    if choix == "Espresso":
        prix = 1.50
    elif choix == "Latte":
        prix = 2.20
    elif choix == "Cappuccino":
        prix = 2.50
    elif choix == "Americano":
        prix = 2.50
    elif choix == "Irish Coffee":
        prix = 2.80
    elif choix == "Espresso Macchiato":
        prix = 2.75   
    elif choix == "Mocha":
        prix = 3.20   
    else:
        prix = 0.00
    
    #messagebox.showinfo("Commande", f"Merci ! Vous avez choisi {choix} Payer svp: {prix} €")
    #messagebox.showwarning("Commande", f"Merci ! Vous avez choisi {choix} Payer svp: {prix} €")
    if messagebox.showinfo("Commande", f"Vous avez choisi {choix}. Prix: {prix} €"):
        # démarrer l'animation si ok
        lancer_animation()

# Fonction pour lancer une animation de "chargement"
def lancer_animation():
    # Créer une nouvelle fenêtre de type "sablier"
    sablier = tk.Toplevel(fenetre)
    sablier.title("Commande en cours")
    sablier.geometry("200x100")
    sablier_label = tk.Label(sablier, text="Préparation en cours...")
    sablier_label.pack(pady=10)
    
    sablier_icon = tk.Label(sablier, text="⌛", font=("Arial", 40))
    sablier_icon.pack()

    # Fonction pour changer de couleur toutes les 100 ms
    def alterner_couleur():
        current_color = sablier_icon.cget("foreground")
        new_color = "black" if current_color == "blue" else "blue"
        sablier_icon.config(foreground=new_color)
        # Replanifier cette fonction toutes les 100 ms
        sablier.after(100, alterner_couleur)
    
    # Démarrer l'animation de changement de couleur
    alterner_couleur()
    
    # Fermer la fenêtre après 3 secondes
    fenetre.after(3000, sablier.destroy)


# fenêtre principale
fenetre = tk.Tk()
fenetre.title(":: Coffee Distributor ::")
fenetre.geometry("500x500")
fenetre['bg'] = 'PeachPuff2'

# Intégrer une image cafe
#photo = PhotoImage(file="/Users/ridabelaqziz/Desktop/Revision/projetCafe/cafe.png")
#canvas = Canvas(fenetre,width=450, height=200)
#canvas.create_image(0, 0, anchor="nw", image=photo)
#canvas.pack(pady=10)


# Label 
label = tk.Label(fenetre, text="Veuillez choisir votre café !", font=("Verdana", 14,"bold "))
label.pack(pady=10)

# choix de café
selection = tk.StringVar()
selection.set("Espresso")  # par défaut

# Options de café
options = ["Espresso", "Latte", "Cappuccino","Americano" ,"Irish Coffee" , "Espresso Macchiato","Mocha" ]
for option in options:
    bouton = tk.Radiobutton(fenetre, text=option, variable=selection, value=option)
    bouton.pack(anchor="w")







# Bouton pour choisir
bouton_choisir = tk.Button(fenetre, text="Choisir", command=choisir)
bouton_choisir.pack(pady=20)

# Boucle principale (boucle infinie)
fenetre.mainloop()