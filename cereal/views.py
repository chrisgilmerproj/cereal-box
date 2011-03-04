from django.db.models.query import ValuesQuerySet
from django.http import HttpResponse
from django.utils import simplejson as json

import cereal

def to_json(obj):
	if type(obj) == ValuesQuerySet: return list(obj)

def json_api(request, model, function):
	return HttpResponse(json.dumps(cereal.call(model, function,
		**request.REQUEST), default=to_json), mimetype='application/json')
