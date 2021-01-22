"""update calendarevent fields

Revision ID: 7b2af1ac9344
Revises: 89d2904673b8
Create Date: 2021-01-22 22:45:19.043138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b2af1ac9344'
down_revision = '89d2904673b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendarEvent', sa.Column('announcer', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'calendarEvent', 'clubMember', ['announcer'], ['id'])
    op.add_column('clubRole', sa.Column('canDecideAds', sa.Boolean(), nullable=True))
    op.add_column('clubRole', sa.Column('canManageFunds', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clubRole', 'canManageFunds')
    op.drop_column('clubRole', 'canDecideAds')
    op.drop_constraint(None, 'calendarEvent', type_='foreignkey')
    op.drop_column('calendarEvent', 'announcer')
    # ### end Alembic commands ###
