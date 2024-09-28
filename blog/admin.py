from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_view','status','login_require','published_date','created_date')
    list_filter = ('status','author')
    ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
    
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('post','subject','name','approved','created_date','email')
    list_filter = ('post','approved')
    search_fields = ['post','subject']
