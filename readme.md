# Django events Project
## Описание сервиса
Данный сервис создан для организации спортивных мероприятий двух видов: марафоны и более официальные соревнования. 
Для записи на марафон необходимо лишь указать текст примечания, в то время как для отправки отклика на соревнование 
нужно заполнить форму, включающую в себя такие поля, как заголовок отклика, основной текст, спортивную команду 
участника, его разряд, а также приложить файл с документами, необходимыми для участия в данном соревновании. Спортивные 
мероприятия могут быть занесены в систему только пользовтелями, зарегистрировавшимися в качестве организаторов. 
Пользователи, зарегестрированные в роли участников могут лишь отправлять заявки и отклики на спортивные мероприятия. 
Все заявки и отклики по каждому мероприятию видны организатору данного события с данными, которые участник указал 
в анкете к заявке или отклику. 

## Приступая к работе
1. Чтобы приступить к работе с сервисом, необходимо загрузить его в .zip формате из 
[git-репозитория](https://github.com/abakums/django_events). Распакуйте скачанный файл в удобную для вас папку 
2. Откройте командную строку и перейдите в папку, в которую произвели распаковку. 
3. Выполните запуск сервиса, предварительно загрузив docker на свой локальный компьютер, с помощью единственной 
команды в командной строке из папки, содержащей файлы проекта:

```console
    docker-compose up
```


## Работа с сервисом
1. После запуска сервиса перейдите в браузере на [начальную страницу](http://127.0.0.1:8000/)
2. Это направит Вас на главную страницу, где доступны кнопки "Войти" и "Зарегистрироваться". Если у Вас нет учетной 
записи - создайте ее, заполнив данные формы после нажатия кнопки "Зарегистрироваться" (Во время регистрации доступны 
две роли - Организатор и Участник). Если аккаунт уже есть - перейдтие к форме входа в систему, нажав на кнопку "Войти".
3. После регистрации или авторизации Вы попадете на станицу со всеми доступными мероприятиями.
4. Если Вы авторизованы как организатор, то Вы можете создать новое мероприятие нажатием на соответствующую кнопку.
После создания очередного мероприятия, Вы можете перейти к списку организованных Вами мероприятий, где есть 
возможность нажать на заголовок определенного события для перехода к заявкам и откликам на него. Кроме того, после 
отправки отклика или заявки на Ваше мероприятие, Вы автоматически получаете уведомление на указанную при регистрации 
электронную почту. 
5. Если Вы авторизованы как Участник, то Вы можете создать новый отклик или заявку, нажав на соответствующую кнопку под
нужным Вам мероприятием, после чего заполнить форму. После отправки заявки или отклика Вы можете ознакомиться с ними,
нажав соответственно на кнопку "Мои заявки" или "Мои отклики". 
6. В списке откликов у каждой позиции есть такое поле как документ, где содержится ссылка на скачивание приложенного к 
данному отклику документа. После нажатия на кнопку "Документ" произойдет его скачивание. 


## Контакты
По всем вопросам можно написать на почту abakumovs882@gmail.com
