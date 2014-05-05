from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def index (request):
	t = get_template('index.html')
	html = t.render()
	return HttpResponse(html)