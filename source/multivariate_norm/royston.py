# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.multivariate_norm.normality_test import NormalityTest
from rpy2.robjects import r
import pandas as pd
import gc


class Royston(NormalityTest):
    """
    Implements the Royston test for multivariate normality

    """

    def __init__(self, df: pd.DataFrame):
        """
        Constructor / Initiate the class

        Parameters
        ----------
        df      : pandas.DataFrame
                  df to be analysed

        """
        super().__init__(df)

    def run_royston_test(self):
        """
        Runs the Royston test for multivariate normality by delegating the task to the
        MVN module in r

        """
        r('require("MVN", character.only = TRUE)')
        r.assign("df", self.df)
        r('res <- mvn(df, mvnTest = "royston")')
        gc.collect()

    def print_results(self):
        """
        Gets the Royston test statistic and p-value

        Returns
        -------
        Out     : tuple
                  (royston test statistic, p-value)

        """
        self.run_royston_test()
        roy = r('as.numeric(res$multivariateNormality["H"])')
        p_roy = r('as.numeric(res$multivariateNormality["p value"])')
        return tuple(list(roy) + list(p_roy))
