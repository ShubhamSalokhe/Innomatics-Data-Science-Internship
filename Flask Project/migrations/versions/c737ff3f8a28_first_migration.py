"""First Migration

Revision ID: c737ff3f8a28
Revises: 
Create Date: 2021-10-31 11:35:44.087703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c737ff3f8a28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long', sa.String(), nullable=True),
    sa.Column('short', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urls')
    # ### end Alembic commands ###
