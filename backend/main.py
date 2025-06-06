from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command
from config import settings
from database import init_db
from routes import router as api_router

# Initialize FastAPI app
app = FastAPI(title="Telegram Store API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize bot and dispatcher
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

# Serve static files (React build)
app.mount("/static", StaticFiles(directory="../frontend/dist"), name="static")

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

# Bot command handlers
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Handle /start command"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(
                text="Open Store",
                web_app=WebAppInfo(url=settings.FRONTEND_URL)
            )
        ]],
        resize_keyboard=True
    )
    await message.answer(
        "Welcome to our store! Click the button below to start shopping:",
        reply_markup=keyboard
    )

# API endpoints
@app.get("/api/products")
async def get_products():
    """Get all products"""
    # TODO: Implement database integration
    return [
        {
            "id": 1,
            "name": "Product 1",
            "price": 1999,
            "image": "https://via.placeholder.com/200",
            "description": "Sample product description"
        }
    ]

@app.get("/api/orders/{user_id}")
async def get_user_orders(user_id: int):
    """Get orders for a specific user"""
    # TODO: Implement database integration
    return [
        {
            "id": 1,
            "products": ["Product 1"],
            "status": "processing",
            "total": 1999,
            "date": "2024-02-15"
        }
    ]

@app.post("/api/orders")
async def create_order(order: dict):
    """Create a new order"""
    # TODO: Implement order creation logic
    return {"status": "success", "order_id": 1}

# Webhook route for Telegram
@app.post("/webhook")
async def webhook(update: dict):
    """Handle Telegram webhook updates"""
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)
    return {"ok": True}

# Startup and shutdown events
@app.on_event("startup")
async def on_startup():
    """Initialize database and set webhook on startup"""
    await init_db()
    await bot.set_webhook(settings.WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    """Remove webhook on shutdown"""
    await bot.delete_webhook()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
 