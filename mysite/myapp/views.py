from django.shortcuts import render , render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login ,logout
from myapp.forms import *
from django.contrib.auth.models import User
from myapp.models import Document


def index(request):
	return render(request,'index.html',{'message': 'hello'})
  
def profile(request ,username):
	user = User.objects.get(username=username)
	return render(request, 'profile.html', {},{"user":user}) 

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
			if not request.POST.get('remember_me', None):
				request.session.set_expiry(0)
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

def upload_file(request):
	form = DocumentForm() # A empty, unbound form
	# Load documents for the list page
	documents = Document.objects.all()
	context = RequestContext(request)
	return render_to_response('upload.html',{'form': form}, context)

def success_upload(request):
	if request.method == 'POST':
		documents = Document.objects.all()
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('myapp.views.success_upload'))
