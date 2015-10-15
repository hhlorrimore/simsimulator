import random 
character_dict = {}
 
class Character():
    def __init__(self, name, sex, skill_dictionary = {}, pregnant = False):    
        self.name = name
        self.sex = sex
        character_dict[self.name] = self        
        self.relationship_dictionary = {}
        self.skill_dictionary = skill_dictionary
        self.pregnant = pregnant              

    def __repr__(self):
    	"""
    	Making this longer
    	"""
        return str(self.name)

    def romance(self, other_character):
    	if self.relationship_dictionary[other_character] < 50:
    		if self.relationship_dictionary[other_character] < 10:
    			self.relationship_dictionary[other_character] = 0
    		else:
    			self.relationship_dictionary[other_character] -= 10
    	if self.relationship_dictionary[other_character] >= 100 and (self.sex is not character_dict[other_character].sex):
    		if self.sex is 'Female':
    			self.pregnant = True
    			print str(self.name) + " is now pregant with " + other_character + "'s baby!"
    		if character_dict[other_character].sex is 'Female':
    			character_dict[other_character].pregnant = True 
    			print other_character + " is now pregant with " + self.name + "'s baby!"

def relationship_creator():
	for character in character_dict:
		for other_character in character_dict:
			if character is not other_character:
				character_dict[character].relationship_dictionary[character_dict[other_character].name] = 0

def relationship_change():
	character_1 = "False"
	character_2 = "False"
	while character_1 is character_2:
		character_1 = random.choice(character_dict.keys())
		character_2 = random.choice(character_dict.keys())
