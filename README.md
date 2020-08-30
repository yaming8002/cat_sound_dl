### 目錄  

[model使用範例](#use_example)  
* [範例建置](#example_build)  
* [範例顯示](#example_show)  


[model的建置](#creat_model)  
* [前處理](#prework)  
* [練習model](#practice)  

<a name="use_example"/>

# 使用案例

作業系統：windows10

程式語言：python3.8

<a name="example_build"/>

## 範例建置

系統是使用Django建置網頁服務

1. 導入API套件

建議在venv中建置
```
 pip install -r requirements.txt
```

2. 建立Django

使用命令提示字元，指定到特定的資料夾位置，輸入
```
django-admin startproject cat_sound
\\ 建立名為cat_sound的Django資料夾模板
```

3. 將本範例中的cat_vedio資料夾移入cat_sound中

cat_vedio的內容如下：
![](https://i.imgur.com/OvyJueX.png)

4. sound_model.zip.001~004解壓縮，放入cat_vedio資料夾內
![](https://i.imgur.com/2NarLZq.png)

5. 到.\cat_sound\cat_sound\settings.py中的INSTALLED_APPS，加入'cat_vedio'

如下圖
![](https://i.imgur.com/h9a1DL8.png)

6. 到 .\cat_sound\cat_sound\urls.py修改成以下內容
```
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from cat_vedio.views import cat_view
from cat_vedio.views import data_back


urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/cat_vedio/view
    url(r'^cat_vedio/', include('cat_vedio.urls')),
]

```

8. 執行django
```
python cat_sound\manage.py runserver
```

<a name="example_show"/>

## 範例顯示

在啟動django後，使用chrome輸入
`http://127.0.0.1:8000/cat_vedio/view`

網頁顯示如下：
![](https://i.imgur.com/3A5zXaf.png)

輸入貓咪影片的網址，例如
`https://www.youtube.com/watch?v=DXUAyRRkI6k`

點擊播放，可呈現

![](https://i.imgur.com/HD9b6ag.png)
判斷貓咪目前的狀態


<a name="creat_model"/>

# model的建置

作業系統：windows10

程式語言：python3.8

<a name="prework"/>

## 前處理


<a name="practice"/>

## 練習model
