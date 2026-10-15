import pygame
from tiles import TileType
from objects import ObjectType, OBJECT_SIZES


class TextureManager:
    def __init__(self, tile_size):
        self.tile_textures = {
            TileType.WATER: self._load_texture("assets/tiles/water.png", (tile_size, tile_size), False, False),
            TileType.SAND: self._load_texture("assets/tiles/sand.png", (tile_size, tile_size), False, False),
            TileType.WATER_SAND_1: self._load_texture("assets/tiles/water_sand.png", (tile_size, tile_size), False, False),
            TileType.WATER_SAND_2: self._load_texture("assets/tiles/water_sand.png", (tile_size, tile_size), False, True),
            TileType.WATER_SAND_3: self._load_texture("assets/tiles/water_sand.png", (tile_size, tile_size), True, False),
            TileType.WATER_SAND_4: self._load_texture("assets/tiles/water_sand.png", (tile_size, tile_size), True, True),
            TileType.GRASS: self._load_texture("assets/tiles/grass.png", (tile_size, tile_size), False, False),
        }
        
        self.object_textures = {
            ObjectType.STONE_0: self._load_texture("assets/objects/stone_0.png", OBJECT_SIZES[ObjectType.STONE_0], False, False),
            ObjectType.TREE_0: self._load_texture("assets/objects/tree_0.png", OBJECT_SIZES[ObjectType.TREE_0], False, False),
        }
        
    def get_tile_texture(self, tile_type):
        return self.tile_textures.get(tile_type)
    
    def get_object_texture(self, object_type):
        return self.object_textures.get(object_type)
    
    def _load_texture(self, path, size, mirror_horizontal, mirror_vertical):
        texture = pygame.image.load(path).convert_alpha()
        texture = pygame.transform.scale(texture, size)
        texture = pygame.transform.flip(texture, mirror_horizontal, mirror_vertical)
        return texture
    