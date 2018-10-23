from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from  basic.models import Topic,Playlist
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render (request,'basic/home.html')


def signin(request):
	if request.method=="POST":
		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			
			ob=Topic.objects.all()
			context={'post':ob}
			return render(request,'basic/topic.html',context)
	return render(request,'basic/login.html')

def viewtopic(request):
	ob=Topic.objects.all()
	context={'post':ob}
	return render(request,'basic/topic.html',context)

def signup(request):
	if request.method=="POST":

		username = request.POST.get('username')
		if User.objects.filter(username=username).exists():
			return HttpResponse("User name already exists")
		email = request.POST.get('email')
		if User.objects.filter(email=email).exists():
			return HttpResponse("email already exists")
		password = request.POST.get('password')
		repassword=request.POST['repassword']

		if username is not None:
			if password==repassword:
				user = User.objects.create_user(username,email,password)
				user.save()
				return redirect(signout)

			else:
				return HttpResponse("password mismatch")

	return render(request,'basic/signup.html')

	
@login_required
def playvideo(request,topic_id,p_id):
	tid=Topic.objects.get(pk=topic_id)
	video=Playlist.objects.get(topic=tid,pk=p_id)
	context={'posts':video.url,'pid':p_id,'topic_id':topic_id, 'playlist':video}
	return render(request,'basic/list.html',context)

@login_required
def collection(request,topic_id):
	tid=Topic.objects.get(pk=topic_id)
	video=Playlist.objects.filter(topic=tid)

	context={'posts':video,'tid':topic_id}

	return render(request,'basic/collection.html',context)


@login_required
def createplay(request):
	if request.method=="POST":
		if request.user.is_authenticated:

			username = request.user
			print(username)
			topic = request.POST['topic']
			t=Topic.objects.get(name=topic)
			title=request.POST['title']
			description=request.POST['description']
			np=Playlist.objects.create(user=username,topic=t,title=title,description=description)
			np.save()
			return HttpResponse("Playlist created")
		else:
			return redirect(signin)

	post=Topic.objects.all()
	context={'post':post}
	return render(request,'basic/createplaylist.html',context)


@login_required	
def addurl(request,topic_id,pid):
	if(request.method=='POST'):
		u=request.POST['url']
		l=[]
		if u is not "":
			if 'youtbe.be'in u:
				e=u.split('/')
				l.append(e[2])
			elif 'www.youtube.com/watch?v=' in u:
				e=u.split('=')
				l.append(e[1])

			else:
				e=u.split('/')
				l.append(e[-1])

			tid=Topic.objects.get(pk=topic_id)
			video=Playlist.objects.filter(topic=tid,pk=pid)
			for a in video:
					
				if l not in a.url:
					a.url.append(l[0])
					a.save()
		return redirect(playvideo,topic_id=topic_id,p_id=pid)
																			
	return redirect(playvideo,topic_id=topic_id,p_id=pid)

def signout(request):
    logout(request)
    return redirect(home)




















