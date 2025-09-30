from telethon import loader, utils


@loader.tds
class MyModule(loader.Module):
    strings = {"name": "TestModule"}

    async def testcmd(self, message):
        await utils.answer(message, "Работает!")