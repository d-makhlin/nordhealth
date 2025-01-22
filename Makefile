run:
	pip install -r requirements.txt
	python3 main.py

test:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
	pytest --verbose --disable-warnings --cache-clear
	rm -rf .pytest_cache