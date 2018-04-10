"""empty message

Revision ID: 643a83eaa72f
Revises: 
Create Date: 2018-04-10 09:40:16.474977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '643a83eaa72f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###