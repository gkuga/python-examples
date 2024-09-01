import logging
import asyncio
import time
from functools import partial
from time import sleep

logger = logging.getLogger(__name__)


async def run():
    loop = asyncio.get_event_loop()
    st = time.time()
    logger.info("**start**")
    result = await asyncio.gather(
        loop.run_in_executor(None, partial(sleep, 3)),
        loop.run_in_executor(None, partial(sleep, 3)),
        loop.run_in_executor(None, partial(sleep, 3)),
    )
    logger.info("**end** %r %r", result, time.time() - st)


logging.basicConfig(level=logging.INFO, format="%(asctime)s" + logging.BASIC_FORMAT)
asyncio.run(run(), debug=True)
