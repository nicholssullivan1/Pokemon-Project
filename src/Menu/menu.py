
class Menu:
    """ Represents a menu in the game """
    
    def __init__(self, entries=None):
        """ Build the menu """
        self.running = True
        if entries is None:
            self.addEntries()
        else:
            self.entries = entries
        self.current = 0
        self.selectEntry()
        
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = []
        
    def addEntry(self, entry):
        """ Add an entry to the window """
        self.entries.append(entry)
        
    def up(self):
        """ Select the previous entry """
        if self.current > 0:
            self.changeSelected(-1)
            
    def down(self):
        """ Select the next entry """
        if self.current < len(self.entries)-1:
            self.changeSelected(1)
            
    def enter(self):
        """ Call the selected entry """
        if self.entries != []:
            self.entries[self.current].call()
        
    def quit(self):
        """ Quits the game """
        self.running = False
        
    def changeSelected(self, mod):
        """ Change the highlighted menu entry """
        self.deselectEntry()
        self.current += mod
        self.current %= len(self.entries)
        self.selectEntry()
        
    def selectEntry(self):
        """ Select the current entry """
        if self.entries != []:
            self.entries[self.current].select()
        
    def deselectEntry(self):
        """ Deselect the current entry """
        if self.entries != []:
            self.entries[self.current].deselect()