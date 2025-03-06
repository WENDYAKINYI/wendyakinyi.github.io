import pandas as pd
import matplotlib.pyplot as plt
from contents.helper_functions.hf import retrieve_files, record_loader_gen


class BabyNames:
    """
    A class to analyze baby name trends based on Social Security Administration data.

     Methods:
    - __init__(): Initializes the BabyNames instance by loading data into a pandas DataFrame.
    - sort_data(): Sorts the names DataFrame in ascending order by year.
    - m_f_names(start_year=1880, end_year=2022): Creates a line plot showing the total number of male
      and female names for each year.
    - most_popular_ever(): Identifies the top 3 most popular names throughout history and plots their
      evolution over the years.
    - unisex(): Calculates and creates a histogram over the years for the total number of births
      for every name that was given to both men and women.
    - unisex_evolution(): Allows the user to select unisex names and plots the number of births over
      the years for every selected name.

    """

    def __init__(self):
        """
        Initializes the BabyNames instance by loading data into a pandas DataFrame.

        """
        file_paths = retrieve_files('.txt')
        records = record_loader_gen(file_paths)
        self.names_df = pd.DataFrame(
            records, columns=['Name', 'Gender', 'Births', 'Year'])
        self.sort_data()

    def sort_data(self):
        """
        Sorts the names DataFrame in ascending order by year.
        """
        self.names_df.sort_values(by='Year', inplace=True)

    def m_f_names(self, start_year=1880, end_year=2022):
        """
        Creates a line plot showing the total number of male and female names for each year.

        Parameters:
        - start_year (int): The starting year for the analysis.
        - end_year (int): The ending year for the analysis.
        """
        # Filter DataFrame
        filtered_df = self.names_df[(self.names_df['Year'] >= start_year) & (
            self.names_df['Year'] <= end_year)]
        gender_counts = filtered_df.groupby(['Year', 'Gender'])[
            'Births'].sum().unstack()
        gender_counts.plot(kind='line')
        plt.title('Total Male and Female Names from {} to {}'.format(
            start_year, end_year))
        plt.xlabel('Year')
        plt.ylabel('Total Names')
        plt.legend(['Female', 'Male'])
        plt.show()

    def most_popular_ever(self):
        """
        Identifies the top 3 most popular names throughout history and plots their evolution over the years.
        """
        # Top 3 most popular names
        top_names = self.names_df.groupby(
            'Name')['Births'].sum().sort_values(ascending=False).head(3)
        print(top_names)

        for name in top_names.index:
            name_df = self.names_df[self.names_df['Name'] == name].groupby('Year')[
                'Births'].sum()
            plt.plot(name_df.index, name_df.values, label=name)
        plt.title('Top 3 Most Popular Names Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Number of Births')
        plt.legend()
        plt.show()

    def unisex(self):
        """
        Calculates and creates a histogram over the years for the total number of births
        for every name that was given to both men and women.
        """
        # Names given to both genders
        gender_names = self.names_df.groupby('Name')['Gender'].nunique()
        unisex_names = gender_names[gender_names == 2].index
        unisex_df = self.names_df[self.names_df['Name'].isin(unisex_names)]
        yearly_births = unisex_df.groupby('Year')['Births'].sum()
        yearly_births.plot(kind='bar')
        plt.title('Total Unisex Name Births by Year')
        plt.xlabel('Year')
        plt.ylabel('Total Births')
        plt.show()

    def unisex_evolution(self):
        """
        Allows the user to select unisex names and plots the number of births over the years
        for every selected name.
        """
        # Unisex names
        gender_names = self.names_df.groupby('Name')['Gender'].nunique()
        unisex_names = gender_names[gender_names == 2].index
        print("Unisex Names:", unisex_names.tolist())
        chosen_names = []
        while True:
            name = input("Enter a name to analyze or 'q' to quit: ")
            if name == 'q':
                break
            if name in unisex_names:
                chosen_names.append(name)
            else:
                print("Please enter a valid unisex name.")

        for name in chosen_names:
            name_df = self.names_df[self.names_df['Name'] == name]
            total_births_per_year = name_df.groupby('Year')['Births'].sum()

            plt.plot(total_births_per_year.index,
                     total_births_per_year.values, label=f"{name}")

        plt.title('Evolution of Chosen Unisex Names')
        plt.xlabel('Year')
        plt.ylabel('Number of Births')
        plt.legend()
        plt.show()


# if __name__ == "__main__":
#     bn = BabyNames()
#     bn.m_f_names()
#     bn.most_popular_ever()
#     bn.unisex()
#     bn.unisex_evolution()
