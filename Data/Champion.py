class Champion:

    def __init__(self, champion, skin_list):
        self.champion = champion
        self.skin_list = skin_list
        self.active = False
        self.hidden = False

    def change_hidden(self):
        self.hidden = not self.hidden
