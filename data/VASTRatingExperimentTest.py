import unittest
import matplotlib.pyplot as plt
import VASTRatingExperiment

class TestImageAnalysis(unittest.TestCase):
    def test_graph_generation(self):
        fig = VASTExperiment.fig;         ax = VASTExperiment.axes
        
        self.assertIsInstance(fig, plt.Figure)  # confirm figure is returned
        self.assertEqual(len(ax), 3) 

if __name__ == "__main__":
    unittest.main()
