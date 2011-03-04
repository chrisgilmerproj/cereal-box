from django.db import models

class Cereal(models.Model):
	name        = models.CharField(max_length=20)
	sugar_level = models.PositiveIntegerField()
	def __unicode__(self): return self.name

import cereal # Nevermind the naming snafu
cereal.register(Cereal, [cereal.functions.filter()])
