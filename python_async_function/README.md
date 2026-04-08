# async and await syntax
    async: async def foo(): pass  ->  Define a coroutine
    await: await foo()   ->   Put inside of an async function. It gives back control to the event loop.

# How to execute an async program with asyncio
    asyncio.run()
# How to run concurrent coroutines
    await asyncio.gather()
# How to create asyncio tasks
    asyncio.create_task()
# How to use the random module

# What's Coroutine
    A coroutine is a special type of function that can pause its execution to give back the control to the Event loop. this allows other task to run at the same time. After the Event loop is finished, it goes back where it left off.
# What's an Event Loop
    It's the core of a asyncio app. It schedules and executes tasks and callbacks, manages 1/O operations and handles events.