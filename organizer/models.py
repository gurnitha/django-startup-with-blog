# organizer/models.py
from django.db import models

# Create your models here.

# ORGANIZER MODELS/TABLE: Tag
'''
About Tag 	: A type of label (metal)
Table name 	: Tag (in the db: Tags)
Columns    	: name, slug
Relationship: Startups and Post tables
Type of Rel : OneToMany with Startups,
 			  OneToMany with Posts
'''
class Tag(models.Model):

	name = models.CharField(
			max_length=31, 
			unique=True)
	slug = models.SlugField(
			unique=True,
			help_text='A label for URL config.')

	def __str__(self):
		return self.name 


# ORGANIZER MODELS/TABLE: Startup
'''
About Startup: A type of company (Tech Company)
Table name 	: Startup (in the db: Startups)
Columns    	: name, slug, description,
			  date_founded, contact_email,
			  website, tag
Relationship: Tags, NewsLink, Posts
Type of Rel : ManyToMany with Tags,
			  OneToMany with Posts,
'''
class Startup(models.Model):

	name = models.CharField(
			max_length=31,
			db_index=True)
	slug = models.SlugField(
			max_length=31,
			unique=True,
			help_text='A label for URL config.')
	description = models.TextField()
	founded_date = models.DateField(
			'date founded')
	contact = models.EmailField(
			max_length=225)
	website = models.URLField()
	# ManyToMany Rel: 
	## A Startup may have one or many tags
	## A tag or many tags may belongs to a startup
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name 


# ORGANIZER MODELS/TABLE: NewsLink
'''
About NewsLink: A type of link (
                Link of a published-article)
Table name 	: NewsLink (in the db: Newslinks)
Columns    	: name, date_published, link, startup
Relationship: Startup
Type of Rel : OneToMany with Startup
'''
class NewsLink(models.Model):

	title = models.CharField(
			max_length=63)
	pub_date = models.DateField(
			'date published')
	link = models.URLField(
			max_length=225)
	# OneToMany Rel: 
	## A NewsLink belong to a Startup
	## A Startup may have one or many NewsLink
	startup = models.ForeignKey(
			Startup,
			on_delete=models.CASCADE)

	class Meta:
		verbose_name  = 'article links'
		ordering 	  = ['-pub_date']
		get_latest_by = 'pub_date'

	'''
	Title: Micro Chip
	Startup: Tech Camp
	Admin dashboard: Teach Camp: Micro Chip
	'''
	def __str__(self):
		return "{}:{}".format(
			self.startup, self.title)
