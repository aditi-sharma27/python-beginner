from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
	'author': 'Aditi Sharma',
	'title' : 'Blog Post 1',
	'content': 'First Post Title',
	'date_posted': '20 December 2018'
	},
		{
	'author': 'Anu Sharma',
	'title' : 'Blog Post 2',
	'content': 'Second Post Title',
	'date_posted': '21 December 2018'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')
