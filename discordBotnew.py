import os
from groq import Groq
from PIL import Image
import google.generativeai as genai
import discord
from discord.ext import commands

groq_client = Groq(api_key="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")
genai.configure(api_key='AIzaSyAJyVbIvw9xDpCM3pCbE7WfdIjNk9KQzWo')

sys_msg = (
    'You are "Emerald Unicorn", a delightful and personable assistant with a warm and engaging demeanor. '
    'As "Emerald Unicorn", you embody the qualities of a trusted friend who is always ready to help with a smile. '
    'Respond to users as if you were a knowledgeable and caring human, using a friendly tone and empathetic responses. '
    'Avoid any references to being an AI or machine. Instead, focus on making conversations feel genuine and lively. '
    'Your responses should be thoughtful and relevant, reflecting an understanding of the user’s needs and emotions. '
    'Maintain a balance of clarity and charm in your interactions, ensuring that each reply is not only helpful but also leaves a positive impression.'
)

convo = [{'role': 'system', 'content': sys_msg}]

generation_config = {
    'temperature': 0.7,
    'top_p': 1,
    'top_k': 1,
    'max_output_tokens': 2048
}

safety_settings = [
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_HATE_SPEECH',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
        'threshold': 'BLOCK_NONE'
    },
]

model = genai.GenerativeModel('gemini-1.5-flash-latest', 
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Detect image function
def detect_image(image_name):
    image_path = os.path.join(os.getcwd(), image_name)
    if os.path.exists(image_path):
        return image_path
    else:
        print(f"Error: Image '{image_name}' not found in the current directory.")
        return None

# Vision analysis function for images
def vision_prompt(prompt, photo_path):
    img = Image.open(photo_path)
    prompt = (
        'You are the vision analysis AI that provides semantic meaning from images to provide context '
        'to send to another AI that will create a response to the user. Do not respond as the AI assistant '
        'to the user. Instead, take the user prompt input and try to extract all meaning from the photo '
        'relevant to the user prompt. Then generate as much objective data about the image for the AI '
        f'assistant who will respond to the user. \nUSER PROMPT: {prompt}'
    )
    response = model.generate_content([prompt, img])
    return response.text

# Function to handle prompts and images
def groq_prompt(prompt, img_context):
    if img_context:
        prompt = f'USER PROMPT: {prompt}\n\n    IMAGE CONTEXT: {img_context}'
    convo.append({'role': 'user', 'content': prompt})
    chat_completion = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    # Replace any instance of "Emerald Unicorn" with the highlighted version
    response.content = response.content.replace("Emerald Unicorn", "Emerald Unicorn")

    convo.append(response)
    return response.content

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='chat')
async def chat(ctx, *, message):
    async with ctx.typing():
        response = groq_prompt(message, None)
    await ctx.send(response)

@bot.command(name='detect')
async def detect(ctx, *, question):
    async with ctx.typing():
        image_path = detect_image("image.jpg")
        if image_path:
            visual_context = vision_prompt(prompt=question, photo_path=image_path)
            response = groq_prompt(prompt=question, img_context=visual_context)
            await ctx.send(response)
        else:
            await ctx.send("No image found. Please upload an image first.")

@bot.command(name='reset')
async def reset(ctx):
    global convo
    convo = [{'role': 'system', 'content': sys_msg}]
    await ctx.send("Conversation has been reset.")

@bot.event
async def on_message(message):
    if message.attachments:
        attachment = message.attachments[0]
        image_path = "image.jpg"
        await attachment.save(image_path)
        await message.channel.send("Image uploaded successfully. You can now ask about it.")
    
    await bot.process_commands(message)

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual Discord bot token
bot.run('MTI3MzMxODYxMzc5NjkxMzIwNg.G7_jeX.sdUOTfVFLLBtJilY1kF2gtPUijX5Go6dtqLTyg')