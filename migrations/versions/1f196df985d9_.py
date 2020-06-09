"""empty message

Revision ID: 1f196df985d9
Revises: 03abb9fc04c7
Create Date: 2020-06-09 19:59:24.710642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f196df985d9'
down_revision = '03abb9fc04c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('title', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'title')
    # ### end Alembic commands ###