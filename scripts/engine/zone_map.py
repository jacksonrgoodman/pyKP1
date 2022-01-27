
####################
#
# dictionary = {
#     "key" : "string",
#     "bool" : True,
#     "int" : 0,
#     "array" : [],
#     "set": {}
# }
####################

# zone_map = {
#     'a1': {
# 'ID': 1,
#         'ZONENAME': "",
#         'DESCRIPTON': '',
#         'EXAMINATION': '',
#         'SOLVED': False,
#         'UP': '',
#         'DOWN': 'b1',
#         'LEFT': '',
#         'RIGHT': 'a2',
#     }
# }

zone_map = {
    'a1': {
        'ID': 1,
        'ZONENAME': "Field1",
        'DESCRIPTION': 'an empty field',
        'EXAMINATION': 'nothing yetA1',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2',
    },
    'a2': {
        'ID': 2,
        'ZONENAME': "Field2",
        'DESCRIPTION': 'a somber field',
        'EXAMINATION': 'nothing yetA2',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3',
    },
    'a3': {
        'ID': 3,
        'ZONENAME': "Field3",
        'DESCRIPTION': 'a weary field',
        'EXAMINATION': 'nothing yetA3',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4',
    },
    'a4': {
        'ID': 4,
        'ZONENAME': "Field4",
        'DESCRIPTION': 'a scary field',
        'EXAMINATION': 'nothing yetA4',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': '',
    },
    'b1': {
        'ID': 5,
        'ZONENAME': "Town1",
        'DESCRIPTION': 'a dreary village',
        'EXAMINATION': 'nothing yetB1',
        'SOLVED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'LEFT': '',
        'RIGHT': 'b2',
    },
    'b2': {
        'ID': 6,
        'ZONENAME': "Town2",
        'DESCRIPTION': 'a dying tavern',
        'EXAMINATION': 'nothing yetB2',
        'SOLVED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3',
    },
    'b3': {
        'ID': 7,
        'ZONENAME': "Town3",
        'DESCRIPTION': 'empty hospitals',
        'EXAMINATION': 'nothing yetB3',
        'SOLVED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4',
    },
    'b4': {
        'ID': 8,
        'ZONENAME': "Town4",
        'DESCRIPTION': 'a burnt church',
        'EXAMINATION': 'nothing yetB4',
        'SOLVED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': '',
    },
    'c1': {
        'ID': 9,
        'ZONENAME': "Castle1",
        'DESCRIPTION': 'a barricaded farm',
        'EXAMINATION': 'nothing yetC1',
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': 'd1',
        'LEFT': '',
        'RIGHT': 'c2',
    },
    'c2': {
        'ID': 10,
        'ZONENAME': "Castle2",
        'DESCRIPTION': 'a watchtower',
        'EXAMINATION': 'nothing yetC2',
        'SOLVED': False,
        'UP': 'b2',
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3',
    },
    'c3': {
        'ID': 11,
        'ZONENAME': "Castle3",
        'DESCRIPTION': 'old concrete foxhole',
        'EXAMINATION': 'nothing yetC3',
        'SOLVED': False,
        'UP': 'b3',
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4',
    },
    'c4': {
        'ID': 12,
        'ZONENAME': "Castle4",
        'DESCRIPTION': 'outside of the bunker',
        'EXAMINATION': 'nothing yetC4',
        'SOLVED': False,
        'UP': 'b4',
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': '',
    },
    'd1': {
        'ID': 13,
        'ZONENAME': "Dungeon1",
        'DESCRIPTION': 'a dark crawlspace',
        'EXAMINATION': 'nothing yetD1',
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
    },
    'd2': {
        'ID': 14,
        'ZONENAME': "Dungeon2",
        'DESCRIPTION': 'a dark hall',
        'EXAMINATION': 'nothing yetD2',
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
    },
    'd3': {
        'ID': 15,
        'ZONENAME': "Dungeon3",
        'DESCRIPTION': 'expansive caverns',
        'EXAMINATION': 'nothing yetD3',
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
    },
    'd4': {
        'ID': 16,
        'ZONENAME': "Dungeon4",
        'DESCRIPTION': 'inside the bunker',
        'EXAMINATION': 'nothing yetD4',
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
    }
}


def location_card(zone_map_key):

    value = zone_map_key
    if value == 1:
        print('#####################################')
        print('#               Field               #')
        print('#####################################')
    if value == 2:
        print('#####################################')
        print('#               Field               #')
        print('#####################################')
    if value == 3:
        print('#####################################')
        print('#               Field               #')
        print('#####################################')
    if value == 4:
        print('#####################################')
        print('#               Field               #')
        print('#####################################')
    if value == 5:
        print('#####################################')
        print('#             Village               #')
        print('#####################################')
    if value == 6:
        print('#####################################')
        print('#             Village               #')
        print('#####################################')
    if value == 7:
        print('#####################################')
        print('#             Village               #')
        print('#####################################')
    if value == 8:
        print('#####################################')
        print('#             Village               #')
        print('#####################################')
    if value == 9:
        print('#####################################')
        print('#              Castle               #')
        print('#####################################')
    if value == 10:
        print('#####################################')
        print('#              Castle               #')
        print('#####################################')
    if value == 11:
        print('#####################################')
        print('#              Castle               #')
        print('#####################################')
    if value == 12:
        print('#####################################')
        print('#              Castle               #')
        print('#####################################')
    if value == 13:
        print('#####################################')
        print('#              Dungeon              #')
        print('#####################################')
    if value == 14:
        print('#####################################')
        print('#              Dungeon              #')
        print('#####################################')
    if value == 15:
        print('#####################################')
        print('#              Dungeon              #')
        print('#####################################')
    if value == 16:
        print('#####################################')
        print('#              Dungeon              #')
        print('#####################################')

    return
