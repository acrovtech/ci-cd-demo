# Informe de Práctica: Actividad CI/CD Sesión 06

**Nombre del Alumno:** [Tu Nombre]  
**Curso:** Despliegue y Operación - DevOps  

---

## 1. Código Fuente y Entorno Virtual
Se creó un entorno virtual y se desarrolló una aplicación CRUD en Python utilizando la librería `tkinter` para la interfaz gráfica.

**Captura 1: Ejecución local de la aplicación**
> *(Pega aquí la captura de tu pantalla mostrando la aplicación CRUD ejecutándose en Windows `python app.py`)*

---

## 2. Pruebas Unitarias con Pytest
Se implementaron pruebas unitarias en `tests/test_crud.py` para validar la lógica del CRUD en memoria.

**Captura 2: Ejecución exitosa de pytest localmente**
> *(Pega aquí la captura de tu terminal mostrando el resultado de correr `pytest` donde se vea que las pruebas pasaron ✅)*

---

## 3. Repositorio en GitHub
El código fuente fue subido a un repositorio en GitHub, incluyendo la estructura de carpetas solicitada.

**Captura 3: Repositorio en GitHub**
> *(Pega aquí la captura de tu navegador mostrando tu repositorio de GitHub con todos los archivos subidos, incluyendo la carpeta `.github/workflows`)*

---

## 4. Pipeline CI/CD (GitHub Actions)
Se configuró el workflow `.github/workflows/ci-cd.yml` el cual se lanza con cada `push` a la rama `main`. El pipeline realiza las siguientes etapas:
1. **CI:** Prepara Python, instala dependencias vía `requirements.txt` y ejecuta `pytest`.
2. **CD:** Si los tests pasan, utiliza `pyinstaller` para empaquetar la aplicación en un ejecutable y lo guarda como un "Artifact".

**Captura 4: Ejecución del Workflow en GitHub Actions**
> *(Pega aquí la captura de la pestaña "Actions" en GitHub, mostrando el check verde del pipeline finalizado)*

**Captura 5: Detalle de los Steps y Artifacts generados**
> *(Pega aquí la captura del resumen del Workflow ejecutado, asegurándote de que en la parte inferior se vea el Artifact `python-crud-executable` listo para descargar)*

---

## Conclusión
Se logró implementar de manera exitosa un ciclo CI/CD completo para una aplicación gráfica de escritorio. El pipeline automatiza la ejecución de pruebas cada vez que se actualiza el código, y prepara la aplicación lista para su distribución a los usuarios mediante `pyinstaller`.
