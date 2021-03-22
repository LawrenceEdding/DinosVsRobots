import random

# sudo Randomize stats of robots and dinosaurs.
# Make attacks have a chance to miss and Spd stat?
# Play vs cpu.


class Robot:
    def __init__(self):
        self.name = ''  # assign at creation
        self.health = random.randint(20, 40)  # Bad practice Make 0 then modify with method call.
        self.power_level = 100
        self.Weapon = Weapon()  # Make weapon type a class??
        self.attack_power = 0
        self.is_fight = False

    def attack(self):
        # based on weapon modifies attack power?
        # roll to hit??
        self.power_level -= 10
        return self.attack_power

    def get_hit(self, damage):
        self.health -= damage
        print(f'{self.name} has {self.health} hp left.')

    def assign_attack_power(self):
        if self.Weapon.type == 'blunt':
            self.attack_power = 5
        if self.Weapon.type == 'ranged':
            self.attack_power = 7
        if self.Weapon.type == 'piercing':
            self.attack_power = 10


class Dinosaur:
    def __init__(self):
        self.type = ''  # Make class???
        self.health = random.randint(20, 40)
        self.energy = 100
        self.attack_power = 0

    def attack(self):
        print(f'Choose your attack: \n'
              f'[1] Tail slap\n'
              f'[2] Charge\n'
              f'[3] Bite\n'
              f'(Press the corresponding number)\n')
        while True:
            response = input()
            if response == '1':
                self.attack_power = 5
                break
            if response == '2':
                self.attack_power = 10
                break
            if response == '3':
                self.attack_power = 7
                break
            else:
                print(f'Please choose 1, 2, or 3')
        self.energy -= 10
        # based on attack choice. Make choice every time from 3. Modified accuracy.
        # roll to hit?? if hit return atk power else return 0
        return self.attack_power

    def get_hit(self, damage):
        self.health -= damage
        print(f'{self.type} has {self.health} hp left.')


class Fleet:
    def __init__(self):
        self.robots = []

    def join_fleet(self, robot):
        self.robots.append(robot)

    def robot_die(self):
        counter = 0
        while counter < len(self.robots):
            if self.robots[counter].health <= 0:
                print(f'{self.robots[counter].name} has died.')
                del self.robots[counter]

            counter += 1


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

    def join_herd(self, dino):
        self.dinosaurs.append(dino)

    def dino_die(self):
        counter = 0
        while counter < len(self.dinosaurs):
            if self.dinosaurs[counter].health <= 0:
                print(f'{self.dinosaurs[counter].type} has died.')
                del self.dinosaurs[counter]
            counter += 1


class Battlefield:
    def __init__(self):
        self.terrain = ''
        self.robot_combatant = Robot()
        self.dino_combatant = Dinosaur()

    # def check_win(self, combatant_one, combatant_two):
    #     if len(combatant_two) and len(combatant_one) == 0:
    #         print(f'Draw')
    #     if len(combatant_one) == 0:
    #         pass
    #     if len(combatant_two) == 0:
    #         pass

    def enter_battlefield(self, robot, dino):
        self.robot_combatant = robot
        self.dino_combatant = dino
