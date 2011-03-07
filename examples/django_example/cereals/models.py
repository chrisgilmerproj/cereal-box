from django.db import models

class Cereal(models.Model): # Nevermind the naming snafu
	name        = models.CharField(max_length=20)
	sugar_level = models.PositiveIntegerField()
	def __unicode__(self): return self.name

import cereal
cereal.register(Cereal, [cereal.functions.filter(),
	cereal.functions.page_filter()])
