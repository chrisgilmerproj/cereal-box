from django.db.models.query import ValuesQuerySet
from django.http import HttpResponse
from django.utils import simplejson as json

import cereal

def json_api(request, model, function):
	ret = cereal.call(model, function, **request.REQUEST)
	if type(ret) == ValuesQuerySet: ret = list(ret)
	return HttpResponse(json.dumps(ret), mimetype='application/json')
