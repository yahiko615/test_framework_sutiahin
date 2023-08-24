# from work_with_mongo.character_collection import CharacterCollection
# from work_with_mongo.weapons_collection import WeaponsCollection
#
# weapons_collection = WeaponsCollection()
# character_collection = CharacterCollection()
#
# # weapons_collection.drop_collection('weapons')
# # character_collection.drop_collection('character')
#
#
# weapon = {
#     'weapon_name': 'Gorehowl',
#     'critical_strike': '22%',
#     'mastery': '33%'
# }
# insert_weapon = weapons_collection.insert_one(weapon).inserted_id
# print(f"Inserted user with ID: {insert_weapon}")
#
# characters = [
#     {'name': 'Irel', 'level': 22},
#     {'name': 'Anduin', 'level': 4},
#     {'name': 'Garrosh', 'level': 71}
# ]
# character_ids = character_collection.insert_many(characters).inserted_ids
# print(f"Inserted products with IDs: {character_ids}")
#
# found_with_weapon_name = weapons_collection.find_one({'weapon_name': 'Gorehowl'})
# print(found_with_weapon_name)
#
# found_characters = character_collection.find({'level': {'$gt': 20}})
# for character in found_characters:
#     print(character)
