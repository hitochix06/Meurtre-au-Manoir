# Système d'interrogatoire
label interroger:
    menu:
        "Dans quelle pièce souhaitez-vous interroger les suspects ?"
        
        "Le salon":
            scene salon_meurtre with fade
            "Dans le salon, vous voyez :"
            python:
                for perso in localisation_personnages["salon"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Éloïse Marceau":
                    call dialogue_eloise
                "Victor Delmas":
                    call dialogue_victor
                "Retour":
                    jump interroger
        
        "Le bureau":
            scene bureau with fade
            "Dans le bureau, vous voyez :"
            python:
                for perso in localisation_personnages["bureau"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Clara Duvivier":
                    call dialogue_clara
                "Retour":
                    jump interroger
        
        "La cuisine":
            scene cuisine with fade
            "Dans la cuisine, vous voyez :"
            python:
                for perso in localisation_personnages["cuisine"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Antoine Durand":
                    call dialogue_antoine
                "Retour":
                    jump interroger
        
        "La bibliothèque":
            scene bibliotheque with fade
            "Dans la bibliothèque, vous voyez :"
            python:
                for perso in localisation_personnages["bibliotheque"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Madeleine Rousseau":
                    call dialogue_madeleine
                "Retour":
                    jump interroger
        
        "La cave":
            scene cave with fade
            "Dans la cave, vous voyez :"
            python:
                for perso in localisation_personnages["cave"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Charles Beaumont":
                    call dialogue_charles
                "Retour":
                    jump interroger
        
        "Retour au menu principal":
            jump menu_principal
    
    jump interroger 