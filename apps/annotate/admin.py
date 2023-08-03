from django.contrib import admin
from .models import Author, Book, AuthorBook

class AuthorAdminInline(admin.TabularInline):
    model = AuthorBook
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_editable = ('name',)
    list_display_links = None

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_year')
    list_display_links = ('title',)
    inlines = (AuthorAdminInline,)

@admin.register(AuthorBook)
class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ('author', 'book')
