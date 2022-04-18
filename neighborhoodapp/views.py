
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Profile,Neighborhood,Business,Post
from .forms import NewNeighborhoodForm,NewBusinessForm,UpdateProfileForm,NewPostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request):
    message='profile'
    current_user = request.user
    # post = Neighborhood.objects.filter(profile=current_user.id).all
    return render(request,'profile.html',{'message':message})
@login_required(login_url='/accounts/login/')
def update_profile(request):
    message='update user prifile'
    return render(request,'update_profile.html',{'message':message})

def homepage(request):
    message='WELCOME TO NEIGHBORHOOD'
    projects=Neighborhood.objects.all()
    return render(request,'homepage.html',{'message':message,'projects':projects})
# def new_post(request):
#     message='register new post'

#    return render(request,'new_post.html',{'message':message})
@login_required(login_url='/accounts/login/')
def new_neighborhood(request):


    message='register new home'
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user

            neighbourhood.save()

        return redirect('homepage')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'new_neighborhood.html', {"form": form})





    return render(request,'new_neighborhood.html',{'message':message})
def deletehood(request,id):
    deletehood = Neighborhood.objects.get(id=id)
    deletehood.delete()
    return redirect('homepage')

@login_required(login_url='/accounts/login/')
def moreabout_neighborhood(request,id):
    message=' more about home'
    project=Neighborhood.objects.filter(id=id).get()
    businesses = Business.objects.filter(neighborhood=id)
    posts = Post.objects.filter(neighborhood=id)
    return render(request,'moreabout.html',{'message':message,'project': project,'businesses':businesses,'posts':posts})
    



@login_required(login_url='/accounts/login/')
def new_business(request):
    message='register new business'
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('homepage')

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form,'message':message})


 
def deletebusiness(request,id):
    deletebiz= Business.objects.get(id=id)
    deletebiz.delete()
    return redirect('homepage')
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user=request.user
    if request.method == 'POST':
        form=NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect('homepage')
    else:
        form=NewPostForm()
    return render(request,'new_post.html',{"form":form})
def delete_post(request,id):
    deletepost= Post.objects.filter(id=id)
    deletepost.delete()
    return redirect('homepage')
@login_required(login_url='/accounts/login/')
def search(request):
    # message='search here'
    # return render(request,'search.html',{'message':message})
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Neighborhood.find_neigborhood(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"searched_articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
