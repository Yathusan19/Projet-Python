# RPG

import pygame
import random
import math
import sys

pygame.init()

buisson = True
or1 = True
or2 = True
or3 = True
or4 = True
or5 = True
or6 = True
help = True
plage = True
runningMenu = False
arme_entrer = False
potion_entrer = False


while runningMenu:
    # GENERE LA FENETRE DU JEU
    pygame.display.set_caption("The Escape")
    screen = pygame.display.set_mode((1080, 720))
    # quit
    '''quit_button = pygame.image.load("Assets/quit.png")
    quit_button = pygame.transform.scale(quit_button, (100, 70))
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.x = 20
    quit_button_rect.y = 650'''
    # start
    '''play_button = pygame.image.load("../Projetpython2/Assets prj2/bouton.png")
    play_button = pygame.transform.scale(play_button, (200, 100))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_height() / 1.70)
    play_button_rect.y = math.ceil(screen.get_height() / 1.20)'''
    # BACKGROUND
    background = pygame.image.load("ASSETS/home.png")
    background = pygame.transform.scale(background, (1080, 720))
    y_background = 0
    x_background = 0

    # APPLIQUER LE FOND / start / Quitter
    screen.blit(background, (x_background, y_background))
    '''screen.blit(play_button, (play_button_rect.x, play_button_rect.y))'''
    '''screen.blit(quit_button, (quit_button_rect.x, quit_button_rect.y))'''
    # METTRE A JOUR LE FOND
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button_rect.collidepoint(event.pos):
                print("Lancement du jeu")
                runningMenu = False
            elif quit_button_rect.collidepoint(event.pos):
                print("Vous allez quitter")
                runningMenu = False
                pygame.quit()
                sys.exit()


# Monstrelvl1
class monster:
    vie_monstre = 100
    attaque_monstre = 10


# Monsterlvl2
class monster2:
    vie_monster2 = 105
    attaque_monster2 = 11


# Monsterlvl3
class monster3:
    vie_monster3 = 110
    attaque_monster3 = 12


# Monsterlvl4
class monster4:
    vie_monster4 = 115
    attaque_monster4 = 13


# Monsterlvl5BOSS
class monster5:
    vie_monster5 = 120
    attaque_monster5 = 14


# JOUEUR
class Player(pygame.sprite.Sprite):
    vie_joueur = 100
    attaque_joueur = 10
    liste_degats = [10, 30, 20, 10, 10, 20, 0, 0]
    liste_or = [10, 10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 40, 40, 50, 60, 70, 80, 90, 100]
    argents = 10
    compteur = 0

    def __init__(self):
        super().__init__()
        # self.health = 100  # vie
        self.max_health = 100  # vie max
        # self.attack = 10  # attaque
        self.velocity = 10  # vitesse de deplacement
        self.image = pygame.image.load("ASSETS/player_d.png")
        self.image = pygame.transform.scale(self.image, (1500, 1500))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.estEntre = False

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity


# GENERE LA FENETRE DU JEU
pygame.display.set_caption("The Escape")
screen = pygame.display.set_mode((1080, 720))

right_player = pygame.image.load("ASSETS/player_r.png")
right_player = pygame.transform.scale(right_player, (1500, 1500))

left_player = pygame.image.load("ASSETS/player_l.png")
left_player = pygame.transform.scale(left_player, (1500, 1500))

up_player = pygame.image.load("ASSETS/player_u.png")
up_player = pygame.transform.scale(up_player, (1500, 1500))

down_player = pygame.image.load("ASSETS/player_d.png")
down_player = pygame.transform.scale(down_player, (1500, 1500))

# BACKGROUND
background = pygame.image.load("ASSETS/MAP_FINAL2.png")
player = Player()
pressed = {}
y_background = 0
x_background = 0
running = True
while running:

    if player.rect.x == 370 and player.rect.y == 130 and buisson == True and player.vie_joueur < 100:
        print("je devrais vraiment goùter ces trucs ??")
        player.vie_joueur = 100
        print("vous avez maintenat :", player.vie_joueur, "pv")
        print("je devrais devenir vegan !!")
        buisson = False
        player.estEntre = False

    if player.rect.x == 190 and player.rect.y == 380 and plage == True:
        print("Pas le temps de se reposer !!")
        plage = False

    if player.rect.x == 170 and player.rect.y == 10 and or1 == True:
        player.argents += 10
        print("Vous avez trouvé 10 pièces d'or !!")
        or1 = False

    if player.rect.x == 340 and player.rect.y == 120 and or2 == True:
        player.argents += 10
        print("Vous avez trouvé 10 pièces d'or !!")
        or2 = False

    if player.rect.x == 240 and player.rect.y == 130 and or3 == True:
        player.argents += 10
        print("Vous avez trouvé 10 pièces d'or !!")
        or3 = False

    if player.rect.x == 80 and player.rect.y == 190 and or4 == True:
        player.argents += 10
        print("Sérieux les pièces au fond de la fontaine [+10 d'or] ?!")
        or4 = False

    if player.rect.x == 190 and player.rect.y == 320 and or5 == True:
        player.argents += 10
        print("Vous avez trouvé 10 pièces d'or !!")
        or5 = False

    if player.rect.x == 290 and player.rect.y == 230 and or6 == True:
        player.argents += 10
        print("Vous avez trouvé 10 pièces d'or !!")
        or6 = False

    # print(player.argents)
    # print(monster.vie_monstre)
    # print(player.vie_joueur)
    # print(player.rect.x, player.rect.y)
    # print(player.compteur)
    # APPLIQUER LE FOND
    screen.blit(background, (x_background, y_background))

    # appliquer l'image du joueur
    screen.blit(player.image, player.rect)

    # quelle touche est utilisée
    if pressed.get(pygame.K_RIGHT) and player.rect.x < 400:
        player.image = right_player
        x_background -= 10
    elif pressed.get(pygame.K_LEFT) and player.rect.x > 0:
        player.image = left_player
        x_background += 10
    elif pressed.get(pygame.K_UP) and player.rect.y > -20:
        player.image = up_player
        y_background += 10
    elif pressed.get(pygame.K_DOWN) and player.rect.y < 380:
        player.image = down_player
        y_background -= 10

    # METTRE A JOUR LE FOND
    pygame.display.flip()

    # si le joueur ferme le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            # detecte si une touche est activé
        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False

    # entrer dans la grotte
    if player.rect.x == 300 and player.rect.y == 360 and player.estEntre == False and player.compteur < 1:
        entrer = int(input("Voulez-vous enter ? (1)"))
        # combat1
        if entrer == 1:
            player.estEntre = True
            print("Vous allez commencer à combattre.")
            monster.vie_monstre -= player.attaque_joueur
            print("Vous avez attaqué ,", "il lui reste", monster.vie_monstre, "pv", ", à son tour d'attaquer !!")
            Player.vie_joueur -= monster.attaque_monstre
            print("Le monstre a attaqué, il vous reste", Player.vie_joueur, "pv")
            print("Tentez une attaque critique et essayé d'infliger soit 10, 20, 30 ou 0 de dégâts !!")
            monster.vie_monstre -= random.choice(Player.liste_degats)
            print("Attaque réaliser avec succès, il lui reste", monster.vie_monstre, "pv.")
            print("Tips pour tes futures combats: choix 1 = 10 dégâts/choix 2 = ~37.5% de chance de faire 10 dégâts, ~25% de faire 20 dégâts, ~25% de faire 0 dégât et ~12.5% de faire 30 dégâts.")
            Player.vie_joueur -= monster.attaque_monstre
            print("Le monstre a attaqué, il vous reste", Player.vie_joueur, "pv")

            while monster.vie_monstre > 0 and player.vie_joueur > 0:
                choix = int(input("Choix 1 / Choix 2 :"))
                if choix == 1:
                    monster.vie_monstre -= player.attaque_joueur
                    print("Vous avez attaqué ,", "il lui reste", monster.vie_monstre, "pv",
                          ", à son tour d'attaquer !!")
                else:
                    monster.vie_monstre -= random.choice(Player.liste_degats)
                    print("Attaque réaliser avec succès, il lui reste", monster.vie_monstre, "pv.")
                Player.vie_joueur -= monster.attaque_monstre
                print("Le monstre a attaqué, il vous reste", Player.vie_joueur, "pv")
            if monster.vie_monstre <= 0:
                print("Vous avez vaincu le monstre bien joué !!")
                print("il vous reste :", player.vie_joueur, "PV.Vous êtes salement amoché, aller vous soigner !!")
                player.argents += random.choice(Player.liste_or)
                print("Vous avez gagné", player.argents, '\033[33m' + "d'or", '\033[0m'"!!")
                print("Vous avez :", player.argents, "d'or.")
                player.estEntre = True
                player.compteur += 1
                potion_entrer = True
                arme_entrer = True
                help = True
            if player.vie_joueur <= 0:
                print("Vous êtes mort, retentez votre chance une prochaine fois")
                player.estEntre = True
                arme_entrer = True
                potion_entrer = True
                help = True
    # soins du joueur
    while player.rect.x == 90 and player.rect.y == 320 and player.vie_joueur < 100 and player.argents >= 10:
        soins = int(input("Voulez-vous vous soigner ? (1) / Quitter (2) "))
        if soins == 1:
            player.argents -= 10
            player.vie_joueur = 100
            player.estEntre = False
            print("Vous avez récupéré :", player.vie_joueur, "pv !!")
            print("Vous avez maintenant", player.argents, "d'or !!")

        elif soins == 2:
            player.rect.y -= 1
            print("À la prochaine !!")
            player.estEntre = False

    # potions (pour pv sup) probleme choix 4
    while player.rect.x == 120 and player.rect.y == 40 and player.vie_joueur == 100 and player.argents >= 15 and player.vie_joueur <= 130 and potion_entrer == True:
        print("Vous avez:", player.argents, "d'or")
        potion = int(input("+10pv pour 15 d'or (1)/ +20pv pour 25 d'or (2)/ +30pv pour 35 d'or (3)/ Quitter (4)"))
        if potion == 1 and player.argents >= 15:
            player.argents -= 15
            player.vie_joueur = 110
            print("Vous voilà avec:", player.vie_joueur, "pv")
            print("Vous avez maintenant", player.argents, "d'or !!")
            potion_entrer = False
        elif potion == 2 and player.argents >= 25:
            player.argents -= 25
            player.vie_joueur = 120
            print("Vous voilà avec:", player.vie_joueur, "pv")
            print("Vous avez maintenant", player.argents, "d'or !!")
            potion_entrer = False
        elif potion == 3 and player.argents >= 35:
            player.argents -= 35
            player.vie_joueur = 130
            print("Vous voilà avec:", player.vie_joueur, "pv")
            print("Vous avez maintenant", player.argents, "d'or !!")
            potion_entrer = False
        elif potion == 4:
            print("Repasse quand tu veux!")
            potion_entrer = False

    # armes plus puissante
    while player.rect.x == 180 and player.rect.y == 180 and player.argents >= 10 and player.vie_joueur >= 100 and arme_entrer == True:
        armes = int(input(
            "+5 de dégâts pour 10 d'or(1) / +10 de dégâts pour 20 d'or(2)/ +15 de dégâts pour 30 d'or(3)/ Quitter(4)"))
        if armes == 1 and player.argents >= 10 and player.attaque_joueur >= 10:
            player.argents -= 10
            player.attaque_joueur = 15
            print("Votre nouvelle arme fait 5 dégâts de plus (15 dégâts au total) !!")
            print("Il vous reste:", player.argents, "d'or")
            arme_entrer = False
        elif armes == 2 and player.argents >= 20 and player.attaque_joueur < 20:
            player.argents -= 20
            player.attaque_joueur = 20
            print("Votre nouvelle arme fait 10 dégâts de plus (20 dégâts au total) !!")
            print("Il vous reste:", player.argents, "d'or")
            arme_entrer = False
        elif armes == 3 and player.argents >= 30:
            player.argents -= 30
            player.attaque_joueur = 25
            print("Votre nouvelle arme fait 15 dégâts de plus (25 dégâts au total) !!")
            print("Il vous reste:", player.argents, "d'or")
            arme_entrer = False
        elif armes == 4:
            print("Au revoir !!")
            arme_entrer = False

    # combat 2
    if player.rect.x == 60 and player.rect.y == 360 and player.estEntre == False and monster.vie_monstre <= 0 and player.compteur == 1:
        entrer = int(input("Prêt pour ton deuxième combat ? (1)"))
        if entrer == 1:
            player.estEntre = True
            print("Vous allez commencer à combattre.")
            monster2.vie_monster2 -= player.attaque_joueur
            print("Vous avez attaqué ,", "il lui reste", monster2.vie_monster2, "pv", ", à son tour d'attaquer !!")
            player.vie_joueur -= monster2.attaque_monster2
            print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            while monster2.vie_monster2 > 0 and player.vie_joueur > 0:
                choix = int(input("Choix 1 / Choix 2 :"))
                if choix == 1:
                    monster2.vie_monster2 -= player.attaque_joueur
                    print("Vous avez attaqué ,", "il lui reste", monster2.vie_monster2, "pv",
                          ", à son tour d'attaquer !!")
                else:
                    monster2.vie_monster2 -= random.choice(Player.liste_degats)
                    print("Attaque réaliser avec succès, il lui reste", monster2.vie_monster2, "pv.")
                player.vie_joueur -= monster2.attaque_monster2
                print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            if monster2.vie_monster2 <= 0:
                print("Vous avez vaincu le monstre bien joué !!")
                print("Il vous reste :", player.vie_joueur, "PV.Vous êtes salement amoché, aller vous soigner !!")
                player.argents += random.choice(Player.liste_or)
                print("Vous avez gagné", player.argents, '\033[33m' + "d'or", '\033[0m'"!!")
                print("Vous avez :", player.argents, "d'or.")
                player.estEntre = True
                player.compteur += 1
                potion_entrer = True
                arme_entrer = True
                help = True
            if player.vie_joueur <= 0:
                print("Vous êtes mort, retentez votre chance une prochaine fois")
                player.estEntre = True
                potion_entrer = True
                arme_entrer = True
                help = True

    # combat 3
    if player.rect.x == 250 and player.rect.y == 300 and player.estEntre == False and monster2.vie_monster2 <= 0 and player.compteur == 2:
        entrer = int(input("Prêt pour ton troisième combat ? (1)"))
        if entrer == 1:
            player.estEntre = True
            print("Vous allez commencer à combattre.")
            monster3.vie_monster3 -= player.attaque_joueur
            print("Vous avez attaqué ,", "il lui reste", monster3.vie_monster3, "pv", ", à son tour d'attaquer !!")
            player.vie_joueur -= monster3.attaque_monster3
            print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            while monster3.vie_monster3 > 0 and player.vie_joueur > 0:
                choix = int(input("Choix 1 / Choix 2 :"))
                if choix == 1:
                    monster3.vie_monster3 -= player.attaque_joueur
                    print("Vous avez attaqué ,", "il lui reste", monster3.vie_monster3, "pv",
                          ", à son tour d'attaquer !!")
                else:
                    monster3.vie_monster3 -= random.choice(Player.liste_degats)
                    print("Attaque réaliser avec succès, il lui reste", monster3.vie_monster3, "pv.")
                player.vie_joueur -= monster3.attaque_monster3
                print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            if monster3.vie_monster3 <= 0:
                print("Vous avez vaincu le monstre bien joué !!")
                print("Il vous reste :", player.vie_joueur, "PV.Vous êtes salement amoché, aller vous soigner !!")
                player.argents += random.choice(Player.liste_or)
                print("Vous avez gagné", player.argents, '\033[33m' + "d'or", '\033[0m'"!!")
                print("Vous avez :", player.argents, "d'or.")
                player.estEntre = True
                player.compteur += 1
                potion_entrer = True
                arme_entrer = True
                help = True
            if player.vie_joueur <= 0:
                print("Vous êtes mort, retentez votre chance une prochaine fois")
                player.estEntre = True
                potion_entrer = True
                arme_entrer = True
                help = True

    # combat 4
    if player.rect.x == 330 and player.rect.y == 30 and player.estEntre == False and monster3.vie_monster3 <= 0 and player.compteur == 3:
        entrer = int(input("Prêt pour ton quatrième combat ? (1)"))
        if entrer == 1:
            player.estEntre = True
            print("Vous allez commencer à combattre.")
            monster4.vie_monster4 -= player.attaque_joueur
            print("Vous avez attaqué ,", "il lui reste", monster4.vie_monster4, "pv", ", à son tour d'attaquer !!")
            player.vie_joueur -= monster4.attaque_monster4
            print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            while monster4.vie_monster4 > 0 and player.vie_joueur > 0:
                choix = int(input("Choix 1 / Choix 2 :"))
                if choix == 1:
                    monster4.vie_monster4 -= player.attaque_joueur
                    print("Vous avez attaqué ,", "il lui reste", monster4.vie_monster4, "pv",
                          ", à son tour d'attaquer !!")
                else:
                    monster4.vie_monster4 -= random.choice(Player.liste_degats)
                    print("Attaque réaliser avec succès, il lui reste", monster4.vie_monster4, "pv.")
                player.vie_joueur -= monster4.attaque_monster4
                print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            if monster4.vie_monster4 <= 0:
                print("Vous avez vaincu le monstre bien joué !!")
                print("Il vous reste :", player.vie_joueur, "PV.Vous êtes salement amoché, aller vous soigner !!")
                player.argents += random.choice(Player.liste_or)
                print("Vous avez gagné", player.argents, '\033[33m' + "d'or", '\033[0m'"!!")
                print("Vous avez :", player.argents, "d'or.")
                player.estEntre = True
                player.compteur += 1
                potion_entrer = True
                arme_entrer = True
                help = True
            if player.vie_joueur <= 0:
                print("Vous êtes mort, retentez votre chance une prochaine fois")
                player.estEntre = True
                potion_entrer = True
                arme_entrer = True
                help = True
    # combat 5
    if player.rect.x == 290 and player.rect.y == 70 and player.estEntre == False and monster4.vie_monster4 <= 0 and player.compteur == 4:
        entrer = int(input("Prêt pour ton cinquième combat ? (1)"))
        if entrer == 1:
            player.estEntre = True
            print("Vous allez commencer à combattre.")
            monster5.vie_monster5 -= player.attaque_joueur
            print("Vous avez attaqué ,", "il lui reste", monster5.vie_monster5, "pv", ", à son tour d'attaquer !!")
            player.vie_joueur -= monster5.attaque_monster5
            print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            while monster5.vie_monster5 > 0 and player.vie_joueur > 0:
                choix = int(input("Choix 1 / Choix 2 :"))
                if choix == 1:
                    monster5.vie_monster5 -= player.attaque_joueur
                    print("Vous avez attaqué ,", "il lui reste", monster5.vie_monster5, "pv",
                          ", à son tour d'attaquer !!")
                else:
                    monster5.vie_monster5 -= random.choice(Player.liste_degats)
                    print("Attaque réaliser avec succès, il lui reste", monster5.vie_monster5, "pv.")
                player.vie_joueur -= monster5.attaque_monster5
                print("Le monstre a attaqué, il vous reste", player.vie_joueur, "pv")
            if monster5.vie_monster5 <= 0:
                print("L'effort est le clé de la victoire ! Bien joué, vous venez de battre le boss et vous avez fini vos combats.")
                # print("Il vous reste :", player.vie_joueur, "PV.Vous êtes salement amoché, aller vous soigner !!")
                player.argents += random.choice(Player.liste_or)
                print("Vous avez fini la partie avec : ", player.argents, '\033[33m' + "d'or", '\033[0m'"!!")
                # print("Vous avez :", player.argents, "d'or.")
                player.estEntre = True
                potion_entrer = True
                arme_entrer = True
                help = True
                running = False
            if player.vie_joueur <= 0:
                print("Vous êtes mort, retentez votre chance une prochaine fois")
                player.estEntre = True
                potion_entrer = True
                arme_entrer = True
                help = True

    if player.rect.x == 20 and player.rect.y == 40 and help == True:
        bot = int(input("[AMIRA] : Bonjour étranger comment puis-je t'aider ? (1) "))
        if bot == 1:
            print("[BOB] : Dis moi où sommes-nous ?")
            print("[AMIRA] : Nous sommes sur l'île des damnées .")
            print("[BOB] : Quoi ?! et comment est-ce qu'on sort de cet endroit  ?")
            print("[AMIRA] : Eh bien c'est simple c'est IM-PO-SSIBLE !!")
            print("[AMIRA] : Pour t'echapper de l'ile tu va devoir triomphé des 5 calamités et crois moi c'est peine perdue, ")
            print("tu devrais abandonné l'idée de pouvoir rentrer un jour chez toi.")
            print("[BOB] : Très bien où puis-je trouver ces calamités")
            print("[AMIRA] : Tu les trouvera dans des grottes plus ou moins dispersés, mais il y a un ordre à respecter .")
            print("[BOB] : Qui est ?? ")
            print("[AMIRA] : Non mais je vais quand meme pas tout dévoiler, gardons un peu de suspens ! ")
            print("[AMIRA] : Par contre ce que je peux te dire c'est que tu auras besoin de ressources pour pouvoir acheter des armes et des potions, ")
            print("nos échanges commerciaux sont possible avec de l'or, si tu veux en obtenir tu seras obliger de défaire une calamité.")
            print("[AMIRA] : Oh et je vous présente mon chien Ronald . Attention il mord !!!")
            print("[RONALD] : WOUAF WOUAF !!")
            print("[BOB] : Vaut mieux pas traîner ici . ")
            print("Tips : Peut-être qu'en te baladant sur l'île tu trouveras des petites récompenses .")
            help = False
