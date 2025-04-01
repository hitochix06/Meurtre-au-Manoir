### Script des dialogues et interactions avec les personnages ###

init python:
    # Définition des variables pour les personnages
    suspect_notes = {
        "Eloise": {"alibi": False, "mobile": False, "preuve": False},
        "Antoine": {"alibi": False, "mobile": False, "preuve": False},
        "Victor": {"alibi": False, "mobile": False, "preuve": False},
        "Clara": {"alibi": False, "mobile": False, "preuve": False},
        "Charles": {"alibi": False, "mobile": False, "preuve": False},
        "Madeleine": {"alibi": False, "mobile": False, "preuve": False}
    }

# Définition des personnages avec leurs caractéristiques
define detective = Character("Inspecteur", color="#2980b9")
define eloise = Character("Éloïse Marceau", color="#D36E70")
define antoine = Character("Antoine Durand", color="#D39056")
define victor = Character("Victor Delmas", color="#7CBD74")
define clara = Character("Clara Duvivier", color="#9B59B6")
define charles = Character("Charles Beaumont", color="#34495E")
define madeleine = Character("Madeleine Rousseau", color="#E67E22")

# Introduction des dialogues dans les pièces
label interrogations:
    menu:
        "Quelle pièce examiner ?"
        
        "Le salon":
            jump salon
        
        "La cuisine":
            jump cuisine
        
        "Le jardin":
            jump jardin
        
        "Le bureau":
            jump bureau
        
        "La bibliothèque":
            jump bibliotheque
        
        "La cave":
            jump cave
    
    return

label salon:
    scene salon_meurtre with fade
    show eloise neutral at right
    eloise "J'étais sortie fumer après une dispute avec Hugo... Vous ne pensez pas que je suis coupable ?"
    detective "Que savez-vous d'Antoine ?"
    eloise "Il rôdait autour du salon. Je crois qu'il n'aimait pas Hugo, et je pense qu'il l'a tué."
    return

label cuisine:
    scene cuisine_manoir with fade
    show antoine neutral at right
    antoine "Moi ? J'étais dans la cuisine. Hugo faisait des dettes de jeu avec des inconnus souvent douteux. Peut-être que c'est un de ses ennemis."
    detective "Pouvez-vous me dire qui d'autre était présent ce soir-là ?"
    antoine "Je... je ne me souviens pas exactement. Il y avait beaucoup de monde."
    return

label jardin:
    scene jardin_manoir with fade
    show victor neutral at right
    victor "Je ne comprends pas... Hugo était un bon ami. Je ne sais pas qui pourrait vouloir lui faire du mal."
    victor "Mais j'ai entendu Antoine et Hugo se disputer hier soir."
    detective "Quelle était la nature de cette dispute ?"
    victor "Je... je ne sais pas exactement. Mais Antoine semblait très en colère."
    return

label bureau:
    scene bureau with fade
    show clara neutral at right
    clara "J'étais en train de travailler sur des documents importants."
    detective "Quels documents ?"
    clara "Des... des papiers personnels d'Hugo. Il m'avait demandé de les examiner."
    return

label bibliotheque:
    scene bibliotheque with fade
    show madeleine neutral at right
    madeleine "Je lisais, comme d'habitude. Cette bibliothèque est si paisible..."
    detective "Avez-vous entendu quelque chose d'inhabituel ?"
    madeleine "Peut-être... des pas dans le couloir, mais je ne peux pas en être sûre."
    return

label cave:
    scene cave with fade
    show charles neutral at right
    charles "Je cherchais une bouteille particulière. Hugo m'avait demandé de la sortir."
    detective "Avez-vous trouvé cette bouteille ?"
    charles "Non... Je... je ne l'ai pas trouvée. Je suis remonté bredouille."
    return

# Scènes d'interrogatoire individuelles
label interroger_eloise:
    scene salon with fade
    show eloise neutral at right
    
    detective "Madame Marceau, parlez-moi de votre soirée."
    eloise "J'étais sortie fumer après une dispute avec Hugo... Je sais que ça me rend suspecte."
    
    menu:
        "Comment poursuivre ?"
        
        "La questionner sur la dispute":
            detective "Quelle était la raison de cette dispute ?"
            eloise "Il... il me cachait des choses. Des documents étranges, des appels secrets..."
            $ suspect_notes["Eloise"]["mobile"] = True
        
        "Lui demander ce qu'elle a vu":
            detective "Avez-vous remarqué quelque chose d'inhabituel ?"
            eloise "J'ai vu Antoine rôder près du salon. Il déteste mon mari, vous savez."
            $ suspect_notes["Eloise"]["preuve"] = True
    
    return

label interroger_antoine:
    scene cuisine with fade
    show antoine neutral at right
    
    detective "Monsieur Durand, vous étiez en cuisine ?"
    antoine "Oui, je rangeais après le dîner. Mais écoutez, Victor est louche dans cette histoire."
    
    menu:
        "Quelle approche adopter ?"
        
        "Questionner sur Victor":
            detective "Pourquoi soupçonnez-vous Victor ?"
            antoine "Il doit de l'argent à Hugo et en parle toujours avec rage."
            $ suspect_notes["Antoine"]["preuve"] = True
        
        "Vérifier son alibi":
            detective "Quelqu'un peut confirmer votre présence en cuisine ?"
            antoine "Je... non, j'étais seul. Mais je n'ai pas quitté mon poste !"
            $ suspect_notes["Antoine"]["alibi"] = True
    
    return

label interroger_victor:
    scene jardin with fade
    show victor neutral at right
    
    detective "Monsieur Delmas, vous étiez dans le jardin ?"
    victor "Oui, je fumais. J'y suis resté toute la soirée."
    
    menu:
        "Comment continuer ?"
        
        "Parler d'Éloïse":
            detective "Avez-vous vu Madame Marceau ?"
            victor "Elle était furieuse après la dispute... Je l'ai vue quitter le salon en larmes."
            $ suspect_notes["Victor"]["preuve"] = True
        
        "Évoquer ses dettes":
            detective "On me dit que vous deviez de l'argent à la victime..."
            victor "Ce... ce n'est pas ce que vous croyez..."
            $ suspect_notes["Victor"]["mobile"] = True
    
    return

label interroger_clara:
    scene bibliotheque with fade
    show clara neutral at right
    
    detective "Mademoiselle Duvivier, vous étiez à la bibliothèque ?"
    clara "Oui, je lisais. Seule... Je sais que ce n'est pas un bon alibi."
    
    menu:
        "Comment procéder ?"
        
        "Questionner sur Antoine":
            detective "Que pensez-vous d'Antoine Durand ?"
            clara "Il m'a confié ne plus supporter Hugo. Ses mots étaient... inquiétants."
            $ suspect_notes["Clara"]["preuve"] = True
        
        "Le mot d'Hugo":
            detective "On vous a vue recevoir un mot d'Hugo..."
            clara "Ce... ce n'était rien d'important..."
            $ suspect_notes["Clara"]["mobile"] = True
    
    return

label interroger_charles:
    scene cave with fade
    show charles neutral at right
    
    detective "Monsieur Beaumont, vous étiez à la cave ?"
    charles "Oui, je cherchais une bouteille particulière après le dîner."
    
    menu:
        "Quelle direction prendre ?"
        
        "Parler de Victor":
            detective "Que pouvez-vous me dire sur Victor Delmas ?"
            charles "Il s'est toujours montré agressif envers Hugo. Les disputes étaient fréquentes."
            $ suspect_notes["Charles"]["preuve"] = True
        
        "La bouteille":
            detective "Avez-vous trouvé cette fameuse bouteille ?"
            charles "Je... Non, finalement. J'ai dû remonter bredouille..."
            $ suspect_notes["Charles"]["alibi"] = True
    
    return

label interroger_madeleine:
    scene chambre with fade
    show madeleine neutral at right
    
    detective "Madame Rousseau, vous vous êtes retirée tôt ?"
    madeleine "Oui, juste après le dîner. Mais j'ai vu quelque chose d'intéressant..."
    
    menu:
        "Comment poursuivre ?"
        
        "Le mot mystérieux":
            detective "Que pouvez-vous me dire sur Clara et Hugo ?"
            madeleine "J'ai vu Hugo glisser un mot à Clara. Ils cachaient quelque chose, j'en suis sûre."
            $ suspect_notes["Madeleine"]["preuve"] = True
        
        "Vérifier son départ":
            detective "Quelqu'un vous a vue monter ?"
            madeleine "Non... Je suppose que non..."
            $ suspect_notes["Madeleine"]["alibi"] = True
    
    return
