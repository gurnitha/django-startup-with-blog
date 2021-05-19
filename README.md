## Building a Startup with Blog
https://github.com/gurnitha/django-startup-with-blog

#### 1. Django project and apps created and installed

	(venv3921) ing| tree -L 2
	.
	├── README.md
	├── _config
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── blog
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── admin.py
	│   ├── apps.py
	│   ├── migrations
	│   ├── models.py
	│   ├── tests.py
	│   └── views.py
	├── manage.py
	└── organizer
	    ├── __init__.py
	    ├── __pycache__
	    ├── admin.py
	    ├── apps.py
	    ├── migrations
	    ├── models.py
	    ├── tests.py
	    └── views.py

#### 2. Adding html templates

	modified:   README.md
	modified:   _config/settings.py
	modified:   _config/urls.py
	new file:   blog/urls.py
	modified:   blog/views.py
	new file:   db.sqlite3
	new file:   organizer/urls.py
	modified:   organizer/views.py
	new file:   templates/base.html
	new file:   templates/blog/post_detail.html
	new file:   templates/blog/post_list.html
	new file:   templates/organizer/startup_detail.html
	new file:   templates/organizer/startup_list.html
	new file:   templates/organizer/tag_detail.html
	new file:   templates/organizer/tag_list.html

#### 3. Template inheritance

	modified:   README.md
	modified:   templates/base.html
	modified:   templates/blog/post_detail.html
	modified:   templates/blog/post_list.html
	modified:   templates/organizer/startup_detail.html
	modified:   templates/organizer/startup_list.html
	modified:   templates/organizer/tag_detail.html
	modified:   templates/organizer/tag_list.html
	new file:   templates/shared/footer.html
	new file:   templates/shared/navbar.html


#### 4. Models

	modified:   README.md
	modified:   blog/models.py
	modified:   organizer/models.py

