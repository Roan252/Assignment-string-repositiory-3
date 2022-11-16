# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_scorer_0 = "Ruud Gullit"   
goal_scorer_1 = "Marco van Basten"
goal_0 = 32     #note, python is case sensitive!
goal_1 = 54
scorers = (f'{goal_scorer_0} {goal_0}, {goal_scorer_1} {goal_1}')
print(scorers)
report = (f'{goal_scorer_0} scored in the {goal_0}nd minute\n{goal_scorer_1} scored in the {goal_1}th minute')
print(report)

player = "Lionel Messi"
space = player.find(" ")
first_name = player [0:player.find(' ')] # This takes 0=the first letter till ' '=the space
last_name = player [player.find (' ') +1:]  # This takes the first letter after space till : =the end of player 
first_name_len = len(first_name)

print(first_name)
print(last_name)
last_name_len = len(last_name)
print(last_name_len)
name_short = first_name[0] + ". " + last_name
print(name_short)

chanting = (first_name) + "! "  #take small steps at a time
chant_len = (f'{chanting}'*len(first_name))
chant = chant_len [:-1] #here the last space must be removed
print(chant)
good_chant = (chant[:-1] != " ") 
print(good_chant)
