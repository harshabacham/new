"""
Vercel Serverless & ASGI Production Entrypoint for SIH26184 Forecasting Platform.
Exports top-level variables: app, application, handler.
"""

from api import app, application, handler

__all__ = ["app", "application", "handler"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)
