import pandas as pd
import kaggle


def extract_data():
    kaggle.api.authenticate()

    kaggle.api.dataset_download_files('andrexibiza/grocery-sales-dataset', path=r'C:\Users\TiagoCosta\Kaggle\data', unzip=True)
    
    return 'Data Extracted'

extract_data()    