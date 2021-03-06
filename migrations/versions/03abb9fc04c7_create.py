"""create

Revision ID: 03abb9fc04c7
Revises: 
Create Date: 2020-06-09 13:48:02.202624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03abb9fc04c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('creation_date', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('secondname', sa.String(length=200), nullable=True),
    sa.Column('updated_on', sa.Integer(), nullable=True),
    sa.Column('is_cooker', sa.Boolean(), nullable=True),
    sa.Column('biography', sa.String(length=20000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.Column('creation_date', sa.Integer(), nullable=True),
    sa.Column('deadline', sa.Float(), nullable=True),
    sa.Column('updated_on', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('user')
    # ### end Alembic commands ###
