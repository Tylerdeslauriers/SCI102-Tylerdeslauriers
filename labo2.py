from datetime import datetime

def age(annee_naissance: int) -> str:
    annee_courante = datetime.now().year
    age_calcule = annee_courante - int(annee_naissance)
    return f"Votre âge est {age_calcule} ans."
