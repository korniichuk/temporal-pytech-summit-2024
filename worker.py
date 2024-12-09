import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from example import HelloWorld


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(client, task_queue="example-tasks", workflows=[HelloWorld])
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
