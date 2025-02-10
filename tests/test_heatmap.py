import unittest
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestHeatmapPlot(unittest.TestCase):
    def setUp(self):
        self.data = np.random.rand(10, 10)
        self.df = pd.DataFrame(self.data)
        
    def test_heatmap_creation(self):
        plt.figure(figsize=(10,8))
        heatmap = sns.heatmap(self.df)
        self.assertIsNotNone(heatmap)
        plt.close()
        
    def test_heatmap_with_annotations(self):
        plt.figure(figsize=(10,8))
        heatmap = sns.heatmap(self.df, annot=True)
        self.assertIsNotNone(heatmap)
        self.assertTrue(len(heatmap.texts) > 0)
        plt.close()
        
    def test_heatmap_colormap(self):
        plt.figure(figsize=(10,8))
        heatmap = sns.heatmap(self.df, cmap='YlOrRd')
        self.assertIsNotNone(heatmap)
        self.assertEqual(heatmap.get_cmap().name, 'YlOrRd')
        plt.close()
        
    def test_heatmap_with_mask(self):
        mask = np.zeros_like(self.data)
        mask[np.triu_indices_from(mask)] = True
        plt.figure(figsize=(10,8))
        heatmap = sns.heatmap(self.df, mask=mask)
        self.assertIsNotNone(heatmap)
        plt.close()
        
    def test_heatmap_dimensions(self):
        plt.figure(figsize=(10,8))
        heatmap = sns.heatmap(self.df)
        self.assertEqual(heatmap.get_array().shape, (10, 10))
        plt.close()

if __name__ == '__main__':
    unittest.main()
