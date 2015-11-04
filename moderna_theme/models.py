from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import RichText, Slugged
from mezzanine.pages.models import Page

class HomePage(Page, RichText):
		'''
		The representation of the custom HomePage
		'''
		#paragraph blurb
		paragraph_blurb = models.CharField(max_length = 600, help_text = 'Paragraph under the top heading', default = 'This is a test. I am a robot.')

		#heading for paragraph just under the slider
		heading = models.CharField(max_length = 100, help_text = 'Heading for paragraph', default = 'Super Cool Heading')

		class Meta:
				verbose_name = _('Home Page')
				verbose_name_plural = _('Home Pages')