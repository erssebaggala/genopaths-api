"""empty message

Revision ID: e36adc79c024
Revises: 4d66979c0b70
Create Date: 2023-08-21 01:36:50.283682

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e36adc79c024'
down_revision = '4d66979c0b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
#     with op.batch_alter_table('projects', schema=None) as batch_op:
#         batch_op.alter_column('created_at',
#                existing_type=postgresql.TIMESTAMP(),
#                nullable=False,
#                existing_server_default=sa.text('now()'))
#         batch_op.alter_column('updated_at',
#                existing_type=postgresql.TIMESTAMP(),
#                nullable=False,
#                existing_server_default=sa.text('now()'))
#         batch_op.create_unique_constraint(None, ['name'])

#     with op.batch_alter_table('users', schema=None) as batch_op:
#         batch_op.alter_column('role',
#                existing_type=postgresql.ENUM('admin', 'user', name='roletype'),
#                type_=sa.String(length=20),
#                existing_nullable=True)
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
#     with op.batch_alter_table('users', schema=None) as batch_op:
#         batch_op.alter_column('role',
#                existing_type=sa.String(length=20),
#                type_=postgresql.ENUM('admin', 'user', name='roletype'),
#                existing_nullable=True)

#     with op.batch_alter_table('projects', schema=None) as batch_op:
#         batch_op.drop_constraint(None, type_='unique')
#         batch_op.alter_column('updated_at',
#                existing_type=postgresql.TIMESTAMP(),
#                nullable=True,
#                existing_server_default=sa.text('now()'))
#         batch_op.alter_column('created_at',
#                existing_type=postgresql.TIMESTAMP(),
#                nullable=True,
#                existing_server_default=sa.text('now()'))
    pass

    # ### end Alembic commands ###