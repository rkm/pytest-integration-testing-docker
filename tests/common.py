"""
Common test code
"""


def app_test(app):
	"""
	Simple test to show that both the unit (in-memory dict store) and integration (MongoDB
	provided by Docker) tests pass.
	:param app:
	:return:
	"""

	assert app.get_data_count() == 0, ''

	app.run({'test': 'data'})
	assert app.get_data_count() == 1, ''

	app.clear_data()
	assert app.get_data_count() == 0, ''
