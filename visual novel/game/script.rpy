﻿define m = Character('mike', color="#df30e5")
define o = Character('owner', color="#1eecec")
define s = Character('sidney', color="#a7fc00")

image computer = Movie(play="images/computer.webm", loop=True)

label main_menu:
    image begin = Movie(play="images/begin.webm", loop=True)
    show begin
    jump main_menu_screen

label start:

    show computer

    s "Я Сидни Харпер. Когда мне было чуть за 20, я работала в крупной фирме в своём городе. Работа, конечно, хорошо оплачиваемая, но в ущерб моему душевному спокойствию."
    s "Поэтому один из моих друзей по колледжу — Майк — предложил нам съездить на выходные в сельскую местность штата Вермонт."
    s "Это звучало как отличный перерыв от работы. План был прост: мы арендуем небольшой домик, заканчиваем смену пораньше в пятницу, уезжаем и возвращаемся в понедельник. Позже Майк заехал за мной…"
    hide computer

    scene parking 
    with fade
    show mike1
    m "Приятно, если в дороге у меня будет компания. Ты можешь просто забросить свои вещи на заднее сиденье, и мы отправимся в путь." 
    scene house1
    m "Какое замечательное место! Я знал, что могу на тебя положиться." 
    s "Мне приятно, давай осмотрим дом."

 # Переход в комнату с силуэтом     
    scene house2
    with fade
    show owner1    
    o "Привет, вы здесь!" 
    s "Вы напугали нас! Кто вы?" 
    o "Я не хотел. Добро пожаловать в мой милый дом. Я искал свою кошку и вспомнил, что телевизор сломался."
    o "Просто подумал запустить его снова. Последние жильцы оставили плохой отзыв о нём, но я уже собираюсь уходить. Кстати, какое имя было указано при бронировании?" 
    s "Это Сидни." 
    hide owner1
    show owner2
    o "А, Сидни, точно."
 
    # Хозяин уходит 
    hide owner2
    show mike1    
    m "Мне кажется, он действительно очень странный." 
    s "Ты прав." 
    s "Ладно, я чувствую себя уставшей и пойду спать." 
    m "Я тоже." 

    # Переход к ночи, 2 этаж корридор    
    scene corridor 
    with fade    
    "Ночь. Я просыпаюсь от шума." 
    s "Ты всё ещё не спишь? Я слышу шум на первом этаже."
    show mike1
    m "Давай спустимся и напишем хозяину, вдруг это его кошка."

    # Переход вниз, встреча с хозяином
    scene house2 
    with fade    
    show mike3
    s "Это правда его кошка, я напишу ему."    
    scene display
    with fade    
    m "Хорошо."

    # Хозяин появляется снова    
    hide mike3 
    scene house2    
    show owner1    
    o "Что вы здесь делаете?" 
    hide owner1    
    show mike3
    m "Наверное, эта кошка ваша."    
    hide mike3
    show owner3    
    o"Да, моя. На вашем месте я бы не беспокоился об этом." 
    o"Погода такого типа приносит самых разных людей. Не все из них знают, когда нужно держаться подальше."    
    hide owner3
    scene answer
    with fade   
    s "Что?!"
    scene house2
    show mike2        
    s "Он не хозяин дома!" 
    hide mike2    
    show owner1
    o "С вами всё хорошо?"    
    m "Нет! Вы не Рик! Кто вы? Уходите сейчас же!" 
    hide owner1    
    show owner2
    o"Что вы сейчас сказали?"    
    # Динамика действия        
    scene corridor 
    s "Быстрее, на второй этаж!"
    # Переход к комнате Сидни         
    scene loft 
    show mike2        
    m "Запирай дверь!" 

    # Темнеет экран     
    scene dark     
    "Мужчина выбивает дверь и начинает обыскивать комнату. Вы слышите его шаги приближаются к вам..." 

    return  # Завершает игру
   