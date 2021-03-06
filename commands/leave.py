from utils import embedded_message


# Disconnects bot from voice channel
async def leave(ctx):
    if ctx.guild.voice_client:
        await ctx.voice_client.disconnect()
        await embedded_message(ctx, "**Bye Bye** :call_me:", "_Disconnected_")
    else:
        await embedded_message(ctx, "**Not Connected**", ":exclamation: _I'm currently not connected_")

