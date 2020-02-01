"""empty message

Revision ID: 77807a09c60c
Revises: 
Create Date: 2020-02-01 13:57:07.321001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77807a09c60c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('res_h', sa.Integer(), nullable=True),
    sa.Column('res_w', sa.Integer(), nullable=True),
    sa.Column('form', sa.String(length=10), nullable=True),
    sa.Column('date_orig', sa.String(length=50), nullable=True),
    sa.Column('user_orig', sa.String(length=50), nullable=True),
    sa.Column('date_dupl', sa.String(length=300), nullable=True),
    sa.Column('user_dupl', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('file_contents')
    # ### end Alembic commands ###