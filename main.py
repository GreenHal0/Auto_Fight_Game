from random import randint


# Classe personnage
class perso:
    def __init__(self, attack, hp, armor, dodge):
        self.attack = attack
        self.hp = hp
        self.armor = armor
        self.dodge = dodge

        self.hpR = hp

    def getStats(self):
        return self.attack, self.hp, self.armor, self.dodge

    def getAttack(self):
        return self.attack

    def getHp(self):
        return self.hp

    def getArmor(self):
        return self.armor

    def getDodge(self):
        return self.dodge

    def hit(self, target):
        d = randint(1, 100)
        if d > target.getDodge():
            target.hp -= int(self.getAttack() * (1 -
                                                 (target.getArmor() / 100)))

    def est_vivant(self):
        return self.hp > 0

    def est_mort(self):
        return self.hp <= 0

    def revive(self):
        self.hp = self.hpR


# Classes
Assassin = perso(25, 150, 10, 30)
Tank = perso(15, 200, 40, 5)
Warrior = perso(30, 175, 20, 15)
Archer = perso(55, 120, 5, 10)


# Combat
def round(player1, player2, x):
    if player1.est_vivant() and player2.est_vivant():
        print("Nouveau round !")
        player1.hit(player2)
        player2.hit(player1)
        print(" PV du 1er joueur : ", player1.getHp(),
              "\n PV du 2e joueur  : ", player2.getHp())

        print("Fin du round ", x, " : ", end="")
        if player1.est_mort() and player2.est_mort():
            print("égalite, les deux joueurs sont morts en même temps")
        elif player1.est_mort():
            print("le joueur 1 est mort. Le joueur 2 l'emporte.")
        elif player2.est_mort():
            print("le joueur 2 est mort. Le joueur 1 l'emporte.")
        else:
            print("les deux joueurs sont toujours en vie.")
        print("")
    else:
        return 0


def combat(player1, player2):
    assert player1.hp > 0 and player2.hp > 0
    x = 0
    while player1.est_vivant() and player2.est_vivant:
        x += 1
        round(player1, player2, x)
    player1.revive(), player2.revive()


def combat_rec(player1, player2, x=0):
    round(player1, player2, x)
    if player1.est_vivant() and player2.est_vivant():
        combat_rec(player1, player2, x + 1)
    else:
        player1.revive(), player2.revive()


# Jeu de test

##combat_rec(Assassin,Tank)
##combat_rec(Assassin,Warrior)
##combat_rec(Assassin,Archer)

##combat_rec(Tank,Assassin)
##combat_rec(Tank,Warrior)
##combat_rec(Tank,Archer)

##combat_rec(Warrior,Assassin)
##combat_rec(Warrior,Tank)
##combat_rec(Warrior,Archer)

##combat_rec(Archer,Assassin)
##combat_rec(Archer,Tank)
##combat_rec(Archer,Warrior)

# Creation de son personnage


def creer_perso(nom_du_personnage):
    input("Vous allez maintenant répartir 260points (press 'ok')")
    atk = int(
        input("Choississz votre nombre de points d'attaque (10 à 50) : "))
    hp = int(input("Choississez votre nombre de points de vie (150 à 250) : "))
    armor = int(input("Choississez votre pourcentage de defense (0 à 30) : "))
    dodge = int(input("Choississez votre pourcentage d'esquive (0 à 25) : "))

    assert (atk >= 10 and atk <= 50)
    assert (hp >= 150 and hp <= 250)
    assert (armor >= 0 and armor <= 30)
    assert (dodge >= 0 and dodge <= 25)
    assert (atk + hp + armor + dodge < 260)

    nom_du_personnage = perso(atk, hp, armor, dodge)
    return nom_du_personnage
