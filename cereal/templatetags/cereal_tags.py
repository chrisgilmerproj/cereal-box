from django.template import Library, TemplateSyntaxError, Node, Variable
import cereal

register = Library()

class CerealNode(Node):
	def __init__(self, model, function, variable, **kwargs):
		self.model    = model
		self.function = function
		self.variable = variable
		self.kwargs   = kwargs
	def render(self, context):
		context[self.variable] = cereal.call(self.model,
				self.function, **dict((k, v.resolve(context))
				for k,v in self.kwargs.iteritems()))
		return ''

def cereal_tag(parser, token):
	"""
	Usage::
	{% cereal [model].[function] ([key]=[value]) as [variable] %}
	"""
	args = token.split_contents()
	model, function = args[1].split('.')
	kwargs = dict(((a.split('=')[0], Variable(
		a.split('=')[1])) for a in args[2:-2]))
	return CerealNode(model, function, args[-1], **kwargs)

register.tag('cereal', cereal_tag)
