# Système d'interrogatoire
label interroger:
    scene bibliotheque with fade
    play music "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 2.0 volume 0.3

    # Style du menu
    $ style.menu_choice_button.background = Frame("gui/button/choice_idle_background.png", 0, 0)
    $ style.menu_choice_button.hover_background = Frame("gui/button/choice_hover_background.png", 0, 0)
    $ style.menu_choice_button.padding = (20, 10, 20, 10)
    $ style.menu_choice_button.xalign = 0.5
    $ style.menu_choice_button.yalign = 0.5

    menu:
        "Dans quelle pièce souhaitez-vous interroger les suspects ?"
        
        "Le salon":
            scene salon with dissolve
            "Dans le salon, vous voyez :"
            python:
                for perso in localisation_personnages["salon"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Antoine Durand":
                    call dialogue_antoine
                "Retour":
                    jump interroger
        
        "La cuisine":
            scene cuisine with dissolve
            "Dans la cuisine, vous voyez :"
            python:
                for perso in localisation_personnages["cuisine"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Éloïse Marceau":
                    call dialogue_eloise
                "Retour":
                    jump interroger
        
        "Le bureau":
            scene bureau with dissolve
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
        
        "Le jardin":
            scene jardin with dissolve
            "Dans le jardin, vous voyez :"
            python:
                for perso in localisation_personnages["jardin"]:
                    renpy.say("", "- " + perso)
            menu:
                "Qui souhaitez-vous interroger ?"
                "Victor Delmas":
                    call dialogue_victor
                "Retour":
                    jump interroger
        
        "La bibliothèque":
            scene bibliotheque with dissolve
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
            scene cave with dissolve
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
            stop music fadeout 2.0
            jump menu_principal
    
    jump interroger 