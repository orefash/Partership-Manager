"""empty message

Revision ID: 2d9d2d692093
Revises: 298e2badbdea
Create Date: 2019-04-23 12:14:17.392000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d9d2d692093'
down_revision = '298e2badbdea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('partner_givings', 'arm_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('partner_givings', 'member_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('partner_givings', 'staff_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('partner_givings', 'staff_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('partner_givings', 'member_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('partner_givings', 'arm_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
