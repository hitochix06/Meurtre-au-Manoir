# Scènes d'investigation
# Le label examiner_scene_crime a été déplacé vers script.rpy sous le nom inspecter_scene_meurtre

label fouiller_bureau:
    scene bureau with fade
    
    menu:
        "Que voulez-vous examiner ?"
        
        "Les documents financiers" if "finances" not in indices_decouverts["bureau"]:
            "Vous découvrez des documents compromettants sur les dettes de plusieurs personnes."
            $ indices_decouverts["bureau"].append("finances")
        
        "Le testament" if "testament" not in indices_decouverts["bureau"]:
            "Le testament a été modifié récemment. Clara y est mentionnée..."
            $ indices_decouverts["bureau"].append("testament")
        
        "Les lettres" if "lettres" not in indices_decouverts["bureau"]:
            "Une lettre de menace non signée attire votre attention."
            $ indices_decouverts["bureau"].append("lettres")
        
        "Quitter":
            jump menu_principal
    
    jump fouiller_bureau

label inspecter_cuisine:
    scene cuisine with fade
    
    menu:
        "Que souhaitez-vous vérifier ?"
        
        "Le bloc de couteaux" if "couteau" not in indices_decouverts["cuisine"]:
            "Il manque effectivement un couteau..."
            $ indices_decouverts["cuisine"].append("couteau")
        
        "Le comptoir" if "lutte" not in indices_decouverts["cuisine"]:
            "Des traces de lutte sont visibles sur le comptoir."
            $ indices_decouverts["cuisine"].append("lutte")
        
        "Le sol" if "verre" not in indices_decouverts["cuisine"]:
            "Vous trouvez les débris d'un verre de vin."
            $ indices_decouverts["cuisine"].append("verre")
        
        "Quitter":
            jump menu_principal
    
    jump inspecter_cuisine 