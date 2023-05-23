import argparse

from utils import create_dataframe

if __name__ == "__main__":
    """
        1. Voy a sumar dos numeros
        2. multiplicar matrizes
        3. Bailar
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--NombreArchivo', type=str)
    args = parser.parse_args()
    
    valueA = 1
    valueB = 2 

    create_dataframe(valueA, valueB, args.NombreArchivo)

