from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes, ConversationReference

import os
import asyncio

app_id = os.getenv("MICROSOFT_APP_ID", "my-app-id")
app_password = os.getenv("MICROSOFT_APP_PASSWORD", "my-app-password")
settings = BotFrameworkAdapterSettings(app_id, app_password)
adapter = BotFrameworkAdapter(settings)


conversation_references = {}

async def send_proactive_message(conversation_reference: ConversationReference, message: str):
    async def aux(turn_context: TurnContext):
        await turn_context.send_activity(Activity(type=ActivityTypes.message, text=message))

    await adapter.continue_conversation(conversation_reference, aux, app_id)

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    activity = Activity().deserialize(body)

    if activity.type == ActivityTypes.message and "Olá" in activity.text:
        # Criar a referencia da conversa
        conversation_reference = TurnContext.get_conversation_reference(activity)
        user_id = activity.from_property.id
        conversation_references[user_id] = conversation_reference

        # Enviar mensagem para o utilizador
        asyncio.create_task(send_proactive_message(conversation_reference, "Olá! o seu pedido foi concluido."))

    return web.Response(text="OK")

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3900))
    web.run_app(app, port=port)
