class ForceUser:

    def attacking(self):
        return f'{self.name} is Force attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):
    count = 0

    def __init__(self, name='Random Master', color='Blue'):
        self.name = name
        self.color = color
        JediMaster.count += 1

    def __str__(self):
        return f'{self.name} is in the House!'

    def __repr__(self):
        return f'JediMaster("{self.name}", "{self.color}")'

    def defense(self):
        return f'{self.name} is defending!'

    @staticmethod
    def get_code():
        return 'There is no emotion, there is PEACE.'

    @classmethod
    def get_count(cls):
        return cls.count

class SithLord(ForceUser):
    count = 0

    def __init__(self, name='Random Lord'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie, there is only PASSION.'

    @classmethod
    def get_count(cls):
        return cls.count




if __name__ == '__main__':
    player = JediMaster('Revan')
    print(player.__repr__())
    # player2 = JediMaster('Revan')
    # print(player2)
    1 / 0
 

