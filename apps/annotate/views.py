from django.shortcuts import render
from .models import Author, Book, AuthorBook
# Create your views here.
from django.db.models import Count
def Home(request):
    autors= Author.objects.all()
    books= Book.objects.all()
    authorbooks= AuthorBook.objects.all()


    kitoblar_soni=Book.objects.values('publish_year').annotate(book_count=Count('id'))
    name=AuthorBook.objects.values('author__name').annotate(book_count=Count('id'))

    print(kitoblar_soni)
    print(name)









    data={}
    autors_data=[]
    for author in autors:
        data= {
            'id': author.id,
            'name': author.name,
        }
        autors_data.append(data)

    data={}
    books_data=[]
    for book in books:
        data= {
            'id': book.id,
            'title': book.title,
            'publish_year': book.publish_year,
        }
        books_data.append(data)

    data={}
    authorbooks_data=[]
    for authorbook in authorbooks:
        data= {
            'id': authorbook.id,
            'author': authorbook.author.name,
            'book': authorbook.book.title,
        }
        authorbooks_data.append(data)






    context={
        'autors': autors_data,
        'books': books_data,
        'authorbooks': authorbooks_data,
    }
    return render(request, 'index.html', context)
