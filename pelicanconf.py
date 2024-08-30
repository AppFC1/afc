AUTHOR = 'Adam Sommer'
SITENAME = 'Appalachian FC'
SITEURL = '/afc'
DOMAIN = 'appfc1.github.io'
# DOMAIN = 'asommer70.github.io'
FEED_DOMAIN = SITEURL
# STYLESHEET_URL = '/static/css/site.css'
THEME = 'themes/appfc/'

PATH = "content"

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# PLUGIN_PATHS = ['../pelican-plugins']
# PLUGINS = ['ical', 'pelican.plugins.pelican-data-files']
# PLUGIN_PATHS = ['../ical']
# PLUGINS = ['ical']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 12

# PAGE_URL = '{slug}'
# PAGE_SAVE_AS = '{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
