from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base

# SQLite database URL
DATABASE_URL = "sqlite+aiosqlite:///./store.db"

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
)

# Create async session factory
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db():
    """Initialize the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    """Get a database session"""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

# Database dependency
async def get_db():
    """Database dependency for FastAPI"""
    session = async_session()
    try:
        yield session
    finally:
        await session.close() 