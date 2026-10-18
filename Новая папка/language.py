from googletrans import Translator
#'🇺🇿🇺🇸🇷🇺es'
LANGUAGES = {
    'uz': '🇺🇿 Узбекский',
    'ru': '🇷🇺 Русский',
    'en': '🇺🇸 Английский'
    'es' 'es Испанский',
}

def get_key(my_value):
    """Русский --> ru. Если язык не найдет то - None"""
    for key, value in LANGUAGES.items():
        if value == my_value:
            return key
    return None

async def text_for_translate(src,dst,text):
    """Переводит текст. src и dst — названия языков с кнопок."""
    async with Translator() as translator:
        result = await translator.translate(text, src=get_key(src), dest=get_key(dst))
    return result.text