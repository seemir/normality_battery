# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.util.dataframe_generator import DataFrameGenerator
from source.util.dataframe_generator import Generator
from tests.test_setup import TestSetup
import pandas as pd
import pytest as pt
import numpy as np
import shutil
import os


class TestDataFrameGenerator(TestSetup):

    def test_df_generator_is_subclass_of_abstract_generator(self):
        """
        Test that DataFrameGenerator is subclass of AbstractGenerator

        """
        assert isinstance(self.dfg, Generator)
        assert issubclass(self.dfg.__class__, Generator)

    @pt.mark.parametrize("invalid_seed", [{}, [], (), 'test', True])
    def test_raise_typeerror_when_seed_is_not_int(self, invalid_seed):
        """
        Test that TypeError is thrown when invalid datatype of seed is passed to
        DataFrameGenerator()

        """
        pt.raises(TypeError, self.dfg.__class__, invalid_seed)

    def seed_gets_configured(self):
        """
        Test that seed gets configured when passed through constructor

        """
        assert self.dfg.seed == self.seed

    def test_seed_always_produces_same_df(self):
        """
        Test that the seed configured produces the same df

        """
        arrays = [[[-0.6153267, 0.57127751], [-0.36840213, -0.48346131]],
                  [[1.32508055, -0.48346131], [-0.36840213, 0.11317361]],
                  [[-0.6153267, 0.85020204], [-0.20843305, 0.57127751]]
                  ]
        correct_dfs = [pd.DataFrame(np.array(arr)) for arr in arrays]

        for i, method in enumerate(self.dfg.__getmethods__()):
            test_df = getattr(DataFrameGenerator(seed=90210, size=(2, 2)), method)()
            pd.testing.assert_frame_equal(test_df, correct_dfs[i])

    def test_correct_number_of_calls_made_to_method(self, mocker):
        """
        Mocker of calls to methods in DataFrameGenerator

        """
        for method in self.dfs.keys():
            mocker.spy(DataFrameGenerator, method)
            getattr(self.dfg, method)()
            assert getattr(DataFrameGenerator, method).call_count == 1

    @pt.mark.parametrize("invalid_df", [{}, [], (), 'test', True])
    def test_typeerror_raised_when_non_pd_data_frame_passed_in_to_excel(self, invalid_df):
        """
        TypeError is thrown when non - pd.DataFrame object is passed in to_excel() method

        """
        with pt.raises(TypeError):
            self.dfg.to_excel(invalid_df)

    def test_to_excel_produces_excel_file_with_data_frame(self):
        """
        Static to_excel() method produces excel file with dataframe

        """
        for df in self.dfs.values():
            input_df = pd.DataFrame(df)
            file_dir = 'reports/xlsx'
            self.dfg.to_excel(df=input_df, file_dir=file_dir)
            saved_df = pd.read_excel(file_dir + '/' + os.listdir(file_dir)[-1], index_col=0)
            pd.testing.assert_frame_equal(saved_df, input_df)
        try:
            shutil.rmtree("reports")
        except OSError:
            pass

    def test_os_error_is_thrown_when_dir_cannot_be_created(self):
        """
        OSError raised when invalid file_dir is passed to to_excel() method

        """
        input_df = pd.DataFrame(np.random.rand(30, 30))
        invalid_file_dir = '._?`/1234'  # Invalid dir name
        with pt.raises(OSError):
            self.dfg.to_excel(df=input_df, file_dir=invalid_file_dir)

    @pt.mark.parametrize("dim", [(30, 30), (30, 50), (50, 30)])
    def test_correct_dimensions_in_produced_df(self, dim):
        """
        Shape of df produced are same as configured

        """
        for method in self.dfg.__getmethods__():
            df = DataFrameGenerator(seed=90210, size=dim)
            df = getattr(df, method)()
            assert df.shape == dim
            assert np.prod(df.shape) == np.prod(dim)

    def test_not_possible_to_configure_negative_dimensions(self):
        """
        Negative dimensions are not allowed

        """
        with pt.raises(ValueError):
            DataFrameGenerator(seed=90210, size=(-100, 100))

    def test_normal_data_frame_produces_data_with_mean_close_to_value(self):
        """
        Data in dataframe produced by normal_data_frame() have mean close to configured mean value

        """
        # Default case, mean = 0
        df = self.dfs['normal_data_frame']
        for i, column in df.iteritems():
            assert np.mean(column.to_list()) == pt.approx(0, abs=1)

        for i, row in df.iterrows():
            assert np.mean(row.to_list()) == pt.approx(0, abs=1)

    def test_to_excel_from_df_method(self):
        """
        Possible to save produced df to excel using excel=True argument in df methods, i.e.
        uniform_data_frame(), normal_data_frame() and mixed_data_frame()

        """
        file_dir = 'reports/xlsx'
        for method in self.dfs.keys():
            input_df = getattr(self.dfg, method)(excel=True)
            saved_df = pd.read_excel(file_dir + '/' + os.listdir(file_dir)[-1], index_col=0)
            pd.testing.assert_frame_equal(saved_df, input_df)
        try:
            shutil.rmtree("reports")
        except OSError:
            pass
