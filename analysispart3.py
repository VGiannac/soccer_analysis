import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ExploratoryDataAnalysis:
    def __init__(self, data_url):
        """
        Constructor for ExploratoryDataAnalysis class.

        Args:
            data_url (matches_latest_data_url): The file path or URL for the data that has to be loaded.
        """
        self.data = pd.read_csv(data_url)
    
    def unique_leagues(self):
        """
        Obtain the unique soccer leagues in the dataset.

        Returns:
            numpy.ndarray: An array containing unique league names.
        """
        return self.data['league'].unique()

    def teams_value_counts(self):
       """
        Obtain the value counts of participating teams in matches.

        Returns:
            pandas.Series: A Series with the counts of each team's appearances in matches.
        """
        return self.data[['team1', 'team2']].stack().value_counts()

    def summary_statistics(self):
         """
        Determine the summary statistics for the dataset.

        Returns:
            pandas.DataFrame: A DataFrame containing statistical measures of the dataset.
        """
        return self.data.describe()

    def missing_value_percentage(self):
        """
        Determine the percentage of missing values for each column in the dataset.

        Returns:
            pandas.Series: A Series with the percentage of missing values for each column.
        """
        return self.data.isnull().mean() * 100
            
    # Define other methods for EDA tasks.

        



