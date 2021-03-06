# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.exceptions.base_class_cannot_be_instantiated import BaseClassCannotBeInstantiated
from source.util.assertor import Assertor
from rpy2.robjects import r, numpy2ri
import pandas as pd
import numpy as np
import gc


class NormalityTest:
    """
    Superclass for which all normality tests are subclassed.

    """

    def __init__(self, df: pd.DataFrame = None):
        """
        Constructor / Initiate the class

        Parameters
        ----------
        df      : pandas.DataFrame
                  df to be analysed

        """
        if type(self) == NormalityTest:
            raise BaseClassCannotBeInstantiated(
                "base class '{}' cannot be instantiated".format(self.__class__.__name__))

        Assertor.evaluate_pd_dataframe(df)
        r('if (!is.element("MVN", installed.packages()[,1])){ '
          'install.packages("MVN", dep = TRUE)}')
        self.df = numpy2ri.numpy2ri(np.array(df))
        gc.collect()
