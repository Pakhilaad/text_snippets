from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Snippet
from .forms import SnippetForm
from django.urls import reverse
from django.core.exceptions import PermissionDenied

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            # Generate the URL for the view_snippet page using reverse
            snippet_url = reverse('view_snippet', args=[snippet.id])
            return render(request, 'snippets/create_snippet.html', {'snippet_url': snippet_url})
    else:
        form = SnippetForm()
    return render(request, 'snippets/create_snippet.html', {'form': form})

# def view_snippet(request, snippet_id):
#     snippet = get_object_or_404(Snippet, id=snippet_id)
#     return render(request, 'snippets/view_snippet.html', {'snippet': snippet})

def decrypt_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    if request.method == 'POST':
        key = request.POST.get('key')
        if key == snippet.secret_key:
            return HttpResponse(snippet.content)
        else:
            return HttpResponse("Incorrect key. Access denied.")
    return render(request, 'snippets/decrypt_snippet.html', {'snippet': snippet})

def view_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    
    # Check if the request method is POST (i.e., someone submitted the decryption key)
    if request.method == 'POST':
        provided_key = request.POST.get('key', '')
        if provided_key == snippet.secret_key:
            # If the provided key matches the snippet's secret_key, show the content
            return render(request, 'snippets/view_snippet.html', {'snippet': snippet})
        else:
            # If the key is incorrect, raise a PermissionDenied exception
            raise PermissionDenied("Incorrect key. Access denied.")
    else:
        # If it's a GET request, render the decryption template
        return render(request, 'snippets/decrypt_snippet.html', {'snippet': snippet})