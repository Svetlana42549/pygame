class Player():
    def __init__(self,a,b,c,d,e):
        self.name = a
        self.cloth = b
        self.health = c
        self.weapon = d
        self.impactforce = e

    def print_info(self):
        print('ваше имя:',self.name )
        print('ваша одежда',self.cloth)
        print  ('ваше здоровье' ,self.health)
        print  ('ваше оружие',self.weapon)
        print ('сила удара'  ,self.impactforce)

me = Player('TOM', 'платье', '50', 'нож','100')
me.print_info()




