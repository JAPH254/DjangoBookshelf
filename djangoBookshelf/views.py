from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm


def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = BookForm()
    return render(request, 'addbook.html', {'form': form})


def booklist(request):
    list = Book.objects.all()
    return render(request, 'booklist.html', {'list': list})
