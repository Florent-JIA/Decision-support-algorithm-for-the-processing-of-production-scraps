
import numpy as np
from extraction_chutes import create_dic_chutes
from extraction_criteres import create_dic_criteres
import random as r

chutes_path, criteres_path = "donnees chutes.xlsx", "donnees generales criteres.xlsx"

dict_chutes = create_dic_chutes(chutes_path)
dict_criteres = create_dic_criteres(criteres_path)
Af = dict_criteres["Af"]  # Poids a allouer a l aspect economique(entre 0 et 1)
Ae = dict_criteres["Ae"]  # Poids a allouer a l aspect ecologique(entre 0 et 1)
As = dict_criteres["As"]  # Poids a allouer a l aspect social(entre 0 et 1)
periode = dict_criteres["periode"]  # Periode consideree(nombre de jours)
Cmp = dict_criteres["Cmp"]  # cout de la matiere premiere(€/Tonne)
Cs = dict_criteres["Cs"]  # cout du stockage (€/(m3*jour))
Cgd = dict_criteres["Cgd"]  # cout de gestion des dechets en aval (€/Tonne)
Ctd = dict_criteres["Ctd"]  # taxes sur dechets (€/Tonne)
Ag = dict_criteres["Ag"]  # aide gouvernementale

# CHANGEMENT POUR CES CRITERES : 
equipement = dict_criteres["equipement"] # Cout total des equipements supplementaires sur la periode consideree(€)
nbrOperateur = dict_criteres["nbrOperateur"]  # Nombre d operateur a former(sans unite)
tpsFormation = dict_criteres["tpsFormation"]  # Temps de formation estime(heures)
coutUnitaireFormation = dict_criteres["coutUnitaireFormation"]  # Cout d une heure de formation d un operateur(€/heures)
travailSup = dict_criteres["travailSup"]  # Cout associe au travail supplementaire pour la production a partir de materiaux revalorises (€/m^2)
manutention = dict_criteres["manutention"]  # Cout entraine par la manutention/ acheminement des chutes de production(€/m^3)
coutSupAch = dict_criteres["coutSuppAchat"] # Coût supplémentaire à l'achat du matériau (acheminement, douane,…)
#

empreinteCO2 = dict_criteres["empreinteCO2"]  # Empreinte carbone de l apport d une tonne de matiere premiere a l entreprise (T de Co2/Tonne de matiere premiere)
impactTerritoire = dict_criteres["impactTerritoire"]  # Note de l impact territorial entre 0 et 10 (sans unite)

manutention + travailSup

coutUnitaireFormation * tpsFormation * nbrOperateur + equipement #couts lies au changement de la tâche

Nbc = len(dict_chutes['id']) # nombre de chutes dans le dictionnaire
Set_N = [i for i in range(Nbc)] # indices des chutes

CsansRS = sum(dict_chutes['Bulk_Weight'][i] * dict_chutes['Thickness'][i] * dict_chutes['Used_Surface'][i]*10**(-12)*(Cmp + Cgd + Ctd + coutSupAch) for i in range(Nbc))  # cout dans le pire des cas
print(f"cout sans revalorisation : {CsansRS}")

Dec = Nbc*[0]
for i in range (int(Nbc/2)):
    Dec[2*i] = 1
print(Dec)

best_note = -10000000000000
best_Dec = Dec

for k in range(10000) : #génération des solutions aléatoires en plaçant aléatoirement un certain nombre de 1 dans la liste de décision
    nb_changement = r.randint(1,Nbc)
    #print(f"nombre de changements : {nb_changement}")
    for b in range (nb_changement):
        i = r.randint(0,Nbc-1)
        Dec[i]=1    
    #print(Dec)

    A=1

    # calcul de la note pour chaque situation
    
    Indicateur_financier = 1 - (sum((1-Dec[i])*dict_chutes['Bulk_Weight'][i]*10**(-12) * dict_chutes['Thickness'][i] * dict_chutes['Used_Surface'][i]*(Cmp + Cgd + Ctd + coutSupAch) +
                                    Dec[i]*(dict_chutes['Used_Surface'][i]*(dict_chutes['Thickness'][i]*10**(-9)*(Cs*dict_chutes['Attente_reval'][i]+10**(-3)*dict_chutes['Bulk_Weight'][i]*(manutention-Ag))) 
                                    + dict_chutes['Bulk_Weight'][i]*10**(-12)*dict_chutes['Thickness'][i]*(dict_chutes['Total_Surface'][i] - dict_chutes['Used_Surface'][i])*Cgd)for i in Set_N)
                                    +  A*(coutUnitaireFormation * tpsFormation * nbrOperateur + equipement))/CsansRS

    if Indicateur_financier > best_note :
        best_note = Indicateur_financier
        best_Dec = Dec


    #print(f"Indicateur_financier : {Indicateur_financier}")
    Dec = Nbc*[0]

print(f"meilleure note : {best_note}, decision associée : {best_Dec}")
print('\n')

# calcul de la note obtenue sans revalorisation des chutes 

Indicateur_financier_touteschutes = 1 - (sum(Dec[i]*(dict_chutes['Used_Surface'][i]*(dict_chutes['Thickness'][i]*10**(-9)*(Cs*dict_chutes['Attente_reval'][i]+10**(-3)*dict_chutes['Bulk_Weight'][i]*(manutention-Ag))) 
                                    + dict_chutes['Bulk_Weight'][i]*10**(-12)*dict_chutes['Thickness'][i]*(dict_chutes['Total_Surface'][i] - dict_chutes['Used_Surface'][i])*Cgd)for i in Set_N)
                                    +  A*(coutUnitaireFormation * tpsFormation * nbrOperateur + equipement))/CsansRS

print(f"comparaison avec cas ou on réutilise tout, note : {Indicateur_financier_touteschutes}")