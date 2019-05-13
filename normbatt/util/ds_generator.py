# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from normbatt.util.abstract_generator import AbstractGenerator
from prettytable import PrettyTable
import scipy.stats as stats
import numpy as np


class DescriptiveStatisticsGenerator(AbstractGenerator):
    """
    Class that generates descriptive statistics

    """

    def __init__(self, df, dim, digits):
        """
        Constructor / Initiate the class

        Parameters
        ----------
        df      : pandas.DataFrame
                  Dataframe for which one wants to generate / test
        dim     : string
                  indicate whether one wants to test for normality along the columns 'col' or rows
                  'row', default is 'col'
        digits  : integer
                  number of decimal places to round down

        """
        super().__init__(dim=dim, digits=digits)
        self.evaluate_pd_dataframe(df)
        self.evaluate_data_type({dim: str, digits: int})

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
        desc_table = PrettyTable(vrules=2)
        rnd, d = round, self.digits
        dim_name = 'col' if self.dim == 'col' else 'row'

        decs_header_names = [dim_name,
                             'mean', 'median',
                             'variance', 'stdev',
                             'kurtosis', 'skewness',
                             'min', 'max',
                             'quant (95%)']
        desc_table.field_names = decs_header_names

        vectors = self.df.iteritems() if self.dim == "col" else self.df.iterrows()

        for i, vector in vectors:
            desc_row = [rnd(i + 1, d),
                        rnd(np.mean(vector), d), rnd(np.median(vector), d),
                        rnd(np.var(vector), d), rnd(np.std(vector), d),
                        rnd(stats.kurtosis(vector), d), rnd(stats.skew(vector), d),
                        rnd(min(vector), d), rnd(max(vector), d),
                        rnd(np.quantile(vector, 0.95), d)]
            desc_table.add_row(desc_row)
            desc_table.align = "r"

        desc_table.title = 'Descriptive statistics ' + self.get_dimensions() + ' DataFrame(df)'
        return str(desc_table)
