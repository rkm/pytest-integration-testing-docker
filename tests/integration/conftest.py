import os

import pytest
import yaml

import testeroni_app.settings as s
from testeroni_app import App

SUPPORTED_CI_ENVS = ['TRAVIS', 'CI_DEV_LOCAL']

s.MDB_HOST = 'localhost'
s.MDB_DATABASE = 'test_db'
s.MDB_COLLECTION = 'test_collection'

with open("tests/integration/docker-compose.yml", 'r') as stream:
	try:
		SERVICE = yaml.load(stream)['services']['mongo-db']
		ENV = SERVICE['environment']

		s.MDB_PORT = SERVICE['ports'][0].split(':')[0]
		s.MDB_USER = ENV['MONGO_INITDB_ROOT_USERNAME']
		s.MDB_PASS = ENV['MONGO_INITDB_ROOT_PASSWORD']

	except yaml.YAMLError as exc:
		print(exc)


@pytest.fixture(scope="session", autouse=True)
def assert_ci_build():
	"""
	Assert we are only running integration tests in a CI environment
	:return:
	"""

	def check_var(var):
		return var in os.environ and os.environ.get(var).upper() == 'TRUE'

	is_ci = check_var('CI')
	assert is_ci, 'Expected to be running in a CI environment'

	ci_supported = any(check_var(env) for env in SUPPORTED_CI_ENVS)
	assert ci_supported, 'Expected to detect a supported CI environment'


@pytest.fixture(scope="function")
def docker_test_app():
	assert s.MDB_DATABASE.upper() != 'PROD', 'Should not test on the production database...'

	return App()
