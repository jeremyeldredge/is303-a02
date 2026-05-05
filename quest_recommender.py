"""
Jeremy Eldredge - IS 303
A02 - Quest Recommender

Program that sugguests a quest type based on player level and class

Inputs:
-  Player name (str)
-  Player class (str)
-  Player level (int)

Processes:
-  Validate player class
-  Validate player level
-  Use player class and level to determine available quests

Outputs:
-  Error message if necessary
-  Player name
-  Quest recommendations per class and level range
"""
# input collection
player_name = input("Player name: ")
player_class = input("Player class: ")
player_level = input("Player level: ")

ready_to_process = True

# input validation and error messages

player_class = player_class.lower()
class_is_valid = False
if player_class == "warrior" or player_class == "mage" or player_class == "rogue":
   class_is_valid = True
else:
   print("Invalid class type. Please enter warrior, mage, or rogue.")
   ready_to_process = False

player_level = player_level.replace(".","",1)
level_is_int = player_level.isdigit()
if level_is_int == True:
   player_level = int(player_level)
level_is_reasonable = False
if level_is_int == True and player_level > 0:
   level_is_reasonable = True

if level_is_reasonable == False or level_is_int == False:
   print("Invalid level. Please enter a whole number greater than or equal to 1.")
   ready_to_process = False

# quest determination
hard_quest = ""
normal_quest = ""
easy_quest = ""

if ready_to_process == True:
   if player_level >= 26:
      if player_class == "warrior":
         hard_quest = "Hard quest: Slay the physical form of a deity that has broken free from its prison."
         normal_quest = "Normal quest: Fight through an overrun mine and destroy the creature nest at its core."
         easy_quest = "Easy quest: Hold the village gate against an incoming raid."
      elif player_class == "mage":
         hard_quest = "Hard quest: Stop a cult from completing a ritual that will blot out the sun forever."
         normal_quest = "Normal quest: Locate and seal a cracked ley line before it destabilizes the region."
         easy_quest = "Easy quest: Track down a stolen spellbook before its magic is misued."
      else:
         hard_quest = "Hard quest: Steal the artifact keeping an ancient evil tethered to the world."
         normal_quest = "Normal quest: Intercept secret letters to expose a plot against the crown."
         easy_quest = "Easy quest: Lift a signet ring from a corrupt noble without being seen."
   elif player_level >= 11:
      hard_quest = "Hard quest: Unlocks at level 26."
      if player_class == "warrior":
         normal_quest = "Normal quest: Fight through an overrun mine and destroy the creature nest at its core."
         easy_quest = "Easy quest: Hold the village gate against an incoming raid."
      elif player_class == "mage":
         normal_quest = "Normal quest: Locate and seal a cracked ley line before it destabilizes the region."
         easy_quest = "Easy quest: Track down a stolen spellbook before its magic is misued."
      else:
         normal_quest = "Normal quest: Intercept secret letters to expose a plot against the crown."
         easy_quest = "Easy quest: Lift a signet ring from a corrupt noble without being seen."
   else:
      hard_quest = "Hard quest: Unlocks at level 26."
      normal_quest = "Normal quest: Unlocks at level 11."
      if player_class == "warrior":
         easy_quest = "Easy quest: Hold the village gate against an incoming raid."
      elif player_class == "mage":
         easy_quest = "Easy quest: Track down a stolen spellbook before its magic is misued."
      else:
         easy_quest = "Easy quest: Lift a signet ring from a corrupt noble without being seen."

# outputs

if ready_to_process == True:
   print(f"Available quests for {player_name}:\n"
      f"{hard_quest}\n"
      f"{normal_quest}\n"
      f"{easy_quest}")
      
      
   
    




