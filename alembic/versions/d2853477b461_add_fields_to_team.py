"""Add fields to Team

Revision ID: d2853477b461
Revises: a23d4d63432d
Create Date: 2017-01-04 17:23:20.326509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2853477b461'
down_revision = 'a23d4d63432d'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teams', sa.Column('created_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('teams', sa.Column('description', sa.String(), nullable=True))
    op.add_column('teams', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.add_column('teams', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    op.create_foreign_key(None, 'teams', 'users', ['owner_id'], ['id'])
    op.add_column('users_teams', sa.Column('created_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('users_teams', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('users_teams', sa.Column('team_ud', sa.Integer(), nullable=True))
    op.add_column('users_teams', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    op.drop_constraint('users_teams_team_id_fkey', 'users_teams', type_='foreignkey')
    op.create_foreign_key(None, 'users_teams', 'teams', ['team_ud'], ['id'])
    op.drop_column('users_teams', 'team_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_teams', sa.Column('team_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users_teams', type_='foreignkey')
    op.create_foreign_key('users_teams_team_id_fkey', 'users_teams', 'teams', ['team_id'], ['id'])
    op.drop_column('users_teams', 'updated_at')
    op.drop_column('users_teams', 'team_ud')
    op.drop_column('users_teams', 'id')
    op.drop_column('users_teams', 'created_at')
    op.drop_constraint(None, 'teams', type_='foreignkey')
    op.drop_column('teams', 'updated_at')
    op.drop_column('teams', 'owner_id')
    op.drop_column('teams', 'description')
    op.drop_column('teams', 'created_at')
    ### end Alembic commands ###
