from django.shortcuts import render



def homepage(request):
	"""This view returns the homepage to  base.html"""
	context = {'page_name':'QuickQuiz'}
	return render(request,'common_pages/homepage.html',context)