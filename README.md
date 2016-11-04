# <a href="http://maxsite.org/page/how-to-put-your-project-on-github-com" align="absmiddle"/> [ИСТОЧНИК]</a>

2 СПОСОБА ВЫЛОЖИТЬ ПРОЕКТ: 

### А) Если папка на компьютере уже существует, осталось только выложить:

заходим в папку
```	
git init
git add .
git commit -m "Init"
```

Для связи с GitHub'ом следует указать удаленный репозиторий:

```
git remote add origin https://github.com/USER/demo.git
git push -u origin master
```

Этот код указывает адрес удаленного и отправляет все изменения на гитхабовский сервер. Если мы зайдем на страницу репозитория на гитхабе, то также увидим свой проект.


### Б) Папка на Github, ее нужно добавить на компьютер:

```
git clone https://github.com/USER/demo.git
```

Ссылку также можно скопировать со страницы репозитория в поле «HTTPS clone URL».

### В) Допустим Вы сделали какие - то изменения, теперь этим нужно поделиться:

Добавить все файлы для отслеживания git'ом.
```
git add .
```

 Проверить состояние (до и после add) можно командой

```
git add .
```