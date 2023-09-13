from GibotPy.extensions import reactions
import pickle

g = reactions.ReactionCommandGroup(0)

c = reactions.ReactionCommand(g, "reaction_role", "add/remove", "👍", role="Admin")

g.save()

l = reactions.ReactionCommandGroup.load_from_id(0)

print(l._commands)