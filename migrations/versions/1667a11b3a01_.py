"""empty message

Revision ID: 1667a11b3a01
Revises: None
Create Date: 2015-12-09 14:42:40.773000

"""

# revision identifiers, used by Alembic.
revision = '1667a11b3a01'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'subscribers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('subscribed', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribers')
    ### end Alembic commands ###
