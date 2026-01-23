# Сначала определяем функцию
def build_query_string(params):
    return "&".join(f"{key}={value}" for key, value in sorted(params.items()))


# Затем получаем и выполняем ввод пользователя
user_input = input().strip()
exec(user_input)
