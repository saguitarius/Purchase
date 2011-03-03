This file is for you to describe the Purchase application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``Purchase`` using easy_install::

    easy_install Purchase

Make a config file as follows::

    paster make-config Purchase config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.


ATTENTION!
==========
If Authentication does not work, edit this file:
    
    ~\Python26\Lib\site-packages\authkit\authenticate\form.py
    
Comment these lines:

    #formvars = parse_formvars(environ, include_get_vars=True)
    #username = formvars.get('username')
    #password = formvars.get('password') 
    
And add just after them on the same indentation level:

    if environ.get('webob._parsed_post_vars'):
            formvars = environ.get('webob._parsed_post_vars')
            username = formvars[0]['username']
            password = formvars[0]['password']
            
Also comment line:

    #del environ['paste.parsed_formvars']