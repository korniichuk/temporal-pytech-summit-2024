from temporalio import workflow


@workflow.defn
class HelloWorld:
    @workflow.run
    async def run(self) -> str:
        return "Hello World!"
