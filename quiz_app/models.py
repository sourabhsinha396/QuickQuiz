from django.db import models
from django.conf import settings
from django.utils.text import slugify


#Third Party imports
from ckeditor.fields import RichTextField


SUBJECT_CHOICES = (
	('1','Physics'),
	('2','Chemistry'),
	('3','Programming'),
	('4','Frontend'),
	('5','Backend'),
)


class Quiz(models.Model):
	"""This model is the one that handles making of quiz"""

	user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title           = models.CharField(max_length=200)
	slug            = models.SlugField(unique=True,blank=True,
						null=True,help_text="let it be empty",db_index=True)
	# Used db_index for faster query resolving 
	subject         = models.CharField(max_length=29,default='1',
						choices = SUBJECT_CHOICES)
	total_question  = models.PositiveSmallIntegerField(default=10)
	created         = models.DateField(auto_now_add=True)
	is_active       = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Quiz'
		verbose_name_plural = 'Quizs'
		ordering = ['-created']

	def save(self):
		if not self.id:
			self.slug = slugify(self.title)
		super(Quiz, self).save()

	def __str__(self):
		return str(self.title)[:20]


#########--------------Question Model--------------###############

class Question(models.Model):
	quiz           = models.ForeignKey(Quiz,on_delete=models.CASCADE)
	question       = RichTextField()

	def __str__(self):
		return str(self.question)[:20]