# spbee.py

Genera archivos para deck Anki para entrenar para Spelling Bee

3 fields:
palabra, pronunciacion (hablada), spelling (hablado)

## Uso

1. Crear input.txt con lista de palabras a estudiar
2. `source venv/bin/activate`
3. python gen.py
4. copiar todos los archivos de out en carpeta Windows `cp -a out /mnt/c/Users/hgonz/Downloads`
5. copiar mp3 en collection.media de Anki: `%APPDATA%\Anki2\User 1\collection.media`
6. importar words.csv en Anki como un nuevo deck de tipo `Spelling`
7. exportar deck como .apkg

## Autenticacion

Para usar la API de Google:
```
export GOOGLE_APPLICATION_CREDENTIALS=sofia-spelling-bee-db6056ea3933.json
```