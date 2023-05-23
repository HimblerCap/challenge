import os
import pandas as pd

from pathlib import Path


def create_dataframe(valueA, ValueB, name_file):
    """
    Creando un dataframe para guardar en mi archivo data
    
    Args: 
        valueA: Primer valor a guardar
        valueB: Segundo valor a guardar
        name_file: El nombre del archivo con el que se guardara

    Return:
        Un dataFrame guardado en la carpeta data en formato excel
    """
    file_path = os.path.join(Path(__file__).parent.parent, "data")
    file_name = os.path.join(file_path, name_file)
    df = pd.DataFrame(data=[[valueA, ValueB]], columns=["Valor_1", "Valor2"])

    df.to_excel(file_name) if name_file[-5:] == '.xlsx' else df.to_excel(file_name + '.xlsx')