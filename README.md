# weather_telegram_bot

<div id="header" align="center">
<img src="https://img.icons8.com/color/512/telegram-app.png"  width="auto" height ="auto/>        
                                                                                    
</div>                                                                                                                                                                                                                                                                                                                                         
<div id="header" align="center">
  
  <hr/>
   <img src ="https://img.icons8.com/color/512/bot.png" width="40" height =35">
  <img src="https://img.shields.io/badge/platform-linux--64%20%7C%20win--32%20%7C%20osx--64%20%7C%20win--64-lightgreen" width="auto" height ="auto"/>
  <img src="https://img.shields.io/badge/python-v3.7-green" />    
  <img src = "https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=green" width="80" height =25" />
  <img src = "https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=blue   wight="80" height =20" "/>


</div>

EN
==
BASIC
--
Telegram bot that receives a city from the user, and then checks whether such a city exists in **_all.json** , if so, it searches Google for the weather in this city.
>![image](https://user-images.githubusercontent.com/79650307/211866412-0b367a75-ca17-49aa-a95a-588f3b01fb0c.png)

FUNCTIONS
--
1. Find out the weather in a certain city through Google
2. Get more information by typing /help
3. Get detailed information about who launched the bot: message, id , first name, last name and nickname of the Telegram user

FOR EXAMPLE
--
We are looking for a bot in Telegram with the name @weather_by_cities_bot or <a href="https://web.telegram.org/k/#@weather_by_cities_bot">weather_by_cities_bot</a>

Presses start, we write the city,
we get the answer:
>
>![image](https://user-images.githubusercontent.com/79650307/211865688-af02d653-0eaa-4870-bc02-d70e1065d144.png)



ERROR PROCESSING
--
Since we have a local database of cities (this is _all.json - stores about 16,000 cities), the bot checks the user's request with the database.
If there is no such city -
an error and the request to Google is cancelled:
>
>![image](https://user-images.githubusercontent.com/79650307/211865866-28196f29-b7d2-40cb-bbab-4c4692ef8311.png)


SPECIAL ERROR
--
Sometimes the user may enter a little-known city - Bug, which IS in the **_all.json** database, but Google will not be able to find the weather in this city,
since there is no data when parsing the Google page:
```{python}<space>{if user_city in cities:
        print("is")
        site = ("https://www.google.com/search?q=weather+at+"+str(user_city.split())+"&hl=en&sxsrf=ALiCzsaDFVg-
mJ46G9JY1k2woiVs07EDkw%3A1671210270761&source=hp&ei=HqWcY4jKLOGGwPAP9cKtgAo&iflsig=AJiK0e8AAAAAY5yzLqFF0IHK5muOVlySe3enRck5K4dR&ved=0ahUKEwiI0aC0z_77AhVhAxAIHXVhC6AQ4dUDCAc&uact=5&oq=погода+в+моске&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEIMBEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6B
-wiz")
        headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
        full_page = requests.get(site, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span",{"class":"wob_t",
"class":"q8U8x"})
        convert_1 = soup.findAll("span",{ "id":"wob_dc"})
        d=""
        for temperature in convert :
            d+=temperature.getText()+" "
        for weah_r in convert_1:
            d+=weah_r.getText()
        answer = "Weather in the city: "+str(user_city)+" "+str(d)}
  ```


Consequently:
>![image](https://user-images.githubusercontent.com/79650307/211866925-7fb18936-348e-4c11-81ee-11e66b3952ea.png)



FOR USE
--
If you want to use a bot: download both files, create a new bot in Telegram at <a href="https://web.telegram.org/k/#@BotFather">BotPather</a> and copy the token into the code, save , start and you can write to your bot🦎

RU
==

ОСНОВЫ
--
Telegram-бот, который получает город от пользователя, а затем проверяет, существует ли такой город в **_all.json** , если да, то ищет в Google погоду в этом городе.
>![изображение](https://user-images.githubusercontent.com/79650307/211866412-0b367a75-ca17-49aa-a95a-588f3b01fb0c.png)

ФУНКЦИИ
--
1. Узнать погоду в конкретном городе с помощью Google
2. Получите дополнительную информацию, набрав /help
3. Получить подробную информацию о том, кто запустил бота: сообщение, id, имя, фамилию и никнейм пользователя Telegram

НАПРИМЕР
--
Ищем бота в Telegram с именем @weather_by_cities_bot или <a href="https://web.telegram.org/k/#@weather_by_cities_bot">weather_by_cities_bot</a>

Нажимаем старт, пишем город, получаем ответ:
>
>![изображение](https://user-images.githubusercontent.com/79650307/211865688-af02d653-0eaa-4870-bc02-d70e1065d144.png)



ОБРАБОТКА ОШИБКИ
--
Так как у нас есть локальная база городов (это _all.json — хранит около 16000 городов),
затем бот сверяет запрос пользователя с базой данных.
Если такого города нет - ошибка ; запрос в гугл отменяется:
>
>![изображение](https://user-images.githubusercontent.com/79650307/211865866-28196f29-b7d2-40cb-bbab-4c4692ef8311.png)


СПЕЦИФИЧЕСКАЯ ОШИБКА
--
Иногда пользователь может ввести малоизвестный город - Буг,
который находится в базе данных **_all.json** , но при этом Google не сможет найти погоду в этом городе, так как нет данных при парсинге страницы Google:

```{python}<пробел>{if user_city in cities:
        print("есть")
        site  = ("https://www.google.com/search?q=погода+в+"+str(user_city.split())+"&hl=ru&sxsrf=ALiCzsaDFVg-mJ46G9JY1k2woiVs07EDkw%3A1671210270761&source=hp&ei=HqWcY4jKLOGGwPAP9cKtgAo&iflsig=AJiK0e8AAAAAY5yzLqFF0IHK5muOVlySe3enRck5K4dR&ved=0ahUKEwiI0aC0z_77AhVhAxAIHXVhC6AQ4dUDCAc&uact=5&oq=погода+в+моске&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEIMBEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6BAgjECc6CwgAEIAEELEDEIMBOgUIABCABDoICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgwIIxAnEJ0CEEYQgAI6DggAEIAEELEDEIMBEMkDUABYpBBgzRFoAHAAeACAAeEBiAGvDJIBBTcuNi4xmAEAoAEB&sclient=gws-wiz")
        headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
        full_page = requests.get(site, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span",{"class":"wob_t","class":"q8U8x"})
        convert_1 = soup.findAll("span",{ "id":"wob_dc"})
        d = ""
        for temperature in convert :
            d+=temperature.getText()+" "
        for weah_r in convert_1:
            d+=weah_r.getText()
        answer  = "Погода в городе: "+str(user_city)+" "+str(d)}
   ```

Следовательно:
>![изображение](https://user-images.githubusercontent.com/79650307/211866925-7fb18936-348e-4c11-81ee-11e66b3952ea.png)



ДЛЯ ИСПОЛЬЗОВАНИЯ
--
Если вы хотите использовать бота: скачайте оба файла, создайте нового бота в Telegram по адресу <a href="https://web.telegram.org/k/#@BotFather">BotPather</a> и скопируйте токен в код, сохраните, запускаем и можно писать своему боту🦎.

