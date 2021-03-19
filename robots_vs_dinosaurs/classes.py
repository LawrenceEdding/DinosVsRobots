# sudo Randomize stats of robots and dinosaurs.
# Make attacks have a chance to miss and Spd stat?
# Play vs cpu.

class Robot:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.power_level = 0
        self.Weapon = self.Weapon()  # Make weapon type a class??
        self.attack_power = 0
        self.is_fight = False

    def attack(self):
        # based on weapon modifies attack power?
        # roll to hit??
        return self.attack_power


class Dinosaur:
    def __init__(self):
        self.type = ''  # Make class???
        self.health = 0
        self.energy = 0
        self.attack_power = 0
        self.is_fight = False

    def attack(self):
        # based on weapon modifies attack power?
        # roll to hit??
        return self.attack_power


class Fleet:
    def __init__(self):
        self.robots = []

    def robot_die(self):
        if self.robots[0].health <= 0:
            del self.robots[0]
            print(f'{self.robots[0].name} has died.')


class Weapon:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.weapon_list = ['sword', 'katana', 'pistol', 'shotgun', 'bat', 'hammer', 'bow']

    def assign_weapon_type(self):
        if self.name == 'sword' or 'katana' or 'dagger' or 'axe':
            self.type = 'piercing'
        if self.name == 'pistol' or 'shotgun' or 'bow':
            self.type = 'ranged'
        if self.name == 'bat' or 'hammer':
            self.type = 'blunt'

    def assign_weapon(self):
        flag = False
        while not flag:
            self.name = input(f'choose which weapon you would like to use from {self.weapon_list}.')
            for i in self.weapon_list:
                if self.name == i:
                    flag = True
                    break
            if not flag:
                print(f'please choose a weapon from the list.')
        self.assign_weapon_type()


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def dino_die(self):
        if self.dinosaurs[0].health == 0:
            del self.dinosaurs[0]
            print(f'{self.dinosaurs[0].name} has died.')


class Battlefield:
    def __init__(self):
        self.terrain = ''
        self.robot_combatant = Robot()
        self.dino_combatant = Dinosaur()

    def check_win(self):
        pass
