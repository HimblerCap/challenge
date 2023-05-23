import requests
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

    response = requests.get("https://rickandmortyapi.com/api/character/153")
    response = response.json()
    valueA = response["id"]
    valueB = response["name"]

    create_dataframe(valueA, valueB, args.NombreArchivo)

