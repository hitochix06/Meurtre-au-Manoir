# Système d'accusation
label menu_accusation:
    scene bureau with fade
    
    "Le moment est venu de désigner le coupable."
    
    menu:
        "Qui accusez-vous ?"
        
        "Éloïse Marceau":
            $ accuse = "Eloise"
        "Antoine Durand":
            $ accuse = "Antoine"
        "Victor Delmas":
            $ accuse = "Victor"
        "Clara Duvivier":
            $ accuse = "Clara"
        "Charles Beaumont":
            $ accuse = "Charles"
        "Madeleine Rousseau":
            $ accuse = "Madeleine"
    
    # Vérification de l'accusation
    if accuse == "Antoine" and "couteau" in indices_decouverts["cuisine"] and "lutte" in indices_decouverts["cuisine"]:
        "Vous avez résolu l'affaire ! Antoine est bien le coupable."
        "Les preuves étaient là : le couteau manquant, les traces de lutte..."
        "Bravo, inspecteur !"
    else:
        "Votre accusation ne tient pas... Il vous manque des preuves."
        "Continuez votre enquête."
        jump menu_principal
    
    return 