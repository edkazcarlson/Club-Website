"""postgis

Revision ID: 464b718613bc
Revises: e3af73f664c5
Create Date: 2021-01-25 21:00:47.914130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from geoalchemy2.types import Geography

# revision identifiers, used by Alembic.
revision = '464b718613bc'
down_revision = 'e3af73f664c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendarEvent', sa.Column('location', Geography(geometry_type='POINT', srid=4326, from_text='ST_GeogFromText', name='geography'), nullable=True))
    op.add_column('club', sa.Column('clubLocation', Geography(geometry_type='POINT', srid=4326, from_text='ST_GeogFromText', name='geography'), nullable=True))
    op.drop_column('club', 'clubLong')
    op.drop_column('club', 'clubLat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('club', sa.Column('clubLat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('club', sa.Column('clubLong', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('club', 'clubLocation')
    op.drop_column('calendarEvent', 'location')
    # ### end Alembic commands ###