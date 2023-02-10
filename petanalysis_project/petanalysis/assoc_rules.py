import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth
from mlxtend.frequent_patterns import association_rules

def read_data_file(filename):
    """
    Summary : This function reads the data from filename
    Input Parameters : str - filename
    Returns : df - dataframe
    """
    try:
        df = pd.read_csv(filename)
        
        return df
    
    except Exception as err:
        print(f"File not found! Unexpected {err=}, {type(err)=}")
        raise
        

##Data Wrangling

##Spliting breeds attribute to primary, secondary, mixed and unknown

def file_data_wrangle(df):
    """
    Summary : This function is for wrangling data, pre-processing and One-hot encoding
    Input : dataframe
    Returns : dataframe
    """
    try:
        df_new = df[["species","breeds","colors","age","gender","size","coat","attributes","environment","tags","name"]]

        ls = df_new["breeds"].str.split(",", expand=True)

        ls.rename(columns = {0:'Primary_breed',
                         1:'Secondary_breed',
                         2:'Mixed_breed',
                         3:'Unknown_breed'}, 
                inplace = True)

        ls["Primary_breed"] = ls["Primary_breed"].str.replace("{'primary':","", regex=True)

        ls["Secondary_breed"] = ls["Secondary_breed"].str.replace("'secondary': ","", regex=True)

        ls["Mixed_breed"] = ls["Mixed_breed"].str.replace("'mixed':","", regex=True)

        ls["Unknown_breed"] = ls["Unknown_breed"].str.replace("'unknown': ","", regex=True)

        ls["Unknown_breed"] = ls["Unknown_breed"].str.replace("}","", regex=True)

        df1 = pd.concat([df_new, ls], axis=1, join="inner")

    ##Spliting colors attribute to primary, secondary, mixed and unknown

        ls1 = df_new["colors"].str.split(":", expand=True)

        ls1[1] = ls1[1].str.replace(", 'secondary'","", regex=True)
        ls1[2] = ls1[2].str.replace(", 'tertiary'","", regex=True)
        ls1[3] = ls1[3].str.replace("}","", regex=True)

        ls1.rename(columns = {1:'Primary_color',
                         2:'Secondary_color',
                         3:'Tertiary_color'}, 
                inplace = True)

        ls1.drop(columns=0, inplace=True)

        df2 = pd.concat([df1, ls1], axis=1, join="inner")

    ##Spliting attributes to spayed_neutered, house_trained, declawed, special_needs and shots_current

        ls2 = df2["attributes"].str.split(",", expand=True)

        ls2[0]=ls2[0].str.replace("{'spayed_neutered':","", regex=True)
        ls2[1]=ls2[1].str.replace("'house_trained':","", regex=True)
        ls2[2]=ls2[2].str.replace("'declawed': ","", regex=True)
        ls2[3]=ls2[3].str.replace("'special_needs': ","", regex=True)
        ls2[4]=ls2[4].str.replace("'shots_current': ","", regex=True)
        ls2[4]=ls2[4].str.replace("}","", regex=True)

        ls2.rename(columns = {0:'spayed_neutered',
                         1:'house_trained',
                         2:'declawed',
                         3:'special_needs',
                         4:'shots_current'}, 
                inplace = True)

        df3 = pd.concat([df2, ls2], axis=1, join="inner")

    ##Spliting environment to children, dogs and cats

        ls3 = df3["environment"].str.split(",", expand=True)

        ls3[0]=ls3[0].str.replace("{'children':","", regex=True)
        ls3[1]=ls3[1].str.replace("'dogs': ","", regex=True)
        ls3[2]=ls3[2].str.replace("'cats': ","", regex=True)
        ls3[2]=ls3[2].str.replace("}","", regex=True)

        ls3.rename(columns = {0:'env_children',
                         1:'env_dogs',
                         2:'env_cats'}, 
                inplace = True)

        pets_data = pd.concat([df3, ls3], axis=1, join="inner")

        pets_data.drop(columns=["breeds","colors","attributes","environment"], inplace=True)

        pets_data["tags"] = pets_data["tags"].str.replace("\\[]","N/A",regex=True)

        pets_data["coat"] = pets_data["coat"].fillna("N/A")

        ##Getting rid of name as it doesn't qualify for calculating associations
        ##species and declawed as no variation in data

        pets_data.drop(columns=["name","species","declawed"], inplace=True)
        
        df_dummy = pd.get_dummies(pets_data[['age', 'gender','size','coat','Primary_breed','Secondary_breed','Primary_color','Secondary_color']])
        
        pets_data = pd.concat([df_dummy, pets_data], axis=1, join="inner")

        pets_data.drop(columns=['age', 'gender','size','coat','Primary_breed','Secondary_breed','Primary_color','Secondary_color','tags'],
              inplace=True)
        
        ls = ['Mixed_breed','Unknown_breed','Tertiary_color','spayed_neutered','house_trained','special_needs','shots_current','env_children','env_dogs','env_cats']

        try:
            for i in ls:
                pets_data[i] = pets_data[i].str.strip().apply(lambda x: 1 if x=='True' else 0)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            pass
        
        return pets_data
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def assoc_rules(min_supp=0.1, min_conf=0.8, sort_by_col='lift', rule_cnt=25):
    """
    Summary : This function is for calculating association rules
    Input :
    ------
        min_supp (default=0.1) type:float
        min_conf (default=0.8) type:float
        sort_by_col (default='lift') type:str
        rule_cnt (default=25) type:int
    Returns :
    --------
        dataframe
    """
    try: 
        df = read_data_file("petanalysis/Dog Data all.csv")

        ##Wrangle the datafile

        pets_data_df = file_data_wrangle(df)
        
        if (min_supp >=0 and min_supp<=1): 
            frequent_itemsets = apriori(pets_data_df, min_support=min_supp, use_colnames=True)
        else: 
            print("min_support should be between 0 and 1")
            
        if (min_conf >=0 and min_conf<=1):
            ar_data = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_conf)
        else:
            print("min_confidence should be between 0 and 1")
            
        dat = ar_data.sort_values(by=[sort_by_col],ascending=False).head(rule_cnt)
        
        return dat
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
