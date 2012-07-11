"""The main visual theme"""

import serge.blocks.themes

theme = serge.blocks.themes.Manager()
theme.load({
    'main':('',{
    # global settings
    'screen-height': 480,
    'screen-width': 320,
    'screen-title': 'Jumpy Car',
    'scroll-speed': 2,
    # size of a block
    'block-size': 64,
    'framerate': 30,
    'player-car-x':160,
    'player-car-y':450,
    'player-car-speed':5,
    # npc settings
    'npc-speed-normal':3,
    # bg settings
    'bg-pos-x':160,
    'bg-pos-y':0,
    # Number of lans
    'lane-num':10
    }),
    '__default__':'main'
})
G = theme.getProperty
