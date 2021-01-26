"""more calendar columns

Revision ID: e3af73f664c5
Revises: 7b2af1ac9344
Create Date: 2021-01-25 20:35:36.155513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3af73f664c5'
down_revision = '7b2af1ac9344'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendarEvent', sa.Column('isAllDay', sa.Boolean(), nullable=True))
    op.add_column('calendarEvent', sa.Column('isNegativeEvent', sa.Boolean(), nullable=True))
    op.add_column('calendarEvent', sa.Column('recurring', sa.String(), nullable=True))
    op.add_column('club', sa.Column('clubColor', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('club', 'clubColor')
    op.drop_column('calendarEvent', 'recurring')
    op.drop_column('calendarEvent', 'isNegativeEvent')
    op.drop_column('calendarEvent', 'isAllDay')
    # ### end Alembic commands ###