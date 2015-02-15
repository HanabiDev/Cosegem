from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User

from forms import *

from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.

def home(request):
	users = User.objects.all()

	return render_to_response('users_index.html', {'users':users}, context_instance=RequestContext(request))

def profile(request, user_id):
	user = User.objects.get(id=user_id)

	return render_to_response('account.html', {'site_user':user}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('auth.add_user', login_url='/backend/permisos_insuficientes/')
def new_user(request):

	if request.method == 'GET':
		form = UserAddForm()
		return render_to_response('add_user.html', {'form':form}, context_instance=RequestContext(request))
	
	elif request.method == 'POST':
		form = UserAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.avatar = 'uploads/avatars/avatar.png'
            new_user.save()

            return redirect(reverse('users:edit',kwargs={'user_id':str(new_user.id)}))
        else:
        	return render_to_response('add_user.html',
							  {'form':form}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def edit_user(request, user_id):

	if request.method == 'GET':
		user = User.objects.get(id=user_id)
		form = UserEditForm(instance=user)
		return render_to_response('edit_user.html', {'form':form, 'site_user':user}, 
						context_instance=RequestContext(request))

	elif request.method == 'POST':
		user = User.objects.get(id=user_id)
		form = UserEditForm(request.POST, instance=user)

		if form.is_valid():

			user = form.save()

			if request.FILES:
				user.avatar = request.FILES.get('avatar')
			
			user.save()
			
			return redirect(reverse('users:home'))


    	return render_to_response('edit_user.html', {'form':form, 'site_user':user}, 
						context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def toggle_lock(request, user_id):
	user = User.objects.get(id=user_id)
	user.is_active = not user.is_active
	user.save()

	return redirect('users:home')

