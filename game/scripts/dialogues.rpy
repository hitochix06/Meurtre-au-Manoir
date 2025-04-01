# Dialogues des personnages

# Configuration des dialogues
init python:
    # Constantes pour l'affichage des personnages
    CHARACTER_DISPLAY = {
        "zoom": 1.5,
        "yalign": 0.2,
        "xalign": 0.5
    }
    
    # Association des personnages avec leurs lieux
    CHARACTER_LOCATIONS = {
        "madeleine": "chambre",
        "eloise": "jardin",
        "antoine": "cuisine",
        "victor": "jardin",
        "clara": "bibliotheque",
        "charles": "cave"
    }
    
    # Configuration audio
    AMBIENT_SOUND = "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3"
    
    # Transitions rapides
    quick_fade = Fade(0.2, 0.0, 0.2)
    quick_dissolve = Dissolve(0.2)
    
    def setup_character(character_name, scene_name):
        # On cache d'abord le personnage actuel s'il existe
        renpy.hide(character_name)
        
        # On affiche la nouvelle scène avec une transition douce
        renpy.with_statement(quick_dissolve)
        renpy.show(scene_name)
        
        # On affiche le personnage avec une transition douce
        renpy.with_statement(quick_dissolve)
        renpy.show(character_name, 
                  at_list=[Transform(
                      zoom=CHARACTER_DISPLAY["zoom"],
                      yalign=CHARACTER_DISPLAY["yalign"],
                      xalign=CHARACTER_DISPLAY["xalign"]
                  )])
        
        # On démarre la musique
        renpy.music.play(AMBIENT_SOUND, channel="sound", fadein=0.5)

    def end_dialogue(character_name):
        renpy.music.stop(channel="sound", fadeout=0.5)
        renpy.with_statement(quick_dissolve)
        renpy.hide(character_name)

    def start_dialogue(character_name):
        setup_character(character_name, CHARACTER_LOCATIONS[character_name])

# Dialogues individuels
label dialogue_madeleine:
    $ start_dialogue("madeleine")
    madeleine "Je suis Madeleine Rousseau. Je me suis retirée dans ma chambre immédiatement après le dîner."
    detective "Avez-vous remarqué quelque chose d'inhabituel avant de vous retirer ?"
    madeleine "Oui... J'ai vu Hugo glisser un mot à Clara. Ils cachaient quelque chose, c'était évident."
    detective "Pensez-vous que Clara pourrait être impliquée ?"
    madeleine "Je ne veux pas accuser qui que ce soit, mais leur comportement était suspect."
    $ end_dialogue("madeleine")
    return

label dialogue_eloise:
    $ start_dialogue("eloise")
    eloise "Je suis Éloïse Marceau, la femme de la victime. J'étais sortie fumer après ma dispute avec Hugo."
    detective "Pouvez-vous me parler de cette dispute ?"
    eloise "C'était... c'était une dispute banale. Je l'ai quitté en larmes."
    detective "Avez-vous remarqué quelque chose de suspect ?"
    eloise "Oui, j'ai vu Antoine rôder près du salon. Il déteste mon mari, vous savez."
    $ end_dialogue("eloise")
    return

label dialogue_antoine:
    $ start_dialogue("antoine")
    antoine "Antoine Durand, le majordome. J'étais à la cuisine pour ranger après le dîner."
    detective "Avez-vous vu quelqu'un passer par la cuisine ?"
    antoine "Non, j'étais seul. Mais je dois dire que je ne supportais plus Hugo."
    detective "Qui soupçonnez-vous ?"
    antoine "Victor Delmas. Il lui doit de l'argent et en parle toujours avec rage."
    $ end_dialogue("antoine")
    return

label dialogue_victor:
    $ start_dialogue("victor")
    victor "Victor Delmas, le jardinier. J'ai fumé dans le jardin toute la soirée."
    detective "Avez-vous vu quelqu'un dans le jardin ?"
    victor "Oui, Madame Marceau. Elle était furieuse après la dispute... Je l'ai vue quitter le salon en larmes."
    detective "Pensez-vous qu'elle pourrait être impliquée ?"
    victor "Je ne veux pas accuser qui que ce soit, mais son comportement était étrange."
    $ end_dialogue("victor")
    return

label dialogue_clara:
    $ start_dialogue("clara")
    clara "Clara Duvivier, la secrétaire de Monsieur Marceau. J'étais à la bibliothèque, seule, en train de lire."
    detective "Avez-vous parlé à quelqu'un ce soir-là ?"
    clara "Oui, j'ai parlé à Antoine. Il m'a confié qu'il ne supportait plus Hugo."
    detective "Avez-vous remarqué quelque chose d'inhabituel ?"
    clara "Non, tout semblait normal. Je n'ai rien vu d'étrange."
    $ end_dialogue("clara")
    return

label dialogue_charles:
    $ start_dialogue("charles")
    charles "Charles Beaumont, le propriétaire du manoir. Je suis descendu à la cave pour chercher une bouteille après le dîner."
    detective "Avez-vous vu ou entendu quelque chose ?"
    charles "Non, la cave est bien isolée. Mais je dois dire que Victor s'est toujours montré agressif envers Hugo. Les disputes étaient fréquentes."
    detective "Pensez-vous que Victor pourrait être impliqué ?"
    charles "Je ne veux pas faire d'accusations, mais il y avait beaucoup de tension entre eux."
    $ end_dialogue("charles")
    return 