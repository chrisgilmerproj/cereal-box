import cereal

def queryset(queryset, **kwargs):
	pass

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
	Applied filter on Model.%s
	""" % manager
	return cereal.ize(getattr(model, manager).filter(**kwargs))

@managerize
def page_filter(model, **kwargs):
	"""
	Applied paginated filter on Model.%s
	""" % manager
	ret = getattr(model, manager).filter(**kwargs)
	return {'count':ret.count(), 'objects':cereal.ize(ret)}
