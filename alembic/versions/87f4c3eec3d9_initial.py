"""initial

Revision ID: 87f4c3eec3d9
Revises: da7151073cf0
Create Date: 2023-11-24 14:58:03.328238

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87f4c3eec3d9'
down_revision: Union[str, None] = 'da7151073cf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('contacts', sa.Column('comments', sa.Text(), nullable=True))
    op.add_column('contacts', sa.Column('favorite', sa.Boolean(), nullable=True))
    op.drop_column('contacts', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('contacts', 'favorite')
    op.drop_column('contacts', 'comments')
    op.drop_column('contacts', 'phone')
    # ### end Alembic commands ###
