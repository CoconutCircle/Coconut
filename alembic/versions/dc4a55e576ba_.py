"""empty message

Revision ID: dc4a55e576ba
Revises: e224589e2b4b
Create Date: 2025-03-13 16:57:42.439787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc4a55e576ba'
down_revision: Union[str, None] = 'e224589e2b4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
