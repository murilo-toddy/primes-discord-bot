async def join(ctx):
    bot_channel = ctx.guild.voice_client
    
    if bot_channel:
        await ctx.channel.send("ja to conectado parsa")
    
    else:
        await ctx.author.voice.channel.connect()
        bot_channel = ctx.guild.voice_client
        bot_channel.pause()