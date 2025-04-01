init python:
    # Système de QR code pour la réalité augmentée avec Adobe Aero
    def verifier_qr_code(code_entre):
        # Code unique pour activer la réalité augmentée
        if code_entre == "AERO123":
            return True
        return False

label scanner_qr_aero:
    scene bureau with fade
    
    "Vous trouvez un QR code mystérieux sur le bureau..."
    "Il semble contenir des informations sur toutes les pièces et les armes."
    
    # Afficher l'image du QR code
    show qr_code at truecenter with dissolve
    
    "Scannez ce QR code avec Adobe Aero pour voir toutes les pièces et les armes en réalité augmentée."
    
    menu:
        "Retourner à l'enquête":
            return
    
    jump scanner_qr_aero
