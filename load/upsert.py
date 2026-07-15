from sqlalchemy.dialects.postgresql import insert
from load.models import PaymentRecord
from load.database import engine


def upsert_data(df):
    """
    Insert new records into PostgreSQL.
    If a record with the same id already exists,
    update the amount and status instead of creating duplicates.
    """

    # Convert Polars DataFrame to list of dictionaries
    stmt = insert(PaymentRecord).values(df.to_dicts())

    # PostgreSQL UPSERT using ON CONFLICT
    on_conflict_stmt = stmt.on_conflict_do_update(
        index_elements=["id"],
        set_={
            "amount": stmt.excluded.amount,
            "status": stmt.excluded.status,
        },
    )

    with engine.connect() as conn:
        conn.execute(on_conflict_stmt)
        conn.commit()