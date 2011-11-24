        About Turbo Django Forms
        -------------------------
        
        AsyncJob is a TurboGears2 extension made to handle background/synchronous jobs.
        Permits to quickly return responses to the user while the system performs more work on
        background, it can be useful for video transcoding, thumbnails generation or other
        tasks where the user cannot expect the require time before getting an answer.
        
        Installing
        -------------------------------
        
        tgext.asyncjob can be installed both from pypi::
        
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
        
        Rendering Forms
        ----------------------------
        
        You ::
        
            from tgext.asyncjob import asyncjob_perform
        
            def background_task(number):
                print number*2
        
            asyncjob_perform(background_task, 5)