# Instalaciones de python.exe en el sistema:

Python Install Manager (en el paquete MSIX instalado de Microsoft Store):
C:\Users\Andres\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.PythonManager_3847v3x7pw1km\python.exe
Alias de ejecución de Windows:
C:\Users\Andres\AppData\Local\Microsoft\WindowsApps\python.exe

Lanzador de Python gestionado por Python Install Manager::
C:\Users\Andres\AppData\Local\Python\bin\python.exe
Instalación de CPython 3.13 de 64 bits:
C:\Users\Andres\AppData\Local\Python\pythoncore-3.13-64\python.exe

Instalación base de Conda de ArcGIS Pro:
C:\Program Files\ArcGIS\Pro\bin\Python\python.exe
Entorno predeterminado de ArcGIS Pro (arcgispro-py3):
C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
Entorno clonado de ArcGIS Pro (arcgispro-py3-clone):
C:\Users\Andres\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe


# Comandos de inspección de Python:
where python # Muestra las rutas de los ejecutables python.exe encontrados en el PATH, en orden de prioridad.
python -c "import sys; print(sys.executable)" # Muestra la ruta del intérprete de Python que se está ejecutando.
py -0p # Muestra las versiones de Python registradas en Python Launcher y sus rutas de instalación.

# Instalación de nuevas versiones de Python mediante Python Install Manager de Windows (py o pymanager):
py list 		# Muestra las versiones de Python instaladas y gestionadas por Python Install Manager.
py list --online 	# Muestra las versiones de Python disponibles para instalar.
py install 3.12 	# Instala Python 3.12 mediante Python Install Manager.
py uninstall 3.12 	# Desinstala Python 3.12 

# Creación de un entorno virtual de Python
python -m venv venv 		# Crea el entorno virtual en la carpeta venv, dentro del directorio actual.
venv\Scripts\activate.bat 	# Activa el entorno virtual en CMD.
deactivate 			# Desactiva el entorno virtual.

# Gestión de paquetes dentro del entorno virtual:
python -m pip list 			# Lista los paquetes instalados en el entorno activo.
python -m pip install pandas 		# Instala pandas en el entorno activo.
python -m pip install --upgrade pandas	# Actualiza pandas en el entorno activo.
python -m pip uninstall pandas 		# Desinstala pandas del entorno activo.
python -m pip show pandas 		# Muestra información sobre un paquete instalado.
python -m pip freeze 			# Lista los paquetes instalados con sus versiones.

# Herramientas de Esri para ejecutar Python y gestionar entornos de ArcGIS Pro:
propy.bat # Ejecuta Python con la configuración de entorno de ArcGIS Pro en CMD.
proenv.bat # Configura una consola CMD para trabajar con Conda y los entornos de Python de ArcGIS Pro en CMD.
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "C:\ruta\script.py" # Ejecuta un script con el intérprete del entorno predeterminado de ArcGIS Pro y sus paquetes instalados.
"C:\Users\Andres\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe" "C:\ruta\script.py" # Ejecuta un script con el intérprete del entorno clonado de ArcGIS Pro y sus paquetes instalados.