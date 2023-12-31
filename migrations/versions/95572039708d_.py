"""empty message

Revision ID: 95572039708d
Revises: 
Create Date: 2023-12-29 11:47:40.585655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95572039708d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('all_products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uniq_id', sa.String(), nullable=True),
    sa.Column('crawl_timestamp', sa.DateTime(), nullable=True),
    sa.Column('product_url', sa.String(), nullable=True),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('product_category_tree', sa.String(), nullable=True),
    sa.Column('pid', sa.String(), nullable=True),
    sa.Column('retail_price', sa.String(), nullable=True),
    sa.Column('discounted_price', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('is_FK_Advantage_product', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('product_rating', sa.String(), nullable=True),
    sa.Column('overall_rating', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('product_specifications', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('regular_fit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fabric', sa.String(), nullable=True),
    sa.Column('idealfor', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relaxed_fit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fabric', sa.String(), nullable=True),
    sa.Column('idealfor', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relaxed_fit')
    op.drop_table('regular_fit')
    op.drop_table('all_products')
    # ### end Alembic commands ###
