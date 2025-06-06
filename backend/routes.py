from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Product, Order, User
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    image_url: str | None
    stock: int

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    status: str
    total: float
    created_at: datetime
    products: List[ProductResponse]

    class Config:
        from_attributes = True

@router.get("/products", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    """Get all available products"""
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products

@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific product by ID"""
    result = await db.execute(select(Product).filter(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/users/{telegram_id}/orders", response_model=List[OrderResponse])
async def get_user_orders(telegram_id: int, db: AsyncSession = Depends(get_db)):
    """Get all orders for a specific user"""
    # First get the user
    result = await db.execute(select(User).filter(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Then get their orders
    result = await db.execute(
        select(Order)
        .filter(Order.user_id == user.id)
        .order_by(Order.created_at.desc())
    )
    orders = result.scalars().all()
    return orders

class OrderCreate(BaseModel):
    telegram_id: int
    product_ids: List[int]

@router.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    """Create a new order"""
    # Get user or create if doesn't exist
    result = await db.execute(select(User).filter(User.telegram_id == order.telegram_id))
    user = result.scalar_one_or_none()
    if not user:
        user = User(telegram_id=order.telegram_id)
        db.add(user)
        await db.commit()
    
    # Get products
    result = await db.execute(
        select(Product).filter(Product.id.in_(order.product_ids))
    )
    products = result.scalars().all()
    
    if len(products) != len(order.product_ids):
        raise HTTPException(status_code=400, detail="Some products not found")
    
    # Calculate total
    total = sum(product.price for product in products)
    
    # Create order
    new_order = Order(
        user_id=user.id,
        total=total,
        products=products
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    
    return new_order 