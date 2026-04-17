# Inheritence

class Loadout:

    def __init__(self, primary, side, melee):
        self.primary = primary
        self.side = side
        self.melee = melee

    def __str__(self):
        return "Primary: {}, Side: {}, Melee {}".format(self.primary, self.side, self.melee)

    def side_statTrak(kills):
        self.side += kills

# INHERIT the loadout class
class Sniper(Loadout):

    def __init__(self, primary, side, melee, exp):

        # SUPER lets you access parent class and initialize everything inside
        super(Sniper, self).__init__(primary, side, melee)
        self.exp = exp

    # Overriding Methods to show exp in string
    def __str__(self):
        text = super(Sniper, self).__str__()
        text += ", Base EXP {}".format(self.exp)
        return text


    def double_exp(self):
        return self.exp * 2

sniper1 = Sniper("DSR-50", "1911", "Bayonet", 386)
print(sniper1)
print(f"double EXP!:{sniper1.double_exp()}")
