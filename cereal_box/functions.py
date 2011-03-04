def filter(manager='_default_manager'):
	"""
	Usage:
		cereal_box.register(Model, [filter()]) # Defaults to _default_manager
		cereal_box.register(Model, [filter('objects')])
	"""
	def filter_fn(model, **kwargs):
		"""
		Applied filter on Model.%s
		""" % manager
		return getattr(model, manager).filter(**kwargs)
	filter_fn.__name__ = 'filter'
	return filter_fn
