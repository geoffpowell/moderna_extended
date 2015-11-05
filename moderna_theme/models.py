from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

class HomePage(Page, RichText):
		'''
		custom HomePage
		'''
		#heading for paragraph just under the slider
		heading = models.CharField(max_length = 100, 
																help_text = 'Heading for paragraph', default = 'Super Cool Heading')
		#paragraph blurb
		paragraph_blurb = models.CharField(max_length = 600, 
																			help_text = 'Paragraph under the top heading', 
																			default = 'This is a test. I am a robot.')
		class Meta:
				verbose_name = _('Home Page')
				verbose_name_plural = _('Home Pages')

class Slide(Orderable):
		'''
		Slider used on the HomePage
		'''
		homepage = models.ForeignKey(HomePage, related_name ='slides')
		image = FileField( verbose_name=_('Image'),
											upload_to = upload_to('theme.Slide.image', 'slider'),
											format = 'Image',
											max_length = 255, null = True, blank = True)


		caption_heading = models.CharField( max_length = 30 )
		caption_blurb = models.CharField( max_length = 100,
																			default = 'Blurb for image')
