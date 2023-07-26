"""'Init'

Revision ID: f002ca8ee05b
Revises: 2a608153ad70
Create Date: 2023-07-26 20:52:04.020299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f002ca8ee05b'
down_revision = '2a608153ad70'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token_black_list', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column('token_black_list', 'token_type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token_black_list', sa.Column('token_type', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('token_black_list', 'created_at')
    # ### end Alembic commands ###
