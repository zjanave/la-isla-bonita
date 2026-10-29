import pygame
from tiles import TileType
from objects import ObjectType, Object
from textures import TextureManager


class World:
    def __init__(self, tile_size):        
        self.tile_size = tile_size
        # the numbers correspond to TileType values
        self.tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 0],
            [0, 0, 3, 1, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 0, 0],
            [0, 0, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 6, 6, 6, 6, 6, 6, 1, 1, 4, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0],
            [0, 0, 2, 1, 4, 0, 0, 2, 1, 1, 1, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        self.objects = [
            Object(ObjectType.STONE_0, 320, 280),
            Object(ObjectType.STONE_0, 270, 270),
            Object(ObjectType.TREE_0, 250, 100),
            Object(ObjectType.TREE_0, 290, 170),
            Object(ObjectType.TREE_0, 180, 140),
        ]
        
        self.texture_manager = TextureManager(self.tile_size)
        
        
    def draw(self, screen):
        row_cnt = len(self.tile_map)
        col_cnt = len(self.tile_map[0])
        for row_idx in range(row_cnt):
            for col_idx in range(col_cnt):
                tile_x = col_idx * self.tile_size
                tile_y = row_idx * self.tile_size
                tile_type = self.tile_map[row_idx][col_idx]
                tile_texture = self.texture_manager.get_tile_texture(tile_type)
                screen.blit(tile_texture, (tile_x, tile_y))
        for obj in self.objects:
            texture = self.texture_manager.get_object_texture(obj.obj_type)
            screen.blit(texture, (obj.x, obj.y))
