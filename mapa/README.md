# ✨ MapGlow - Sistema de Geolocalización Elegante

Sistema de geolocalización con diseño femenino y moderno que permite visualizar ubicaciones desde archivos Excel en un mapa interactivo suave y elegante.

![Python](https://img.shields.io/badge/Python-3.8+-purple.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-pink.svg)
![Leaflet](https://img.shields.io/badge/Leaflet-1.9-lavender.svg)

## 💝 Características Principales

- 📤 **Carga intuitiva** con drag & drop
- 🗺️ **Mapa suave** con estilo Voyager pastel
- 🎀 **Datos de ejemplo** incluidos
- 💫 **Marcadores personalizados** en gradiente morado-rosa
- 📊 **Estadísticas en vivo** en el header
- 🌸 **Diseño femenino** con colores suaves y curvas
- 📱 **100% responsive** y adaptable

## 🎨 Diseño Único y Femenino

Este sistema destaca por:
- **Paleta suave** con morados (#9333ea), rosas (#ec4899) y lavanda
- **Layout de 2 columnas** con sidebar flotante
- **Tipografía amigable** usando Quicksand y Poppins
- **Animaciones delicadas** con transiciones suaves
- **Mapa claro** estilo pastel con CartoDB Voyager
- **Efectos visuales** como pulsos, floats y gradientes
- **Header expandido** con burbujas de estadísticas

## 📁 Estructura del Proyecto

```
mapglow/
├── app.py                      # Aplicación Flask
├── templates/
│   └── index.html             # Interfaz con diseño femenino
├── uploads/                    # Archivos temporales
├── requirements.txt           # Dependencias
├── crear_excel_ejemplo.py     # Generar Excel de ejemplo
├── ubicaciones_ejemplo.xlsx   # Datos de muestra
├── Procfile                   # Para deploy
└── README.md                  # Este archivo
```

## 🚀 Instalación

### 1. Preparar entorno (opcional)

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear archivo de ejemplo

```bash
python crear_excel_ejemplo.py
```

### 4. Ejecutar aplicación

```bash
python app.py
```

### 5. Abrir en navegador

```
http://localhost:5000
```

## 📋 Formato del Excel

El archivo debe tener **2 columnas**:

| Columna A | Columna B |
|-----------|-----------|
| Descripción del lugar | Coordenadas (lat, lon) |

### Ejemplo:

```
┌──────────────────────┬──────────────────┐
│ Descripción          │ Coordenadas      │
├──────────────────────┼──────────────────┤
│ Plaza de Armas       │ -6.6408, -79.387 │
│ Cafetería Central    │ -6.6425, -79.389 │
│ Biblioteca           │ -6.6395, -79.386 │
└──────────────────────┴──────────────────┘
```

## 🎯 Datos de Demostración

MapGlow incluye 6 ubicaciones de ejemplo:

1. Plaza de Armas
2. Parque Principal
3. Centro Comercial
4. Cafetería del Centro
5. Instituto Tecnológico
6. Biblioteca Municipal

Haz clic en **"Ver Datos de Ejemplo"** para cargarlos.

## 🎨 Paleta de Colores

```css
Morado Principal:    #9333ea
Morado Secundario:   #c084fc
Rosa Acento:         #ec4899
Rosa Claro:          #f9a8d4
Fondo:               #fdf4ff - #fae8ff
Texto Oscuro:        #4c1d95
```

## 🌸 Características de Diseño

### Layout Único de 2 Columnas

- **Columna Izquierda (420px)**: 
  - Card de carga con upload zone
  - Card de lista de ubicaciones
  
- **Columna Derecha (flexible)**: 
  - Mapa interactivo grande

### Header Expandido y Decorativo

- Logo con emoji animado
- Título grande y elegante
- Burbujas flotantes con estadísticas
- Fondo con gradiente y decoraciones

### Elementos Visuales Únicos

- Bordes redondeados (30px)
- Degradados suaves morado-rosa
- Animaciones de float y bounce
- Sombras delicadas
- Efectos hover suaves

## 🛠️ Tecnologías

- **Backend**: Python 3.8+ con Flask
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Mapas**: Leaflet.js con CartoDB Voyager (estilo pastel)
- **Excel**: openpyxl
- **Tipografía**: Google Fonts (Quicksand, Poppins)

## 📱 Responsive

Se adapta perfectamente a:

- **Desktop (>1200px)**: Layout completo de 2 columnas
- **Tablet (768px-1200px)**: Columnas apiladas
- **Mobile (<768px)**: Layout vertical optimizado

## 🔧 Solución de Problemas

### El mapa no carga
- Verifica conexión a internet
- Revisa consola del navegador

### Coordenadas no reconocidas
- Formato correcto: `latitud, longitud`
- Usa punto decimal: `-6.6408, -79.3875`
- No uses comas europeas: ~~`-6,6408 -79,3875`~~

### Error al subir Excel
- Formato válido: `.xlsx` o `.xls`
- Debe tener 2 columnas
- Primera fila son los encabezados

## 🌐 Deploy en Render

1. Crear `Procfile` (ya incluido):
```
web: gunicorn app:app
```

2. En Render:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`

3. El sistema se desplegará automáticamente

## 💡 Personalización

### Cambiar colores

Edita las variables CSS en `templates/index.html`:

```css
:root {
    --primary: #9333ea;      /* Morado principal */
    --secondary: #c084fc;    /* Morado secundario */
    --accent: #ec4899;       /* Rosa acento */
    /* ... */
}
```

### Cambiar fuentes

```html
<link href="https://fonts.googleapis.com/css2?family=TU_FUENTE" rel="stylesheet">
```

## 🎀 Diferencias con Otros Sistemas

MapGlow es único porque:

✅ Diseño **femenino y suave** (vs. corporativo/oscuro)
✅ Colores **morado/rosa/lavanda** (vs. azul/verde/dorado)
✅ Layout **2 columnas** con sidebar (vs. 3 columnas/horizontal)
✅ Tema **claro y luminoso** (vs. oscuro)
✅ Mapa **pastel Voyager** (vs. dark/satélite)
✅ Tipografía **redondeada** Quicksand (vs. serif clásica)
✅ Animaciones **delicadas** (vs. profesionales/técnicas)

## 🤝 Uso

Proyecto educativo para IESTP Chongoyape, Lambayeque, Perú.

---

**MapGlow** ✨ - *Geolocalización con estilo y elegancia*
