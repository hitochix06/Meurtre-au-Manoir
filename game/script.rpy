### Menu principal ###

# Définition des personnages
define detective = Character("Détective", color="#c8ffc8")
define eloise = Character("Éloïse Marceau", color="#D36E70")
define antoine = Character("Antoine Durand", color="#D39056")
define victor = Character("Victor Delmas", color="#7CBD74")
define clara = Character("Clara Duvivier", color="#9B59B6")
define charles = Character("Charles Beaumont", color="#34495E")
define madeleine = Character("Madeleine Rousseau", color="#E67E22")

init python:
    # Variables pour suivre les indices découverts
    indices_decouverts = {
        "salon": [],
        "bureau": [],
        "cuisine": [],
        "jardin": [],
        "bibliotheque": [],
        "cave": []
    }

# Le jeu commence ici.
label start:
    scene salon_meurtre with fade
    "Le corps d'Hugo Marceau, riche propriétaire du manoir, a été découvert ce matin dans le salon."
    "En tant que détective privé, vous devez résoudre ce mystère."
    
    jump menu_principal

# Menu principal des actions
label menu_principal:
    menu:
        "Que souhaitez-vous faire ?"
        
        "Voir en réalité augmentée":
            call scanner_qr_aero
        
        "Interroger les suspects":
            call interroger
        
        "Accuser un suspect":
            call menu_accusation
        
        "Quitter":
            return

# Consultation des notes
label consulter_notes:
    "Vos notes sur l'enquête :"
    python:
        for piece, indices in indices_decouverts.items():
            if indices:
                renpy.say("", "\nDans " + piece + " :")
                for indice in indices:
                    renpy.say("", "- " + indice)
    menu:
        "Retour au menu principal":
            jump menu_principal 