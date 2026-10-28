# Режиссёрский пульт

Памятка Telegram-канала [«дизайн ремесленник»](https://t.me/design_remeslo) для видео в нейросетях: шаблоны промтов, модели Higgsfield, движения камеры и правила из реальных генераций, с поиском и фильтрами по разделам. Тёмная пара к [«Закромам ремесленника»](https://a-revazyan.github.io/zakroma-remeslennika/).

Модели и приёмы пересказаны своими словами по гайдам Higgsfield и курсу [Higgsfield Academy](https://higgsfield.ai/academy); источник указан в каждой карточке.

## Как устроено

- `index.html` — сама страница, без сборки и зависимостей (шрифт Inter подключается с Google Fonts).
- `data.json` — все шаблоны, модели, движения камеры и правила. Страница берёт данные отсюда.
- Копия данных также зашита в `index.html` для мгновенной первой отрисовки; при открытии страница подтягивает свежий `data.json`.

## Ссылки на карточку и тему

- `#templates/t07` — открыть шаблон (так же `#models/g01`, `#moves/m01`);
- `#rules/Звук` — правила одной темы.

## Как добавить запись

Открой `data.json`, добавь объект в нужный массив и закоммить:

- `templates`: `id`, `cat` (одна из `tcats`), `status` («Проверено», «Из гайда», «Заготовка»), `name`, `models`, `purpose`, `howto`, `notes`, `body`, по желанию `example` и `source`;
- `models`: `id`, `cat` (одна из `gcats`), `status`, `name`, `models`, `when`, `limits`, `rules` (массив строк), `ours`, `source`, `url`;
- `moves`: `id`, `type` (`push`, `arc`, `crane`, `track`, `fly`…), `status`, `name`, `sees`, `phrase`, `fov`, `speed`, `style`, `notes`;
- `rules`: `id`, `code`, `cat` (одна из `rcats`), `text`, `why`.

Поля в [квадратных скобках] в шаблонах и фразах подсвечиваются как места, которые меняют под сцену.
