
from ..common import app_test


def test_testeroni_integration(docker_test_app):
	app_test(docker_test_app)
