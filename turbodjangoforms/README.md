About Turbo Django Forms
-------------------------

Turbo Django Forms is a basic package that allows you to use Django forms
in turbogears. You should be able to follow the django documentation to
deal with validation etc.

Installing
-------------------------------

tgext.djangoforms can be installed from pypi::

    pip install tgext.djangoforms

should just work for most of the users

Enabling Turbo Django Forms
----------------------------------

In your application *lib/app_globals.py* import **TDForms**::

    from tgext.djangoforms import TDForms

And call it inside the **__init__**::

    class Globals(object):
        def __init__(self):
            self.tdf = TDForms()

Creating Forms
----------------------------

Creating forms works the same as with standard Django::

    from django import forms

    class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField()
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

Controller
----------------------------

You can follow most of the django forms tutorial::

    @expose('mysite.templates.index')
    def index(self, **kw):
        """Handle the front-page."""
        if kw:
            form = ContactForm(kw)
            
            if form.is_valid():
                print form.cleaned_data
                //do stuff
                tg.flash("Form OK")
        else:
            form = ContactForm()
            
        return dict(page='Index', form=form)

Rendering Forms
----------------------------

You can use the standard django style template notation in your Genshi template - but add a g.tdf(...)::

    <form>
    ${g.tdf(form.as_p)}
    <button>Submit</button>
    </form>