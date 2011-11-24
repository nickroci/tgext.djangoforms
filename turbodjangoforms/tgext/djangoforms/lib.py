'''
Created on 24 Nov 2011

@author: nick
'''
import os
from genshi.core import Markup
from tgext.djangoforms.constants import DEFAULT_SETTINGS_MODULE

class TDForms(object):
    def __init__(self, settings_module=None):
        if settings_module:
            self.settings_module = settings_module
        else:
            self.settings_module = DEFAULT_SETTINGS_MODULE   
        
        os.environ['DJANGO_SETTINGS_MODULE'] = self.settings_module
        
    def __call__(self, obj):
        if callable(obj):
            return Markup(obj())
        return Markup(obj)