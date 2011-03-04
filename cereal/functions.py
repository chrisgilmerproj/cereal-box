import cereal

def filter(manager='_default_manager'):
	"""
	Usage:
		cereal.register(Model, [filter()]) # Defaults to _default_manager
		cereal.register(Model, [filter('objects')])
	"""
	def filter_fn(model, **kwargs):
		"""
		Applied filter on Model.%s
		""" % manager
		return cereal.ize(getattr(model, manager).filter(**kwargs))
	filter_fn.__name__ = 'filter'
	return filter_fn

def page_filter(manager='_default_manager'):
	"""
	Extends filter function to return pagination data.
	"""
	def filter_fn(model, **kwargs):
		"""
		Applied paginated filter on Model.%s
		""" % manager
		ret = getattr(model, manager).filter(**kwargs)
		return {'count':ret.count(), 'objects':cereal.ize(ret)}
	filter_fn.__name__ = 'page_filter'
	return filter_fn
