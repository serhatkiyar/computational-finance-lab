import unittest
import pandas as pd
import numpy as np
from ols_utils import validate_ols_input

class TestOLSValidation(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'SPY': [1.0, 2.0, 3.0],
            'VIX': [10.0, 20.0, 30.0]
        })

    def test_valid_data(self):
        sonuc = validate_ols_input(self.df, 'SPY', ['VIX'])
        self.assertTrue(sonuc)

    def test_missing_column(self):
        with self.assertRaises(ValueError):
            validate_ols_input(self.df, 'Altin', ['VIX'])

    def test_nan_values(self):
        bozuk_df = self.df.copy()
        bozuk_df.iloc[0, 0] = np.nan

        with self.assertRaises(ValueError):
            validate_ols_input(bozuk_df, 'SPY', ['VIX'])

    def test_inf_values(self):

        inf_df = self.df.copy()
        inf_df.iloc[0, 0] = np.inf

        with self.assertRaises(ValueError):
            validate_ols_input(inf_df, 'SPY', ['VIX'])


if __name__== '__main__':
    unittest.main()