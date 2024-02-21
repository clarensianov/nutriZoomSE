"""empty message

Revision ID: 861dd4b63f64
<<<<<<< HEAD
Revises: 
Create Date: 2024-02-20 00:32:01.260240
=======
Revises: ba332370e130
Create Date: 2024-02-20 14:55:07.108349
>>>>>>> 18c823be95a1b21b9a497d633965efc467ab4a77

"""
from alembic import op
import sqlalchemy as sa
<<<<<<< HEAD
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '861dd4b63f64'
down_revision = None
=======


# revision identifiers, used by Alembic.
revision = '861dd4b63f64'
down_revision = 'ba332370e130'
>>>>>>> 18c823be95a1b21b9a497d633965efc467ab4a77
branch_labels = None
depends_on = None


def upgrade():
<<<<<<< HEAD
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipedetails', schema=None) as batch_op:
        batch_op.alter_column('recipe_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.alter_column('ingredients_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.drop_constraint('recipedetails_ibfk_1', type_='foreignkey')
        batch_op.drop_constraint('recipedetails_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'recipes', ['recipe_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'ingredients', ['ingredients_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('id')

    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_column('favorite_count')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))

    with op.batch_alter_table('recipedetails', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('recipedetails_ibfk_2', 'recipes', ['recipe_id'], ['id'])
        batch_op.create_foreign_key('recipedetails_ibfk_1', 'ingredients', ['ingredients_id'], ['id'])
        batch_op.alter_column('ingredients_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
        batch_op.alter_column('recipe_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###
=======
    pass


def downgrade():
    pass
>>>>>>> 18c823be95a1b21b9a497d633965efc467ab4a77