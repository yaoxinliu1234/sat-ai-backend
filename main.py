import uvicorn
import os
from app.db.session import SessionLocal
from app.db.init_db import init_db

def main():
    # Initialize database
    try:
        db = SessionLocal()
        init_db(db)
        db.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Database initialization failed: {e}")
        # Continue anyway, database might already exist
    
    # Get port from environment variable (Railway sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Start server
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Disable reload in production
    )

if __name__ == "__main__":
    main()
