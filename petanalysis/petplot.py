class usrInputError(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return(repr(self.value))

try:
    import pandas as pd
    import seaborn as sns
    import matplotlib.pylab as plt
    
    import usrerror as err
    
    def visualize():
    
        """
        Summary : This is the main visualization function used in the petanalysis package. The user will be prompted to select an option from a menu and then the appropriate function for displaying the desired plot will be called. The menu will reappear until the user enters the option 'x' to exit the program.
        Input : none
        Returns : none
        """

        dogs = pd.read_csv("petanalysis/Dog Data all.csv")

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
        """
        Summary : This is a support function that takes in a dataframe of dog data and plots a histogram of the ages of adoptable dogs based on gender. 
        Input : a dataframe
        Returns : none
        Output: the histogram plot, count of adoptable dog ages based on age and gender.
        """
        
        df['age'] = pd.Categorical(df['age'],categories=['Baby','Young','Adult','Senior'],ordered=True)
        sns.catplot(data=df, x="age", hue="gender", kind="count")
        plt.title("Current Age, Per Gender, Distribution of Adoptable Dogs")
        plt.show()

    def size_heatmap(df):
        """
        Summary : This is a support function that takes in a dataframe of dog data and plots a heatmap of the ages and sizes of adoptable dogs. 
        Input : a dataframe
        Returns : none
        Output: the heatmap, count of adoptable dog for each age and size group.
        """
        
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
