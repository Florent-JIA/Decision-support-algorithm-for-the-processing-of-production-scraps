import pandas as pd

# Input Data Preparation #
def read_excel_data(filename, sheet_name="Feuil1"):
    data = pd.read_excel(filename, sheet_name="Feuil1", header=None)
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
        print(f"     {len(data.columns)} chutes ont bien ete prises en compte ")
        print('\n')
        return data_dict , len(data.columns) , len(values)

def filtrer(chutes):
    print("----------------------------------------------------")
    print(f"               Filtrage des chutes")
    print("----------------------------------------------------")
    for chute in chutes :
        if chute[1] =='MAUVAISE' or chute[2]=='NON' :
            chutes.remove(chute)
    return chutes

def reshape_to_dict(donnees):
    dict = {}
    id=[]
    Quality = []
    Compability = []
    Total_Surface = []
    Used_Surface = []
    Bulk_Weight = [] # masse volumique
    Thickness = [] # epaisseur
    Attente_reval = [] # attente avant la revalorisation d'une chute donnee
    All = [id,Quality,Compability,Total_Surface,Used_Surface,Bulk_Weight,Thickness,Attente_reval]

    for attribus_chute in donnees:
        for j in range(len(attribus_chute)) :
            All[j].append(attribus_chute[j])
    names = ['id','Quality','Compability','Total_Surface','Used_Surface','Bulk_Weight','Thickness','Attente_reval']

    for critere in All :
        dict[names.pop(0)] = critere
    print(f"     apres filtrage, il reste {len(All[0])} chute(s)")
    print("\n")

    print(f"            -- IMPORTATION TERMINEE -- ")
    print(dict)
    return dict


def create_dic_chutes(data_file_path,sheet_name = "Feuil1" ):
    print("----------------------------------------------------")
    print(f"  Extraction des donnees individuelles des chutes")
    print("----------------------------------------------------")
    donn, n, m = read_excel_data(data_file_path, "sheet_name")
    nbr_chutes = n - 1
    nbr_lignes = m
    chutes = [[] for i in range(nbr_chutes)]
    for i in range(nbr_chutes):
        for j in range(0, nbr_lignes):
            chutes[i].append(donn[(j + 1, i + 2)])
    return reshape_to_dict(filtrer(chutes))