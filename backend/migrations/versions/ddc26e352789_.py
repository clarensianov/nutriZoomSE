"""empty message

Revision ID: ddc26e352789
Revises: bb1271cbc08b
Create Date: 2024-02-21 17:33:50.998481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddc26e352789'
down_revision = 'bb1271cbc08b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
