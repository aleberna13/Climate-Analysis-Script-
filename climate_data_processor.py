import pandas as pd;
#importo i df, climate data clean revisionato sarebbe il file climate data clean dove ho eliminato
#direttamente da excel alcune colonne che non mi servivano
df=pd.read_excel("climate data clean revisionato.xlsx");
df2=pd.read_csv("variables.csv");
#creo una lista con i nomicdei codici delle variabili del primo df
codici=list(df.columns);
#creo un dataframe con una sola colonna fatta dei codici
dfcodici=pd.DataFrame(codici);
dfcodici.rename(columns={0: "code"}, inplace=True);
#creo un nuovo dataframe facendo una join con il df dei codici e quello delle variabili
df3=dfcodici.merge(df2, how='left', left_on='code', right_on='Name');
#creo una lista dei nomi da sostituire ai codici nelle variabili
domande=list(df3['Label']);
#cambio i nomi delle variabili
df.columns=domande;
#definisco una funzione per sostituire i valori mancanti con la media dei valori in colonna
def nantomean(a,b):
    a[b]=a[b].fillna(a[b].mean());
k='Country';
#sostituisco tutti i valori mancanti con le medie
for i in df.columns:
    if i != k:
        nantomean(df, i);
#trasformo tutto in interi
for i in df.columns:
    if i != k:
        df[i]=df[i].astype(int);
#MI porto tutte le domande su una sola colonna e creo la variabile questions
dfpivot=pd.melt(df, id_vars=["Respondent's identification number", "Country"], var_name='questions', value_name='score');
#salvo il mio database
dfpivot.to_csv('climate data clean pivot.csv', index=False);
