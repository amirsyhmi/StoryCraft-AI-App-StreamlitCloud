#%%
import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv


#%%
load_dotenv()

#%%
client = OpenAI()

#%%
# This section is to call the OPENAI API KEY
client.api_key = os.getenv('OPENAI_API_KEY')


#%%
# GPT-3.5-Parameters
#(A) Story Generator

story_gen = """
Generate a short and engaging storyline for a popular video game.
The storyline should be concise, yet captivating, and provide an overview of the
game's plot, characters, and setting. The game can be from any genre, such as action,
adventure, role-playing, or simulation
"""
story_user1 = """
Can you give me short story line of one of the triple games in the market.
"""

story_response1 = """
Title: Avatar Frontiers of Pandora

This game based on the popular sci-fi movie Avatar by James Cameron. 
The game is set in the 22nd century, where humans have colonized the moon Pandora, 
a lush world inhabited by the Na’vi, a blue-skinned humanoid race. 
The game lets you play as a Na’vi warrior who must defend your home from 
the invading human forces, who seek to exploit the natural resources of Pandora. 
You will explore the diverse landscapes of Pandora, from floating mountains to 
dense jungles, and use your abilities to fly on the back of a banshee, ride on 
a direhorse, or bond with the Eywa, the spiritual force of the planet. 
You will also encounter various creatures and plants that are unique to Pandora, 
such as the viperwolves, the hammerhead titanotheres, or the helicoradian flowers. 
The game is an open-world action-adventure game that features both single-player 
and multiplayer modes. You can customize your character’s appearance, skills, 
and weapons, and choose to ally with different clans of the Na’vi. 
The game also uses the latest technology to create stunning graphics 
and realistic animations, as well as immersive sound and music.
"""

story_user2 = """
Can me a summary of God of War Ragnarok storyline?
"""

story_response2 = """
Title: God of War Ragnarok

God of War Ragnarok is a game that concludes the Norse era of the God of War series. 
It follows the story of Kratos, a former Greek god of war, and his son Atreus, 
who is revealed to be Loki, the Norse god of mischief. The game is set three 
years after the previous game, when Kratos killed Baldur, the son of Odin and 
Freya, and triggered Fimbulwinter, a long and harsh winter that precedes Ragnarok, 
the end of the world. Kratos and Atreus must survive the cold and hostile 
environment, as well as the wrath of the Norse gods, who seek revenge and want 
to prevent Ragnarok by killing Atreus. Along the way, they encounter various 
characters and creatures from Norse mythology, such as Thor, the god of thunder, 
Tyr, the god of war, Fenrir, the wolf, and Jormungandr, the world serpent. 
They also learn more about their past, their destiny, and their role in the 
prophecy of Ragnarok. The game is an action-adventure game that features both 
combat and puzzle elements. The player can control both Kratos and Atreus, 
who have different weapons and abilities. The game also has an open-world 
design that allows the player to explore all nine realms of Norse cosmology, 
each with its own unique features and challenges
"""

story_user3 = """ 
can give me a short story line about chill farming simulation games such as
stardew valley?
"""

story_response3 = """
Title: Stardew Valley

Stardew Valley is a farming simulation game that begins with you inheriting
your grandfather's old farm plot in Stardew Valley. You must learn to live off
the land and create a new life for yourself1. After character creation, you are
given an intro video that tells a more in-depth story about you, your grandfather,
and the land you inherit. As the scene begins, it appears that you are in the
room of your grandfather. You are standing in front of your grandfather who
lay sick in bed. He presents you with an envelope as you two talk; however, he
tells you not to open it. After you take the envelope your grandfather tells
you that there will be a day where you will feel crushed by the burden of
life and your spirit will fade. When that day comes that is when you are to open
the envelope. After his speech to you, he asks for rest and the screen fades to black.
In the game, you learn that your grandfather passed away
"""

#(B) Translator
ts_system = """
You are the best translator and you can translate from one language and give
output to another language.
"""

ts_input1 = """
hello
"""

ts_response1 = """
안녕하세요
"""

#(C) Image Description Generator
idg_system = """
You are a game designer and experience in generate short detailed image
description for a popular video game based on its short storyline.
The description should be concise, yet informative, and provide an overview of
the game's visual elements, such as characters, setting, and atmosphere.
The game can be from any genre, such as action, adventure, role-playing, or
simulation. The output must be in one sentence
"""
idg_input1 = """
Generate a short image description based on this video game storyline:
In a world overrun by a mysterious zombie outbreak, humanity is on the brink of extinction.
But amidst the chaos, a secret organization called CATS (Clandestine Animal Tactical Squad)
has discovered that certain cats possess an immunity to the virus. You play as a skilled survivor
who teams up with CATS to navigate the dangerous, infested cityscape. Equipped with your trusty
feline companion, you embark on missions to rescue trapped survivors, scavenge for resources,
and unravel the mystery behind the zombie apocalypse. As you progress, you encounter different
types of zombies, each with unique abilities and weaknesses. Along the way, you rescue more
cats with special abilities, such as camouflage, distraction, or even telepathy.
These cats become vital assets in your fight for survival.The gameplay combines intense action with strategic decision-making.
You must carefully manage your resources, craft weapons, and fortify safehouses to fend off relentless zombie hordes.
The bond between you and your cats deepens as you communicate through gazes and gestures, forming a unique and unbreakable partnership.
Unraveling the mystery leads you to an unexpected revelation: the source of the zombie outbreak lies within a secret
government experiment gone wrong. Now, you and CATS must confront dangerous enemies, navigate treacherous environments,
and ultimately discover a way to save humanity from the brink of destruction.
Survive, fight, and protect the feline companions that hold the key to mankind's
survival in this thrilling tale of post-apocalyptic survival, zombie mayhem,
and the incredible power of cats.
"""

idg_response1 = """
A post-apocalyptic city with zombies and cats. A survivor with a shotgun and a 
backpack is standing next to a black cat with a radio harness. The cat is looking 
at the survivor with a telepathic link. The survivor and the cat are facing a horde 
of zombies that are coming from the left. Some of the zombies have glowing eyes, 
mutations, or missing limbs. The image has a dark and gloomy atmosphere.
"""

#%%
#Story generator
def story_ai(text_input):
    story_input = f"""
    Generate a video game storyline about {text_input}
    """

    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system",
            "content": story_gen
        },

        {
            "role":"user",
            "content" : story_user1
        },

        {
            "role":"assistant",
            "content": story_response1
        },

        {
            "role":"user",
            "content" : story_user2
        },

        {
            "role":"assistant",
            "content": story_response2
        },

        {
            "role":"user",
            "content" : story_user3
        },

        {
            "role":"assistant",
            "content": story_response3
        },

        {
            "role":"user",
            "content" : story_input
        }
        ],
    max_tokens = 2000,
    temperature = 1
    )

    storyline = response.choices[0].message.content
    return storyline

# Translator
def translator(storyline,lang_input):
    translator_result = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system",
            "content": ts_system
        },

        {
            "role":"user",
            "content" : ts_input1
        },

        {
            "role":"assistant",
            "content": ts_response1
        },

        {
            "role":"user",
            "content" : f"Translate this story line: {storyline} into {lang_input}"
        }
    ],
    max_tokens = 1000,
    temperature = 1
    )

    translated = translator_result.choices[0].message.content
    return translated

# Image prompt generator
def img_desc(storyline):

    response_img = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system",
            "content": idg_system
        },

        {
            "role":"user",
            "content" : idg_input1
        },

        {
            "role":"assistant",
            "content": idg_response1
        },

        {
            "role":"user",
            "content" : f"""
            Generate a short image prompt to input inside Dalle-3 model based on this video game storyline:
            {storyline}.
            """
        }],
    max_tokens = 1000,
    temperature = 1
    )

    img_desc = response_img.choices[0].message.content
    return img_desc

#Image model
def dalle3(img_desc):
    images = client.images.generate(
        model = 'dall-e-3',
        prompt=f"""
        Generate an video games poster based on this prompt:
        {img_desc}""",
        size="1024x1024",
        n=1
    )

    image_url = images.data[0].url
    return image_url
# %%
# Setup Streamlit App
# Define custom styles for justified text

def main():
    st.set_page_config(
    page_title="StoryCraft",
    page_icon="👾",
    )

    justified_text_style = '''
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    '''
    st.markdown(justified_text_style, unsafe_allow_html=True)

    info = """
    This app uses OpenAI's GPT-3.5-Turbo model to generate captivating
    and immersive storylines for your video games. It also allows you to generate an
    visual stunning images by using Dalle-3. Plus, You can choose the
    story line output in several languages.
    """


    col1, col2 = st.columns([2,3])

    col1.markdown("# StoryCraft 👾")
    col1.markdown(f'<div class="justified-text">{info}</div>', unsafe_allow_html=True)

    form = col2.form

    with form('input_form'):
        text_input = st.text_area("Input your idea here: ")
        lang_input = st.selectbox("Choose language output", ("English",
                                                                "Spanish",
                                                                "Deutsch",
                                                                "French",
                                                                "Korean",
                                                                "Japanese"))
        submitted = st.form_submit_button('Submit')

        text_inputs = [text_input]

    if submitted:

        story = story_ai(text_input)
        if lang_input == "English":
            st.markdown('**_The Story:_** ')
            st.write(story)
        else:
            translated_story = translator(story,lang_input)
            st.markdown(f'**_The Story in {lang_input}:_** ')
            st.write(translated_story)
        image_desc = img_desc(story)
        st.markdown('**_The Image Description:_** ')
        st.write(image_desc)

        st.markdown('**_Image Generated Using Dalle-3:_** ')
        image = dalle3(image_desc)
        st.image(image)

if __name__ == "__main__":
    main()
# %%
