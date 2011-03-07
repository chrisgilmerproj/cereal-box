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
	Filter on Model by properties (max 100 results).
	"""
	return cereal.ize(getattr(model, manager).filter(**kwargs))

@managerize
def page_filter(model, manager, **kwargs):
	"""
	Paginated filter on Model.
	per_page - Number of results (up to 100)
	page     - Current page number (starting at 1)
	"""
	per_page = int(kwargs.get('per_page', 10))
	if per_page > 100 or per_page < 1: per_page = 100
	page = int(kwargs.get('page', 1))
	if 'page' in kwargs:     del kwargs['page']
	if 'per_page' in kwargs: del kwargs['per_page']
	if page < 1: page = 1
	offset = page*per_page
	ret      = getattr(model, manager).filter(**kwargs)
	count    = ret.count()
	return {'total' : ret.count(),
			'items' : cereal.ize(ret[offset-per_page:offset])}
