from django.contrib import admin
from .models import UpdateCatagory, Update, UpdateComment


admin.site.register(UpdateCatagory)
admin.site.register(Update)

@admin.register(UpdateComment)
class UpdateCommentAdmin(admin.ModelAdmin):
    list_filter = ['comment_status']
    
