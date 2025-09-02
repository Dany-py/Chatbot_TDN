"""new update

Revision ID: cc7f67fa97c4
Revises: 165bcfe87fd9
Create Date: 2025-08-28 12:31:55.011236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc7f67fa97c4'
down_revision: Union[str, None] = '165bcfe87fd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
