import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

class DataSummary:
    def __init__(self, data_url):
        """
        Constructor for DataSummary class.

        Args:
            data_url (matches_latest_data_url): The file path or URL for the data that has to be loaded.
        """
        self.data = pd.read_csv(data_url)

    def display_head(self):
        """
        Show the dataset's initial few rows.
        """
        display(self.data.head())

    def display_tail(self):
        """
        Show the dataset's final few rows.
        """
        display(self.data.tail())

    def get_shape(self):
        """
        Determine the dataset's shape, or the total number of rows and columns.

        Returns:
            tuple: A tuple that indicates how many rows and columns there are.
        """
        return self.data.shape

    def missing_value_percent(self):
        """
        Determine each column's percentage of missing values.

        Returns:
            pandas.Series: A series that shows each column's percentage of missing values.
        """
        return self.data.isna().sum() / len(self.data) * 100

    def data_info(self):
        """
        Use the data.info() method to display basic dataset information.
        """
        self.data.info()

    def categorical_descriptive_statistics(self):
        """
        For columns with categories, generate descriptive stats.

        Returns:
            pandas.DataFrame: A DataFrame with descriptive statistics for columns that are classified.
        """
        return self.data.describe(include=['object'])

    def numerical_descriptive_statistics(self):
        """
        Calculate the descriptive statistics for columns with numbers.

        Returns:
            pandas.DataFrame: A DataFrame containing descriptive statistics for numerical columns.
        """
        return self.data.describe()

    def data_types(self):
        """
        Find out what kind of data each column in the dataset is.

        Returns:
            pandas.Series: A Series containing the data types of each column.
        """
        return self.data.dtypes

    # ... rest of your methods ...
    