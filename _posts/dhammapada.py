class Person():
    def __init__(
            self,
            teachings,
            actions
    ):
        self.teachings = teachings
        self.actions = actions


""" 19-20 """
person = Person('many', 'skillfull')

if person.actions == 'skillfull':
    person.contemplative_benefits = 'many'

print(person.contemplative_benefits)

""" 33 """
class Mind():
    def __init__(
            self,
            state='agitated'
    ):
        self.state = state

def sage(mind):
    mind.state = 'straight'
    return mind

m = Mind()
m = sage(m)

# penguin classics
