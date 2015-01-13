# django-teenyweeny
A simple django app for manual url shortening. Input of new URLs is only possible via the django admin. They are not generated automatically.

It was created for [MyComoda](https://www.mycomoda.de) to allow short campaign links without loosing "social influence" on search engines to bit.ly or similar services.

# Requirements
Tested on django 1.6, python 2.7

# Installation
Add `'teeny_weeny'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'teeny_weeny',
        ...
    )

Add unique short_url_namespace (`'l'` in this example) to your root urls.py

	urlpatterns = patterns('',
	...
	url(r'^l/', include('teeny_weeny.urls')),
	...
	)

Visit the admin to create a new short url; alternatively use the interactive shell like so

	$ python manage.py shell
	Python 2.7.6 (default, Nov 18 2013, 15:12:51) 
	[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> from teeny_weeny.models import ShortLink
	>>> ShortLink(short='lmgtfy', link='http://www.google.de/').save()
	
Test the redirection

	$ curl -i http://127.0.0.1:8000/l/lmgtfy
	HTTP/1.0 301 MOVED PERMANENTLY
	Date: Tue, 13 Jan 2015 14:10:07 GMT
	Server: WSGIServer/0.1 Python/2.7.6
	X-Frame-Options: SAMEORIGIN
	Content-Type: text/html; charset=utf-8
	Location: http://www.google.de/

# Credits
Designed by [Linda Eich](https://www.mycomoda.de/accounts/profile/Linda/outfits)