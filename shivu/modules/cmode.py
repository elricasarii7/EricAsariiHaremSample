from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("hhmode"))
async def hhmode_handler(client, message: Message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("SORT BY ANIME", callback_data="sort_anime"),
                InlineKeyboardButton("SORT BY RARITY", callback_data="sort_rarity"),
            ],
            [
                InlineKeyboardButton("DEFAULT MODE", callback_data="default_mode"),
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/77b4b93aa35b7f4bafc59.jpg",  # Ganti link sesuai kebutuhan
        caption="**Please choose your harem mode:**",
        reply_markup=buttons
    )

@Client.on_callback_query(filters.regex("sort_anime"))
async def sort_by_anime(_, callback_query):
    await callback_query.answer("You selected: Sort by Anime", show_alert=True)

@Client.on_callback_query(filters.regex("sort_rarity"))
async def sort_by_rarity(_, callback_query):
    await callback_query.answer("You selected: Sort by Rarity", show_alert=True)

@Client.on_callback_query(filters.regex("default_mode"))
async def default_mode(_, callback_query):
    await callback_query.answer("You selected: Default Mode", show_alert=True)
