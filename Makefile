tdd:
	clear
	watchmedo shell-command --patterns='*.py' --recursive --command='clear;flake8 . && py.test'
