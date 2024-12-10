from datetime import timedelta

from temporalio import activity
from temporalio import workflow

from nbp import get_usd_rate


@workflow.defn
class HelloWorld:
    @workflow.run
    async def run(self) -> str:
        num = 2 + 2  # deterministic
        text = await workflow.execute_activity(
            nbp, start_to_close_timeout=timedelta(seconds=5))
        return f"num: {num}\n\n{text}"


@activity.defn
async def nbp() -> str:
    text = await get_usd_rate()
    return text
