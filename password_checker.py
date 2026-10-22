def verifier_mot_de_passe(mdp):
    score = 0
    conseils = []

    if len(mdp) >= 8:
        score += 2
    else:
        conseils.append("-> Trop court : mets au moins 8 caractères")

    if any(c.isupper() for c in mdp):
        score += 1
    else:
        conseils.append("-> Ajoute au moins une MAJUSCULE")

    if any(c.islower() for c in mdp):
        score += 1
    else:
        conseils.append("-> Ajoute au moins une minuscule")

    if any(c.isdigit() for c in mdp):
        score += 1
    else:
        conseils.append("-> Ajoute au moins un chiffre (0-9)")

    caracteres_speciaux = "!@#$%^&*()_-+=<>?"
    if any(c in caracteres_speciaux for c in mdp):
        score += 1
    else:
        conseils.append("-> Ajoute un caractère spécial : ! @ # $ %")

    print(f"\nMot de passe testé : {mdp}")
    print(f"Score : {score}/6")

    if score == 6:
        print("✅ EXCELLENT - Mot de passe très fort")
    elif score >= 4:
        print("🟡 MOYEN - Peut être amélioré")
    else:
        print("🔴 FAIBLE - Dangereux")

    if conseils:
        print("\nConseils :")
        for c in conseils:
            print(c)

mon_mdp = input("Entre ton mot de passe à tester : ")
verifier_mot_de_passe(mon_mdp)