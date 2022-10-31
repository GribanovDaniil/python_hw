import module
a = input('Добро пожаловать! Какой у вас вопрос?')
if 'расп' in a:
    module.raspisanie(a)
elif 'конт' in a:
    module.kontakti(a)
elif 'сум' in a:
    module.oplata(a)
elif 'с собой' in a:
    module.chtonado(a)
elif 'трансф' in a:
    module.transfer(a)