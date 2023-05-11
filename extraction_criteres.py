import pandas as pd

  # Input Data Preparation #
def read_excel_data(data_file_path, sheet_name="Feuil1"):
    data = pd.read_excel(data_file_path, sheet_name=sheet_name, header=None)
    values = data.values

    if min(values.shape) == 1:  # This If is to make the code insensitive to column-wise or row-wise expression #
        if values.shape[0] == 1:
            values = values.tolist()
        else:
            values = values.transpose()
            values = values.tolist()
        return values[0]
    else:
        data_dict = {}
        if min(values.shape) == 2:  # For single-dimension parameters in Excel
            if values.shape[0] == 2:
                for i in range(values.shape[1]):
                    data_dict[i+1] = values[1][i]
            else:
                for i in range(values.shape[0]):
                    data_dict[i+1] = values[i][1]

        else:  # For two-dimension (matrix) parameters in Excel
            for i in range(values.shape[0]):
                for j in range(values.shape[1]):
                    data_dict[(i+1, j+1)] = values[i][j]
        return data_dict

def create_dic_criteres(data_file_path,sheet_name = "Feuil1" ):
    print('\n')
    print("----------------------------------------------------")
    print(f"  Extraction et Importation des criteres generaux ")
    print("----------------------------------------------------")

    # Remplissage du dictionnaire avec tous les criteres generaux

    dic = {}
    donn = read_excel_data(data_file_path, sheet_name)
    dic["Af"] = donn[2]  # Poids a allouer a l aspect economique(entre 0 et 1)
    dic["Ae"] = donn[3]  # Poids a allouer a l aspect ecologique(entre 0 et 1)
    dic["As"] = donn[4]  # Poids a allouer a l aspect social(entre 0 et 1)
    dic["periode"] = donn[5]  # Periode consideree(nombre de jours)
    dic["Cmp"] = donn[6]  # cout de la matiere premiere
    dic["Cs"] = donn[7]  # cout du stockage
    dic["Cgd"] = donn[8]  # cout de gestion des dechêts en aval
    dic["Ctd"] = donn[9]  # taxes sur dechets
    dic["Ag"] = donn[10]  # aide gouvernementale
    dic["equipement"] = donn[11];  # Cout total des equipements supplementaires sur la periode consideree(€)
    dic["nbrOperateur"] = donn[12];  # Nombre d operateur a former(sans unite)
    dic["tpsFormation"] = donn[13];  # Temps de formation estime(heures)
    dic["coutUnitaireFormation"] = donn[14];  # Cout d une heure de formation d un operateur(€/heures)
    dic["travailSup"] = donn[15];  # Cout associe au travail supplementaire pour la production a partir de materiaux revalorises (€)
    dic["manutention"] = donn[16];  # Cout entraine par la manutention/ acheminement des chutes de production(€)
    dic["empreinteCO2"] = donn[17];  # Empreinte carbone de l apport d une tonne de matiere premiere a l entreprise (T de Co2/Tonne de matiere premiere)
    dic["impactTerritoire"] = donn[18];  # Note de l impact territorial entre 0 et 10 (sans unite)
    dic["coutSuppAchat"] = donn[19] # Cout supplementaire a l'achat du materiau (acheminement, douane,…)
    print(f"            -- IMPORTATION TERMINEE -- ")
    return dic