from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide

# Register your models here.

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class HomePageAdmin(PageAdmin):
    inlines = [SlideInline]

admin.site.register(HomePage, HomePageAdmin)