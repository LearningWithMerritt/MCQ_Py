class Chapter():

    def __init__(self,name):
        self.name = name
        self.sections = {}


    def __str__(self):
        return self.name

    def to_dict(self):
        return {self.name : self.sections}


    def add_section(self,name,filename):
        self.sections[name] = Section(self,name,filename)

    def get_section(self, section):
        return self.sections[section]



class Section():
    def __init__(self,chapter,name,filename):
        self.chapter = chapter
        self.name = name
        self.filename =  f"q_set{filename}.json"

    def __str__(self):
        return self.name

