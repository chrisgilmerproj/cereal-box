def values(include=None):
	"""
	Usage:
		cereal_box.register(Model, [], serializer=values())
		cereal_box.register(Model, [], serializer=values(['id', 'name']))
	"""
	include = include or []
	def values_fn(queryset):
		"""
		Serializer to values(*%s) of queryset
		""" % include
		return queryset.values(*include)
	return values_fn
