from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

from django.views.generic import TemplateView, DetailView

from datetime import datetime, timedelta, date
import settings
import simplejson as json

from mapper.models import *


@login_required
def home(request):
	ctx = {}

	ctx["maps"] = Map.objects.filter(user=request.user)
	ctx["gallery"] = Map.objects.filter(public=True)[:5]

	return render_to_response("home.html", ctx, context_instance=RequestContext(request))


@login_required
def new(request):
	ctx = {}

	ctx["tiers"] = Tier.objects.all()
	ctx["entityclasses"] = EntityClass.objects.all()
	

	return render_to_response("new.html", ctx, context_instance=RequestContext(request))


def viewmap(request, id):
	ctx = {}
	ctx["map"] = Map.objects.get(id=id)
	ctx["tiers"] = Tier.objects.all()
	ctx["entityclasses"] = EntityClass.objects.all()

	return render_to_response("new.html", ctx, context_instance=RequestContext(request))


@login_required
def get_resources(request, tier, need):
	ctx = {}
	t = Tier.objects.get(id=tier)
	n = Need.objects.get(id=need)
	ctx["resources"] = list(Resource.objects.filter(serviceprovider__tier = t, needs = n))
		
	return HttpResponse(json.dumps(ctx))



@login_required
def new_resouce(request, serviceproviders, needs, name):
	ctx = {}
	s = ServiceProvider.objects.filter(id__in=serviceproviders)
	n = Need.objects.filter(id__in=needs)

	r = Resource()
	r.name = name
	r.save()
	r.need.add(n)
	r.serviceprovider.add(s)

	ctx["resource"] = {"name": r.name, "id": r.id}

	return HttpResponse(json.dumps(ctx))


@login_required
def new_serviceprovider(request, tier, name):
	ctx = {}

	t = Tier.objects.get(id=tier)

	s = ServiceProvider()
	s.name = name
	s.tier = t
	s.save()

	ctx["serviceprovider"] = {"name": s.name, "id": s.id}

	return HttpResponse(json.dumps(ctx))
