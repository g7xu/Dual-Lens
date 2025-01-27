# this file will call API and download
import io

import pandas as pd
import requests


def download_data():

    # getting cases data
    response = requests.get("https://api.vitaldb.net/cases")

    with open("data/cases.csv", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
        print("Download completed! File saved as 'cases.csv'.")

    # getting track list data
    response = requests.get("https://api.vitaldb.net/trks")

    with open("data/trks.csv", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
        print("Download completed! File saved as 'trks.csv'.")

    # getting track list data
    response = requests.get("https://api.vitaldb.net/labs")

    with open("data/labs.csv", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
        print("Download completed! File saved as 'labs.csv'.")


def get_track_data(tid):
    response = requests.get(f"https://api.vitaldb.net/{tid}")

    return pd.read_csv(io.BytesIO(response.content))


if __name__ == "__main__":
    download_data()
