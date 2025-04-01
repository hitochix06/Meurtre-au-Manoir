init python:
    # Variables pour suivre la progression des dialogues
    dialogues_debloques = {
        "Eloise": {"base": True, "documents": False, "victor": False, "clara": False, "preuves": False},
        "Antoine": {"base": True, "couteaux": False, "eloise": False, "victor": False, "clara": False},
        "Victor": {"base": True, "dettes": False, "documents": False, "clara": False, "antoine": False},
        "Clara": {"base": True, "mot": False, "testament": False, "antoine": False, "eloise": False},
        "Charles": {"base": True, "bouteille": False, "sang": False, "victor": False, "clara": False},
        "Madeleine": {"base": True, "clara": False, "antoine": False, "bruits": False, "tissu": False}
    }
    
    # Localisation des personnages
    localisation_personnages = {
        "salon": ["Antoine"],
        "cuisine": ["Eloise"],
        "bureau": ["Clara"],
        "jardin": ["Victor"],
        "bibliotheque": ["Madeleine"],
        "cave": ["Charles"]
    }

# Labels pour les dialogues de chaque personnage
label dialogue_eloise:
    scene cuisine
    show eloise neutral
    
    if not dialogues_debloques["Eloise"]["documents"] and "finances" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Eloise"]["documents"] = True
        eloise "Ces papiers... Je les ai vus sur son bureau. Il les cachait dès que j'approchais."
        eloise "Je pense qu'il avait des problèmes d'argent, mais il refusait d'en parler."
    
    if not dialogues_debloques["Eloise"]["victor"] and "dettes" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Eloise"]["victor"] = True
        eloise "Victor ? Oui, il venait souvent. Toujours pour emprunter de l'argent à Hugo."
        eloise "Leur dernière dispute était violente. J'ai entendu Hugo menacer de tout révéler."
    return

label dialogue_antoine:
    scene salon_meurtre
    show antoine neutral
    
    if not dialogues_debloques["Antoine"]["couteaux"] and "poudre" in indices_decouverts["salon"]:
        $ dialogues_debloques["Antoine"]["couteaux"] = True
        antoine "Les traces de poudre ? Je... je ne les avais pas remarquées."
        antoine "Le salon est si grand, il y a toujours des choses qui passent inaperçues..."
    
    if not dialogues_debloques["Antoine"]["clara"] and "testament" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Antoine"]["clara"] = True
        antoine "Cette demoiselle ? Elle traîne souvent dans le manoir."
        antoine "Je l'ai surprise une fois à fouiller dans le bureau d'Hugo."
    return

label dialogue_victor:
    scene jardin
    show victor neutral
    
    if not dialogues_debloques["Victor"]["dettes"] and "finances" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Victor"]["dettes"] = True
        victor "C'est vrai, je lui devais de l'argent. Beaucoup d'argent."
        victor "Il menaçait de tout révéler à ma famille, à mes associés..."
    
    if not dialogues_debloques["Victor"]["antoine"] and "poudre" in indices_decouverts["salon"]:
        $ dialogues_debloques["Victor"]["antoine"] = True
        victor "Antoine ? Il détestait Hugo, c'était évident."
        victor "Je l'ai entendu dire qu'il 'règlerait son compte' à Hugo."
    return

label dialogue_clara:
    scene bureau
    show clara neutral
    
    if not dialogues_debloques["Clara"]["mot"] and any([x in indices_decouverts["salon"] for x in ["note", "lettre"]]):
        $ dialogues_debloques["Clara"]["mot"] = True
        clara "Ce mot ? Ce n'était rien d'important..."
        clara "Hugo voulait juste me parler de certains documents..."
    
    if not dialogues_debloques["Clara"]["testament"] and "testament" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Clara"]["testament"] = True
        clara "Le testament ? Je... je ne savais pas qu'il m'y avait incluse."
        clara "Nous avions une relation particulière... professionnelle."
    return

label dialogue_charles:
    scene cave
    show charles neutral
    
    if not dialogues_debloques["Charles"]["bouteille"] and "sang" in indices_decouverts["cave"]:
        $ dialogues_debloques["Charles"]["bouteille"] = True
        charles "Ces traces de sang ? Je les ai trouvées comme ça."
        charles "J'ai voulu les nettoyer, c'est pour ça qu'il y a mes empreintes."
    
    if not dialogues_debloques["Charles"]["sang"] and "sang" in indices_decouverts["cave"]:
        $ dialogues_debloques["Charles"]["sang"] = True
        charles "Du sang dans l'escalier ? Je... je ne l'ai pas remarqué."
        charles "Il faisait sombre, vous comprenez..."
    return

label dialogue_madeleine:
    scene bibliotheque
    show madeleine neutral
    
    if not dialogues_debloques["Madeleine"]["clara"] and "testament" in indices_decouverts["bureau"]:
        $ dialogues_debloques["Madeleine"]["clara"] = True
        madeleine "Oh oui, j'ai vu Hugo glisser un mot à Clara pendant le dîner."
        madeleine "Ils pensaient être discrets, mais je vois tout, vous savez..."
    
    if not dialogues_debloques["Madeleine"]["antoine"] and "poudre" in indices_decouverts["salon"]:
        $ dialogues_debloques["Madeleine"]["antoine"] = True
        madeleine "Antoine ? Il était particulièrement nerveux ce soir-là."
        madeleine "Je l'ai vu sortir du salon avec quelque chose sous sa veste."
    return 