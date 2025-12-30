Explicacion del Proyecto:

Mi objetivo con este proyecto es intentar implementar mis conocimientos aprendido es python a un programa real, aparte de intentar
refrescar mi memoria y entrenarme en temas como estructura de proyecto, organizacion de archivos, carpetas y organizacion general
------------------------------------------
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
-------------------------------------------
📂 engine/ – Lógica del juego
Aquí vive el “motor” del RPG: las reglas y el flujo del juego.

game_loop.py → controla el bucle principal del juego.

combat.py → sistema de combate, turnos, daño, cálculo de estadísticas.

events.py → eventos aleatorios, encuentros, sucesos del mundo.

world.py → definición de zonas, mapas o progresión entre áreas.

Esta carpeta es el corazón del funcionamiento interno.

📂 entities/ – Personajes y criaturas
Define todos los seres vivos del juego.

player.py → clase del jugador, estadísticas, inventario, nivel.

enemy.py → enemigos, sus atributos y comportamiento.

npc.py → personajes no jugables.

stats.py → sistema de estadísticas base (vida, ataque, defensa, etc.).

Todo lo que “existe” en el mundo está aquí.

📂 items/ – Objetos y equipamiento
Contiene las clases relacionadas con objetos utilizables o equipables.

weapons.py → armas y sus efectos.

armor.py → armaduras y protección.

consumables.py → pociones, comida, objetos de un solo uso.

Permite ampliar fácilmente el inventario del juego.

📂 skills/ – Habilidades y progresión
Define el sistema de habilidades del jugador o enemigos.

skill_tree.py → árbol de habilidades, desbloqueos, requisitos.

skill_effects.py → efectos concretos de cada habilidad.

Aquí se gestiona la progresión del personaje.

📂 data/ – Datos externos
Archivos JSON que contienen información del juego sin hardcodear.

enemies.json → lista de enemigos, estadísticas y descripciones.

items.json → objetos, armas, armaduras.

skills.json → habilidades y efectos.

Permite modificar contenido sin tocar el código.

📂 utils/ – Utilidades y herramientas
Funciones auxiliares que no pertenecen a un módulo concreto.

save_system.py → sistema de guardado/carga de partidas.

logger.py → registro de eventos o depuración.

helpers.py → funciones pequeñas de apoyo.

🧪 Carpeta tests/
Contiene pruebas unitarias para asegurar que las mecánicas del juego funcionan correctamente.

test_combat.py → pruebas del sistema de combate.

test_player.py → pruebas del jugador y sus estadísticas.

test_items.py → pruebas de objetos y equipamiento.