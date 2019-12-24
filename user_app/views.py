from django.shortcuts import render, redirect
from .models import UserModel
from .forms import EditProfileForm


# Create your views here.
def login(request):
    if 'user_id' in request.session:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            if username and password:
                user = UserModel.objects.filter(username=username, password = password).first()
                if(user):
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    return redirect('index')
        return render(request, 'user_app/login.html')

def logout(requst):
    requst.session.flush()
    return redirect('login')


def edit(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id',None)
    user = UserModel.objects.filter(id=userid).first()

    if user:
        if request.method == 'POST':
            form = EditProfileForm(data=request.POST, files=request.FILES, instance=user)
            if form.is_valid():
                form.save()
                request.session['username'] = user.username
                return redirect('profile', user.username)
            else:
                return render(request,'user_app/edit.html',{'form':form})
        else:
            form = EditProfileForm(instance=user)
            d={
                'form': form,
                'user': user
            }
            return render(request,'user_app/edit.html',d)
    return redirect('index')

