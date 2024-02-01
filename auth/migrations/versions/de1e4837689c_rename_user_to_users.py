"""Rename user to users

Revision ID: de1e4837689c
Revises: eee0acce8b34
Create Date: 2024-01-04 23:17:00.458779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'de1e4837689c'
down_revision = 'eee0acce8b34'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
   pass
    # ### end Alembic commands ###
