class Champion:

    def __init__(self, champion, skin_list, active):#TODO maybe add hidden here
        self.champion = champion
        self.skin_list = skin_list
        self.active = active
        self.hidden = False

    def change_hidden(self):
        self.hidden = not self.hidden

#welcher champion
#welche skins vom champion
#welche größe der skins vom champion
#soll der champion überhaupt