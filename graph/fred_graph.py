import requests
import pandas as pd
import os 

def fred_grapher(search_text):
	url = 'http://api.stlouisfed.org/fred/series/search'
	
	request_params = {'search_text': search_text,
			  'api_key':'82101274da6dbda5de2d568e76b9d6a4',
			  'file_type':'json',
			  'limit':'10', #default value of number of search results to return
			  'order_by':'popularity' #results ordered by popularity are by default sorted in desc order
	 }			

	results = requests.get(url, params = request_params).json()
	df = pd.DataFrame(results['seriess'])

	#grabbing the series id of the most popular search result
	series_id = df.ix[0, 'id']
	
	#now onto the portion of the code that imports and graphs the observations of the most popular series 
	url_data = 'http://api.stlouisfed.org/fred/series/observations'
	
	request_params = {'series_id': series_id,
				 'api_key':'82101274da6dbda5de2d568e76b9d6a4',
				 'file_type':'json'
			 	 }
		
	#req_json holds the json data that the get request returns		 	 
	raw_data = requests.get(url_data, params = request_params)
		
	#req_json holds the parsed json data, converted into a python dictinoary
	data = raw_data.json()
		
	#req_df holds the parsed json in a pandas dataframe
	data = pd.DataFrame(data['observations'])
		
	#transforming data and exporting to json
	data.drop(['realtime_start', 'realtime_end'], axis = 1, inplace = True)
	data_json = data.to_json(orient = 'records')
	
	return data_json

	
		

		