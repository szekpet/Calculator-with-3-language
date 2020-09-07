import json


class Config:

    def __init__(self):
        self.config_file = 'config.json'
        # IDOSZAKOSAN LETEZIK , IDOSZKAOSAN HOZ LETRE A WITH OPEN
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
            self.refreshValues()
        return

    def refreshValues(self):  # EZ A FUGGVENYUNK FRISSITI AZ ADATUNKAT A SZAMOLOGEPBEN
        self.languages = self.config['languages']
        self.default = self.config['default']
        self.user = self.config['user'].strip()
        if not self.user:
            self.user = self.default
        return

    def setValue(self, key, value):  # ERTEK VALASZTUNK A NYELVNEK TEHAT A ROMANRA IRJUK ROMAN LESZ
        self.config[key] = value
        self.refreshValues()
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)
        return

    def GetValueByLanguage(self, lang_value):
        return self.languages[self.user][lang_value]

    def GetAvailabeLanguages(self):
        nyelvek = (self.user, )
        for nyelv in self.languages:
            nyelvek += (nyelv, )
        return nyelvek
