class Champion:

    def __init__(self, champion, skin_list, active):
        self.champion = champion
        self.skin_list = skin_list
        self.active = active
        self.hidden = False

    def change_hidden(self):
        self.hidden = not self.hidden
