import os

class Config:
    """Base config class"""
    SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://zceslwfcsxgifgfqhdsa.supabase.co')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpjZXNsd2Zjc3hnaWZnZnFoZHNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg3MTU1MDksImV4cCI6MjA0NDI5MTUwOX0.uXHtoCZv7rgUQ_PZSQPL7lMuoNMPY93qBaMNmovK-8o')

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False
