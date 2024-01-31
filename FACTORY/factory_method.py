from abc import ABCMeta, abstractclassmethod


class Section(metaclass=ABCMeta):
    @abstractclassmethod
    def __repr__(self) -> str:
        pass


class SectionPersonal(Section):
    def __repr__(self) -> str:
        return "Personal"


class SectionProfissional(Section):
    def __repr__(self) -> str:
        return "Profissional"


class SectionGroups(Section):
    def __repr__(self) -> str:
        return "Groups"


class SectionProjects(Section):
    def __repr__(self) -> str:
        return "Projects"


class Profile(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.sections = []
        self.create_profile()

    @abstractclassmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def current_sessions_message(self):
        return f"This account has {len(self.sections)} sections: {self.sections}"

    def append_section(self, section):
        self.sections.append(section)


class LinkedinAccount(Profile):
    def create_profile(self):
        self.append_section(SectionPersonal())
        self.append_section(SectionProjects())


class FacebookAccount(Profile):
    def create_profile(self):
        self.append_section(SectionGroups())
        self.append_section(SectionPersonal())


if __name__ == "__main__":
    linkedin_account = LinkedinAccount()
    facebook_account = FacebookAccount()

    print(facebook_account.current_sessions_message())  # 4fun
    print(linkedin_account.current_sessions_message())
