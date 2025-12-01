from google.adk.storage import MemoryBank
import asyncio
import logging
MEMORY_BANK = MemoryBank(name='UserPreferences', max_entries=50)
async def initialize_memory():
    await MEMORY_BANK.add_entry('UserRule', 'Never schedule deep work before 10 AM.', metadata={'type': 'constraint'})
    await MEMORY_BANK.add_entry('UserRule', 'Laundry must be completed by Sunday at 8 PM.', metadata={'type': 'deadline_rule'})
    logging.info("MemoryBank initialized with user rules.")
