import cereal

def managerize(function):
	"""
	Decorator to parameterize the manager in functions.
	Usage:
		cereal.register(Model, [function()]) # Defaults to _default_manager
		cereal.register(Model, [function('objects')])
	"""
	fn_name = function.__name__
	def manager_fn(manager='_default_manager'):
		def inner_fn(model, **kwargs):
			return function(model, manager, **kwargs)
		inner_fn.__name__ = fn_name
		return inner_fn
	return manager_fn

@managerize
def filter(model, manager, **kwargs):
	"""
	Filter on Model.
	"""
	return cereal.ize(getattr(model, manager).filter(**kwargs))

@managerize
def page_filter(model, manager, **kwargs):
	"""
	Paginated filter on Model.
	""" % manager
	ret = getattr(model, manager).filter(**kwargs)
	return {'count':ret.count(), 'objects':cereal.ize(ret)}
