# This is a sample Python script.
from classes import Robot
from classes import Dinosaur
from classes import Battlefield
from classes import Fleet
from classes import Herd
from classes import Weapon
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dino1 = Dinosaur()
    dino2 = Dinosaur()
    dino3 = Dinosaur()

    robot1 = Robot()
    robot2 = Robot()
    robot3 = Robot()

    dino1.type = 'stegosaurus'
    dino2.type = 't-rex'
    dino3.type = 'pterodactyl'

    robot1.name = 'ryan'
    robot2.name = 'ryan 2.0'
    robot3.name = 'slasher mk II'

    robot1.Weapon.assign_weapon()
    robot2.Weapon.assign_weapon()
    robot3.Weapon.assign_weapon()
    robot1.assign_attack_power()
    robot2.assign_attack_power()
    robot3.assign_attack_power()

    robo_list = Fleet()
    dino_list = Herd()
    robo_list.join_fleet(robot1)
    robo_list.join_fleet(robot2)
    robo_list.join_fleet(robot3)
    dino_list.join_herd(dino1)
    dino_list.join_herd(dino2)
    dino_list.join_herd(dino3)

    battle = Battlefield()
    while True:
        battle.enter_battlefield(robo_list.robots[0], dino_list.dinosaurs[0])
        battle.dino_combatant.get_hit(battle.robot_combatant.attack())
        battle.robot_combatant.get_hit(battle.dino_combatant.attack())
        robo_list.robots[0] = battle.robot_combatant
        dino_list.dinosaurs[0] = battle.dino_combatant

        robo_list.robot_die()
        dino_list.dino_die()

        if not robo_list.robots:
            winner = 'dinosaurs'
            break

        if not dino_list.dinosaurs:
            winner = 'robots'
            break

    print(f'{winner} has won')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
