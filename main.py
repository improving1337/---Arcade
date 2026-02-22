import arcade

# Конфиг
W, H = 1000, 600
CELL = 60
VISIBLE_UP_BLOCKS = 10
VISIBLE_DOWN_BLOCKS = 3
VISIBLE_TOTAL_BLOCKS = VISIBLE_UP_BLOCKS + VISIBLE_DOWN_BLOCKS  # 13
SCROLL_SPEED = 420.0
GRAVITY = 2200.0
JUMP_V = 650.0
PLAYER_W = 44
PLAYER_H = 44
SPAWN_CELL = (1, 1)

# Настройка игрового уровня, мир в координатах и можно ставить. Так же есть Editor.py, в нём можно создать свой уровень:
#   (x, y, "block")               -> полный блок
#   (x, y, "emptyblock")          -> контур
#   (x, y, "halfblock", "up")     -> верхняя половина блока
#   (x, y, "halfblock", "down")   -> нижняя половина блока
#
# Шипы:
#   (x, y, "spike")
#   (x, y, "spike", "up|down|left|right")
#
# Маленький шип:
#   (x, y, "smallspike", dir, half)
#   half = up|down
#   dir  = up|down|left|right
#
LEVEL = [
    (5, 14, 'spike', 'up'),
    (6, 1, 'smallspike', 'down', 'up'),
    (6, 2, 'block'),
    (6, 3, 'block'),
    (6, 4, 'block'),
    (6, 5, 'block'),
    (6, 6, 'block'),
    (6, 7, 'block'),
    (6, 8, 'block'),
    (6, 9, 'block'),
    (6, 10, 'block'),
    (6, 11, 'block'),
    (6, 12, 'block'),
    (6, 13, 'block'),
    (7, 3, 'spike', 'down'),
    (7, 4, 'block'),
    (7, 5, 'spike', 'up'),
    (8, 3, 'spike', 'down'),
    (8, 4, 'block'),
    (8, 5, 'spike', 'up'),
    (9, 3, 'spike', 'down'),
    (9, 4, 'block'),
    (9, 5, 'spike', 'up'),
    (10, 1, 'smallspike', 'down', 'up'),
    (10, 2, 'block'),
    (10, 3, 'block'),
    (10, 4, 'block'),
    (10, 5, 'block'),
    (10, 6, 'block'),
    (10, 7, 'block'),
    (10, 8, 'block'),
    (10, 9, 'block'),
    (10, 10, 'block'),
    (10, 11, 'block'),
    (10, 12, 'block'),
    (10, 13, 'block'),
    (11, 3, 'spike', 'down'),
    (11, 4, 'block'),
    (11, 5, 'spike', 'up'),
    (12, 3, 'spike', 'down'),
    (12, 4, 'block'),
    (12, 5, 'spike', 'up'),
    (13, 3, 'spike', 'down'),
    (13, 4, 'block'),
    (13, 5, 'spike', 'up'),
    (14, 1, 'smallspike', 'down', 'up'),
    (14, 2, 'block'),
    (14, 3, 'block'),
    (14, 4, 'block'),
    (14, 5, 'block'),
    (14, 6, 'block'),
    (14, 7, 'block'),
    (14, 8, 'block'),
    (14, 9, 'block'),
    (14, 10, 'block'),
    (14, 11, 'block'),
    (14, 12, 'block'),
    (14, 13, 'block'),
    (24, 7, 'spike', 'left'),
    (24, 13, 'spike', 'left'),
    (25, 0, 'smallspike', 'up', 'down'),
    (25, 6, 'spike', 'down'),
    (25, 7, 'emptyblock'),
    (25, 8, 'spike', 'up'),
    (25, 12, 'spike', 'down'),
    (25, 13, 'emptyblock'),
    (26, 0, 'block'),
    (26, 7, 'spike', 'right'),
    (26, 13, 'spike', 'right'),
    (27, 0, 'halfblock', 'up'),
    (27, 9, 'spike', 'left'),
    (28, 0, 'block'),
    (28, 8, 'spike', 'down'),
    (28, 9, 'emptyblock'),
    (28, 10, 'spike', 'up'),
    (29, 0, 'smallspike', 'up', 'down'),
    (29, 9, 'spike', 'right'),
    (30, 0, 'block'),
    (30, 1, 'block'),
    (31, 0, 'smallspike', 'up', 'down'),
    (31, 1, 'block'),
    (31, 3, 'spike', 'down'),
    (31, 4, 'block'),
    (31, 5, 'halfblock', 'down'),
    (31, 12, 'spike', 'left'),
    (32, 0, 'smallspike', 'up', 'down'),
    (32, 1, 'block'),
    (32, 3, 'spike', 'down'),
    (32, 4, 'block'),
    (32, 11, 'spike', 'down'),
    (32, 12, 'emptyblock'),
    (32, 13, 'spike', 'up'),
    (33, 0, 'smallspike', 'up', 'down'),
    (33, 1, 'block'),
    (33, 3, 'spike', 'down'),
    (33, 4, 'block'),
    (33, 5, 'halfblock', 'down'),
    (33, 9, 'spike', 'left'),
    (33, 12, 'spike', 'right'),
    (34, 0, 'block'),
    (34, 1, 'block'),
    (34, 8, 'spike', 'down'),
    (34, 9, 'emptyblock'),
    (34, 10, 'spike', 'up'),
    (35, 0, 'smallspike', 'up', 'down'),
    (35, 1, 'block'),
    (35, 9, 'spike', 'right'),
    (36, 0, 'smallspike', 'up', 'down'),
    (36, 1, 'block'),
    (37, 0, 'smallspike', 'up', 'down'),
    (37, 1, 'block'),
    (38, 0, 'block'),
    (38, 1, 'block'),
    (38, 9, 'spike', 'left'),
    (39, 0, 'smallspike', 'up', 'down'),
    (39, 1, 'block'),
    (39, 3, 'spike', 'down'),
    (39, 4, 'block'),
    (39, 5, 'halfblock', 'down'),
    (39, 8, 'spike', 'down'),
    (39, 9, 'emptyblock'),
    (39, 10, 'spike', 'up'),
    (40, 0, 'smallspike', 'up', 'down'),
    (40, 1, 'block'),
    (40, 3, 'spike', 'down'),
    (40, 4, 'block'),
    (40, 9, 'spike', 'right'),
    (40, 12, 'spike', 'left'),
    (41, 0, 'smallspike', 'up', 'down'),
    (41, 1, 'block'),
    (41, 3, 'spike', 'down'),
    (41, 4, 'block'),
    (41, 5, 'halfblock', 'down'),
    (41, 11, 'spike', 'down'),
    (41, 12, 'emptyblock'),
    (41, 13, 'spike', 'up'),
    (42, 0, 'block'),
    (42, 1, 'block'),
    (42, 12, 'spike', 'right'),
    (43, 0, 'smallspike', 'up', 'down'),
    (44, 9, 'spike', 'left'),
    (45, 8, 'spike', 'down'),
    (45, 9, 'emptyblock'),
    (45, 10, 'spike', 'up'),
    (46, 9, 'spike', 'right'),
    (49, 0, 'block'),
    (49, 4, 'spike', 'down'),
    (49, 5, 'block'),
    (49, 6, 'block'),
    (49, 7, 'block'),
    (49, 8, 'block'),
    (49, 9, 'block'),
    (49, 10, 'block'),
    (49, 11, 'block'),
    (49, 12, 'block'),
    (49, 13, 'block'),
    (50, 0, 'smallspike', 'up', 'down'),
    (51, 0, 'smallspike', 'up', 'down'),
    (52, 0, 'block'),
    (52, 1, 'block'),
    (52, 5, 'spike', 'down'),
    (52, 6, 'block'),
    (52, 7, 'block'),
    (52, 8, 'block'),
    (52, 9, 'block'),
    (52, 10, 'block'),
    (52, 11, 'block'),
    (52, 12, 'block'),
    (52, 13, 'block'),
    (53, 0, 'smallspike', 'up', 'down'),
    (54, 0, 'smallspike', 'up', 'down'),
    (55, 0, 'block'),
    (55, 4, 'spike', 'down'),
    (55, 5, 'block'),
    (55, 6, 'block'),
    (55, 7, 'block'),
    (55, 8, 'block'),
    (55, 9, 'block'),
    (55, 10, 'block'),
    (55, 11, 'block'),
    (55, 12, 'block'),
    (55, 13, 'block'),
    (56, 0, 'smallspike', 'up', 'down'),
    (57, 0, 'smallspike', 'up', 'down'),
    (58, 0, 'block'),
    (58, 1, 'block'),
    (58, 5, 'spike', 'down'),
    (58, 6, 'block'),
    (58, 7, 'block'),
    (58, 8, 'block'),
    (58, 9, 'block'),
    (58, 10, 'block'),
    (58, 11, 'block'),
    (58, 12, 'block'),
    (58, 13, 'block'),
    (59, 0, 'smallspike', 'up', 'down'),
    (60, 0, 'smallspike', 'up', 'down'),
    (61, 0, 'block'),
    (61, 1, 'block'),
    (61, 2, 'block'),
    (61, 6, 'spike', 'down'),
    (61, 7, 'block'),
    (61, 8, 'block'),
    (61, 9, 'block'),
    (61, 10, 'block'),
    (61, 11, 'block'),
    (61, 12, 'block'),
    (61, 13, 'block'),
    (62, 0, 'smallspike', 'up', 'down'),
    (63, 0, 'smallspike', 'up', 'down'),
    (63, 11, 'spike', 'left'),
    (64, 0, 'block'),
    (64, 1, 'block'),
    (64, 2, 'block'),
    (64, 10, 'spike', 'down'),
    (64, 11, 'emptyblock'),
    (64, 12, 'spike', 'up'),
    (65, 2, 'block'),
    (65, 7, 'spike', 'left'),
    (65, 11, 'spike', 'right'),
    (66, 0, 'block'),
    (66, 1, 'block'),
    (66, 2, 'block'),
    (66, 6, 'spike', 'down'),
    (66, 7, 'emptyblock'),
    (66, 8, 'spike', 'up'),
    (67, 7, 'spike', 'right'),
    (68, 9, 'spike', 'left'),
    (69, 0, 'block'),
    (69, 1, 'block'),
    (69, 2, 'block'),
    (69, 8, 'spike', 'down'),
    (69, 9, 'emptyblock'),
    (69, 10, 'spike', 'up'),
    (70, 2, 'block'),
    (70, 9, 'spike', 'right'),
    (71, 0, 'block'),
    (71, 1, 'block'),
    (71, 2, 'block'),
    (72, 0, 'spike', 'up'),
    (73, 0, 'smallspike', 'up', 'down'),
    (74, 0, 'smallspike', 'up', 'down'),
    (74, 9, 'spike', 'left'),
    (75, 8, 'spike', 'down'),
    (75, 9, 'emptyblock'),
    (75, 10, 'spike', 'up'),
    (76, 9, 'spike', 'right'),
    (78, 0, 'spike', 'up'),
    (78, 6, 'spike', 'left'),
    (79, 0, 'spike', 'up'),
    (79, 5, 'spike', 'down'),
    (79, 6, 'emptyblock'),
    (79, 7, 'spike', 'up'),
    (80, 0, 'block'),
    (80, 6, 'spike', 'right'),
    (81, 9, 'spike', 'left'),
    (82, 2, 'spike', 'down'),
    (82, 3, 'block'),
    (82, 8, 'spike', 'down'),
    (82, 9, 'emptyblock'),
    (82, 10, 'spike', 'up'),
    (83, 9, 'spike', 'right'),
    (84, 11, 'spike', 'left'),
    (85, 10, 'spike', 'down'),
    (85, 11, 'emptyblock'),
    (85, 12, 'spike', 'up'),
    (86, 0, 'spike', 'up'),
    (86, 11, 'spike', 'right'),
    (90, 0, 'block'),
    (90, 7, 'smallspike', 'down', 'up'),
    (90, 8, 'block'),
    (90, 9, 'block'),
    (90, 10, 'block'),
    (90, 11, 'block'),
    (90, 12, 'block'),
    (90, 13, 'block'),
    (91, 0, 'block'),
    (91, 7, 'spike', 'down'),
    (91, 8, 'block'),
    (91, 9, 'block'),
    (91, 10, 'block'),
    (91, 11, 'block'),
    (91, 12, 'block'),
    (91, 13, 'block'),
    (92, 0, 'block'),
    (92, 7, 'spike', 'down'),
    (92, 8, 'block'),
    (92, 9, 'block'),
    (92, 10, 'block'),
    (92, 11, 'block'),
    (92, 12, 'block'),
    (92, 13, 'block'),
    (93, 0, 'block'),
    (93, 7, 'spike', 'down'),
    (93, 8, 'block'),
    (93, 9, 'block'),
    (93, 10, 'block'),
    (93, 11, 'block'),
    (93, 12, 'block'),
    (93, 13, 'block'),
    (94, 0, 'block'),
    (94, 1, 'block'),
    (94, 8, 'spike', 'down'),
    (94, 9, 'block'),
    (94, 10, 'block'),
    (94, 11, 'block'),
    (94, 12, 'block'),
    (94, 13, 'block'),
    (95, 0, 'block'),
    (95, 1, 'block'),
    (95, 8, 'spike', 'down'),
    (95, 9, 'block'),
    (95, 10, 'block'),
    (95, 11, 'block'),
    (95, 12, 'block'),
    (95, 13, 'block'),
    (96, 0, 'block'),
    (96, 1, 'block'),
    (96, 8, 'spike', 'down'),
    (96, 9, 'block'),
    (96, 10, 'block'),
    (96, 11, 'block'),
    (96, 12, 'block'),
    (96, 13, 'block'),
    (97, 0, 'block'),
    (97, 1, 'block'),
    (97, 8, 'spike', 'down'),
    (97, 9, 'block'),
    (97, 10, 'block'),
    (97, 11, 'block'),
    (97, 12, 'block'),
    (97, 13, 'block'),
    (98, 0, 'block'),
    (98, 1, 'block'),
    (98, 2, 'block'),
    (98, 9, 'spike', 'down'),
    (98, 10, 'block'),
    (98, 11, 'block'),
    (98, 12, 'block'),
    (98, 13, 'block'),
    (99, 0, 'block'),
    (99, 1, 'block'),
    (99, 2, 'block'),
    (99, 9, 'spike', 'down'),
    (99, 10, 'block'),
    (99, 11, 'block'),
    (99, 12, 'block'),
    (99, 13, 'block'),
    (100, 0, 'block'),
    (100, 1, 'block'),
    (100, 2, 'block'),
    (100, 9, 'spike', 'down'),
    (100, 10, 'block'),
    (100, 11, 'block'),
    (100, 12, 'block'),
    (100, 13, 'block'),
    (101, 0, 'block'),
    (101, 1, 'block'),
    (101, 2, 'block'),
    (101, 3, 'smallspike', 'up', 'down'),
    (101, 9, 'spike', 'down'),
    (101, 10, 'block'),
    (101, 11, 'block'),
    (101, 12, 'block'),
    (101, 13, 'block'),
    (102, 0, 'block'),
    (102, 1, 'block'),
    (102, 2, 'block'),
    (102, 3, 'spike', 'up'),
    (102, 9, 'spike', 'down'),
    (102, 10, 'block'),
    (102, 11, 'block'),
    (102, 12, 'block'),
    (102, 13, 'block'),
    (103, 0, 'block'),
    (103, 1, 'block'),
    (103, 2, 'block'),
    (103, 3, 'halfblock', 'down'),
    (103, 9, 'spike', 'down'),
    (103, 10, 'block'),
    (103, 11, 'block'),
    (103, 12, 'block'),
    (103, 13, 'block'),
    (104, 0, 'block'),
    (104, 1, 'block'),
    (104, 2, 'block'),
    (104, 9, 'spike', 'down'),
    (104, 10, 'block'),
    (104, 11, 'block'),
    (104, 12, 'block'),
    (104, 13, 'block'),
    (105, 0, 'block'),
    (105, 1, 'block'),
    (105, 2, 'block'),
    (105, 3, 'smallspike', 'up', 'down'),
    (105, 9, 'spike', 'down'),
    (105, 10, 'block'),
    (105, 11, 'block'),
    (105, 12, 'block'),
    (105, 13, 'block'),
    (106, 0, 'block'),
    (106, 1, 'block'),
    (106, 2, 'block'),
    (106, 3, 'smallspike', 'up', 'down'),
    (106, 4, 'halfblock', 'down'),
    (106, 8, 'smallspike', 'down', 'up'),
    (106, 9, 'block'),
    (106, 10, 'block'),
    (106, 11, 'block'),
    (106, 12, 'block'),
    (106, 13, 'block'),
    (107, 0, 'block'),
    (107, 1, 'block'),
    (107, 2, 'block'),
    (107, 3, 'smallspike', 'up', 'down'),
    (107, 7, 'smallspike', 'down', 'up'),
    (107, 8, 'block'),
    (107, 9, 'block'),
    (107, 10, 'block'),
    (107, 11, 'block'),
    (107, 12, 'block'),
    (107, 13, 'block'),
    (108, 0, 'block'),
    (108, 1, 'block'),
    (108, 2, 'block'),
    (108, 8, 'smallspike', 'down', 'up'),
    (108, 9, 'block'),
    (108, 10, 'block'),
    (108, 11, 'block'),
    (108, 12, 'block'),
    (108, 13, 'block'),
    (109, 0, 'block'),
    (109, 1, 'block'),
    (109, 2, 'block'),
    (109, 9, 'spike', 'down'),
    (109, 10, 'block'),
    (109, 11, 'block'),
    (109, 12, 'block'),
    (109, 13, 'block'),
    (110, 0, 'block'),
    (110, 1, 'block'),
    (110, 2, 'block'),
    (110, 9, 'spike', 'down'),
    (110, 10, 'block'),
    (110, 11, 'block'),
    (110, 12, 'block'),
    (110, 13, 'block'),
    (111, 0, 'block'),
    (111, 1, 'block'),
    (111, 2, 'block'),
    (111, 8, 'spike', 'down'),
    (111, 9, 'block'),
    (111, 10, 'block'),
    (111, 11, 'block'),
    (111, 12, 'block'),
    (111, 13, 'block'),
    (112, 0, 'block'),
    (112, 1, 'block'),
    (112, 2, 'block'),
    (112, 4, 'spike', 'down'),
    (112, 5, 'block'),
    (112, 6, 'block'),
    (112, 7, 'block'),
    (112, 8, 'block'),
    (112, 9, 'block'),
    (112, 10, 'block'),
    (112, 11, 'block'),
    (112, 12, 'block'),
    (112, 13, 'block'),
    (113, 0, 'block'),
    (113, 1, 'block'),
    (113, 2, 'block'),
    (113, 8, 'spike', 'down'),
    (113, 9, 'block'),
    (113, 10, 'block'),
    (113, 11, 'block'),
    (113, 12, 'block'),
    (113, 13, 'block'),
    (114, 0, 'block'),
    (114, 1, 'block'),
    (114, 2, 'block'),
    (114, 9, 'spike', 'down'),
    (114, 10, 'block'),
    (114, 11, 'block'),
    (114, 12, 'block'),
    (114, 13, 'block'),
    (115, 0, 'block'),
    (115, 1, 'block'),
    (115, 2, 'block'),
    (115, 9, 'spike', 'down'),
    (115, 10, 'block'),
    (115, 11, 'block'),
    (115, 12, 'block'),
    (115, 13, 'block'),
    (116, 0, 'block'),
    (116, 1, 'block'),
    (116, 2, 'block'),
    (116, 9, 'spike', 'down'),
    (116, 10, 'block'),
    (116, 11, 'block'),
    (116, 12, 'block'),
    (116, 13, 'block'),
    (117, 0, 'block'),
    (117, 1, 'block'),
    (117, 8, 'spike', 'down'),
    (117, 9, 'block'),
    (117, 10, 'block'),
    (117, 11, 'block'),
    (117, 12, 'block'),
    (117, 13, 'block'),
    (118, 0, 'block'),
    (118, 1, 'block'),
    (118, 8, 'spike', 'down'),
    (118, 9, 'block'),
    (118, 10, 'block'),
    (118, 11, 'block'),
    (118, 12, 'block'),
    (118, 13, 'block'),
    (119, 0, 'block'),
    (119, 1, 'block'),
    (119, 8, 'spike', 'down'),
    (119, 9, 'block'),
    (119, 10, 'block'),
    (119, 11, 'block'),
    (119, 12, 'block'),
    (119, 13, 'block'),
    (120, 0, 'block'),
    (120, 1, 'block'),
    (120, 8, 'spike', 'down'),
    (120, 9, 'block'),
    (120, 10, 'block'),
    (120, 11, 'block'),
    (120, 12, 'block'),
    (120, 13, 'block'),
    (121, 0, 'block'),
    (121, 1, 'block'),
    (121, 8, 'spike', 'down'),
    (121, 9, 'block'),
    (121, 10, 'block'),
    (121, 11, 'block'),
    (121, 12, 'block'),
    (121, 13, 'block'),
    (122, 0, 'block'),
    (122, 7, 'spike', 'down'),
    (122, 8, 'block'),
    (122, 9, 'block'),
    (122, 10, 'block'),
    (122, 11, 'block'),
    (122, 12, 'block'),
    (122, 13, 'block'),
    (123, 0, 'block'),
    (123, 6, 'spike', 'down'),
    (123, 7, 'block'),
    (123, 8, 'block'),
    (123, 9, 'block'),
    (123, 10, 'block'),
    (123, 11, 'block'),
    (123, 12, 'block'),
    (123, 13, 'block'),
    (124, 0, 'block'),
    (124, 3, 'spike', 'down'),
    (124, 4, 'block'),
    (124, 5, 'block'),
    (124, 6, 'block'),
    (124, 7, 'block'),
    (124, 8, 'block'),
    (124, 9, 'block'),
    (124, 10, 'block'),
    (124, 11, 'block'),
    (124, 12, 'block'),
    (124, 13, 'block'),
    (125, 0, 'block'),
    (125, 7, 'spike', 'down'),
    (125, 8, 'block'),
    (125, 9, 'block'),
    (125, 10, 'block'),
    (125, 11, 'block'),
    (125, 12, 'block'),
    (125, 13, 'block'),
    (126, 0, 'spike', 'up'),
    (126, 8, 'spike', 'down'),
    (126, 9, 'block'),
    (126, 10, 'block'),
    (126, 11, 'block'),
    (126, 12, 'block'),
    (126, 13, 'block'),
    (127, 0, 'spike', 'up'),
    (127, 9, 'spike', 'down'),
    (127, 10, 'block'),
    (127, 11, 'block'),
    (127, 12, 'block'),
    (127, 13, 'block'),
    (128, 0, 'block'),
    (128, 7, 'spike', 'left'),
    (128, 10, 'spike', 'down'),
    (128, 11, 'block'),
    (128, 12, 'block'),
    (128, 13, 'block'),
    (129, 0, 'halfblock', 'up'),
    (129, 6, 'spike', 'down'),
    (129, 7, 'emptyblock'),
    (129, 8, 'spike', 'up'),
    (129, 11, 'spike', 'down'),
    (129, 12, 'block'),
    (129, 13, 'block'),
    (130, 0, 'block'),
    (130, 7, 'spike', 'right'),
    (130, 12, 'spike', 'down'),
    (130, 13, 'block'),
    (131, 0, 'spike', 'up'),
    (131, 13, 'spike', 'down'),
    (132, 0, 'spike', 'up'),
    (133, 0, 'block'),
    (133, 9, 'spike', 'left'),
    (134, 0, 'smallspike', 'up', 'down'),
    (134, 8, 'spike', 'down'),
    (134, 9, 'emptyblock'),
    (134, 10, 'spike', 'up'),
    (135, 0, 'smallspike', 'up', 'down'),
    (135, 9, 'spike', 'right'),
    (136, 0, 'block'),
    (136, 1, 'block'),
    (137, 0, 'smallspike', 'up', 'down'),
    (137, 7, 'spike', 'left'),
    (138, 0, 'smallspike', 'up', 'down'),
    (138, 6, 'spike', 'down'),
    (138, 7, 'emptyblock'),
    (138, 8, 'spike', 'up'),
    (139, 0, 'halfblock', 'up'),
    (139, 1, 'block'),
    (139, 2, 'block'),
    (139, 7, 'spike', 'right'),
    (140, 0, 'smallspike', 'up', 'down'),
    (141, 0, 'smallspike', 'up', 'down'),
    (141, 11, 'spike', 'left'),
    (142, 0, 'smallspike', 'up', 'down'),
    (142, 1, 'halfblock', 'up'),
    (142, 2, 'block'),
    (142, 3, 'block'),
    (142, 10, 'spike', 'down'),
    (142, 11, 'emptyblock'),
    (142, 12, 'spike', 'up'),
    (143, 0, 'smallspike', 'up', 'down'),
    (143, 11, 'spike', 'right'),
    (144, 0, 'smallspike', 'up', 'down'),
    (145, 3, 'halfblock', 'up'),
    (145, 4, 'block'),
    (145, 9, 'spike', 'left'),
    (146, 8, 'spike', 'down'),
    (146, 9, 'emptyblock'),
    (146, 10, 'spike', 'up'),
    (147, 5, 'halfblock', 'up'),
    (147, 6, 'block'),
    (147, 9, 'spike', 'right'),
    (148, 11, 'spike', 'left'),
    (149, 7, 'spike', 'left'),
    (149, 10, 'spike', 'down'),
    (149, 11, 'emptyblock'),
    (149, 12, 'spike', 'up'),
    (150, 4, 'block'),
    (150, 6, 'spike', 'down'),
    (150, 7, 'emptyblock'),
    (150, 8, 'spike', 'up'),
    (150, 11, 'spike', 'right'),
    (151, 2, 'block'),
    (151, 7, 'spike', 'right'),
    (152, 8, 'spike', 'left'),
    (153, 4, 'block'),
    (153, 7, 'spike', 'down'),
    (153, 8, 'emptyblock'),
    (153, 9, 'spike', 'up'),
    (153, 11, 'spike', 'left'),
    (154, 8, 'spike', 'right'),
    (154, 10, 'spike', 'down'),
    (154, 11, 'emptyblock'),
    (154, 12, 'spike', 'up'),
    (155, 5, 'block'),
    (155, 11, 'spike', 'right'),
    (156, 1, 'block'),
    (157, 3, 'block'),
    (157, 7, 'block'),
    (157, 10, 'block'),
    (159, 5, 'block'),
    (159, 10, 'block'),
    (160, 8, 'block'),
    (161, 12, 'block'),
    (162, 2, 'block'),
    (162, 5, 'block'),
    (162, 7, 'block'),
    (164, 4, 'block'),
    (164, 9, 'block'),
    (164, 11, 'block'),
    (166, 2, 'block'),
    (166, 5, 'block'),
    (166, 11, 'block'),
    (167, 8, 'block'),
    (168, 7, 'block'),
    (169, 3, 'block'),
    (169, 11, 'block'),
    (170, 7, 'block'),
    (171, 3, 'block'),
    (171, 5, 'block'),
    (171, 9, 'block'),
    (171, 12, 'block'),
    (172, 7, 'block'),
    (173, 1, 'block'),
    (173, 11, 'block'),
    (174, 4, 'block'),
    (174, 8, 'block'),
    (174, 10, 'block'),
    (175, 2, 'block'),
    (176, 7, 'block'),
    (176, 9, 'block'),
    (176, 11, 'block'),
]


def aabb(ax, ay, aw, ah, bx, by, bw, bh):
    return (ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by)


def _norm_dir(s: str) -> str:
    s = (s or "up").lower()
    if s not in ("up", "down", "left", "right"):
        return "up"
    return s


def _norm_half(s: str) -> str:
    s = (s or "down").lower()
    if s not in ("up", "down"):
        return "down"
    return s


def build_level(level_cells):
    objs = []
    max_x_cell = SPAWN_CELL[0]

    for item in level_cells:
        if len(item) < 3:
            raise ValueError(f"Bad LEVEL entry: {item}")

        xc, yc, kind = int(item[0]), int(item[1]), str(item[2]).lower()
        xw = xc * CELL
        yw = yc * CELL

        max_x_cell = max(max_x_cell, xc)

        if kind in ("block", "emptyblock"):
            objs.append({"kind": kind, "x": xw, "y": yw, "w": CELL, "h": CELL})

        elif kind == "halfblock":
            half = _norm_half(item[3] if len(item) >= 4 else "down")
            hh = CELL // 2
            hy = yw + (hh if half == "up" else 0)
            objs.append({"kind": "halfblock", "x": xw, "y": hy, "w": CELL, "h": hh, "half": half})

        elif kind == "spike":
            d = _norm_dir(item[3] if len(item) >= 4 else "up")
            objs.append({"kind": "spike", "x": xw, "y": yw, "w": CELL, "h": CELL, "dir": d})

        elif kind in ("smallspike", "smallship"):
            d = _norm_dir(item[3] if len(item) >= 4 else "up")
            half = _norm_half(item[4] if len(item) >= 5 else "down")
            hh = CELL // 2
            hy = yw + (hh if half == "up" else 0)
            objs.append({"kind": "smallspike", "x": xw, "y": hy, "w": CELL, "h": hh, "dir": d, "half": half})

        else:
            raise ValueError(f"Unknown kind: {kind} entry={item}")

    level_end = (max_x_cell + 12) * CELL
    objs.sort(key=lambda o: o["x"])
    return objs, level_end


def spike_hitbox_world(x, y, w, h, direction: str):
    d = _norm_dir(direction)
    inset_x = int(w * 0.18)
    inset_y = int(h * 0.10)
    if d in ("left", "right"):
        inset_y = int(h * 0.18)
    return (x + inset_x, y + inset_y, w - 2 * inset_x, h - 2 * inset_y)


def tri_points(x, y, w, h, direction: str):
    d = _norm_dir(direction)
    pad = 6
    if d == "up":
        return (x + pad, y), (x + w - pad, y), (x + w / 2, y + h - pad)
    if d == "down":
        return (x + pad, y + h), (x + w - pad, y + h), (x + w / 2, y + pad)
    if d == "left":
        return (x + w, y + pad), (x + w, y + h - pad), (x + pad, y + h / 2)
    return (x, y + pad), (x, y + h - pad), (x + w - pad, y + h / 2)


class UIButton:
    def __init__(self, x, y, w, h, text):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.text = text
        self.hover = False

    def contains(self, mx, my):
        return self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h

    def draw(self):
        bg = (38, 38, 38) if not self.hover else (55, 55, 55)
        arcade.draw_lbwh_rectangle_filled(self.x, self.y, self.w, self.h, bg)
        arcade.draw_lbwh_rectangle_outline(self.x, self.y, self.w, self.h, (235, 235, 235), border_width=2)
        arcade.draw_text(
            self.text,
            self.x + self.w / 2,
            self.y + self.h / 2,
            (240, 240, 240),
            18,
            anchor_x="center",
            anchor_y="center",
        )


class Game(arcade.Window):
    def __init__(self):
        super().__init__(W, H, "GD-like (Arcade 3.3.3) — Fixed Coords + AutoScale", resizable=True)
        arcade.set_background_color((10, 10, 10))

        self.level, self.level_end = build_level(LEVEL)
        self.best_percent = 0
        self.is_full = False
        self.btn_restart = None
        self.btn_exit = None
        self.view_scale = 1.0
        self.floor_screen_y = 0.0
        self.camera_x = 0.0

        self.reset()

    def recompute_view(self):
        w, h = self.get_size()
        self.view_scale = h / (VISIBLE_TOTAL_BLOCKS * CELL)
        self.floor_screen_y = VISIBLE_DOWN_BLOCKS * CELL * self.view_scale

    def world_to_screen(self, xw, yw):
        xs = (xw - self.camera_x) * self.view_scale
        ys = self.floor_screen_y + (yw * self.view_scale)
        return xs, ys

    def rect_world_to_screen(self, xw, yw, ww, hh):
        xs, ys = self.world_to_screen(xw, yw)
        return xs, ys, ww * self.view_scale, hh * self.view_scale

    def reset(self):
        sx, sy = SPAWN_CELL
        self.player_x = float(sx * CELL)
        self.player_y = float(sy * CELL)
        self.vy = 0.0
        self.on_ground = True
        self.dead = False
        self.win = False
        self.jump_held = False
        self.jump_buffer = False
        self.run_best_this_try = 0
        self.btn_restart = None
        self.btn_exit = None
        self.recompute_view()
        self.update_camera()

    def toggle_fullscreen(self):
        self.is_full = not self.is_full
        self.set_fullscreen(self.is_full)
        self.recompute_view()

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.recompute_view()

    def update_camera(self):
        w, _ = self.get_size()
        visible_w_world = w / self.view_scale
        self.camera_x = max(0.0, self.player_x - visible_w_world / 2)

    def do_jump(self):
        self.vy = JUMP_V
        self.on_ground = False
        self.jump_buffer = False

    def request_jump(self):
        if self.dead or self.win:
            return
        if self.on_ground:
            self.do_jump()
        else:
            self.jump_buffer = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F11:
            self.toggle_fullscreen()
            return

        if self.dead:
            if key == arcade.key.R:
                self.reset()
            return

        if key in (arcade.key.SPACE, arcade.key.UP, arcade.key.W):
            self.jump_held = True
            self.request_jump()
            return

        if key == arcade.key.R:
            self.reset()

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.SPACE, arcade.key.UP, arcade.key.W):
            self.jump_held = False
            self.jump_buffer = False

    def on_mouse_motion(self, x, y, dx, dy):
        if self.dead and self.btn_restart and self.btn_exit:
            self.btn_restart.hover = self.btn_restart.contains(x, y)
            self.btn_exit.hover = self.btn_exit.contains(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.dead and self.btn_restart and self.btn_exit:
            if self.btn_restart.contains(x, y):
                self.reset()
            elif self.btn_exit.contains(x, y):
                self.close()
            return

        self.request_jump()

    def progress_percent(self):
        p = int((self.player_x / max(1, self.level_end)) * 100)
        return max(0, min(100, p))

    def iter_solids_world(self):
        for o in self.level:
            if o["kind"] in ("block", "emptyblock", "halfblock"):
                yield o["x"], o["y"], o["w"], o["h"]

    def resolve_floor_and_platforms(self, prev_y):
        landed = False

        if self.player_y <= 0.0:
            self.player_y = 0.0
            if self.vy < 0:
                self.vy = 0.0
            if not self.on_ground:
                landed = True
            self.on_ground = True

        if self.vy <= 0:
            px, py = self.player_x, self.player_y
            pw, ph = PLAYER_W, PLAYER_H
            best_top = None

            for bx, by, bw, bh in self.iter_solids_world():
                top = by + bh
                horizontal = (px + pw > bx) and (px < bx + bw)
                crossed_top = (prev_y >= top) and (py <= top)

                if horizontal and crossed_top:
                    if best_top is None or top > best_top:
                        best_top = top

            if best_top is not None:
                self.player_y = best_top
                if self.vy < 0:
                    self.vy = 0.0
                if not self.on_ground:
                    landed = True
                self.on_ground = True

        return landed

    def check_spike_death_world(self):
        px, py, pw, ph = self.player_x, self.player_y, PLAYER_W, PLAYER_H
        for o in self.level:
            if o["kind"] not in ("spike", "smallspike"):
                continue
            hx, hy, hw, hh = spike_hitbox_world(o["x"], o["y"], o["w"], o["h"], o.get("dir", "up"))
            if aabb(px, py, pw, ph, hx, hy, hw, hh):
                return True
        return False

    def check_left_wall_death_world(self):
        px, py = self.player_x, self.player_y
        pw, ph = PLAYER_W, PLAYER_H
        pr = px + pw

        for bx, by, bw, bh in self.iter_solids_world():
            if (py + ph) <= by or py >= (by + bh):
                continue

            tol = 2.0
            if (pr > bx + tol) and (px < bx):
                if py < (by + bh - 6):
                    return True
        return False

    def ensure_death_menu(self):
        if self.btn_restart and self.btn_exit:
            return
        w, h = self.get_size()
        bw, bh = 220, 54
        gap = 16
        cx, cy = w / 2, h / 2

        self.btn_restart = UIButton(cx - bw - gap / 2, cy - bh / 2 - 10, bw, bh, "Restart")
        self.btn_exit = UIButton(cx + gap / 2, cy - bh / 2 - 10, bw, bh, "Exit")

    def on_update(self, dt):
        if self.dead or self.win:
            return

        self.player_x += SCROLL_SPEED * dt

        prev_y = self.player_y
        self.vy -= GRAVITY * dt
        self.player_y += self.vy * dt

        landed = self.resolve_floor_and_platforms(prev_y)

        if landed and (self.jump_held or self.jump_buffer):
            self.do_jump()

        self.update_camera()

        p = self.progress_percent()
        self.run_best_this_try = max(self.run_best_this_try, p)
        self.best_percent = max(self.best_percent, self.run_best_this_try)

        if self.check_spike_death_world() or self.check_left_wall_death_world():
            self.dead = True
            self.ensure_death_menu()
            return

        if self.player_x >= self.level_end:
            self.win = True
            self.best_percent = max(self.best_percent, 100)

    def draw_floor(self):
        w, _ = self.get_size()
        arcade.draw_lrbt_rectangle_filled(0, w, 0, self.floor_screen_y, (18, 18, 18))
        arcade.draw_lrbt_rectangle_filled(0, w, self.floor_screen_y, self.floor_screen_y + 4, (28, 28, 28))

    def draw_level(self):
        for o in self.level:
            xs, ys, ws, hs = self.rect_world_to_screen(o["x"], o["y"], o["w"], o["h"])
            w_scr, _ = self.get_size()
            if xs < -400 or xs > w_scr + 400:
                continue

            kind = o["kind"]
            if kind == "block":
                arcade.draw_lbwh_rectangle_filled(xs, ys, ws, hs, (60, 60, 60))
                arcade.draw_lbwh_rectangle_outline(xs, ys, ws, hs, (150, 150, 150), border_width=2)

            elif kind == "emptyblock":
                arcade.draw_lbwh_rectangle_outline(xs, ys, ws, hs, (230, 230, 230), border_width=2)
                arcade.draw_lbwh_rectangle_outline(xs + 4, ys + 4, ws - 8, hs - 8, (120, 120, 120), border_width=1)

            elif kind == "halfblock":
                arcade.draw_lbwh_rectangle_filled(xs, ys, ws, hs, (60, 60, 60))
                arcade.draw_lbwh_rectangle_outline(xs, ys, ws, hs, (150, 150, 150), border_width=2)

            elif kind in ("spike", "smallspike"):
                p1, p2, p3 = tri_points(xs, ys, ws, hs, o.get("dir", "up"))
                arcade.draw_triangle_filled(*p1, *p2, *p3, (230, 230, 230))

    def draw_player(self):
        xs, ys = self.world_to_screen(self.player_x, self.player_y)
        arcade.draw_lbwh_rectangle_filled(
            xs,
            ys,
            PLAYER_W * self.view_scale,
            PLAYER_H * self.view_scale,
            (220, 220, 220) if not self.dead else (255, 80, 80),
        )

    def draw_progress_bar(self):
        w, h = self.get_size()
        p = self.progress_percent()

        bar_margin = 22
        bar_h = 16
        bar_y = h - 26
        bar_x = bar_margin
        bar_w = w - bar_margin * 2 - 90

        arcade.draw_lbwh_rectangle_filled(bar_x, bar_y, bar_w, bar_h, (40, 40, 40))
        arcade.draw_lbwh_rectangle_filled(bar_x + 2, bar_y + 2, bar_w - 4, bar_h - 4, (18, 18, 18))

        fill_w = int((bar_w - 6) * (p / 100.0))
        if fill_w > 0:
            arcade.draw_lbwh_rectangle_filled(bar_x + 3, bar_y + 3, fill_w, bar_h - 6, (90, 255, 120))

        arcade.draw_lbwh_rectangle_outline(bar_x, bar_y, bar_w, bar_h, (240, 240, 240), border_width=2)

        arcade.draw_text(f"{p:>3d}%", bar_x + bar_w + 14, bar_y - 2, (240, 240, 240), 18)
        arcade.draw_text(f"Best: {self.best_percent}%", 18, h - 52, (220, 220, 220), 14)

    def draw_death_overlay(self):
        self.ensure_death_menu()
        w, h = self.get_size()

        arcade.draw_lbwh_rectangle_filled(0, 0, w, h, (0, 0, 0, 160))
        arcade.draw_text("You lost", w / 2, h / 2 + 70, (255, 90, 90), 34, anchor_x="center")

        self.btn_restart.draw()
        self.btn_exit.draw()

    def on_draw(self):
        self.clear()
        self.draw_floor()
        self.draw_level()
        self.draw_player()
        self.draw_progress_bar()

        if self.dead:
            self.draw_death_overlay()


def main():
    Game()
    arcade.run()


if __name__ == "__main__":
    main()