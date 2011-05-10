class Template:

    def __init__(self, file):
        f = open(file, "r")
        self.contents = ""
        for line in f:
            self.contents = self.contents + line
        f.close

    def render(self, dict):
        return self.contents % dict

