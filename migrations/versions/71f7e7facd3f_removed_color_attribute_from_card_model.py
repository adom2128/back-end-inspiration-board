"""removed color attribute from Card model

Revision ID: 71f7e7facd3f
Revises: 7c8c75d32cde
Create Date: 2023-06-27 11:33:25.365694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71f7e7facd3f'
down_revision = '7c8c75d32cde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'color')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('color', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
