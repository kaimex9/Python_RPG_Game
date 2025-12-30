# 🐍 Proyecto RPG en Python

Este proyecto tiene como objetivo aplicar y reforzar mis conocimientos de Python desarrollando un juego RPG modular, bien estructurado y mantenible. El enfoque principal es practicar arquitectura, organización de archivos y buenas prácticas de desarrollo.

---

## 📁 Estructura del Proyecto

│
├── main.py
├── requirements.txt
├── README.md
│
├── game/
│   ├── engine/
│   ├── entities/
│   ├── items/
│   ├── skills/
│   ├── data/
│   └── utils/
│
└── tests/

---

## ⚙️ game/engine — Motor del juego

| Archivo | Descripción |
|--------|-------------|
| `game_loop.py` | Controla el bucle principal del juego. |
| `combat.py` | Sistema de combate, turnos, daño y cálculos. |
| `events.py` | Eventos aleatorios, encuentros y sucesos. |
| `world.py` | Definición de zonas, mapas y progresión. |

---

## 🧍 game/entities — Personajes y criaturas

| Archivo | Descripción |
|--------|-------------|
| `player.py` | Clase del jugador, estadísticas, inventario y nivel. |
| `enemy.py` | Enemigos, atributos y comportamiento. |
| `npc.py` | Personajes no jugables. |
| `stats.py` | Sistema de estadísticas base (vida, ataque, defensa…). |

---

## 🗡️ game/items — Objetos y equipamiento

| Archivo | Descripción |
|--------|-------------|
| `weapons.py` | Armas y sus efectos. |
| `armor.py` | Armaduras y protección. |
| `consumables.py` | Pociones, comida y objetos de un solo uso. |

---

## ✨ game/skills — Habilidades y progresión

| Archivo | Descripción |
|--------|-------------|
| `skill_tree.py` | Árbol de habilidades, requisitos y desbloqueos. |
| `skill_effects.py` | Efectos concretos de cada habilidad. |

---

## 📦 game/data — Datos externos (JSON)

| Archivo | Descripción |
|--------|-------------|
| `enemies.json` | Lista de enemigos y estadísticas. |
| `items.json` | Objetos, armas y armaduras. |
| `skills.json` | Habilidades y efectos. |

---

## 🛠️ game/utils — Utilidades y herramientas

| Archivo | Descripción |
|--------|-------------|
| `save_system.py` | Guardado y carga de partidas. |
| `logger.py` | Registro de eventos y depuración. |
| `helpers.py` | Funciones auxiliares de apoyo. |

---

## 🧪 tests/ — Pruebas unitarias

| Archivo | Descripción |
|--------|-------------|
| `test_combat.py` | Pruebas del sistema de combate. |
| `test_player.py` | Pruebas del jugador y estadísticas. |
| `test_items.py` | Pruebas de objetos y equipamiento. |

---

## 🚀 Objetivo del proyecto

- Practicar estructura profesional de proyectos Python  
- Implementar un RPG modular y escalable  
- Entrenar organización de carpetas y archivos  
- Trabajar con datos externos (JSON)  
- Añadir pruebas unitarias para asegurar calidad del código  

