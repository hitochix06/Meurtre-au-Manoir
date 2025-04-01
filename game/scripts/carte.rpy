### Carte interactive ###
label carte:
    scene map_manoir with fade
    "Vous consultez le plan du manoir. Où souhaitez-vous aller ?"

    menu:
        "Salon (Scène du crime)":
            jump scene_crime
            
        "Bureau":
            scene bureau with dissolve
            "Le bureau est rempli de documents..."
            menu:
                "Que faire ?"
                "Fouiller les documents":
                    "Vous trouvez des documents financiers troublants..."
                    $ indices_trouves["note"] = True
                "Quitter":
                    jump carte
            
        "Cuisine":
            scene cuisine with dissolve
            "La cuisine est impeccablement rangée..."
            menu:
                "Que faire ?"
                "Examiner les couteaux":
                    "Il manque un couteau dans le bloc..."
                    $ indices_trouves["arme"] = True
                "Quitter":
                    jump carte
            
        "Jardin":
            scene jardin with dissolve
            "Le jardin est calme et sombre..."
            menu:
                "Que faire ?"
                "Chercher des indices":
                    "Rien de particulier à signaler..."
                "Quitter":
                    jump carte
            
        "Retourner à l'enquête":
            jump choix_action
    
    return

screen map_screen():
    imagemap:
        auto "lieux/carte_interactive_%s.png"
        hotspot (300, 200, 100, 100) action Jump("salon")
        hotspot (400, 300, 100, 100) action Jump("cuisine")
        hotspot (500, 400, 100, 100) action Jump("jardin")
