### Menu principal ###

# Définition des images
# Images des lieux
image salon = "images/lieux/salon.png"
image bibliotheque = "images/lieux/bibliotheque.png"
image salon_meurtre = "images/salon_meurtre.png"
image cuisine = "images/lieux/cusine.png"
image cave = "images/lieux/cave.png"
image manoir = "images/lieux/manoir.png"
image bureau = "images/lieux/bureau.png"
image jardin = "images/lieux/jardin.png"


# Images des personnages
image madeleine = "images/personnage/madeleine.png"
image eloise = "images/personnage/eloise.png"
image antoine = "images/personnage/antoine.png"
image victor = "images/personnage/victor.png"
image clara = "images/personnage/clara.png"
image charles = "images/personnage/charles.png"

# Définition des sons
define audio.salon_ambiance = "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3"

# Définition des personnages
define detective = Character("Inspecteur", color="#2980b9")
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
    # Variable pour suivre si des interrogatoires ont été effectués
    interrogatoires_effectues = False
    
    # Localisation des personnages
    localisation_personnages = {
        "salon": ["Antoine"],
        "cuisine": ["Eloise"],
        "bureau": ["Clara"],
        "jardin": ["Victor"],
        "bibliotheque": ["Madeleine"],
        "cave": ["Charles"]
    }

    # Variables pour suivre les notes sur les suspects
    suspect_notes = {
        "Eloise": {"alibi": False, "mobile": False, "preuve": False},
        "Antoine": {"alibi": False, "mobile": False, "preuve": False},
        "Victor": {"alibi": False, "mobile": False, "preuve": False},
        "Clara": {"alibi": False, "mobile": False, "preuve": False},
        "Charles": {"alibi": False, "mobile": False, "preuve": False},
        "Madeleine": {"alibi": False, "mobile": False, "preuve": False}
    }

# Le jeu commence ici.
label start:
    jump introduction

# Introduction du jeu
label introduction:
    scene black with fade
    play music "audio/ambiance_mystere.mp3" fadein 2.0
    scene manoir with dissolve
    "Une nuit au manoir Beaumont."
    "Le prestigieux détective Hugo Delacourt est retrouvé mort dans le salon, tué d'une balle en plein cœur."
    "Sur la table, six objets sont soigneusement disposés, chacun lié aux convives présents ce soir-là."
    "Tous avaient un mobile."
    "Mais un seul a appuyé sur la détente."
    "Vous incarnez l'inspecteur Jouvet."
    "Votre objectif : comprendre qui a tué Hugo, pourquoi... et comment."
    scene black with fade
    stop music fadeout 2.0
    scene salon_meurtre with fade
    play music salon_ambiance fadein 2.0
    "Le corps d'Hugo Marceau, riche propriétaire du manoir, a été découvert ce matin dans le salon."
    "En tant que détective privé, vous devez résoudre ce mystère."
    
    jump menu_principal

# Menu principal des actions
label menu_principal:
    menu:
        "Que souhaitez-vous faire ?"
        
        "Interroger les suspects":
            $ interrogatoires_effectues = True
            call interroger
        
        "Accuser un suspect" if interrogatoires_effectues:
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