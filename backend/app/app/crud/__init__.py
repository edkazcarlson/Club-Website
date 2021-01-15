from .crud_user import user
from .crud_club import club
from .crud_clubRole import clubRole
from .crud_clubMember import clubMember

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
