
import pytest

from testeroni_app import App


@pytest.fixture(scope="function")
def dict_test_app():
	class DictApp(App):

		def __init__(self):
			self.collection = {}

		def run(self, data):
			self.collection.update(data)

		def get_data_count(self):
			return len(self.collection)

		def clear_data(self):
			self.collection = {}

	return DictApp()
