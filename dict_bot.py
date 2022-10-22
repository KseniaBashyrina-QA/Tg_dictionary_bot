# В google colab добавить: !pip install pyTelegramBotAPI
# Укажите свой личный токен
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='Вставьте токен', parse_mode='html') # создание бота
# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'чекать': 'Проверить; отметить (галочкой)',
    'фича': 'функциональность, функциональная возможность, характерная особенность программы.',
    'кастомер': 'Заказчик, пользователь (программы), покупатель, клиент.',
    'кастомерский': 'Пользовательский, имеющий отношение к заказчику или пользователю программы.',
    'фича': 'Функциональность, функциональная возможность, характерная особенность программы.',
    'айтишник ': 'Специалист, профессионально занимающийся работами в области информационных технологий.',
    'апдейт': 'Модернизация, корректировка, обновление информации, данных; новая версия, обновленный вариант.',
    'аутиться': 'Выходить за пределы',
    'баг': 'Выявленная ошибка в программе или в документации.',
    'бага': 'Выявленная ошибка в программе или в документации.',
    'билд': 'Конечный вид программы или её модуля, который можно тестировать.',
    'бэкап': 'Создание резервных копий данных с целью их восстановления в случае потери оригинальных данных по каким-либо причинам.',
    'генериться': 'Генерироваться, формироваться',
    'дебажить': 'Отлаживать',
    'дедлок': 'Состояние системы (программы), при котором ее внутренние процессы конфликтуют и блокируют друг друга.',
    'деплоить': 'Развертывание приложения на сервере (часто в выражении "задеплоить на Тест").',
    'дизэйблить': 'Зпрещать/отменять что-либо',
    'дизэйблиться': 'Быть в нерабочем состоянии, не работать.',
    'забукать': ' Зарегистрировать, заказать',
    'залить': 'Закачать (например, файл, данные)',
    'налить ': 'Закачать (например, файл, данные)',
    'замапить': 'Сопоставить,составить схему обработки данных.',
    'замапать': 'Сопоставить,составить схему обработки данных.',
    'заплата': 'Исправление ошибок и недоработок программы, выявленных в процессе эксплуатации.',
    'зачарджить': 'Списать деньги с карты.',
    'заюзить': 'Использовать.',
    'кавередж': 'Покрытие, зона действия (например, покрытие процесса тестирования).',
    'капча': 'Аббревиатура от английских слов «Completely Automatic Public Turing Test to Tell Computers and Humans Apart»,используется для предотвращения автоматической регистрации и в формах отправки сообщений на интернет страницах и представляет из себя изображение, состоящее из искаженных букв и цифр. Предполагается что человек гораздо точнее определит исходную комбинацию.',
    'кетч': 'Перехват (например, исключений, событий и др.)',
    'кетчиться': 'Перехватывать.',
    'комбокс': 'Комбинированный список, элемент управления интерфейса, формы и т.д., с помощью которого можно выбирать "готовые" значения из списка, а также, в некоторых случаях, вводить новые значения самостоятельно.',
    'коммит': 'Сохранение, фиксация (в архиве, репозитарии и др.) изменений в программном коде.',
    'коммитить': 'Выполнить коммит.',
    'компилить ': 'Компилировать.',
    'конвертить ': 'Преобразовать, конвертировать.',
    'коннекшн': 'Связь, контакт',
    'конфиг': 'Конфигурационный файл, вспомогательный файл, определяющий конфигурацию программы и необходимый для ее запуска.',
    'кривой': 'Некорректный.',
    'лейбл': 'Надпись, элемент управления интерфейса, формы и т.д., в который выводится некоторый заранее определенный текст.',
    'лог': 'Файл, содержащий информацию о деятельности и об успешности (и об ошибках) прохождения программы.',
    'логгирование': 'Процесс формирования лог-файла.',
    'логиниться': 'Входить в систему (программу) путем введения логина и пароля.',
    'залогиниться': 'Входить в систему (программу) путем введения логина и пароля.',
    'локаль': 'Набор параметров, включая набор символов, язык пользователя, страну, часовой пояс, а также другие предустановки, которые пользователь ожидает видеть в пользовательском интерфейсе.',
    'маппинг': 'Процесс составления схемы того, какими данными следует обмениваться, как они будут использоваться и каким системам управления бизнесом они нужны. Маппинг выполняется функциональным менеджером, ответственным за систему управления бизнесом. Маппинг является первым шагом при разработке приложения-связки.',
    'мигрировать': 'Переносить данные (например, из одной базы данных в другую)',
    'накат': 'Перемещение вперед, выполнение нового действия; выполнение последнего отмененного ранее действия (команда Redo). Противоположно слову откат;установка новой версии программы поверх старой.',
    'накатить': 'Выполнить накат - перемещение вперед, выполнение нового действия; выполнение последнего отмененного ранее действия (команда Redo). Противоположно слову откат;установка новой версии программы поверх старой.',
    'обваливаться': 'Перестать работать, начиная с определенного момента.',
    'опшен': 'Переключатель, элемент управления интерфейса, формы и т.д., выполненный в форме нескольких кружков. При выборе (активизации) переключателя в нем появляется точка. Обычно можно выбрать (активизировать) только один переключатель, относящийся к одной группе.',
    'откат': 'Отмена предыдущего действи.',
    'откатить': 'Отменить, выполнить откат.',
    'падать': 'Перестать работать, начиная с определенного момента.',
    'пересортировка': 'Повторное выполнение сортировки некоторого набора данных.',
    'пинговать': '1.Проверять качество интернет-соединения. 2.Утилита Ping для проверки работоспособности сети.3. Напоминать о чём-то.',
    'поп-ап': 'Всплывающий, появляющийся. Например, окно, которое открывается произвольно, без участия пользователя программы; всплывающее окно.',
    'прога': 'Программа',
    'пэкедж': 'Упакованный программный файл.',
    'расшарить': 'Дать совместный или общий доступ к компьютерным ресурсам.',
    'реквест': 'Запрос.',
    'рейндж': 'Порядок (сортировки), ранг, граница.',
    'ресайзить': 'Изменять размер.',
    'ридер': 'Программа для считывания информации.',
    'рулы': 'Правила (например, правила обработки данных).',
    'cабскрипт': 'Нижний индекс, подстрочный индекс',
    'скин': 'Вариант интерфейса.',
    'скрипт': 'Небольшая программа (например, для автоматизации тестирования).',
    'cкролл': 'Полоса прокрутки, элемент управления интерфейса, формы и т.д., выполненное в форме полосы с "ползунком", с помощью которого можно быстро перемещать изображение на экране, открывая ту часть интерфейса или формы, которая не поместилась на экране. Обычно полосы прокрутки находятся в правой и в нижней части экрана.',
    'cпек': 'Спецификация, утвержденный документ, являющийся основой для разработки компьютерной программы и для ее тестирования.',
    'стартап': 'Появляться, запускать.',
    'стейтмент': 'Выражение; положение нормативного документа, содержащее информацию.',
    'стенд-алон': 'Отдельное, самодостаточное устройство, которому для работы не нужны другие устройства.',
    'суперскрипт': 'Верхний индекс, надстрочный индекс, показатель степени.',
    'текстбокс': 'Текстовое поле, элемент управления интерфейса, формы и т.д., в который можно вводить те или иные текстовые значения.',
    'трассировать': 'Выполнять пошагово.',
    'трейсабилити': 'Отслеживаемость, характеристика, позволяющая устанавливать связь между элементами аппаратуры или процессами, между требованием и источником требования, между методом проверки и его основным требованием.',
    'тул': 'Вспомогательная программа, утилита, инструментарий (например, для тестирования).',
    'убить': 'Прекратить (напр., процесс автоматического тестирования).',
    'фидбэк': 'Отзыв, отклик, ответная реакция на какое-либо действие или событие.',
    'фикс': 'Исправление ошибки, выявленной в процессе тестирования, путем корректировки кода программы, а также "заплатка" к программе.',
    'фиксить': 'Произвести указанное исправление',
    'пофикситься': 'Исправиться',
    'филд-инженер': 'Инженер, занимающийся установкой, наладкой и внедрением нового программного продукта у потребителя (заказчика).',
    'хедер': 'Часть файла (обычно в начале файла), в которой содержится информация системного характера.',
    'хотфикс': 'Срочное исправление ошибок и недоработок программы, выявленных в процессе эксплуатации, "заплата".',
    'чекбокс': 'Флажок, элемент управления интерфейса, формы и т.д., выполненный в форме квадратика. При выборе (активизации) флажка в нем появляется знак галочки. Можно выбрать (активизировать) один или несколько флажков, относящихся к одной группе.',
    'чекать': 'Отмечать галочкой или каким-л. знаком (что-л. проверенное)) - проверить; отметить (галочкой).',
    'чекпойнт': 'Вид автосохранения текущего состояния программы или теста, с которого тестировщик может продолжить свою работу в случае неудачи.',
    'шариться': 'Предоставляться для совместного или общего доступа;разделяться.',
    'шаринг': 'Предоставление совместного или общего доступа; разделение.',
    'шары': 'Компьютерные ресурсы совместного или общего использования.',
    'шейдер': 'Небольшая программа, выполняющаяся на графическом, а не на центральном процессоре.',
    'юзабилист': 'Специалист по разработке или тестированию интерфейса.',
    'юзабилити-тестирование': 'Тестовая оценка качества интерфейса.',
    'релиз': 'Передача продукта конечному пользователю.',
    'дев': 'Сервер, на который разработчики деплоят нестабильные версии приложения для отладки; а также непосредственно подразделение разработки.',
    'таска': 'Какая-либо задача (обычно в системе управления); задача для выполнения приложением внутри бизнес-процесса.',
    'таск': 'Какая-либо задача (обычно в системе управления); задача для выполнения приложением внутри бизнес-процесса.',
    'митинг': 'Собрание, совещание (обычно online).',
    'нормал': 'Незначительный дефект.',
    'мажор': 'Дефект, влияющий на какую-то функциональную часть приложения.',
    'критикал': 'Дефект, блокирующий UI, можно обойти, используя специальный инструментарий.',
    'блокер': 'Дефект, блокирующий дальнейшее выполнение теста, исправляется в первую очередь',
    'тривиал': 'Наименее значимый, косметический дефект, исправляется в последнюю очередь (а часто так и остается в длинном to-do списке).',
    'лоу': 'Наименее значимый, косметический дефект, исправляется в последнюю очередь (а часто так и остается в длинном to-do списке).',
    'тест': 'Сервер, на который разработчики или тестировщики деплоят отлаженную версию приложения, предназначенную для проведения тестов.',
    'препрод': 'Сервер, на который деплоится протестированная версия приложения, релиз-кандидат.',
    'стейдж': 'Сервер, на который деплоится протестированная версия приложения, релиз-кандидат.',
    'батон ': 'Элемент интерфейса приложения/компьютерной программы, простыми словами "кнопка" (радиобатоны и пуш‑батоны).',
    'банщик': 'Дизайнер, который, с помощью графических редакторов, занимается версткой и созданием рекламных баннеров.',
    'бенефит': 'Некий бонус, использующийся для мотивации сотрудников. Обычно это непрямое денежное или иное нематериальное вознаграждение.',
    'библиотека': 'Набор скомпилированного кода (например, функций), который «упакован» для вторичного использования в других программах. Библиотеки необходимы, для расширения возможностей программ.',
    'бигдата': 'Набор специализированных методов и инструментов, использующихся для хранения и обработки огромных объемов данных, т.е. таких, которые характеризуются «тремя V»: volume (объём), velocity (скорость прироста и обработки), variety (многообразие).',
    'бинк': 'Сокращённое название мейлеров типа BinkleyTerm. Бинком сейчас, чаще всего, называют популярный IP-мейлер binkd.',
    'бипер': 'Встроенный динамик ПК; устройство, которое служит для генерации тонов DTMF, используется совместно с телефонами, не поддерживающими тоновый набор; цифровой пейджер.',
    'битый': 'Некорректный / нерабочий / содержащий ошибку. Так, «битая ссылка» ведет на несуществующую страницу с ошибкой 404 (Error 404), «битые пиксели» - неправильно отображают цвета на мониторе.',
    'бэкап': 'Резервное копирование, т.е. создание резервной копии информации/проекта/сайта, для того, чтобы при каких-либо ошибках и сбоях иметь возможность восстановить данные. Безопасным считается регулярное обновление бэкапов и хранение их на различных устройствах.',
    'бэклог': 'Перечень задач по функционалу в порядке приоритета для реализации в следующих версиях продукта.',
    'выделенка': 'Выделенная линия, т.е. подключение к интернет-провайдеру с использованием индивидуальной линии (кабеля) и сетевой карты.',
    'гектар': 'Другое название гигабайта (кратен единице байта) - единица измерения количественной информации, равная 109 (1 000 000 000) или 230 (1 073 741 824) байт.',
    'жмыл': 'Популярный бесплатный почтовый сервис Gmail от Google, предоставляющий доступ к электронным почтовым ящикам.',
    'зааджастить': 'Немного поменять логику программы, внести легкие изменения, до настроить, привести в порядок, отрегулировать.',
    'зазиповать': 'Перевести готовый архив с какими-то файлами в формат .zip.',
    'залочить': 'Установить блокировку на персональное устройство (ПК, смартфон, планшет) для защиты от несанкционированного доступа сторонних лиц.',
    'засейвить': 'Сохранить некую информацию/версию.',
    'тэдэшка': 'Документ, где описаны логика и функциональность программы.',
    'апликуха': 'Это приложение, приложения называют эппами, тоже от английского сокращения app.',
    'Забэкапить': 'Делать резервную копию.',
    'кракозябры': 'Нечитаемый набор символов. Например, когда при запуске программы на экран выводится какая‑то бессмыслица из математических знаков и случайных букв.',
    'имплементить': 'Внедрять, осуществлять. Так программисты говорят о реализации какого‑то функционала. По сути, это всего лишь синоним глагола «делать».',
    'пушить': 'Нажимать, давить, означает загружать код на сервер GIT — систему отслеживания версий.',
    'репа': 'Репозиторий - место где хранится вся история кода.',
    'парсинг': 'Собирать или анализировать данные.',
    'апишка': 'Это программный интерфейс приложения или интерфейс прикладного программирования; описание способов, которыми одна компьютерная программа может взаимодействовать с другой программой.',
    'галера': 'Компания, где платят низкие зарплаты, не ценят разработчиков и «выжимают» из них все силы.',
    'грумить': 'Приводить в порядок, «причесывать», так сказать.',
    'дыра': 'Уязвимость в коде ПО, которой могут воспользоваться хакеры.',
    'инвестигировать': 'Расследовать инцидент.',
    'костыль': 'Быстрое и простое решение проблемы, применяемое для срочного устранения её последствий, но не влияющее на причины её возникновения.',
    'мержить': 'Объединять или  выполнять слияние веток кода.',
    'мускул': 'База данных MySQL.',
    'реджект': 'Возвращение билда на доработку, отклонение сборки.',
    'сахар': 'Это конструкции, которые делают использование языка программирования удобным для разработчика.',
    'свитчер': 'Специалист, который пришел работать в IT из другой сферы деятельности.',
    'cкипануть': 'Намеренно пропустить что-то.',
    'скрамить': 'Вести разработку способом, при котором сохраняются четкие списки задач на короткие отрезки времени и равномерное распределение ответственности между всеми участниками команды.',
    'спринтить': 'Реализовывать часть проекта в небольшой фиксированный отрезок времени.',
    'сырцы': 'Исходный код.',
    'хрюша': 'Ироничное название для специалиста, который занимается работой с персоналом в компании.',
    'факап': 'Провал задачи, важного дела.',
    'апрув': 'Подтвердить что-нибудь.',
    'компилятор': 'Программа, которая переводит компьютерный код, написанный на одном языке программирования (исходный), на другой (целевой язык).',
    'опенсорс': 'Подход к созданию программ с открытым исходным кодом или программа с открытым исходным кодом',
    'фреймворк': 'Заранее подготовленный набор решений для разработки. Под «капотом» фреймворка — миллион нюансов: работа с файловой системой и базами данных, обработка ошибок, защита паролем и другие.',
    'тултип': 'Всплывающая подсказка, которая появляется при наведении курсора.',
    'трекать': 'Записывать рабочее время.',
    'тупач': 'Очень срочная задача, результаты работ по которой должны попасть в бранч для выкатываемой версии.',
    'поросята': 'Новички, находящиеся на испытательном сроке.',
    'котята': 'Новички, прошедшие испытательный срок.',
    'котаны': 'Сотрудники со стажем.',
    'гол': 'Цель спринта (бывает одна или несколько), которую команда берется сделать. Цель состоит из ряда задач, которые нужно выполнить, чтобы его достигнуть.',
    'дейли': 'Ежедневные короткие (от 5 до 30 минут) встречи команды с целью поделиться прогрессом по выполненным задачам за предыдущий день и озвучить план работ на текущий день.',
    'спринт': 'Заданный отрезок времени, за который нужно выполнить запланированный объем работы, чтобы в конце этого отрезка был ожидаемый результат.',
    'ветка': 'Веткой (термин git) называют полную копию проекта, в которой ведется разработка. В проекте может быть создано много веток, что позволяет работать одновременно с разными частями кода. Потом все ветки загружаются в мастер. Процесс «ответвления» иногда называют «бранчеванием», уже как раз от branch.',
    'мок': 'Макет с UX-дизайном для разработки. Несмотря на то, что слово дословно переводится как «эскиз» или «прототип», в Wrike моками называют готовые проработанные макеты с дизайном.',
    'реф': 'Схожий функционал или внешний вид, который используется для ориентира. Он служит для сравнения.',
    'спека': 'Документ с подробным описанием требований, условий и технических характеристик, как должен работать разрабатываемый функционал.',
    'комплитить': 'Завершать задачу, закрывать задачу, когда она полностью готова.',
    'матчится': 'Полное соответствие чего-либо с чем-либо. Процесс приведения к единообразию.',
    'скоуп': 'Набор фич и частей продукта, закрепленных за отдельной командой.',
    'флоу': 'Порядок действий при работе над задачей. Например, вначале задача берётся в разработку, потом проходит ревью, далее тестируется и т.д.',
    'скрам': 'Методика организации совместного рабочего процесса, в основе которой — поэтапная разработка и совершенствование продукта небольшой командой специалистов различного профиля.',
    'линтер': 'Общее нарицательное название программ, которые анализируют код и предупреждают разработчика об ошибках.',
    'ось': 'Операционная система',
    'подвал': 'То же, что и «футер». Элемент структуры страницы, который находится в нижней части и содержит служебную информацию.',
    'фронтенд': 'Клиентская часть приложения.',
    'бэкенд': 'Серверная сторона сайта или приложения, которая отвечает за его функционирование и хранение данных.',
    'регресс': 'Регрессионное тестирование (редко нерегрессионное тестирование)-это повторный запуск функциональных и нефункциональных тестов для обеспечения того, чтобы ранее разработанное и протестированное программное обеспечение по-прежнему работало после изменения.',
    'смоук': 'Дымовой тест — в тестировании программного обеспечения означает минимальный набор тестов на явные ошибки.',
    'продакшн': 'Обозначение кода для рабочей версии приложения.',
    'дропдаун': 'Выпадающее меню, то же, что и «выпадашка».',
    'деплой': 'Развёртывание, публикация рабочей версии приложения. Пример: задеплоить сайт — перенести сайт с тестового на рабочий сервер, сделать его доступным для пользователей',
    'чек-лист': 'Документ, описывающий, что необходимо протестировать в конкретной программе.',
    'тестовый сценарий': 'Документ, описывающий ступени тестирования с определением их параметров и условий.',
    'план тестирования': 'Документ, описывающий весь объем проводимых работ: описание программы, стратегию тестирования, расписание тестирования, количество тестировщиков и др.',
    'альфа-тестирование': 'Ручное тестирование продукта на ранней стадии разработки, имитирующее работу с ПО разработчиками или командой тестировщиков на стенде разработки, или непосредственно самими пользователями. Форма внутреннего приемочного тестирования, которое проводится перед бета-тестированием.',
    'бета-тестирование': 'Техника тестирования перед выпуском рабочей версии. В процессе происходит интенсивное использование почти готовой версии ПО, которое выявляет оставшиеся ошибки. Три этапа бета-тестирования (внутреннее, закрытое и открытое) позволяют выявить максимум ошибок для последующего их устранения перед непосредственным выводом ПО на потребительский рынок.',
    'валидация':'Процесс, подтверждающий соответствие готового продукта запросам конкретного потребителя, проводимый методом анализа заданных условий в ситуациях, когда проверяется фактический продукт на соответствие заданным условиям.',
    'верификация': 'В отличие от валидации проводится не во всех случаях, а только если эта проверка необходима для определенного продукта в качестве доказательства, что он соответствует неким узким характеристикам, заданным в соответствии с заданными условиями.',
    'жизненный цикл': 'Это весь отрезок времени, в течении которого программное оборудование создается и функционирует, и который заканчивается с момента вывода ПО из эксплуатации.',
    'инсталляционное тестирование': 'Выявление уровня корректности установки и готовности ее к эксплуатации в ходе тестирования в искусственной среде.',
    'конфигурационное тестирование': 'Специальное тестирование программного обеспечения при разнообразных конфигурациях системы, например, при различных конфигурациях компьютеров, драйверах, платформах и т.д.',
    'нагрузочное тестирование': 'Это подвид тестирования производительности, заключается в том, чтобы осуществлять сбор показателей и определять производительность и время отклика программного обеспечения с целью соотнесения работы системы с заявленными требованиям.',
    'нефункциональное тестирование': 'Тестирование характеристик, не отвечающих за функциональность системы, характеристики определяются нефункциональными требованиями.',
    'приемочное тестирование': 'Вид тестирования, целью которого является проверка программного обеспечения в понимании конечного пользователя.',
    'санитарное тестирование': 'Тестирование, в котором проверяются точечные функции программного обеспечения.',
    'серьезность': 'Степень влияния бага (ошибки) на работоспособность программного обеспечения.',
    'спецификация': 'Детальное описание того, как должно работать программное обеспечение.',
    'cравнительное тестирование': 'Сравнение плюсов и минусов программного обеспечении по отношению к ближайшим конкурентам.',
    'стрессовое тестирование': 'Проверка работоспособности продукта с большей нагрузкой, чем при нагрузочном тестировании.',
    'таблица принятия решений': 'Инструмент, целью которого является упорядочение бизнес-требований к программному обеспечению.',
    'тест-кейс': 'Это артефакт тестирования, заключающийся в том, чтобы выполнить определенные действия для проверки соответствия программного обеспечения ожидаемому результату.',
    'тест-план': 'Документ тестирования, в котором перечислен объем работ по тестированию.',
    'функциональное тестирование': 'Тестирование программного обеспечения с целью проверки его работоспособности.',
    'приоритет': 'Это специальный атрибут, указывающий на скорость устранения бага (ошибки), очередность задачи по исправлению бага (ошибки).',
    'артефакт': 'Документ, используемый в процессе тестирования.',
    'баг-репорт': 'Документ, который содержит всю информацию о дефекте.',
    'спек': 'Детальное описание технических характеристик программного продукта.',
    'асайнить': 'Поручить задачку или часть работы.',
    'аттачить': 'Добавить к сообщению или письму фотографию/документ.',
    'патч': 'Экземпляр ПО, являющийся обновлением, выпущенным для исправления ошибок, обнаруженных в версии или релизе ПО. В состав патча входит исполняемый код и описание исправленных в патче ошибок. Патч может распространяться без документации.',
    'тестовое покрытие': 'Мера полноты тестирования для определенной стратегии. Степень, до которой с помощью контрольных примеров проверяют требования к системе или программному продукту.',
    'ролбек': 'Откат к ранее развернутой версии.',
    'стейджинг': 'Среда, идентичная продакшн-окружению, но предназначенная для тестирования.',
    'энви': 'Энвайронмент, окружение — компьютерная система или набор систем, в которых развертывается и выполняется компьютерная программа или программный компонент.',
    'майлстоун': 'Запланированная дата окончания работ по выборочным задачам. Проставление таких «дат» позволяет не сбиваться с графика и отслеживать процесс работы и понимания выполнения целей.',
    'сторя': 'Корневая задача с описанием требований для разработки, она содержит в себе подзадачи, назначенные на разработчиков разных должностей. Это точка входа при разработке какого-либо функционала.',
    'ребут': 'Просто перезагрузка. Если Вас просят «ребутнуться», то вам просто нужно перезагрузить компьютер.',
    'девопс': 'Инженер, который собирает воедино все части проекта.',
    'ламер': 'Начинающий специалист, который считает себя продвинутым экспертом, хотя это не так.',
    'пио': 'Product Owner — владелец продукта. Организует процессы в команде разработки, не отвлекается на маркетинг и продажи. Стыкует пожелания заказчика с возможностями разработки.',
    'пиэм': 'Product Manager — менеджер продукта.Взаимодействует с заказчиком, выясняет его потребности и желания, доносит их до команды.',
    'проджект': 'Project Manager — менеджер проекта. Руководит командой, следит за бюджетом, отвечает за реализацию проекта в срок и его соответствие требованиям заказчика.',
    'секопс': 'Security Operations — операции по обеспечению безопасности.Cистемный администратор по информационной безопасности. Отвечает за безопасность и защиту сетевых систем, приложений и данных.',
    'варез': 'Программа, которую распространяют незаконным путем, нарушают интеллектуальные права владельца.',
    'виджет': 'Программа, с помощью которой на экран выводится полезная информация в виде картинок. К наиболее широко распространенным виджетам относятся новостные ленты, часы, индикаторы погоды, настольные игры. Веб-виджет - это виджет, встраиваемый в веб-страницу сайта.',
    'гайд': 'Инструкция',
    'домен': 'Часть адреса сайта. Домены обозначают принадлежность стране, тематику, разделы сайта.',
    'компилить': 'Собрать код воедино.',
    'плагин': 'Дополнение к готовой программе, которое улучшает ее работу.',
    'прокси': 'Промежуточный сервер, посредник между пользователем и интернет-ресурсом. Помогает скрыть IP-адрес, обойти запрет на доступ к соцсетям на рабочем месте, подключиться к недоступным в вашей стране сайтам.',
    'попандер': 'Агрессивная реклама, которая выглядит как открывающееся окно или плавающий баннер. Перекрывает пользователю обзор на странице сайта или в приложении.',
    'редирект': 'Переадресация на другую страницу.',
    'ручка': 'Сообщение от сервера в ответ на какое-то событие, бэкенд-термин.',
    'хендлер': 'Сообщение от сервера в ответ на какое-то событие, бэкенд-термин.',
    'эндпойнт': 'Сообщение от сервера в ответ на какое-то событие, бэкенд-термин.',
    'метод': 'Сообщение от сервера в ответ на какое-то событие, бэкенд-термин.',
    'секвентальный': 'Последовательный.',
    'софт': 'Software — программное обеспечение.',
    'транслит': 'Замена букв одного алфавита похожими знаками другого.',
    'фавикон': 'Значок интернет-ресурса. Показывается во вкладке браузера рядом с названием сайта.',
    'фейл': 'Неудача. Негативная оценка деятельности.',
    'хедер': 'Блок в верхней части сайта, первый элемент, который видит пользователь. Присутствует на всех страницах.',
    'хинт': 'Всплывающая подсказка.',
    'хит': '1.Запрос графического файла с веб-сервера, который содержит данные о действиях пользователя на сайте. Необходим для веб-аналитики.2. Общее количество входов посетителей на сайт.',
    'хост': '1. Сервер, который предоставляет возможность разместить информацию. 2. Уникальный IP-адрес.3. Уникальное посещение пользователем страницы в интернете.',
    'юзабилити': 'Характеристика, которая показывает, насколько удобно пользоваться интерфейсом программы или приложения.',
    'аджайл': 'Ценности, принципы и правила взаимодействия команды для быстрой разработки программного обеспечения.',
    'дод': 'Список условий. Если их выполнить, вы достигнете цели.',
    'скрам': 'методология гибкой командной работы, в которой быстрая реакция на изменения важнее формальной документации, инструкций. Слово «гибкая» означает способность быстро меняться без потери качества продукта.',
    'валидный': 'Правильный, корректный, работающий. Подтверждение, что данные законные, правильные.',
    'драйвер': 'Программное обеспечение, с помощью которого операционная система взаимодействует с устройствами: мышкой, сканером, видеокартой и другими.',
    'инпут': '1. Входящая информация.2. Форма ввода данных в приложении или на сайте.',
    'эскалировать': 'Привлечь внимание, поднять проблему, которую не можете решить самостоятельно .',
    'анрег': 'Незарегистрированный.',
    'cпам': 'Ненужная информация в большом количестве.',
    'фишинг': 'Действия, с помощью которых мошенники получают доступ к логинам и паролям.',
    'хомяк': 'Страница, которую браузер открывает сразу после загрузки.',
    'вайп': '1. Безвозвратное удаление данных.2. Многократный постинг одинаковых сообщений для спама, троллинга.',
    'вайпить': '1. Безвозвратное удаление данных.2. Многократный постинг одинаковых сообщений для спама, троллинга.',
    'дел-пост': 'Удаленное сообщение',
    'маздай': 'Название Windows, которое используют программисты, если им не нравится эта операционная система.',
    'ослик': 'Браузеры компании Microsoft Internet Explorer.',
    'флуд': 'Сообщения на посторонние, отвлекающие темы.',
    'холивар': 'Яростная дискуссия на форуме или в чатах, чаще бессмысленная, но иногда в ходе спора находится и полезная информация.',
    'куки': 'это файлы с информацией, полученной при посещении веб-ресурса. Информация хранится на жестком диске вашего компьютера, а в ней отображаются ваши предпочтения, наиболее часто посещаемые тематики, логины и пароли. Каждый раз, когда вы посещаете сайт, который использует куки, то устройство отправляет эти данные на сервер для того, чтобы правильно опознать вас среди других пользователей.',
    'кэш': 'это память с большей скоростью доступа, предназначенная для ускорения обращения к данным, содержащимся постоянно в памяти с меньшей скоростью доступа (далее «основная память»)',
    'урл': ' URL это лишь адрес, который выдан уникальному ресурсу в интернете. В теории, каждый корректный URL ведёт на уникальный ресурс. Такими ресурсами могут быть HTML-страница, CSS-файл, изображение и т.д. На практике, существуют некоторые исключения, когда, например, URL ведёт на ресурс, который больше не существует или который был перемещён.',
    'курл': 'это утилита командной строки, которая позволяет выполнять HTTP-запросы с различными параметрами и методами. Вместо того, чтобы переходить к веб-ресурсам в адресной строке браузера, можно использовать командную строку, чтобы получить те же ресурсы, извлеченные в виде текста.',
    'белый ящик': 'предполагает собой работу с «открытой» системой, где ее внутренняя структура, а также устройство и реализация заранее известны тестировщику на момент старта тестов.Тестировщик имеет доступ к реализованному коду, тестовой документации, изучает их и получает всю необходимую информацию, как должен работать продукт.',
    'серый ящик': ' это комбинация тестирования белого ящика и тестирования черного ящика. Целью этого тестирования является поиск дефектов, если таковые имеются, из-за неправильной структуры или неправильного использования приложений.',
    'черный ящик': 'стратегия (метод) тестирования функционального поведения объекта (программы, системы) с точки зрения внешнего мира, при котором не используется знание о внутреннем устройстве (коде) тестируемого объекта.',
    'классы эквивалентности': 'Классом эквивалентности называется набор данных, который запускает одни и те же модули и должен приводить к одним и тем же результатам.',
    'граничные значения': 'Граничными условиями считаются ближайшие значения, стоящие с обеих сторон крайних значений, определяющих границы класса. При тестировании граничных условий из тестируемого диапазона выбираются следующие значения: минимальное значение (min), значение, на одно больше минимального (min+), значение, на одно меньше максимального (max-), и максимальное значение (max).',
    'атрибут': 'Переменная, описание которой создает программист при создании класса. Все данные объекта хранятся в его полях. Доступ к полям осуществляется по их имени. Обычно тип данных каждого поля задаётся в описании класса.',
    'селектор': 'Это часть CSS-правила, которая сообщает браузеру, к какому элементу (или элементам) веб-страницы будет применён стиль.',
    'аутентификация': 'средство защиты, устанавливающее подлинность лица, получающего доступ к автоматизированной системе, путем сопоставления сообщенного им идентификатора и предъявленного подтверждающего фактора.',
    'авторизация': 'предоставление определённому лицу или группе лиц прав на выполнение определённых действий; а также процесс проверки (подтверждения) данных прав при попытке выполнения этих действий',
    'эмулятор': 'эмулирует программное и аппаратное обеспечение',
    'симулятор': 'имитирует только программное обеспечение',
    'тмс': 'Система управления тестированием (Test Management System, TMS) — это важная составляющая процесса, которая объединяет все активности и даёт доступ к отчетности по всему процессу. Такая система нужна тем, кто понимает ценность тестирования, хочет им управлять из единого центра, а не собирать множество разномастных отчётов.',
    'сьют': 'Это набор тест кейсов объединенных некоей логикой (по модулям системы, по пользовательским сценариям, по уровням тестирования.',
    'ран': 'это процесс/результат выполнения теста по шагам, описанным в плане',
    'рест': ' (REST (от англ. Representational State Transfer — «передача репрезентативного состояния» или «передача „самоописываемого“ состояния») — архитектурный стиль взаимодействия компонентов распределённого приложения в сети. Другими словами, REST — это набор правил того, как программисту организовать написание кода серверного приложения, чтобы все системы легко обменивались данными и приложение можно было масштабировать.',
    'апи': 'API (Application Programming Interface или интерфейс программирования приложений) — это совокупность инструментов и функций в виде интерфейса для создания новых приложений, благодаря которому одна программа будет взаимодействовать с другой. Это позволяет разработчикам расширять функциональность своего продукта и связывать его с другими.',
    'соап': 'SOAP — это протокол, по которому веб-сервисы взаимодействуют друг с другом или с клиентами. Название происходит от сокращения Simple Object Access Protocol («простой протокол доступа к объектам»). SOAP API — это веб-сервис, использующий протокол SOAP для обмена сообщениями между серверами и клиентами. При этом сообщения должны быть написаны на языке XML в соответствии со строгими стандартами, иначе сервер вернет ошибку.',
    'гет': 'Метод GET передает параметр запроса в строке URL.апрос GET может передавать только ограниченный объем данных.',
    'пост': 'Позволяет отправить данные на сервер. Поддерживает отправку различных типов файлов, среди которых текст, PDF-документы и другие типы данных в двоичном виде. Обычно метод POST используется при отправке информации (например, заполненной формы логина) и загрузке данных на веб-сайт, таких как изображения и документы.',
    'пут': 'Используется для создания (размещения) новых ресурсов на сервере. Если на сервере данный метод разрешен без надлежащего контроля, то это может привести к серьезным проблемам безопасности.',
    'делит': 'Позволяет удалить существующие ресурсы на сервере.',
    'бургер': 'это иконка скрытого меню на сайте или в мобильном приложении. При нажатии на неё, открывается уже полное меню с разделами, находящимися друг над другом, что, собственно, и формирует принцип бутерброда.',
    'аккордеон': 'элемент интерфейса состоящий из заголовков и скрываемого и открываемого контента.',
    'слайдер': 'переключатель изображений (или другого контента) работающий автоматически или вручную.',
    'поп-ап': 'небольшое всплывающее окно в углу экрана.',
    'модальное окно': ' разновидность всплывающего окна. Оно появляется на большую часть экрана и блокирует работу с остальным сайтом. Это может быть форма обратной связи, или просмотр фотографий в вк и фейсбуке.',
    'превью': 'изображение или часть другого контента, уменьшенная в размере. При нажатии на превью открывается исходный размер контента, отображаемого в превью.',
    'бордер': 'обводка элемента. Бывает solid (цельной), dashed (линиями) и dotted (точками).',
    'тултип': 'подсказка, всплывающая при наведении на элемент.',
    'курсор поинтер': 'тип курсора в виде руки с вытянутым указательным пальцем. Обычно появляется при наведении на ссылку.',
    'маска': 'это значения, указывающие формат допустимых значений входных данных в поле.',
    'хлебные крошки': 'это цепочки навигации, которые отображают путь пользователя от корня сайта до текущей страницы.'
    }
# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        
        bot.send_message(
            chat_id=message.chat.id,
            text='❌Мне жаль, но я этого ещё не знаю💭'
            ),
        # выходим из функции
        return
        
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'✅Рад тебе помочь!👍🏻',
    )

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
