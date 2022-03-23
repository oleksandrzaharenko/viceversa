from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def new_page(request):
	userText = request.GET['usertext']
	reversedText = userText[::-1]
	return render(request, 'new_page.html', {'usertext': userText, 
											'reversedtext':reversedText} )