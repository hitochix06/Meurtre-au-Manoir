init python:
    # Au lieu d'utiliser un générateur de QR code en temps réel,
    # nous allons utiliser des images pré-générées de QR codes
    
    def verifier_qr_code(code_entre):
        # Dictionnaire des codes valides et leurs correspondances
        codes_valides = {
            "ARME123": "Le QR code révèle une information sur l'arme du crime.",
            "INDICE456": "Le QR code contient un indice sur le mobile du meurtrier.",
            "LIEU789": "Le QR code indique un détail important sur la scène de crime."
        }
        
        # Vérifier si le code entré est valide
        return codes_valides.get(code_entre, "Ce code QR n'est pas valide.")

label scanner_qr:
    scene bureau
    
    "Vous pouvez entrer un code QR trouvé dans le manoir."
    
    $ code = renpy.input("Entrez le code trouvé:")
    $ resultat = verifier_qr_code(code.strip().upper())
    
    "[resultat]"
    
    menu:
        "Que souhaitez-vous faire ?"
        
        "Scanner un autre code":
            jump scanner_qr
            
        "Retourner à l'enquête":
            return
