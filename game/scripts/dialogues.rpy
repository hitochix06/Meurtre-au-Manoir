# Dialogues des personnages

label dialogue_madeleine:
    scene bibliotheque with fade
    show madeleine at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    madeleine "Bonjour inspecteur. Je suis Madeleine Rousseau, la bibliothécaire du manoir."
    detective "Bonjour Madame Rousseau. Pouvez-vous me dire où vous étiez au moment du meurtre ?"
    madeleine "J'étais ici, dans la bibliothèque, en train de ranger des livres. Je n'ai rien entendu."
    detective "Avez-vous remarqué quelque chose d'inhabituel ce soir-là ?"
    madeleine "Non, rien de particulier. Tout était calme comme d'habitude."
    stop sound fadeout 1.0
    return

label dialogue_eloise:
    $ renpy.file("textes/dialogue_eloise.txt")
    return

label dialogue_antoine:
    $ renpy.file("textes/dialogue_antoine.txt")
    return

label dialogue_victor:
    $ renpy.file("textes/dialogue_victor.txt")
    return

label dialogue_clara:
    $ renpy.file("textes/dialogue_clara.txt")
    return

label dialogue_charles:
    $ renpy.file("textes/dialogue_charles.txt")
    return 