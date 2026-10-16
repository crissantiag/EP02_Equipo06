# Justificaciones técnicas - Equipo 06

## P1 - Power BI
El déficit total fue de 286.90 mil kWh y la cobertura fue de 90.88 % antes de aplicar los filtros el  déficit se calcula por registro, sumando únicamente las diferencias positivas entre demanda y generación no basta con restar los totales globales porque los excedentes podrían compensar déficits de otros registros  el segmentado por región modifica el contexto de filtro de las medidas DAX por  eso al seleccionar una región los indicadores se recalculan para mostrar únicamente los datos correspondientes.

## P2 - ArcGIS
De las 9 sedes 8 pasaron la validación territorial latitud entre 13 y 15, longitud entre −91 y −87 se excluyó S09 Solar La Unión porque su longitud es −67.844 que cae fuera de El Salvador entre las sedes válidas la de mayor déficit es S04 Solar San Salvador con 77,336.41 kWh. Mostrar una coordenada errónea pondría a la sede a unos  km de distancia erróneo de su lugar real y daría una lectura territorial falsa con lo cual la gerencia podría priorizar o descartar zonas por un error de ubicación.
Enlace del mapa: https://www.arcgis.com/apps/mapviewer/index.html?webmap=bdb110904ef5481ea6ccfee5ff5b8007

## P3 - Reportería
Cuando se  vuelve a crear el informe, la fecha, la hora y los documentos se actualizan de forma automática. Para comprobar que todo esté correcto, los datos se comparan con las metas generales de producción, la cantidad que la gente consume y los faltantes. Su mayor problema es que deja fuera la información de lugares que tienen errores y no toma en cuenta los cambios de clima según la época del año.

## P4 - Predicción
El conjunto de prueba abarcó del 26/05/2026 al 29/06/2026, El MAE del baseline fue de 1,194.57 kWh y el de la regresión lineal fue de 298.77 kWh, con una mejora aproximada del 75 % no se debe entrenar con datos futuros porque se produciría fuga de información y la evaluación no sería realista  el pronóstico está limitado por los 180 días de datos disponibles y los patrones que el modelo logra aprender los eventos inesperados o los cambios en la demanda pueden reducir la precisión de las predicciones reales.