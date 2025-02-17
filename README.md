
# Calendario en Consola

Este proyecto es un generador de calendario en la consola, que muestra el calendario de un año completo, mes por mes, con el nombre de cada mes resaltado en color y el día actual destacado de manera especial.

## Características

- Muestra los meses de un año en un formato limpio y organizado.
- Resalta el mes actual en color.
- Resalta el día actual en color.
- Compatible con la terminal/consola que soporte secuencias de escape ANSI (como la mayoría de terminales de Linux, macOS y algunas de Windows).

## Requisitos

Este proyecto utiliza solo bibliotecas estándar de Python, por lo que no es necesario instalar dependencias adicionales.

### Bibliotecas utilizadas:
- `calendar`: Para generar el calendario.
- `locale`: Para establecer la configuración regional.
- `datetime`: Para obtener la fecha actual.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/calendario-en-consola.git
   ```

2. Accede al directorio del proyecto:

   ```bash
   cd calendario-en-consola
   ```

3. El código está listo para ejecutarse. No necesitas instalar nada más si ya tienes Python instalado en tu sistema.

## Uso

Para generar el calendario del año 2025, simplemente ejecuta el script en tu terminal:

```bash
python calendario.py
```

El calendario se imprimirá en la consola, con los días actuales resaltados y los nombres de los meses con colores.

## Personalización

- **Colores**: Puedes modificar los códigos de color ANSI en el código para cambiar los colores del texto.
- **Año**: Puedes cambiar el valor de la variable `yy` para generar el calendario de otro año.
- **Meses por fila**: La variable `meses_por_fila` te permite ajustar la cantidad de meses que se muestran por fila.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes alguna mejora o sugerencia, no dudes en hacer un pull request o abrir un issue.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
