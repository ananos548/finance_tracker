"""Initial for tracker

Revision ID: 4feab62e1d07
Revises: 
Create Date: 2023-12-26 19:14:37.865985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4feab62e1d07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earnings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expense')
    op.drop_table('earnings')
    # ### end Alembic commands ###
