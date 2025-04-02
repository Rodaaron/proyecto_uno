def e_attaque():
    global cp_hp, dmg_dealt, ce_stam, ce_acc
    hit_chance = randint(1, 100)
    if hit_chance <= ce_acc:  # Échoue si le % random est + grand que l'acc actuelle
        print(int(ce_atk * 25/ ce_def))
        pow_bonus = int((e_pow / 2 - cp_def / 2))
        if pow_bonus < 1:
            pow_bonus = 0
        print(pow_bonus)
        dmg_dealt = int(((ce_atk * 25 / cp_def) + pow_bonus + (randint(-3, 3))))
        if dmg_dealt <= 0:
            dmg_dealt = random.randint(1, 3)
        cp_hp = cp_hp - dmg_dealt
        if cp_hp <= 0:
            cp_hp = 0
        print(f"> L'ennemi t'inflige {dmg_dealt} dmg.")
    else:
        print("L'ennemi rate son attaque!")
    ce_stam = ce_stam - 15
    dmg_dealt = 0
    return None


def e_garde():
    return "clank"


def e_recup():
    global ce_stam, e_stam, ce_def
    stam_regen = int(e_stam / 2)
    ce_stam = ce_stam + stam_regen
    if ce_stam > e_stam:
        stam_regen = e_stam - ce_stam
        ce_stam = e_stam
    print(f"> L'ennemi regagne {stam_regen} pts d'endurance!")
    return None


def e_parry():
    return "ROYAL GUARD"


def e_sorts():
    return "nerd"


def e_cast():
    return "alakazam"

