.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations -n $(MIGRATION_NAME)

.PHONY: run
run:
	python manage.py runserver


.PHONY: run_command
run_command:
	python manage.py $(COMMAND)


.PHONY: test
test:
	python manage.py test --keepdb --parallel=1

.PHONY: test_pattern
test_pattern:
	python manage.py test --keepdb --parallel=1 --pattern=$(PATTERN)

.PHONY: shell
shell:
	python manage.py shell