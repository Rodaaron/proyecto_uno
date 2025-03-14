import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        # Calculate damage based on attack value and enemy defense
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

class Player(Character):
    def __init__(self, name, health, attack, defense, special_ability):
        super().__init__(name, health, attack, defense)
        self.special_ability = special_ability

    def choose_action(self):
        actions = [
            "Attack",
            "Defend",
            "Use Item",
            "Special Ability",
            "Flee"
        ]
        print("Choose an action:")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        choice = int(input("Enter the number of your action: "))
        return choice

    def perform_action(self, action_choice, enemy):
        if action_choice == 1:  # Attack
            self.attack_enemy(enemy)
        elif action_choice == 2:  # Defend
            print(f"{self.name} defends!")
            self.defend()
        elif action_choice == 3:  # Use Item
            print(f"{self.name} uses a healing item.")
            self.use_item()
        elif action_choice == 4:  # Special Ability
            print(f"{self.name} uses {self.special_ability}!")
            self.special_ability_attack(enemy)
        elif action_choice == 5:  # Flee
            print(f"{self.name} attempts to flee!")
            self.flee()
        else:
            print("Invalid action.")

    def defend(self):
        # Defend could temporarily reduce damage taken
        self.defense += 5
        print(f"{self.name}'s defense increased to {self.defense}.")

    def use_item(self):
        # Use item like healing
        self.health += 20
        print(f"{self.name}'s health increased to {self.health}.")

    def special_ability_attack(self, enemy):
        # Special attack might do a lot of damage
        damage = self.attack * 2 - enemy.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} unleashes their special ability for {damage} damage!")
        enemy.take_damage(damage)

    def flee(self):
        # Fleeing logic
        print(f"{self.name} flees the battle!")


class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)


def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        action_choice = player.choose_action()
        player.perform_action(action_choice, enemy)

        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy's turn to attack if still alive
        if enemy.is_alive():
            enemy.attack_player(player)

        if not player.is_alive():
            print(f"{player.name} has been defeated!")


# Example usage
def main():
    player = Player(name="Hero", health=100, attack=25, defense=5, special_ability="Flame Burst")
    enemy = Enemy(name="Goblin", health=50, attack=15, defense=3)

    combat(player, enemy)

main()
