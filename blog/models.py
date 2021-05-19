# blog/models.py
from django.db import models

from organizer.models import Startup, Tag

# Create your models here.

# BLOG MODELS/TABLE: Post
'''
About Post 	: A type of article
Table name 	: Post (in the db: Posts)
Columns    	: title, slug, text, pub_date,
			  tags, startups
Relationship: Tags, Startups
Type of Rel : OneToMany with Tags,
 			  OneToMany with Startups
'''
class Post(models.Model):

	title 	= models.CharField(
			max_length=63,
			help_text='Add your post title here.')
	slug 	= models.SlugField(
			max_length=63,
			help_text='A label for URL config.',
			unique_for_month='pub_date')
	text 	= models.TextField(
			help_text='Add your post body here.')
	pub_date= models.DateField(
			'date published',
			auto_now_add=True,
			help_text='It will not be seen in admin.')
	# ManyToMany Rel:
	## A post may have one or many tags
	## A tag or many tags may belongs to one post
	tags 	= models.ManyToManyField(
			Tag,
			related_name='blog_post')
	# ManyToMany Rel:
	## A post may belongs to one or many startup
	## A startup or many startup may belong to a post
	startups= models.ManyToManyField(
			Startup,
			related_name='blog_post')

	'''
	Title: Nano Chip
	Date: 2021-05-15
	Admin dashboard: Nano Chip on 2021-05-15
	'''
	def __str__(self):
		return "{} on {}".format(
			self.title,
			self.pub_date.strftime('%Y-%m-%d'))


