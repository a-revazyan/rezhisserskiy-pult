# Режиссёрский пульт

Памятка Telegram-канала [«дизайн ремесленник»](https://t.me/design_remeslo) для видео в нейросетях: шаблоны промтов, модели Higgsfield, движения камеры, схемы света и правила из реальных генераций, с поиском и фильтрами по разделам. Тёмная пара к [«Закромам ремесленника»](https://a-revazyan.github.io/zakroma-remeslennika/).

Модели и приёмы пересказаны своими словами по гайдам Higgsfield и курсу [Higgsfield Academy](https://higgsfield.ai/academy); источник указан в каждой карточке.

## Как устроено

- `index.html` — сама страница, без сборки и зависимостей (шрифт Inter подключается с Google Fonts).
- `data.json` — все шаблоны, модели, движения камеры, схемы света и правила. Страница берёт данные отсюда.
- `tools/light.json` — исходник раздела «Свет»: 34 схемы с описанием, фразой для блока LIGHTING и параметрами схемы `d` (источники `lights` с углом `az`, высотой `el`, цветом `c`, жёсткостью `h`; фон `bg`, особые эффекты `fx`). Сборка переносит его в `data.json`.
- Копия данных также зашита в `index.html` для мгновенной первой отрисовки; при открытии страница подтягивает свежий `data.json`.
- `skills/` — наши скиллы для Claude: папка со `SKILL.md` и готовый архив `<имя>.zip` для загрузки в Claude. Описания скиллов и ссылки на чужих авторов — в `SKILLS` в `tools/build_public.py`. Архив пересобрать: `cd skills && zip -r -X <имя>.zip <имя>`.
- `img/` — кадры и картинки из собственных генераций автора (WebP). Запись ссылается на них полем `img`: `[{"src": "img/имя.webp", "cap": "подпись"}]`; в правилах можно пометить пару «как не надо / как надо» флагами `"bad": true` и `"good": true`.

## Ссылки на карточку и тему

- `#templates/t07` — открыть шаблон (так же `#models/g01`, `#moves/m01`, `#light/l03`);
- `#rules/Звук` — правила одной темы (так же `#templates/Листы`);
- `#start` — блок «С чего начать», `#glossary` — словарь терминов.

## Как добавить запись

Открой `data.json`, добавь объект в нужный массив и закоммить:

- `templates`: `id`, `cat` (одна из `tcats`), `status` («Проверено», «Из гайда», «Заготовка»), `name`, `models`, `purpose`, `howto`, `notes`, `body`, по желанию `example` и `source`;
- `models`: `id`, `cat` (одна из `gcats`), `status`, `name`, `models`, `when`, `limits`, `rules` (массив строк), `ours`, `source`, `url`;
- `moves`: `id`, `type` (`push`, `arc`, `crane`, `track`, `fly`…), `status`, `name`, `sees`, `phrase`, `fov`, `speed`, `style`, `notes`;
- `rules`: `id`, `code`, `cat` (одна из `rcats`), `text`, `why`;
- `start`: шаги блока «С чего начать» — `title`, `text`, `links` (`label` и `href` вида `#templates/t11`);
- `glossary`: словарь — `term`, `def`.

Поля в [квадратных скобках] в шаблонах и фразах подсвечиваются как места, которые меняют под сцену.

## Как пересобрать

`data.json` собирается из рабочей базы пульта скриптом `tools/build_public.py` (в публичную версию не попадают названия проектов и примеры из них), потом `tools/assemble.py` зашивает данные в `index.html`:

```sh
python3 tools/build_public.py <папка с выгрузкой базы> data.json
python3 tools/assemble.py tools/index.src.html data.json index.html
```
