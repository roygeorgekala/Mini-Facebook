from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from  .models import *
from django.contrib.auth import authenticate,logout , login
# Create your views here.

def reset(request):
    return render(request,'reset.html')

def signup(request):
    #User.objects.create(username = 'Roy2',first_name='Roy',last_name='George')
    #print("User Object Createddddd")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birthday = request.POST.get('birthday')
        image = request.FILES['image']
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(first_name+"     "+last_name)
        user = User.objects.create(username = email , first_name = first_name , last_name = last_name , email = email)
        print("User Object Created")
        user.password = make_password(password)
        user.save()
        print("User Password Stored")
        userinfo.objects.create(user = user , birthday = birthday, gender = gender, profile_pic = image)
        print("User Info added")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request,'login.html',{'name':'facebook'})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        print(user)
        if user:
            login(request,user)
            print("Worked")
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
        else:
            return render(request,'reset.html')
            #return HttpResponseRedirect(reverse('app:reset'))
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:signup'))

def home(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user=user)
    all_posts = Post.objects.all().order_by('-pk')
    all_users  = userinfo.objects.all().order_by('-pk')
    all_comments = []
    for p in all_posts:
        all_comments.append(Comments.objects.filter(post=p).order_by('-pk'))
    context = {
        'user':user,
        'user_info':user_info,
        'all_posts':all_posts,
        'all_users':all_users,
        'all_comments':all_comments,
    }
    return render(request, 'home.html',context)

def makepost(request,pk):
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    if request.method=='POST':
        text = request.POST.get("text")
        try:
            post_image = request.FILES['image']
        except:
            post_image = None
        try:
            post_video = request.FILES['video']
        except:
            post_video = None

        Post.objects.create(user=user,user_info=user_info,text=text,photo=post_image,video=post_video, l = 0 , c = 0)## TODO: Change the like number
        print("Post Created")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))


def likepost(request):
    post_id = request.GET.get('post_id')
    user_id = request.GET.get('user_id')
    #print(post_id)
    #print(user_id)
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=user_id)
    if likes.objects.filter(post=post).filter(user = user).exists():
        post.l -= 1
        post.save()
        likes.objects.filter(post=post).filter(user=user).delete()
        return HttpResponse(post.l)
    post.l += 1
    likes.objects.create(user=user,post=post)
    post.save()
    return HttpResponse(post.l)
def comment(request):
    print("Hey im in the function!!")
    post_id = request.GET.get('post_id')
    user_id = request.GET.get('user_id')
    body = request.GET.get('body')
    post = Post.objects.get(pk=post_id)
    post.c+=1
    post.save()
    print(user_id)
    user = User.objects.get(pk=user_id)
    c = Comments.objects.create(user=user,post=post,body=body)
    list = []
    list.append(c.user.first_name)
    list.append(c.user.last_name)
    list.append(c.body)
    list.append(post.c)
    return JsonResponse(list,safe=False)#Needed to send anything but a dict

def profile(request,pk,ppk):
    in_user = User.objects.get(pk=pk)
    in_user_info = userinfo.objects.get(user=in_user)

    view_user = User.objects.get(pk=ppk)
    view_user_info = userinfo.objects.get(user=view_user)


    all_posts = Post.objects.filter(user=view_user).order_by('-pk')
    all_comments = Comments.objects.all().order_by('-pk')


    context = {
        'in_user':in_user,
        'in_user_info':in_user_info,
        'view_user':view_user,
        'view_user_info':view_user_info,
        'all_posts':all_posts,
        'all_comments':all_comments,
    }

    return render(request,'profile.html',context)

def cover_pic_change(request,pk):
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    user_info.cover_pic = request.FILES['cover_pic_sub']
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile', args=(user.id,user.id,)))

def profile_img_change(request,pk):
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    user_info.profile_pic = request.FILES['profile_img_sub']
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile', args=(user.id,user.id,)))


def addbio(request,pk):
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    user_info.about = request.POST.get('body')
    print(request.POST.get('body'))
    print(request.method)
    print(request.POST)
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile',args=(user.id,user.id,)))
