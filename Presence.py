import pandas as pd
from datetime import datetime, timedelta
import mysql.connector
def presence(id):
    present=0
    nvindice=int(id/10)
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_presence.csv")
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="bank_of_faces")
    curs=conn.cursor()
    curs.execute('SELECT nom,prenom FROM faces where id =%s',(nvindice,))
    row = curs.fetchone()
    if row is not None:
        dt = datetime.now()
        df_id = df[df['Id'] == nvindice]
        for _, ligne in df_id.iterrows():
            date_presence = pd.to_datetime(ligne['Date'])
            deux_heures_avant = dt - timedelta(hours=2)
            if date_presence >= deux_heures_avant:
                print("ce personne est deja present dans ces 2 heurs")
                present=1
                return present
        if present==0:
            df.loc[len(df)] = {'Id': nvindice, 'Nom': row[0], 'Prenom': row[1], 'Date': dt}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_presence.csv",index=False)
    else:
        present=-1  
    conn.close()
    return present
def hsvpresence(id):
    present=0
    nvindice=int(id/10)
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_hsvpresence.csv")
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="bank_of_faces")
    curs=conn.cursor()
    curs.execute('SELECT nom,prenom FROM faces where id =%s',(nvindice,))
    row = curs.fetchone()
    if row is not None:
        dt = datetime.now()
        df_id = df[df['Id'] == nvindice]
        for _, ligne in df_id.iterrows():
            date_presence = pd.to_datetime(ligne['Date'])
            deux_heures_avant = dt - timedelta(hours=2)
            if date_presence >= deux_heures_avant:
                print("ce personne est deja present dans ces 2 heurs")
                present=1
                return present
        if present==0:
            df.loc[len(df)] = {'Id': nvindice, 'Nom': row[0], 'Prenom': row[1], 'Date': dt}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_hsvpresence.csv",index=False)
    else:
        present=-1  
    conn.close()
    return present
def lbppresence(id):
    present=0
    nvindice=int(id/10)
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_lbppresence.csv")
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="bank_of_faces")
    curs=conn.cursor()
    curs.execute('SELECT nom,prenom FROM faces where id =%s',(nvindice,))
    row = curs.fetchone()
    if row is not None:
        dt = datetime.now()
        df_id = df[df['Id'] == nvindice]
        for _, ligne in df_id.iterrows():
            date_presence = pd.to_datetime(ligne['Date'])
            deux_heures_avant = dt - timedelta(hours=2)
            if date_presence >= deux_heures_avant:
                print("ce personne est deja present dans ces 2 heurs")
                present=1
                return present
        if present==0:
            df.loc[len(df)] = {'Id': nvindice, 'Nom': row[0], 'Prenom': row[1], 'Date': dt}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_lbppresence.csv",index=False)
    else:
        present=-1  
    conn.close()
    return present
def hogpresence(id):
    present=0
    nvindice=int(id/10)
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_hogpresence.csv")
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="bank_of_faces")
    curs=conn.cursor()
    curs.execute('SELECT nom,prenom FROM faces where id =%s',(nvindice,))
    row = curs.fetchone()
    if row is not None:
        dt = datetime.now()
        df_id = df[df['Id'] == nvindice]
        for _, ligne in df_id.iterrows():
            date_presence = pd.to_datetime(ligne['Date'])
            deux_heures_avant = dt - timedelta(hours=2)
            if date_presence >= deux_heures_avant:
                print("ce personne est deja present dans ces 2 heurs")
                present=1
                return present
        if present==0:
            df.loc[len(df)] = {'Id': nvindice, 'Nom': row[0], 'Prenom': row[1], 'Date': dt}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/bank_of_hogpresence.csv",index=False)
    else:
        present=-1  
    conn.close()
    return present