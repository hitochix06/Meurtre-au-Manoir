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
        
        "Examiner la scène du crime":
            call inspecter_scene_meurtre
        
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

# Scène de crime (alternative au label examiner_scene_crime en conflit)
label inspecter_scene_meurtre:
    scene salon_meurtre with fade
    
    menu:
        "Que souhaitez-vous examiner ?"
        
        "Le corps" if "corps" not in indices_decouverts["salon"]:
            "Le corps présente une blessure par arme à feu. La mort remonte à environ 22h."
            $ indices_decouverts["salon"].append("corps")
        
        "Les alentours" if "note" not in indices_decouverts["salon"]:
            "Vous trouvez une note froissée près du corps."
            $ indices_decouverts["salon"].append("note")
        
        "Les traces" if "traces" not in indices_decouverts["salon"]:
            "Des traces de pas mènent vers la fenêtre du salon."
            $ indices_decouverts["salon"].append("traces")
        
        "Quitter":
            jump menu_principal
    
    jump inspecter_scene_meurtre 