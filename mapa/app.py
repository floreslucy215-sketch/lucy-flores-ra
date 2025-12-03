"""
MapGlow - Sistema de Geolocalización con Estilo Femenino
Diseño suave y elegante con colores morados y rosas
"""

from flask import Flask, render_template, request, jsonify
import openpyxl
import os
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Crear carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def parse_coordinates(coord_string):
    """Parsea coordenadas en formato decimal"""
    if coord_string is None:
        return None, None
    
    coord_string = str(coord_string).strip()
    decimal_pattern = r'(-?\d+\.?\d*)[,\s]+(-?\d+\.?\d*)'
    match = re.search(decimal_pattern, coord_string)
    
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon
    
    return None, None

def process_excel(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        
        headers = []
        for cell in sheet[1]:
            if cell.value:
                headers.append(str(cell.value).strip().lower())
            else:
                headers.append('')
        
        desc_col = None
        coord_col = None
        
        for idx, header in enumerate(headers):
            if 'desc' in header or 'nombre' in header or 'lugar' in header:
                desc_col = idx
            if 'coord' in header or 'latitud' in header or 'gps' in header:
                coord_col = idx
        
        if desc_col is None:
            desc_col = 0
        if coord_col is None:
            coord_col = 1 if len(headers) > 1 else 0
        
        locations = []
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row and len(row) > max(desc_col, coord_col):
                descripcion = str(row[desc_col]).strip() if row[desc_col] else "Sin descripción"
                coord_raw = row[coord_col]
                
                lat, lon = parse_coordinates(coord_raw)
                
                if lat is not None and lon is not None:
                    locations.append({
                        'descripcion': descripcion,
                        'lat': lat,
                        'lon': lon,
                        'coordenadas_raw': str(coord_raw)
                    })
        
        workbook.close()
        return locations, None
    
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró archivo'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó archivo'}), 400
    
    if not file.filename.endswith(('.xlsx', '.xls')):
        return jsonify({'error': 'El archivo debe ser Excel (.xlsx o .xls)'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_locations.xlsx')
    file.save(filepath)
    
    locations, error = process_excel(filepath)
    
    try:
        os.remove(filepath)
    except:
        pass
    
    if error:
        return jsonify({'error': f'Error procesando archivo: {error}'}), 400
    
    if not locations:
        return jsonify({'error': 'No se encontraron ubicaciones válidas en el archivo'}), 400
    
    return jsonify({
        'success': True,
        'locations': locations,
        'count': len(locations)
    })

@app.route('/demo', methods=['GET'])
def demo_data():
    """Datos de demostración para Chongoyape, Lambayeque"""
    demo_locations = [
        {
            'descripcion': 'Plaza de Armas',
            'lat': -6.6408,
            'lon': -79.3875,
            'coordenadas_raw': '-6.6408, -79.3875'
        },
        {
            'descripcion': 'Parque Principal',
            'lat': -6.6425,
            'lon': -79.3890,
            'coordenadas_raw': '-6.6425, -79.3890'
        },
        {
            'descripcion': 'Centro Comercial',
            'lat': -6.6395,
            'lon': -79.3862,
            'coordenadas_raw': '-6.6395, -79.3862'
        },
        {
            'descripcion': 'Cafetería del Centro',
            'lat': -6.6418,
            'lon': -79.3868,
            'coordenadas_raw': '-6.6418, -79.3868'
        },
        {
            'descripcion': 'Instituto Tecnológico',
            'lat': -6.6438,
            'lon': -79.3905,
            'coordenadas_raw': '-6.6438, -79.3905'
        },
        {
            'descripcion': 'Biblioteca Municipal',
            'lat': -6.6410,
            'lon': -79.3873,
            'coordenadas_raw': '-6.6410, -79.3873'
        }
    ]
    
    return jsonify({
        'success': True,
        'locations': demo_locations,
        'count': len(demo_locations)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
