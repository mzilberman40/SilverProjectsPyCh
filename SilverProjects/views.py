from django.shortcuts import redirect

def redirect_anecdotes(request):
    return redirect('anecdotes_list_url', permanent=True)
