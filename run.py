
import sys

import testeroni_app


def main():
	app = testeroni_app.App()

	if '--clear' in sys.argv:
		app.clear_data()
		return

	app.run({'some': 'data'})
	print('Data in store: {}'.format(app.get_data_count()))


if __name__ == '__main__':
	main()
