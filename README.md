# ZHOPA ALIFE

# [English](README_EN.md)
## [Changelog RU](changelog_ru.md)
## [Changelog EN](changelog_en.md)

## Описание
ZHOPA — модульная ALife-надстройка для Anomaly 1.5.3, которая управляет sim_squads через децентрализованную модель.

С точки зрения геймплея ZHOPA:
- назначает отрядам задачи и цели;
- ведёт отдельный stalker task FSM и отдельный mutant FSM;

## Настройки
Настройки доступны через `gamedata/configs/zhopa_settings.ltx` и MCM -> `ZHOPA`.

Актуальные группы настроек:
- общие переключатели;
- stalker tasks и targeting;
- mutant behavior;
- trade и fast trading;
- base/dynamic/service fillers;
- loot;
- cache/debug/logging knobs, которые реально используются текущим runtime.

## Совместимость
- Anomaly 1.5.3 + Modded Exes.
- Целевая модель: vanilla ALife + modpacks, которые не ломают базовые engine callbacks и `SIMBOARD`.
- Боевые AI-моды уровня Redone AI / Enhanced Combat AI обычно не конфликтуют напрямую, потому что ZHOPA работает на уровне симулятивных отрядов, а не переписывает боевое поведение online NPC целиком.
