import random
from random import randint

# Base stats, limites fixées et ne changent jamais au fil de la partie.
p_hp = 150
p_atk = 25
p_pow = 40
p_def = 35
p_stam = 70
p_acc = 90
p_aff = 30
p_slots = 5

e_hp = 100
e_atk = random.randint(10, 30)
e_pow = random.randint(10, 45)
e_def = random.randint(20, 60)
e_stam = 70
e_acc = 90
e_aff = random.randint(10, 30)
e_slots = 5
e_yield = 50

# |current stats|, sont elles qui changent au fil du jeu.
cp_hp = p_hp
cp_atk = p_atk
cp_def = p_def
cp_stam = p_stam
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
dmg_taken: int = 0  #Changent au value nécéssaire et retournent à 0
# print(f"Tu as subi {dmg_taken} dmg.") ## à copier quand nécéssaire
# print(f"Tu as infligé {dmg_dealt} dmg.") ## à copier quand nécéssaire

# misc
p_tour = "VOTRE TOUR"
actions_m = "VOS ACTIONS"
print(f"e.atk: {e_atk}, e.def: {e_def}, e_aff: {e_aff}, e_pow: {e_pow}") #voir stats rand
# print(f"Tu as subi {dmg_taken} dmg.") ## à copier quand nécéssaire
# print(f"Tu as infligé {dmg_dealt} dmg.") ## à copier quand nécéssaire


#||plan actions||:
#   attaquer: opération atk vs e_def, check par p_acc, draine p_stam
#   guarder: draine p_stam, monte def 1 tour
#   récup: baisse def, regagne full stam
#   parrer: risqué(1/8) mais annule dégats avec petit regain stam, réduit stam ennemi, coup garranti si échoue
#   sorts: regarder ses sorts, aucune action
#   magie: lancer sort, scale affinité vs e_affinité si offensif. consomme slot(s)

#jeu commence
def main():
    while cp_hp > 0 and ce_hp > 0:
        #Tour joueur !11!!1!1
        print(f">{p_tour:=^20}<")
        print(f"Vos PV: {cp_hp}")
        print(f"Votre endurance: {cp_stam}")
        print(f"PV ennemi: {ce_hp}")
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
            elif action == "2":
                garde()
                break
            elif action == "3":
                recup()
                break
            elif action == "4":
                parry()
                break
            elif action == "5":
                sorts()
                break
            elif action == "6":
                cast()
                break
            elif action == "0":
                suicide()
                break
            else:
                print("Saisissez un chiffre valide.")
    if cp_hp <= 0:
        print("Bruhh t mort esti de pas bon.")
        exit()
    else:
        print(f"""bravo tu as tué ton ennemi.
    Tu as gagné {e_yield} exp.""")
        exit()


def attaque():
    global ce_hp, dmg_dealt, cp_stam, cp_acc
    hit_chance = randint(1, 100)
    if hit_chance <= cp_acc:  # Échoue si le % random est + grand que l'acc actuelle
        dmg_dealt = int(((p_pow * cp_atk / ce_def) / 10) + (p_pow * .5))
        if dmg_dealt <= 0:
            dmg_dealt = random.randint(1, 3)
        ce_hp = ce_hp - dmg_dealt
        if ce_hp <= 0:
            ce_hp = 0
        print(f"> Tu as infligé {dmg_dealt} dmg.")
        print(f"> Il reste {ce_hp} hp à l'ennemi.")
    else:
        print("Tu rates ton attaque!")
    cp_stam = cp_stam - 15
    dmg_dealt = 0
    return None


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
    global dmg_taken
    global cp_hp
    print(cp_hp)
    dmg_taken = cp_hp
    cp_hp = cp_hp - dmg_taken
    print(f"Tu as subi {dmg_taken} dmg.")
    dmg_taken = 0
    return None

if __name__ == "__main__":
    main()