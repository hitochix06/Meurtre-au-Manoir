init python:
    # Variables pour le système d'accusation
    tentatives_accusation = 0
    indices_disponibles = [
        "Éloïse avait un mobile personnel contre Hugo.",
        "On a trouvé des traces de poudre à canon dans le salon.",
        "Un pistolet a été découvert dans le jardin.",
        "Des traces de pas mènent vers la fenêtre du salon.",
        "Une lettre de menace a été trouvée dans le bureau.",
        "Des empreintes ont été relevées sur l'arme."
    ]
    indices_utilises = []

# Système d'accusation
label menu_accusation:
    scene bureau with fade
    
    "Le moment est venu de désigner le coupable."
    
    if tentatives_accusation >= 3:
        "Vous avez fait plusieurs tentatives d'accusation infructueuses."
        "Voulez-vous recevoir un indice pour vous aider ?"
        
        menu:
            "Oui, je veux un indice":
                if indices_disponibles:
                    $ indice = indices_disponibles.pop(0)
                    $ indices_utilises.append(indice)
                    "[indice]"
                else:
                    "Vous avez déjà utilisé tous les indices disponibles."
            
            "Non, je veux continuer l'enquête":
                jump menu_principal
    
    "Qui accusez-vous ?"
    $ suspect = renpy.input("Entrez le nom du suspect:", "", length=20)
    $ suspect = suspect.strip()
    
    "Quelle arme a été utilisée selon vous ?"
    $ arme = renpy.input("Entrez le nom de l'arme:", "", length=20)
    $ arme = arme.strip()
    
    # Vérification de l'accusation
    if suspect.lower() == "eloise" and arme.lower() == "pistolet":
        if "poudre" in indices_decouverts["salon"] and "empreintes" in indices_decouverts["salon"]:
            "Vous avez résolu l'affaire ! Éloïse est bien la coupable."
            "Les preuves étaient là : les traces de poudre, les empreintes sur l'arme..."
            "Bravo, inspecteur !"
            $ tentatives_accusation = 0
            $ indices_utilises = []
            return
        else:
            "Votre accusation ne tient pas... Il vous manque des preuves."
            "Continuez votre enquête."
            $ tentatives_accusation += 1
            jump menu_principal
    else:
        "Votre accusation ne correspond pas aux faits."
        "Continuez votre enquête."
        $ tentatives_accusation += 1
        jump menu_principal
    
    return 