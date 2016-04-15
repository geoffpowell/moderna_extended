from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, Feature, Testimonial

# Register your models here.

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class FeatureInline(TabularDynamicInlineAdmin):
		model = Feature

class TestimomialInline(TabularDynamicInlineAdmin):
		model = Testimonial

class HomePageAdmin(PageAdmin):
    inlines = [SlideInline, FeatureInline, TestimomialInline]

admin.site.register(HomePage, HomePageAdmin)