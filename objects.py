from enum import Enum


class ObjectType(Enum):
    STONE_0 = 0
    TREE_0 = 1
    
    
class Object:
    def __init__(self, obj_type, x, y):
        self.obj_type = obj_type
        self.x = x
        self.y = y
        
        
OBJECT_SIZES = {
    ObjectType.STONE_0: (32, 31),
    ObjectType.TREE_0: (50, 68),
}
