from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
	context = {
		"form": form
	}
	return render(request,"post_form.html", context)

def post_detail(request, id=None):
	#instance = Post.objects.get(id=12)
	instance = get_object_or_404(Post, id=id)
	context = {"title": instance.title,
	"instance": instance
	}
	return render(request,"post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {"title": "Detail",
	"object_list": queryset
	}
	return render(request,"base.html", context)



def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")