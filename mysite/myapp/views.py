from django.shortcuts import render , render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login ,logout
from myapp.forms import UserForm


def index(request):
	return render(request,'index.html',{'message': 'hello'})
     
def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/myapp/')
	else:
		context = RequestContext(request)
		registered = False
		if request.method == 'POST':
			user_form = UserForm(data=request.POST)
			if user_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
				login(request, new_user)
				registered = True
				return HttpResponseRedirect("/myapp/")
			else:
				print user_form.errors
		else:
			user_form = UserForm()
			return render_to_response(
			'register.html',
			{'user_form': user_form,'registered': registered}, context)

def user_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/myapp/')
	else:
		context = RequestContext(request)
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/myapp/')
				else:
					return HttpResponse("Your account is disabled.")
			else:
				print "Invalid login details: {0}, {1}".format(username, password)
				return HttpResponse("Invalid login details supplied.")
		else:
			return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/myapp/')

