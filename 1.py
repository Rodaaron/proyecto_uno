import random

# Base stats, limites fixées et ne changent jamais au fil de la partie.
p_hp = 150
p_atk = 25
p_def = 35
p_stam = 70
p_acc = 90
p_aff = 30
p_slots = 5

e_hp = 100
e_atk = random.randint(10, 30)
e_def = random.randint(5, 40)
e_stam = 70
e_acc = 90
e_aff = random.randint(10, 30)
e_slots = 5

# |current stats|, sont elles qui changent au fil du jeu.
cp_hp = p_hp
cp_atk = p_atk
cp_def = p_def
cp_acc = p_acc
cp_aff = p_aff
cp_slots = p_slots

ce_hp = e_hp
ce_atk = e_atk
ce_def = e_def
ce_acc = e_acc
ce_aff = e_aff
ce_slots = e_slots

#Stats mid combat
dmg_dealt: int = 0  #Changent au value nécéssaire et retournent à 0
dmg_dealt_msg = (f"Tu as infligé {dmg_dealt} dmg")
dmg_taken: int = 0  #Changent au value nécéssaire et retournent à 0
dmg_taken_msg = (f"Tu as subi {dmg_taken} dmg")
# misc
p_tour = "VOTRE TOUR"
actions_m = "VOS ACTIONS"
print(f"e.atk: {e_atk}, e.def: {e_def}, e_aff: {e_aff}") #voir stats rand


#||plan actions||:
#   attaquer: opération atk vs e_def, check par p_acc, draine p_stam
#   guarder: draine p_stam, monte def 1 tour
#   récup: baisse def, regagne full stam
#   parrer: risqué(1/8) mais annule dégats avec petit regain stam, réduit stam ennemi, coup garranti si échoue
#   sorts: regarder ses sorts, aucune action
#   magie: lancer sort, scale affinité vs e_affinité si offensif. consomme slot(s)

#jeu commence
def main():
    while p_hp > 0 and e_hp > 0:
        #Tour joueur !11!!1!1
        print(f">{p_tour:=^20}<")
        print(f"Vos PV: {p_hp}")
        print(f"PV ennemi: {e_hp}")
        print(f">{actions_m:=^10}<")
        print("""    1. Attaquer
    2. Garde
    3. Récupérer
    4. Parrer
    5. Voir vos Sorts (aucune action req.)
    6. Conjurer (nique ta mère si c pas un vrai mot jmen fous)""")
        while True:
            action = input()
            if action == "1":
                attaque()
                break
            elif action == 2:
                garde()
                break
            elif action == 3:
                recup()
                break
            elif action == 4:
                parry()
                break
            elif action == 5:
                sorts()
                break
            elif action == 6:
                cast()
                break
            elif action == "0":
                suicide()
            else:
                print("Saisissez un chiffre valide.")
    if cp_hp <= 0:
        print("Bruhh t mort esti de pas bon.")
    else:
        print("bravo tu as tué ton ennemi")


def attaque():
    return "shink shink"


def garde():
    return "clank"


def recup():
    return "*respire"


def parry():
    return "ROYAL GUARD"


def sorts():
    return "nerd"


def cast():
    return "alakazam"


def suicide():
    print("""> Tu ne pouvais pas continuer de vivre ainsi, les voix dans ta tête ont pris le dessus.
    >Tu te plantes ton épée dans le coeur.""")
    dmg_taken = cp_hp
    cp_hp = -dmg_taken
    print(dmg_taken_msg)
    dmg_taken = 0


if __name__ == "__main__":
    main()