import asyncio
import logging
import os
from google.adk.cli import adk_cli
from google.adk.cli.fast_api import get_adk_proxy_url
from app import create_adk_app
from memory.memory_bank_service import initialize_memory

logging.basicConfig(level=logging.INFO)

async def main():
    if 'GEMINI_API_KEY' not in os.environ or os.environ['GEMINI_API_KEY'] == 'YOUR_GEMINI_API_KEY_HERE':
        print("\n⚠️ ERROR: GEMINI_API_KEY is not set. Please set it before running.\n")
        return
    
    # Set the key from the Colab cell if running directly here
    os.environ['GEMINI_API_KEY'] = 'YOUR_GEMINI_API_KEY_HERE'

    await initialize_memory()
    app = create_adk_app()
    url = get_adk_proxy_url()
    print(f"\nADK Server starting at {url}\n")
    
    # Run server and background MonitorAgent
    adk_cli.run(app, log_level=logging.DEBUG, url_prefix=url, run_server_in_background=True)

if __name__ == "__main__":
    asyncio.run(main())
