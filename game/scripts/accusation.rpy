init python:
    # Variables pour le système d'accusation
    tentatives_accusation = 0
    
    # Liste des suspects et des armes
    suspects = ["Éloïse Marceau", "Antoine Durand", "Victor Delmas", "Clara Duvivier", "Charles Beaumont", "Madeleine Rousseau"]
    armes = ["Pistolet de poche", "Corde nouée", "Statue", "Canne-épée", "Poignard orné"]

# Système d'accusation
label menu_accusation:
    scene bureau with fade
    
    "Le moment est venu de désigner le coupable."
    
    "Qui accusez-vous ?"
    menu:
        "Choisissez un suspect:"
        "Éloïse Marceau":
            $ suspect_choisi = "Éloïse Marceau"
            jump choix_arme
        "Antoine Durand":
            $ suspect_choisi = "Antoine Durand"
            jump choix_arme
        "Victor Delmas":
            $ suspect_choisi = "Victor Delmas"
            jump choix_arme
        "Clara Duvivier":
            $ suspect_choisi = "Clara Duvivier"
            jump choix_arme
        "Charles Beaumont":
            $ suspect_choisi = "Charles Beaumont"
            jump choix_arme
        "Madeleine Rousseau":
            $ suspect_choisi = "Madeleine Rousseau"
            jump choix_arme

label choix_arme:
    "Quelle arme a été utilisée selon vous ?"
    menu:
        "Choisissez une arme:"
        "Pistolet de poche":
            $ arme_choisie = "Pistolet de poche"
            jump verification_accusation
        "Corde nouée":
            $ arme_choisie = "Corde nouée"
            jump verification_accusation
        "Statue":
            $ arme_choisie = "Statue"
            jump verification_accusation
        "Canne-épée":
            $ arme_choisie = "Canne-épée"
            jump verification_accusation
        "Poignard orné":
            $ arme_choisie = "Poignard orné"
            jump verification_accusation

label verification_accusation:
    # Vérification de l'accusation
    if suspect_choisi == "Éloïse Marceau" and arme_choisie == "Pistolet de poche":
        scene victory with fade
        "Vous avez résolu l'affaire ! Éloïse est bien la coupable."
        "Bravo, inspecteur !"
        
        menu:
            "Que souhaitez-vous faire ?"
            "Rejouer":
                $ renpy.full_restart()
            "Quitter le jeu":
                $ renpy.quit()
    else:
        "Ce n'est pas la bonne combinaison. Essayez encore !"
        $ tentatives_accusation += 1
        menu:
            "Que souhaitez-vous faire ?"
            "Réessayer":
                jump menu_accusation
            "Retourner au menu principal":
                jump menu_principal
            "Quitter le jeu":
                $ renpy.quit() 