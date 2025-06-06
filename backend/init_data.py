import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session, init_db
from models import Product

async def init_sample_data():
    """Initialize the database with sample data"""
    # Create tables
    await init_db()
    
    # Sample products
    products = [
        Product(
            name="Gaming Mouse",
            description="High-precision gaming mouse with RGB lighting",
            price=2999.0,
            image_url="https://via.placeholder.com/200",
            stock=50
        ),
        Product(
            name="Mechanical Keyboard",
            description="RGB mechanical keyboard with blue switches",
            price=4999.0,
            image_url="https://via.placeholder.com/200",
            stock=30
        ),
        Product(
            name="Gaming Headset",
            description="7.1 surround sound gaming headset",
            price=3499.0,
            image_url="https://via.placeholder.com/200",
            stock=40
        ),
        Product(
            name="Mouse Pad",
            description="Large gaming mouse pad with RGB edges",
            price=1499.0,
            image_url="https://via.placeholder.com/200",
            stock=100
        )
    ]
    
    async with async_session() as session:
        async with session.begin():
            # Add products
            for product in products:
                session.add(product)
        
        await session.commit()

if __name__ == "__main__":
    asyncio.run(init_sample_data()) 
 