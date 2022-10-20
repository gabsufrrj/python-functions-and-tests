from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            csv_list = list(csv_reader)
        return csv_list
    except FileNotFoundError:
        print("Arquivo não encontrado")
