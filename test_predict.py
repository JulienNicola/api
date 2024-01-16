import unittest
import pandas as pd
import pickle
from typing import Dict
from fast_api import predict_credit, ClientData

data=pd.read_csv("test_sample.csv")

class TestPredictCredit(unittest.TestCase):
    def setUp(self):
        # Load the pre-trained model and threshold for testing
        with open("lgbm.pkl", "rb") as pickle_file:
            self.classifier = pickle.load(pickle_file)

        with open("threshold.pkl", "rb") as pickle_file:
            self.threshold = pickle.load(pickle_file)

    def test_predict_credit1(self):
        # Create a sample request and client data
        request = "sample_request"
        id=data.loc[0, 'SK_ID_CURR']
        clt=data.iloc[0,1:]
        client_data = ClientData(client_id=int(id), features=clt.to_dict())

        # Call the function and get the result
        result = predict_credit(request, client_data)

        # Check if the output is as expected for an accepted case
        self.assertEqual(result['client_id'], int(id))
        self.assertTrue(0 <=result['score']<= 1)
        self.assertTrue(result['decision'])

    def test_predict_credit2(self):
        # Create a sample request and client data
        request = "sample_request"
        id=data.loc[1, 'SK_ID_CURR']
        clt=data.iloc[1,1:]
        client_data = ClientData(client_id=int(id), features=clt.to_dict())

        # Call the function and get the result
        result = predict_credit(request, client_data)

        # Check if the output is as expected for a declined case
        self.assertEqual(result['client_id'], int(id))
        self.assertTrue(0 <=result['score']<= 1)
        self.assertTrue(result['decision'])

if __name__ == '__main__':
    unittest.main()