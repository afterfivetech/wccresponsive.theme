from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource


SCHEMES_CSS={
    'red': 'wccresponsive-scheme-red.css',
    'blue': 'wccresponsive-scheme-blue.css',
    'darkgreen': 'wccresponsive-scheme-darkgreen.css',
    'pantone377': 'wccresponsive-scheme-pantone377.css',
    'brown': 'wccresponsive-scheme-brown.css'
}

class ColorSchemes(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(SCHEMES_CSS.keys())

grok.global_utility(ColorSchemes, IVocabularyFactory,
                name='wccresponsive.theme.colorscheme')
