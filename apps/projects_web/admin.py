from django.contrib import admin

from apps.projects_web.models import CategoryProject, ClientCategoryProject, Project, ProjectImage
from project.admin import website_admin

# Register your models here.
class ProjectImageInlineWeb(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image",)
    
class ProjectWebAdmin(admin.ModelAdmin):
    exclude = ["slug"]
    inlines = [
        ProjectImageInlineWeb,
    ]
   

class CategoryProjectWebAdmin(admin.ModelAdmin):
   exclude = ["slug"]

class ClientCategoryProjectWebAdmin(admin.ModelAdmin):
   exclude = ["slug"]
    






website_admin.register(Project, ProjectWebAdmin)
website_admin.register(CategoryProject, CategoryProjectWebAdmin)
website_admin.register(ClientCategoryProject, ClientCategoryProjectWebAdmin)