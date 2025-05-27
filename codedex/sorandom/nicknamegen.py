import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2).capitalize()

def capitalize_word(w):
  return w.capitalize()

capitalize_suffix = list(map(capitalize_word,suffixes))

random_list_username = [create_fantasy_name(prefixes,capitalize_suffix) for name in range(10)]

def fire_in_name(name):
  return 'Fire' in name


fire_list_name = [fire for fire in random_list_username if fire_in_name(fire) == True]

filter_fire = list(map(fire_in_name,random_list_username))

print(random_list_username)

print(fire_list_name)