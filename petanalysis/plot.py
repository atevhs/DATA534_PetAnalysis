try:
    import pandas as pd
    import seaborn as sns
    import matplotlib.pylab as plt
    
    import usrerror as err
    
    def visualize():

        dogs = pd.read_csv("Dog Data all.csv")

        while True:
            try:
                print(("Select one of these menu options:\n"
                "1    : Plot a histogram of male and female adoptable dogs in each age group.\n"
                "2    : View a heat map of dog sizes in each age group.\n"
                "x    : Quit the session"))

                usrinput = input("Enter your selection: ")

                if usrinput == "x":
                    print("\nThank you for using the pet analysis tool. Good-bye.")
                    break 

                if usrinput == "1":
                    age_histogram(dogs)
                elif usrinput == "2":
                    size_heatmap(dogs)
                elif not(usrinput):
                    raise EOFError
                else:
                    raise err.usrInputError(usrinput)
            
            except EOFError:
                print("\nAn input is required, please try again.\n")
            except err.usrInputError as uie:
                print("")
                print(uie.value,"is an invalid menu option, please try again.\n")
    
    def age_histogram(df):
        
        df['age'] = pd.Categorical(df['age'],categories=['Baby','Young','Adult','Senior'],ordered=True)
        sns.catplot(data=df, x="age", hue="gender", kind="count")
        plt.title("Current Age, Per Gender, Distribution of Adoptable Dogs")
        plt.show()

    def size_heatmap(df):
        
        df['age'] = pd.Categorical(df['age'],categories=['Baby','Young','Adult','Senior'],ordered=True)
        df['size'] = pd.Categorical(df['size'],categories=['Extra Large','Large','Medium','Small'],ordered=True)
        sns.displot(df, x="age", y="size", binwidth=(2, .5), cbar=True)
        plt.title("Current Size and Age Distribution of Adoptable Dogs")
        plt.show()

except ImportError as ierr:
    print("The following import error occured in the plot module:",ierr)
except FileNotFoundError as nof:
    print("The 'Dog Data all.csv' file was not found.")
except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")