"""Add users

Revision ID: 99ad885faa01
Revises: f42af3d26f79
Create Date: 2024-01-04 23:32:41.447136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ad885faa01'
down_revision = 'f42af3d26f79'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
