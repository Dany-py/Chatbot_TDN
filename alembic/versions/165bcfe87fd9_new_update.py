"""new update

Revision ID: 165bcfe87fd9
Revises: dde93c1a0b20
Create Date: 2025-08-28 12:31:46.615549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '165bcfe87fd9'
down_revision: Union[str, None] = 'dde93c1a0b20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
