def visualize():
    import pandas as pd
    import altair as alt

    dogs = pd.read_csv("Dog Data all.csv")

    while True:
        print(("Select one of these menu options:\n"
        "1    : Plot a histogram of the genders of dogs available for adoption.\n"
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
        
def age_histogram(df):
    alt.data_transformers.disable_max_rows()
    (alt.Chart(df).mark_bar().encode(
        alt.X('count()',title='Number of Dogs'),
        alt.Y('gender', type='nominal', title='Gender'))
     .properties(title='Current Gender Distribution of Adoptable Dogs', height = 300, width=600)
     .configure_axis(titleFontSize=14,labelFontSize=12)
     .configure_title(fontSize=16)).display()

def size_heatmap(df):
    alt.data_transformers.disable_max_rows()
    age_order = ['Baby','Young','Adult','Senior']
    (alt.Chart(df).mark_rect().encode(
        alt.X('age', type='nominal', title='Age Group', sort=age_order),
        alt.Y('size', type='nominal', title='Size Group'),
        color='count()')
     .properties(title='Current Size and Age Distribution of Adoptable Dogs', height = 300, width=600)
     .configure_axisX(titleFontSize=14,labelFontSize=12, labelAngle=0)
     .configure_axisY(titleFontSize=14,labelFontSize=12)
     .configure_title(fontSize=16)).display()