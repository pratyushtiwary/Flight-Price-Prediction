import pandas as pd
import sklearn

def predict_price(cleaned_data):
	"""
		This module takes the cleaned_data, i.e. data cleaned using the clean_data module
		and returns the value predicted by the model
	"""

	model = pd.read_pickle("flight_rf.pkl")
	prediction = model.predict([cleaned_data])
	prediction = round(prediction[0],2)

	return prediction