# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.club import Club, ClubMember, ClubRole
from app.models.calendarEvent import CalendarEvent
from app.models.forum import ForumChannel, ForumFolder, ForumPost
# from app.models.demo import Parent, Child, AssocTable