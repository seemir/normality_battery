# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.util.generator import Generator
from source.util.assertor import Assertor
from prettytable import PrettyTable
import scipy.stats as stats
import numpy as np
import pandas as pd


class DescriptiveStatistics(Generator):
    """
    Class that generates descriptive statistics

    """

    def __init__(self, df: pd.DataFrame, dim: str = 'col', digits: int = 5):
        """
        Constructor / Initiate the class

        Parameters
        ----------
        df      : pandas.DataFrame
                  Dataframe for which one wants to generate / test
        dim     : str
                  indicate whether one wants to test for normality along the columns 'col' or rows
                  'row', default is 'col'
        digits  : int
                  number of decimal places to round down

        """
        super().__init__(dim=dim, digits=digits)
        Assertor.evaluate_pd_dataframe(df)
        Assertor.evaluate_numeric_df(df)
        Assertor.evaluate_data_type({dim: str, digits: int})

        self.df = df
        self.dim = dim
        self.digits = digits

    def generate_descriptive_statistics(self):
        """
        Method that generates descriptive statistics from a pandas.DataFrame's column or row
        vectors.

        Returns
        -------
        Out     : str
                  String of descriptive statistics

        """
        desc_table = PrettyTable(vrules=2, hrules=3)
        rnd, d = round, self.digits
        dim_name = 'col' if self.dim == 'col' else 'row'

        decs_header_names = ['        ',
                             dim_name,
                             '      mean',
                             '      median',
                             '  variance',
                             '       stdev',
                             '  kurtosis',
                             '    skewness',
                             '       min',
                             '         max']

        desc_table.field_names = decs_header_names

        vectors = self.df.iteritems() if self.dim == "col" else self.df.iterrows()

        for i, vector in vectors:
            desc_row = [''] + [rnd(param, d) for param in
                               [i + 1, np.mean(vector), np.median(vector),
                                np.var(vector), np.std(vector),
                                stats.kurtosis(vector), stats.skew(vector),
                                min(vector), max(vector)]]
            desc_table.add_row(desc_row)
        desc_table.align = "r"
        return str(desc_table)
