<a href="https://github.com/atknin/MINAT/blob/master/Git_instruction.md" align="absmiddle"/> 1. [GITHUD инструкция]</a>
 

 ### Для начала работы:

1) Активировать  virtualenv;

```	
source myenv/bin/activate
```	

2) работаем с папкой:

```	
TESTproject
```	

3) Внесли изменения, после:

```	
### В) Допустим Вы сделали какие - то изменения, теперь этим нужно поделиться:

Добавить все файлы для отслеживания git'ом.
```
git add .
```

 Проверить состояние (до и после add) можно командой

```
git status
```

Теперь делаем коммит (коментарий к Вашем изменениям):

```
git commit -m "Add project"
```

Отправляем:

```
git push
```
```	