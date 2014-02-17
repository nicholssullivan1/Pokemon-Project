from resources.tags import Tags
from Zone.zone import Zone

import xml.etree.ElementTree

class ZoneFactory:
    """ Factory to build Zones """
    tree = None
    
    @staticmethod
    def getZone(name, callback):
        """ Return the zone with the given name """
        zoneXML = ZoneFactory.getZoneXML(name)
        if zoneXML is not None:
            return ZoneFactory.loadFromXML(zoneXML, callback)
        return None
    
    @staticmethod
    def loadFromXML(tree, callback):
        """ Loads a Zone object from a file """
        rows = int(tree.findtext(Tags.rowsTag))
        columns = int(tree.findtext(Tags.columnsTag))
        
        zone = Zone(rows, columns, callback)
        
        
        return zone
        
    @staticmethod
    def loadFromDB():
        """ AAAAAAAAAGGGGGGGGGGGHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! """
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        zone = Zone()
        
        return zone
        
    @staticmethod
    def getZoneTree():
        """ Opens the zone.xml file as an element tree """
        if ZoneFactory.tree is not None:
            return ZoneFactory.tree
        
        with open("resources/zone.xml", 'r') as zonedex:
            ZoneFactory.tree = xml.etree.ElementTree.ElementTree(file=zonedex)
        return ZoneFactory.tree
        
    @staticmethod
    def getZoneXML(name):
        """ Returns the XML tree for the zone with the name given """
        tree = ZoneFactory.getZoneTree()
        
        for zoneXML in tree.getiterator(Tags.zoneTag):
            if zoneXML.findtext(Tags.nameTag) == name:
                return zoneXML
        else:
            return None 