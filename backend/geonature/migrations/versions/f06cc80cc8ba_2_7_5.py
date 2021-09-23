"""geonature schemas 2.7.5

Revision ID: f06cc80cc8ba
Create Date: 2021-08-10 14:23:55.144250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06cc80cc8ba'
down_revision = None
branch_labels = ('geonature',)
depends_on = (
    'fa35dfe5ff27',  # utilisateurs schema 1.4.7
    '9c2c0254aadc',  # taxonomie schema 1.8.1
)


def upgrade():
    raise Exception("""
    You should manually migrate your database to 2.7.5 version of geonature schemas, then stamp your database version to this revision:
        geonature db stamp f06cc80cc8ba
    """)


def downgrade():
    raise Exception("""
    This revision do not support downgrade (yet).
    """)