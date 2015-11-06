from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, Feature

# Register your models here.

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class FeatureInline(TabularDynamicInlineAdmin):
		model = Feature

class HomePageAdmin(PageAdmin):
    inlines = [FeatureInline, SlideInline]

admin.site.register(HomePage, HomePageAdmin)