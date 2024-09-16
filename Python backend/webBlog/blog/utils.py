menu = [
    {'title': 'Главная', 'url': 'home', 'id': 1},
    {'title': 'Категории', 'url': 'show_all_cats', 'id': 2},
    {'title': 'О сайте', 'url': 'about', 'id': 3},
    {'title': 'Контакты', 'url': 'contacts', 'id': 4},
    {'title': 'Добавить статью', 'url': 'add_article', 'id': 5},

]

class RussianSlugify:
    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
    @classmethod
    def slugify(cls, value: str) -> str:
        to_slugify = value.lower()
        return "".join([cls.alphabet.get(x, x) for x in to_slugify])
