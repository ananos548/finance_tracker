"""Rename expense and category

Revision ID: 07bb274108b1
Revises: b24d2451ddc6
Create Date: 2024-01-04 23:17:34.960210

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '07bb274108b1'
down_revision = 'b24d2451ddc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass