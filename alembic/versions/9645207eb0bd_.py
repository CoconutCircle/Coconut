"""empty message

Revision ID: 9645207eb0bd
Revises: 0261f902d4b2
Create Date: 2025-03-13 16:22:27.808389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9645207eb0bd'
down_revision: Union[str, None] = '0261f902d4b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
