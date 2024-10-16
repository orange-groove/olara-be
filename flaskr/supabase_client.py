from supabase import create_client
from flaskr.config import Config

supabase_url = Config.SUPABASE_URL
supabase_key = Config.SUPABASE_KEY

supabase = create_client(supabase_url, supabase_key)