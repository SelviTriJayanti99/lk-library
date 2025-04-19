from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    # Data K-pop: Nama Grup, Genre Musik, Tahun Debut, Agensi
    data = {
        "Nama Grup": ["BTS", "BLACKPINK", "EXO", "Twice", "Stray Kids"],
        "Genre Musik": ["Hip Hop, Pop, R&B", "K-pop, EDM, Pop", "K-pop, Pop, R&B", "K-pop, Pop", "K-pop, Hip Hop, EDM"],
        "Tahun Debut": [2013, 2016, 2012, 2015, 2018],
        "Agensi": ["BigHit Entertainment", "YG Entertainment", "SM Entertainment", "JYP Entertainment", "JYP Entertainment"]
    }
    df = pd.DataFrame(data)

    # Menggunakan NumPy untuk menghitung statistik lainnya
    average_debut = np.mean(df['Tahun Debut'])
    median_debut = np.median(df['Tahun Debut'])  # Median tahun debut
    std_debut = np.std(df['Tahun Debut'])  # Standar deviasi tahun debut
    cumulative_sum = np.cumsum(df['Tahun Debut'])  # Cumulative sum dari tahun debut

    # Mengubah DataFrame menjadi list of dict untuk template
    kpop_groups = df.to_dict(orient='records')

    # Mengirim data ke template
    return render_template("index.html", kpop_groups=kpop_groups, 
                           average_debut=average_debut, median_debut=median_debut, 
                           std_debut=std_debut, cumulative_sum=cumulative_sum)

if __name__ == '__main__':
    app.run(debug=True)
