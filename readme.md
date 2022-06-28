# Movies and actors

## 영화와 영화 배우

요즘 뜨고 있는 영화 순위를 살펴보고,<br/>
인기가 많은 영화 배우들의 선호도를 공유해요!<br/>

시연 영상: https://youtu.be/juuW8lEicJc<br/>

![screen_shot](/static/pic.PNG)

mongoDB에 init_db.py으로 현재 영화 및 배우 정보를 저장합니다. <br/><br/>
app.py를 실행하면 왼쪽에는 현재 영화 순위대로 영화 정보가 정렬이 되고, <br/> 오른쪽에는 현재 배우 순위대로 배우 정보가 정렬이 됩니다. <br/><br/>
정렬된 영화 순위와 배우 순위의 각 이름을 누르면 해당 정보를 알 수 있는 페이지가 열립니다.<br/><br/>
또한, 정렬된 배우들은 각 사용자가 좋아요 혹은 제외 버튼을 누를 수 있으며, <br/> 좋아요 버튼을 누른 수는 누적되고 제외 버튼을 누르면 mongoDB에 저장된 해당 배우의 데이터가 사라집니다.

## 추가한 CSS 자료

[Bulma](https://bulma.io/)

- 만들어진 스타일 코드를 가져옵니다.

[Fontawesome](https://fontawesome.com/)

- 아이콘이 필요한 경우 사용합니다.

---

## 추가한 JavaScript 라이브러리

[JQuery](https://cdnjs.com/libraries/lodash.js)

- 편리한 Javascript를 미리 작성해둔 라이브러리를 사용합니다.

---

## 추가한 Python 라이브러리(서버 관리)

[mongoDB](https://getbootstrap.com/)

- 데이터를 저장하고 가져와 사용합니다.

[Flask](https://cdnjs.com/libraries/lodash.js)

- 서버를 구동시키는 편한 코드 모음을 가져와 사용합니다.

[bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)

- 웹 페이지의 정보를 쉽게 스크랩할 수 있도록 기능을 제공하는 라이브러리를 사용합니다.
