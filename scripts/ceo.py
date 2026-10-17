import json
from datetime import datetime, timezone
from pathlib import Path

negocios = [
    ('ClickBarrio', 'Verificar oferta y conversion'),
    ('TrendCommerce', 'Verificar proveedor, stock y margen'),
    ('ClickFlow', 'Probar prototipo con datos ficticios'),
    ('AeroPrep', 'Validar ejercicios originales'),
    ('Tienda Digital', 'Probar producto descargable'),
    ('CapitalLab', 'Simular riesgo sin operar capital'),
]
assert len(negocios) == 6
assert len({nombre for nombre, _ in negocios}) == 6
resultado = {
    'generado_utc': datetime.now(timezone.utc).isoformat(),
    'tipo': 'inventario_no_ejecutor',
    'ejecuciones_comerciales': 0,
    'negocios': [{'nombre': n, 'siguiente_control': t, 'estado': 'SIN_EVIDENCIA_NUEVA'} for n, t in negocios],
}
Path('out').mkdir(exist_ok=True)
Path('out/informe.json').write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding='utf-8')
print('Informe generado para', len(resultado['negocios']), 'negocios')
