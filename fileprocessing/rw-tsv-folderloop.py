import pandas as pd
import os

def folder_loop():
    files = os.scandir(os.fspath("."))
    for file in files:
        if not file.is_dir() and file.name[-4:]==".csv":
            print(f"Found CSV file: {file.name}")


