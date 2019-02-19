
import urllib.parse

from pymongo import MongoClient

from . import settings as s


class App:

	def __init__(self):

		auth = ''

		if s.MDB_USER:
			mdb_user = urllib.parse.quote_plus(s.MDB_USER)
			mdb_pass = urllib.parse.quote_plus(s.MDB_PASS)
			auth = f'{mdb_user}:{mdb_pass}@'

		conn_str = f'mongodb://{auth}{s.MDB_HOST}:{s.MDB_PORT}'
		print('\nConnection string: {}'.format(conn_str))

		self.client = MongoClient(conn_str)
		self.database = self.client[s.MDB_DATABASE]
		self.collection = self.database[s.MDB_COLLECTION]

	def run(self, data):
		print('Submitting data...')
		self.collection.insert_one(data)

	def get_data_count(self):
		return self.collection.count_documents({})

	def clear_data(self):
		print('Clearing data...')
		self.collection.drop()
