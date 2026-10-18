import asyncio
import logging
from os import getenv

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from db_utils import db
from keyboard import generate_language
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Bot,Dispatcher ,F, Router
from aiogram.client import bot
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv

from fsm_state import Questions
from google_file import LANGUAGES, text_for_translate



load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
router = Router()
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)




@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        "/translator — перевести текст\n"
        "/history — последние 10 переводов\n"
        "/stats — статистика ваших переводов\n"
        "/clear — очистить историю\n"
        "/cancel — остановить перевод\n"
        "/about — о боте"
    )

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer('Учебный бот-переводчик на aiogram и SQLite.')


@router.message(Command('translator'))
async def start_questions(message: Message, state:FSMContext):
    await state.set_state(Questions.src)
    await message.answer('С какого языка вы хотите перевести', reply_markup= generate_language())

@router.message(Questions.src, F.text.in_(LANGUAGES.values()))
async def set_src(message: Message, state: FSMContext):
    await state.update_data(src=message.text)
    await state.set_state(Questions.dst)
    await message.answer('На какой язык переведём?', reply_markup=generate_language())


@router.message(Questions.dst, F.text.in_(LANGUAGES.values()))
async def set_dst(message: Message, state: FSMContext):
    await state.update_data(dst=message.text)
    await state.set_state(Questions.text)
    await message.answer('Введите текст для перевода', reply_markup=ReplyKeyboardRemove())




@router.message(Questions.text, F.text)
async def catch_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    text =  await text_for_translate(src=data['src'], dst=data['dst'], text=data['text'])
    await message.answer(text)
    db.write_db(message.chat.id,data['src'], data['dst'], data['text'], text)
    await state.clear()

@router.message(Command('history'))
async def cmd_history(message: Message):
    rows = db.read_from_db(message.chat.id)
    if not rows:
        await message.answer('История пуста. Начните с /translator')
        return
    parts = []
    for src, dst, original_text, translated_text, created_at in rows:
        parts.append(
            f'<b>{created_at}</b>\n'
            f'{src} --> {dst}\n'
            f'<b>Ваш текс:</b> {original_text}\n'
            f'<b>Перевод</b>: {translated_text}\n'
        )
        await message.answer('Ваши последние переводы:\n\n'+'\n\n'.join(parts))
@router.message(Command('stats'))
async def cmd_stats(message: Message):
    total = db.count_translation(message.chat.id)
    if total == 0:
        await message.answer('Вы еще ничего не переводили')
        return
    lines = [f'Всего переводов: {total}','', 'Популярные направления:']
    for src, dst, count in db.popular_pairs(message.chat.id):
        lines.append(f'{src}  ➡️  {dst}: {count}')
    await message.answer('\n'.join(lines))

@router.message(Command('clear'))
async def cmd_clear(message: Message):
    deleted = db.clear_history(message.chat.id)
    await message.answer(f'История очищена. Удалено записей: {deleted}')

@router.message(Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Перевод остановлен. Чтобы начать снова /translator',
                         reply_markup=ReplyKeyboardRemove())

async def main():
    db.create_table()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())