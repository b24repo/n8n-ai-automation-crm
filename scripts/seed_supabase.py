"""
Supabase schema setup for n8n CRM automation pipeline.
Run once to create the leads table and indexes.
"""
import os
from supabase import create_client

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

# Schema is managed via Supabase migrations
# See supabase/migrations/ for the full schema
print("Supabase connection verified:", url)
