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
    hide madeleine with dissolve
    return

label dialogue_eloise:
    scene cuisine with fade
    show eloise at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    eloise "Je suis Éloïse Marceau, la femme de la victime."
    detective "Je suis désolé pour votre perte. Pouvez-vous me dire ce qui s'est passé ?"
    eloise "Je... je ne sais pas. J'étais dans la cuisine à préparer le dîner. Quand je suis revenue, il était... il était..."
    detective "Avez-vous remarqué quelque chose d'étrange avant le dîner ?"
    eloise "Non, tout semblait normal. Hugo était de bonne humeur."
    stop sound fadeout 1.0
    hide eloise with dissolve
    return

label dialogue_antoine:
    scene salon with fade
    show antoine at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    antoine "Antoine Durand, le majordome. Comment puis-je vous aider, inspecteur ?"
    detective "Où étiez-vous au moment du meurtre ?"
    antoine "Je faisais le service dans le salon. J'ai entendu un coup de feu, mais je n'ai rien vu."
    detective "Avez-vous remarqué des tensions entre les invités ?"
    antoine "Je ne peux pas dire... Je faisais mon travail, c'est tout."
    stop sound fadeout 1.0
    hide antoine with dissolve
    return

label dialogue_victor:
    scene jardin with fade
    show victor at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    victor "Victor Delmas, le jardinier. Je vous écoute, inspecteur."
    detective "Que faisiez-vous dans le jardin ce soir-là ?"
    victor "Je taillais les haies. Le jardin doit rester impeccable, vous comprenez."
    detective "Avez-vous vu quelqu'un entrer ou sortir du manoir ?"
    victor "Non, je n'ai rien remarqué d'inhabituel."
    stop sound fadeout 1.0
    hide victor with dissolve
    return

label dialogue_clara:
    scene bureau with fade
    show clara at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    clara "Clara Duvivier, la secrétaire de Monsieur Marceau."
    detective "Pouvez-vous me dire ce que vous faisiez dans le bureau ?"
    clara "Je classais des documents importants. Monsieur Marceau voulait que tout soit en ordre."
    detective "Avez-vous remarqué quelque chose de suspect ?"
    clara "Non, tout était normal. Je n'ai rien vu d'étrange."
    stop sound fadeout 1.0
    hide clara with dissolve
    return

label dialogue_charles:
    scene cave with fade
    show charles at center with dissolve
    with Pause(0.5)
    play sound "audio/room-tone-int-living-room_poa_horns_trafic_kitchen-noises_m-18976.mp3" fadein 1.0
    charles "Charles Beaumont, le propriétaire du manoir."
    detective "Que faisiez-vous dans la cave ?"
    charles "Je vérifiais ma collection de vins. Je voulais choisir une bonne bouteille pour le dîner."
    detective "Avez-vous entendu des bruits étranges ?"
    charles "Non, la cave est bien isolée. Je n'ai rien entendu."
    stop sound fadeout 1.0
    hide charles with dissolve
    return 