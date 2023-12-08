"""Changed atrribute name for models (preview_photo -> preview_photo_id)

Revision ID: 3de493b66730
Revises: 96707e2c88b3
Create Date: 2023-12-08 19:05:48.075801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3de493b66730'
down_revision: Union[str, None] = '96707e2c88b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('news') as batch_op:
        batch_op.alter_column(column_name='preview_photo', new_column_name='preview_photo_id')
    with op.batch_alter_table('painting') as batch_op:
        batch_op.alter_column(column_name='preview_photo', new_column_name='preview_photo_id')
    with op.batch_alter_table('project') as batch_op:
        batch_op.alter_column(column_name='preview_photo', new_column_name='preview_photo_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    with op.batch_alter_table('news') as batch_op:
        batch_op.alter_column(column_name='preview_photo_id', new_column_name='preview_photo')
    with op.batch_alter_table('painting') as batch_op:
        batch_op.alter_column(column_name='preview_photo_id', new_column_name='preview_photo')
    with op.batch_alter_table('project') as batch_op:
        batch_op.alter_column(column_name='preview_photo_id', new_column_name='preview_photo')
    # ### end Alembic commands ###
