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

#### 5. Database

	(venv3921) ing| python3 manage.py sqlmigrate organizer 0001
	BEGIN;
	--
	-- Create model NewsLink
	--
	CREATE TABLE "organizer_newslink" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"title" varchar(63) NOT NULL, 
		"pub_date" date NOT NULL, 
		"link" varchar(225) NOT NULL
	);
	--
	-- Create model Startup
	--
	CREATE TABLE "organizer_startup" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"name" varchar(31) NOT NULL, 
		"slug" varchar(31) NOT NULL UNIQUE, 
		"description" text NOT NULL, 
		"founded_date" date NOT NULL, 
		"contact" varchar(225) NOT NULL, 
		"website" varchar(200) NOT NULL
	);
	--
	-- Create model Tag
	--
	CREATE TABLE "organizer_tag" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"name" varchar(31) NOT NULL UNIQUE, 
		"slug" varchar(50) NOT NULL UNIQUE
	);
	--
	-- Add field tags to startup
	----- ManyToMany Rel: 
	----- A Startup may have one or many tags
	----- A tag or many tags may belongs to a startup
	--
	CREATE TABLE "organizer_startup_tags" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"startup_id" integer NOT NULL REFERENCES "organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED, 
		"tag_id"     integer NOT NULL REFERENCES "organizer_tag" ("id")     DEFERRABLE INITIALLY DEFERRED
	);
	--
	-- Add field startup to newslink
	----- OneToMany Rel: 
	----- A NewsLink belong to a Startup
	----- A Startup may have one or many NewsLink
	--
	ALTER TABLE "organizer_newslink" RENAME TO "organizer_newslink__old";
	CREATE TABLE "organizer_newslink" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"title" varchar(63) NOT NULL, 
		"pub_date" date NOT NULL, 
		"link" varchar(225) NOT NULL, 
		"startup_id" integer NOT NULL REFERENCES "organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED
	);
	INSERT INTO "organizer_newslink" (
		"id", 
		"title", 
		"pub_date", 
		"link", 
		"startup_id") 
	SELECT 
		"id", 
		"title", 
		"pub_date", 
		"link",
		NULL 
	FROM "organizer_newslink__old";

	DROP TABLE "organizer_newslink__old";

	CREATE INDEX "organizer_startup_name_0080733f" ON "organizer_startup" ("name");
	CREATE UNIQUE INDEX organizer_startup_tags_startup_id_tag_id_982c6d9a_uniq ON "organizer_startup_tags" ("startup_id", "tag_id");
	CREATE INDEX "organizer_startup_tags_startup_id_94e79a84" ON "organizer_startup_tags" ("startup_id");
	CREATE INDEX "organizer_startup_tags_tag_id_bcc66000" ON "organizer_startup_tags" ("tag_id");
	CREATE INDEX "organizer_newslink_startup_id_ad247707" ON "organizer_newslink" ("startup_id");
	COMMIT;

	(venv3921) ing| python3 manage.py sqlmigrate blog 0001
	BEGIN;
	--
	-- Create model Post
	--
	CREATE TABLE "blog_post" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"title" varchar(63) NOT NULL, 
		"slug" varchar(63) NOT NULL, 
		"text" text NOT NULL, 
		"pub_date" date NOT NULL
	);
	CREATE TABLE "blog_post_startups" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"post_id"    integer NOT NULL REFERENCES "blog_post" ("id")         DEFERRABLE INITIALLY DEFERRED, 
		"startup_id" integer NOT NULL REFERENCES "organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED
	);
	CREATE TABLE "blog_post_tags" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"post_id" integer NOT NULL REFERENCES "blog_post" ("id")     DEFERRABLE INITIALLY DEFERRED, 
		"tag_id"  integer NOT NULL REFERENCES "organizer_tag" ("id") DEFERRABLE INITIALLY DEFERRED
	);

	CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
	CREATE UNIQUE INDEX blog_post_startups_post_id_startup_id_459561f9_uniq ON "blog_post_startups" ("post_id", "startup_id");
	CREATE INDEX "blog_post_startups_post_id_b1153755" ON "blog_post_startups" ("post_id");
	CREATE INDEX "blog_post_startups_startup_id_a3e30c05" ON "blog_post_startups" ("startup_id");
	CREATE UNIQUE INDEX blog_post_tags_post_id_tag_id_4925ec37_uniq ON "blog_post_tags" ("post_id", "tag_id");
	CREATE INDEX "blog_post_tags_post_id_a1c71c8a" ON "blog_post_tags" ("post_id");
	CREATE INDEX "blog_post_tags_tag_id_0875c551" ON "blog_post_tags" ("tag_id");
	COMMIT;

	modified:   README.md
	new file:   blog/migrations/0001_initial.py
	modified:   db.sqlite3
	new file:   organizer/migrations/0001_initial.py

