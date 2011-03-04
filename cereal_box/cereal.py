import logging
import serializers, settings

def register(model, functions, serializer=None):
	"""
	Registers a model with cereal-box.
	model     - The model in question.
	functions - A list of callable functions e.g.
		def filter(model, **kwargs): return model.objects.filter(**kwargs)
	serial    - An optional queryset serializer.
	"""
	name = model.__name__.lower()
	if name in settings.models:
		raise ValueError('Model %s already registered with cereal-box' % name)
	settings.models[name]      = model
	settings.serializers[name] = serializer or serializers.values()
	settings.functions[name]   = {}
	for fn in functions:
		fn_name = fn.__name__.lower()
		if fn_name in settings.functions[name]:
			raise ValueError(
				'Function %s already registered on model %s with cereal-box'
				% (fn_name, name))
		else:
			settings.functions[name][fn_name] = fn
			logging.debug('Registered %s on %s', fn_name, name)

def call(model, function, **kwargs):
	"""
	Calls a function on a registered model.
	model    - The name of the model.
	function - The name of the function.
	**kwargs - Function parameters.
	"""
	return settings.serializers[model](
			settings.functions[model][function](
			settings.models[model], **kwargs))
