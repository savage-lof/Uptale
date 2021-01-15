import sqlite3
from bd import cur, con



def save(lvl, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_left, gg_sprite, el=None, gerl=None,
         npc=None, npc_boss=None):
    if lvl == 'lvl1':
        cur.execute('''INSERT INTO save(lvl, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, 
        wall_4_y, floor_x, floor_y, npc_x, npc_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, 
        gerl_x, gerl_y, el_x, el_y) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (lvl, wall_1.rect.center[0], wall_1.rect.center[1], wall_2.rect.center[0], wall_2.rect.center[1],
                     wall_3.rect.center[0], wall_3.rect.center[1], wall_4.rect.center[0], wall_4.rect.center[1],
                     floor.rect.center[0], floor.rect.center[1], npc.rect[0], npc.rect[1], chest.rect.center[0],
                     chest.rect.center[1], gg_left.rect.x, gg_left.rect.y, gg_sprite.rect.x, gg_sprite.rect.y,
                     gerl.rect.x, gerl.rect.y, el.rect.x, el.rect.y,))
    elif lvl == 'lvl2':
        cur.execute('''INSERT INTO save(lvl, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, 
        wall_4_y, floor_x, floor_y, npc_x, npc_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (lvl, wall_1.rect.center[0], wall_1.rect.center[1], wall_2.rect.center[0], wall_2.rect.center[1],
                     wall_3.rect.center[0], wall_3.rect.center[1], wall_4.rect.center[0], wall_4.rect.center[1],
                     floor.rect.center[0], floor.rect.center[1], npc.rect[0], npc.rect[1], chest.rect.center[0],
                     chest.rect.center[1], gg_left.rect.x, gg_left.rect.y, gg_sprite.rect.x, gg_sprite.rect.y,))
    else:
        cur.execute('''INSERT INTO save(lvl, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, 
        wall_4_y, floor_x, floor_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, npc_boss_x, 
        npc_boss_y) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (lvl, wall_1.rect.center[0], wall_1.rect.center[1], wall_2.rect.center[0], wall_2.rect.center[1],
                     wall_3.rect.center[0], wall_3.rect.center[1], wall_4.rect.center[0], wall_4.rect.center[1],
                     floor.rect.center[0], floor.rect.center[1], chest.rect.center[0],
                     chest.rect.center[1], gg_left.rect.x, gg_left.rect.y, gg_sprite.rect.x, gg_sprite.rect.y,
                     npc_boss.rect.x, npc_boss.rect.y,))
    con.commit()

