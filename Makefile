.PHONY: publish
publish:
	poetry publish --build --repository gitea
clean:
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete -or -type -name "dist" -delete
