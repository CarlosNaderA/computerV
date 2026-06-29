# Sistema de asistencia automatizada con reconocimiento facial

Este proyecto implementa un sistema básico de visión por computadora para registrar asistencia mediante reconocimiento facial en tiempo real usando la cámara de la computadora.

El sistema permite:

- Registrar rostros de estudiantes o empleados.
- Entrenar un modelo de reconocimiento facial.
- Detectar rostros en tiempo real con la cámara.
- Reconocer a la persona detectada.
- Registrar la asistencia en un archivo CSV.
- Simular una notificación cuando una persona es reconocida.

## Proyecto elegido

Proyecto 1: Sistema de asistencia automatizada con reconocimiento facial.

## Tecnologías utilizadas

- Python
- OpenCV
- NumPy
- Pandas
- Haar Cascade para detección de rostros
- LBPH Face Recognizer para reconocimiento facial

## Estructura del proyecto

```text
computerV_reconocimiento_facial/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── config.py
│   ├── register_faces.py
│   ├── train_model.py
│   └── attendance.py
└── data/
    ├── faces/
    ├── models/
    └── attendance/
```

## Instalación

Primero se debe clonar o descargar el repositorio. Después se recomienda crear un entorno virtual.

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Activar el entorno virtual en Mac o Linux:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar el proyecto

### Opción recomendada: menú principal

Ejecuta:

```bash
python app.py
```

El menú permite elegir entre registrar rostros, entrenar el modelo o iniciar el sistema de asistencia.

## Flujo de uso

### 1. Registrar rostros

Ejecuta:

```bash
python src/register_faces.py
```

El programa pedirá el nombre de la persona. Después abrirá la cámara y guardará varias capturas del rostro en la carpeta `data/faces`.

Para capturar correctamente:

- Mira directamente a la cámara.
- Procura tener buena iluminación.
- Evita cubrir el rostro.
- Presiona `q` para salir antes si es necesario.

### 2. Entrenar el modelo

Después de registrar al menos una persona, ejecuta:

```bash
python src/train_model.py
```

Esto entrenará el modelo LBPH y guardará los archivos en `data/models`.

### 3. Registrar asistencia

Ejecuta:

```bash
python src/attendance.py
```

El sistema abrirá la cámara, detectará rostros y tratará de reconocerlos. Cuando reconoce a una persona, registra su asistencia en un archivo CSV dentro de `data/attendance`.

Para cerrar la cámara, presiona `q`.

## Archivo de asistencia

El archivo generado tendrá un formato similar a:

```csv
nombre,fecha,hora
Carlos,2026-06-29,12:35:10
```

El sistema evita registrar varias veces a la misma persona durante la misma ejecución.

## Simulación de notificación

Cuando una persona es reconocida, el sistema imprime un mensaje simulando una notificación:

```text
Notificación: Carlos ha registrado asistencia correctamente.
```

Esta parte simula la comunicación con padres, supervisores o responsables.

## Notas importantes

Este proyecto es una implementación académica básica. Para un uso real se deberían agregar medidas de seguridad, consentimiento informado, protección de datos personales y validaciones adicionales para evitar errores de reconocimiento.

## Conclusión

El proyecto demuestra cómo la visión por computadora puede utilizarse para automatizar el registro de asistencia mediante detección y reconocimiento facial. Aunque algunas partes se simulan con mensajes en consola, el sistema cumple con la funcionalidad principal: detectar, reconocer y registrar la asistencia de una persona usando la cámara.
