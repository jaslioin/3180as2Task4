from Weapon import Weapon
class Axe(Weapon):
	AXE_RANGE = 1
	AXE_INIT_DAMAGE = 40

	def __init__(self,owner):
		Weapon.__init__(self,self.AXE_RANGE,self.AXE_INIT_DAMAGE,owner)

	def enhance(self):
		self.effect +=10

#	override
	def action(self,posx,posy):
		print "You are using axe attacking",posx,posy,"."

		if self.owner.pos.distance(posx,posy) <= self.range:
			player = self.owner.game.getPlayer(posx,posy)

			if player is not None:
				player.decreaseHealth(self.effect)
		else:
			print "Out of reach."


