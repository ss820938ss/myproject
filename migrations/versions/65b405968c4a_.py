"""empty message

Revision ID: 65b405968c4a
Revises: 5c2a388aaa38
Create Date: 2021-08-18 12:42:21.312806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b405968c4a'
down_revision = '5c2a388aaa38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
