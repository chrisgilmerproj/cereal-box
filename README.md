# cereal-box

## Description
cereal-box is a serialization library that exposes defined functions through a custom Django template tag and a JSON API.

## Example
	# models.py
	from django.db import models
	class Example(models.Model):
		text = models.CharField(max_length=20)


	import cereal
	cereal.register(Example, [cereal.functions.filter()])

...

	import cereal
	cereal.call('example', 'filter')
