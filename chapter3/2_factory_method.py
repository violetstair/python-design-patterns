# 팩토리 메소드 구현
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    
    def __repr__(self):
        return r"PersonalSection"

    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    
    def __repr__(self):
        return r"AlbumSection"

    def describe(self):
        print("Album Section")


class PatentSection(Section):
    
    def __repr__(self):
        return r"PatentSection"

    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    
    def __repr__(self):
        return r"PublicationSection"

    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


class linkedin(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class facebook(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == "__main__":
    profile_type = input("which profile you'd like to create?[linkedin or facebook]")
    profile = eval(profile_type.lower())()
    print("creating profile ... ", type(profile).__name__)
    print("profile has selections -- ", profile.get_sections())
