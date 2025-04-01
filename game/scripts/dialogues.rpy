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
        "madeleine": "bibliotheque",
        "eloise": "cuisine",
        "antoine": "salon",
        "victor": "jardin",
        "clara": "bureau",
        "charles": "cave"
    }
    
    # Configuration audio
    AMBIENT_SOUND = "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3"
    
    # Transitions rapides
    quick_fade = Fade(0.2, 0.0, 0.2)
    quick_dissolve = Dissolve(0.2)
    
    def setup_character(character_name, scene_name):
        renpy.scene()
        renpy.with_statement(quick_fade)
        renpy.show(scene_name)
        renpy.with_statement(quick_dissolve)
        renpy.show(character_name, 
                  at_list=[Transform(
                      zoom=CHARACTER_DISPLAY["zoom"],
                      yalign=CHARACTER_DISPLAY["yalign"],
                      xalign=CHARACTER_DISPLAY["xalign"]
                  )])
        renpy.with_statement(Pause(0.2))
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
    madeleine "Bonjour inspecteur. Je suis Madeleine Rousseau, la bibliothécaire du manoir."
    detective "Bonjour Madame Rousseau. Pouvez-vous me dire où vous étiez au moment du meurtre ?"
    madeleine "J'étais ici, dans la bibliothèque, en train de ranger des livres. Je n'ai rien entendu."
    detective "Avez-vous remarqué quelque chose d'inhabituel ce soir-là ?"
    madeleine "Non, rien de particulier. Tout était calme comme d'habitude."
    $ end_dialogue("madeleine")
    return

label dialogue_eloise:
    $ start_dialogue("eloise")
    eloise "Je suis Éloïse Marceau, la femme de la victime."
    detective "Je suis désolé pour votre perte. Pouvez-vous me dire ce qui s'est passé ?"
    eloise "Je... je ne sais pas. J'étais dans la cuisine à préparer le dîner. Quand je suis revenue, il était... il était..."
    detective "Avez-vous remarqué quelque chose d'étrange avant le dîner ?"
    eloise "Non, tout semblait normal. Hugo était de bonne humeur."
    $ end_dialogue("eloise")
    return

label dialogue_antoine:
    $ start_dialogue("antoine")
    antoine "Antoine Durand, le majordome. Comment puis-je vous aider, inspecteur ?"
    detective "Où étiez-vous au moment du meurtre ?"
    antoine "Je faisais le service dans le salon. J'ai entendu un coup de feu, mais je n'ai rien vu."
    detective "Avez-vous remarqué des tensions entre les invités ?"
    antoine "Je ne peux pas dire... Je faisais mon travail, c'est tout."
    $ end_dialogue("antoine")
    return

label dialogue_victor:
    $ start_dialogue("victor")
    victor "Victor Delmas, le jardinier. Je vous écoute, inspecteur."
    detective "Que faisiez-vous dans le jardin ce soir-là ?"
    victor "Je taillais les haies. Le jardin doit rester impeccable, vous comprenez."
    detective "Avez-vous vu quelqu'un entrer ou sortir du manoir ?"
    victor "Non, je n'ai rien remarqué d'inhabituel."
    $ end_dialogue("victor")
    return

label dialogue_clara:
    $ start_dialogue("clara")
    clara "Clara Duvivier, la secrétaire de Monsieur Marceau."
    detective "Pouvez-vous me dire ce que vous faisiez dans le bureau ?"
    clara "Je classais des documents importants. Monsieur Marceau voulait que tout soit en ordre."
    detective "Avez-vous remarqué quelque chose de suspect ?"
    clara "Non, tout était normal. Je n'ai rien vu d'étrange."
    $ end_dialogue("clara")
    return

label dialogue_charles:
    $ start_dialogue("charles")
    charles "Charles Beaumont, le propriétaire du manoir."
    detective "Que faisiez-vous dans la cave ?"
    charles "Je vérifiais ma collection de vins. Je voulais choisir une bonne bouteille pour le dîner."
    detective "Avez-vous entendu des bruits étranges ?"
    charles "Non, la cave est bien isolée. Je n'ai rien entendu."
    $ end_dialogue("charles")
    return 