
# ==========================================
# LAB 7 : LES FONCTIONS EN PYTHON
# ==========================================

# Étape 1 : Créer une fonction et l'appeler

def saluer():
    print("Bonjour depuis une fonction !")
    print("Ravi de te voir !")

saluer()
saluer()


# Étape 2 : Utiliser des paramètres

def bonjour(prenom):
    print(f"Salut {prenom} !")

bonjour("Alice")
bonjour("Mohamed")


def presentation(nom, age):
    print(f"Je m'appelle {nom} et j'ai {age} ans.")

presentation("Ikram", 20)
presentation("Sara", 22)


# Étape 3 : Retourner un résultat avec return

def additionner(a, b):
    total = a + b
    return total

resultat = additionner(3, 5)
print("Résultat :", resultat)
print("Type :", type(additionner(3, 5)))


# Étape 4 : Paramètres optionnels et arguments nommés

def calcul_ttc(prix_ht, taux=0.2):
    prix_ttc = prix_ht * (1 + taux)
    return prix_ttc

print("Prix TTC :", calcul_ttc(100))
print("Prix TTC :", calcul_ttc(100, 0.055))
print("Prix TTC :", calcul_ttc(prix_ht=50, taux=0.1))


def afficher_message(message, prefix="[INFO]"):
    print(f"{prefix} {message}")

afficher_message("Programme démarré")
afficher_message("Erreur détectée", prefix="[ERREUR]")


# Étape 5 : Nombre variable d'arguments (*args)

def somme(*args):
    total = 0
    for valeur in args:
        total += valeur
    return total

print("Somme :", somme(1, 2))
print("Somme :", somme(1, 2, 3, 4))


def produit(*args):
    resultat = 1
    for valeur in args:
        resultat *= valeur
    return resultat

print("Produit :", produit(2, 3, 4))
print("Produit vide :", produit())


# Étape 6 : Variables locales et globales

def test_locale():
    message = "Je suis locale"
    print(message)

test_locale()

compteur = 0

def incrementer():
    global compteur
    compteur += 1

incrementer()
incrementer()

print("Compteur :", compteur)


# Bonne pratique : utiliser return

def incrementer_valeur(valeur):
    return valeur + 1

compteur = 0
compteur = incrementer_valeur(compteur)
print("Compteur après incrémentation :", compteur)


# Étape 7 : Mini-projet : gestion des notes

def moyenne(notes):
    """Calcule la moyenne d'une liste de notes."""
    if not notes:
        return 0
    return sum(notes) / len(notes)


def appliquer_bonus(notes, bonus=1):
    """Ajoute un bonus sans dépasser 20."""
    return [min(note + bonus, 20) for note in notes]


def filtrer_notes(notes, seuil):
    """Conserve les notes supérieures ou égales au seuil."""
    return [note for note in notes if note >= seuil]


def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    """Génère un rapport contenant les informations principales."""

    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes >= {seuil} : {notes_valides}",
        f"Nombre de notes valides : {len(notes_valides)}"
    ]

    return "\n".join(lignes)


# Étape 8 : Exercices supplémentaires

def min_max(notes):
    """Retourne la note minimale et maximale."""
    if not notes:
        return None
    return min(notes), max(notes)


def normaliser(notes, sur=20):
    """Convertit les notes sur une échelle de 20."""
    if not notes:
        return []

    maximum = max(notes)

    if maximum == 0:
        return [0 for note in notes]

    return [(note / maximum) * sur for note in notes]


# Programme principal

if __name__ == "__main__":

    notes = [12, 9, 15, 8, 17, 13, 19, 10]

    print("\n", rapport(notes))

    print("\n", rapport(
        notes,
        bonus=2,
        seuil=14,
        titre="Rapport avancé"
    ))

    print("\nMinimum et maximum :", min_max(notes))

    print("\nNotes normalisées :", normaliser(notes, sur=20))

    # Sauvegarder le rapport dans un fichier
    with open("rapport_notes.txt", "w", encoding="utf-8") as fichier:
        fichier.write(rapport(notes))

    print("\nRapport sauvegardé dans rapport_notes.txt")
