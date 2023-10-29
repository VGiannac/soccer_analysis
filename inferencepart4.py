import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

class Inference:
    def __init__(self, data_url):
        """
        Constructor for the Inference class.

        Args:
            data_url (str): The file path or URL for the data that has to be loaded.
        """
        self.data = pd.read_csv(data_url)

    def scatter_plot_spi1_spi2(self):
        """
        scatter_plot_spi1_spi2: Plot SPI1 vs SPI2 in a scatter plot.

        The relationship between the 'spi1' and 'spi2' columns can be seen using the scatter plot produced by this method.
        """
        plt.scatter(self.data['spi1'], self.data['spi2'])
        plt.title("Scatter Plot of SPI1 vs SPI2")
        plt.xlabel("SPI1")
        plt.ylabel("SPI2")
        plt.show()

    def boxplot_importance1(self):
        """
        boxplot_importance1: Prepare an Importance1 boxplot.

        In order to see the distribution of the 'importance1' column, this method creates a boxplot.
        """
        sns.boxplot(x='importance1', data=self.data)
        plt.title("Boxplot of Importance1")
        plt.xlabel("Importance1")
        plt.show()
    
    def catplot_league_proj_score1(self):
        """
        Set a league vs. proj_score1 catplot.

        This method generates a categorical plot (catplot) to visualize the relationship between the 'league' and 'proj_score1' columns.
        """
        league_initials = {
            "Premier League": "PL",
            "La Liga": "LL",
            "Bundesliga": "BL",
            "Chinese League": "CL",
            "French Ligue 1": "FL",
            "Italy Serie A": "IT",
            "Portuguese Liga": "PL",
            "Spanish Primera Division": "SP"
        }
        self.data['league_initials'] = self.data['league'].map(league_initials)
        warnings.simplefilter(action='ignore', category=FutureWarning)
        sns.catplot(data=self.data, x="league_initials", y="proj_score1", alpha=0.5)

     # ... rest of your methods ...