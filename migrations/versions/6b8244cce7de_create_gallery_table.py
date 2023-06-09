from alembic import op
import sqlalchemy as sa



"""create_gallery\table

Revision ID: 6b8244cce7de
Revises: ab5e73dc839f
Create Date: 2023-04-12 09:37:13.791426

"""

# revision identifiers, used by Alembic.
revision = '6b8244cce7de'
down_revision = 'ab5e73dc839f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('galleries',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album', sa.String(length=55), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('galleries')
    # ### end Alembic commands ###
