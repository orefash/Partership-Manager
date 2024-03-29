"""empty message

Revision ID: 019e6ff75462
Revises: 2d9d2d692093
Create Date: 2019-05-08 20:41:52.096000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019e6ff75462'
down_revision = '2d9d2d692093'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('group_id', sa.Integer(), nullable=True))
    op.add_column('members', sa.Column('pcf_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'members', 'pcfs', ['pcf_id'], ['id'])
    op.create_foreign_key(None, 'members', 'groups', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'members', type_='foreignkey')
    op.drop_constraint(None, 'members', type_='foreignkey')
    op.drop_column('members', 'pcf_id')
    op.drop_column('members', 'group_id')
    # ### end Alembic commands ###
