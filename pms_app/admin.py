from django.contrib import admin
from pms_app.models import Category, Company, Manager, Developer, Project

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Developer)
admin.site.register(Project)
