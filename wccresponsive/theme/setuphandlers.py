from collective.grok import gs
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wccresponsive.theme.interfaces import IThemeSettings

@gs.importstep(
    name=u'wccresponsive.theme', 
    title=u'wccresponsive.theme import handler',
    description=u'')
def setupVarious(context):
    if context.readDataFile('wccresponsive.theme.marker.txt') is None:
        return
    portal = context.getSite()
    registry = getUtility(IRegistry)
    registry.registerInterface(IThemeSettings)

    # do anything here
