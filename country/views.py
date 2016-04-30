# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse, render_to_response, RequestContext, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def render_country(request):

    context = RequestContext(request,
                       {'request': request,
                        })
    return render_to_response('render_country.html', context)

