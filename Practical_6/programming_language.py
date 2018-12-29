
class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.
                """
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        elif self.typing == "Static":
            return False

    def __str__(self):
         return "{}, {} Typing, Reflection={}, First appeared in {}".format(str(self.language), str(self.typing), str(self.reflection), str(self.year))



#from language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)


    language_list = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in language_list:
        if language.is_dynamic():
            print(language.language)

main()