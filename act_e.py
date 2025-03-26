def e_attaque():
    global ce_hp, dmg_dealt, cp_stam, cp_acc
    hit_chance = randint(1, 100)
    if hit_chance <= cp_acc:  # Échoue si le % random est + grand que l'acc actuelle
        print(int(cp_atk * 25/ cp_def))
        pow_bonus = int((p_pow / 2 - ce_def / 2))
        if pow_bonus < 1:
            pow_bonus = 0
        print(pow_bonus)
        dmg_dealt = int(((cp_atk * 25 / cp_def) + pow_bonus + (randint(-3, 3))))
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


def e_garde():
    return "clank"


def e_recup():
    global cp_stam, p_stam, cp_def
    stam_regen = int(p_stam / 2)
    cp_stam = cp_stam + stam_regen
    print(f"> Tu regagnes {stam_regen} pts d'endurance!")
    cp_def =- cp_def - 10
    # TODO réduire défense
    return None


def e_parry():
    return "ROYAL GUARD"


def e_sorts():
    return "nerd"


def e_cast():
    return "alakazam"


def e_suicide():
    print("""> Tu ne pouvais pas continuer de vivre ainsi, les voix dans ta tête ont pris le dessus.
>Tu te plantes ton épée dans le coeur.""")
    global dmg_dealt, cp_hp
    dmg_dealt = cp_hp
    cp_hp = cp_hp - dmg_dealt
    print(f"Tu as subi {dmg_dealt} dmg.")
    return None

