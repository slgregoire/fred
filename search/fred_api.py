import requests
import pandas as pd

class searcher(object):
	'''this class defines a set of objects that are able to access FRED's API, search for a data series based upon the search terms that user enters, and then return the meta data for search term matches. The meta data that is ultimately printed out are the series title and series id.'''

	def __init__(self):
		#initializes object with FRED's API base search url.
		self.url = 'http://api.stlouisfed.org/fred/series/search'
	
	def __call__(self, search_text):
		#pulls search results based upon the search_text entered by the user. Returns complete data set converted from json to python.	
		request_params = {
					'search_text': search_text,
					 'api_key':'82101274da6dbda5de2d568e76b9d6a4',
					 'file_type':'json',
					 'limit':'10', #default value of number of search results to return
					 'order_by':'popularity' #results ordered by popularity are by default sorted in desc order
				 	 }			

		self.results = requests.get(self.url, params = request_params).json()
		
	def shorten_data(self):
		#takes complete search results, converts to DataFrame, and only retains key columns.
		df = pd.DataFrame(self.results['seriess'])

		#set of columns from complete dataset that we wish to retain.
		columns_to_keep = ['id', 
							'title',
							'observation_start',
							'observation_end',
							'frequency',
							'units_short',
							'seasonal_adjustment_short']

		self.df = df.ix[:, columns_to_keep]

	def make_title_list(self):
		#makes a list out of the titles of the search results
		self.title_list = self.df.ix[:, 'title']

		return self.title_list 
