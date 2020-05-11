class Tutorial:

    def __init__(self, branch):
        self.__branch = branch

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, value):
        self.__branch = value


master = Tutorial('master')
print(master.branch)

master.branch = 'tutorial'

print(master.branch)

master.branch = 'help'

print(master.branch)
