"""empty message

Revision ID: e224589e2b4b
Revises: 9645207eb0bd
Create Date: 2025-03-13 16:23:51.193584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e224589e2b4b'
down_revision: Union[str, None] = '9645207eb0bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
