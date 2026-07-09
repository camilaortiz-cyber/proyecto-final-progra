# FinFlow OS

**FinFlow OS** es una plataforma financiera modular para pequeñas y medianas empresas. El sistema permite gestionar usuarios, roles, módulos financieros, reportes, sesiones, auditoría, clientes, proveedores, empresas, presupuestos, metas y alertas inteligentes desde una aplicación construida con Python, Flask, JavaScript y Neon PostgreSQL.

El proyecto nació como una aplicación de consola en Python y evolucionó hacia una plataforma web conectada a base de datos en la nube. Actualmente cuenta con login web conectado a Neon, administración de usuarios desde el dashboard, roles diferenciados y preparación para despliegue en Railway.

---

## Descripción del proyecto

FinFlow OS está diseñado para que una PYME pueda administrar su información financiera y operativa desde una plataforma sencilla, modular y escalable.

La aplicación permite registrar y analizar información financiera, controlar accesos según roles, administrar usuarios desde la web, revisar reportes, manejar clientes y proveedores, configurar datos de empresa y mantener trazabilidad mediante sesiones y auditoría.

El sistema combina:

- Una aplicación de consola en Python.
- Un frontend web moderno.
- Un backend Flask.
- Una base de datos Neon PostgreSQL.
- Integración con variables de entorno.
- Preparación para despliegue en Railway.

---

## Objetivo

El objetivo principal de FinFlow OS es ofrecer una solución financiera modular para PYMES que permita:

- Controlar ingresos y gastos.
- Consultar flujo de caja.
- Generar reportes.
- Administrar usuarios y roles.
- Crear usuarios desde el dashboard web.
- Guardar usuarios reales en Neon.
- Permitir login inmediato de usuarios creados.
- Organizar clientes, proveedores y empresas.
- Gestionar presupuestos y metas financieras.
- Visualizar alertas inteligentes.
- Preparar la aplicación para despliegue en la nube usando Railway.

---

## Estado actual

El proyecto actualmente cuenta con:

- Login web conectado a Neon.
- Login de consola conectado a Neon.
- Administración de usuarios desde consola.
- Administración de usuarios desde web.
- Creación de administradores, gerentes, contadores y empleados.
- Usuarios nuevos guardados directamente en Neon.
- Usuarios nuevos pueden iniciar sesión inmediatamente.
- Cierre de sesión funcional desde web.
- Dashboard visual por rol.
- Identidad real de usuario Neon visible en dashboard.
- Módulos financieros y empresariales.
- Reportes mensuales.
- Auditoría.
- Sesiones.
- Configuración de empresa.
- Base de datos PostgreSQL en Neon.
- Backend Flask.
- Preparación para Railway.

---

## Tecnologías utilizadas

### Python

Python es el lenguaje principal del backend y de la aplicación de consola. Se utiliza para manejar lógica de negocio, conexión con base de datos, administración de usuarios, reportes, sesiones, auditoría y módulos financieros.

### Flask

Flask se utiliza como backend web. Permite servir la página de FinFlow y crear rutas API para conectar el frontend con Neon.

Rutas principales:

```text
GET  /
POST /api/login
GET  /api/usuarios
POST /api/usuarios
```

### Flask-CORS

`flask-cors` permite que el frontend pueda comunicarse correctamente con el backend Flask durante desarrollo y despliegue.

### Neon PostgreSQL

Neon es la base de datos PostgreSQL en la nube utilizada por FinFlow.

Se utiliza para guardar:

- Usuarios.
- Roles.
- Login.
- Nombre.
- Correo.
- Carnet.
- Estado de usuario.
- Empresa ID.
- Sesiones.
- Auditoría.
- Movimientos financieros.

### psycopg

`psycopg` es la librería que conecta Python con PostgreSQL.

Permite ejecutar consultas SQL como:

- `SELECT`
- `INSERT`
- `UPDATE`
- `CREATE TABLE`
- `ALTER TABLE`

### psycopg[binary]

`psycopg[binary]` facilita la instalación de psycopg sin depender de una instalación local completa de PostgreSQL. Es especialmente útil para desarrollo local en Windows y Mac.

### python-dotenv

`python-dotenv` permite cargar variables de entorno desde un archivo `.env`.

Se utiliza principalmente para cargar:

```text
DATABASE_URL=postgresql://...
```

### HTML

HTML se utiliza para construir la estructura visual de la aplicación web.

### CSS

CSS se utiliza para el diseño visual de FinFlow, incluyendo estilos premium, dashboard, tarjetas, botones, formularios, módulos y experiencia responsive.

### JavaScript

JavaScript se utiliza para controlar la interacción web del dashboard, login, cierre de sesión, módulos visuales, creación de usuarios desde web, formularios, reportes demo y conexión con Flask por medio de `fetch`.

---

## Estructura del proyecto

```text
proyecto-final-progra/
│
├── app.py
├── main.py
├── db.py
├── usuarios.py
├── admin_usuarios_db.py
├── sesiones_db.py
├── sesiones.py
├── finanzas.py
├── reportes.py
├── reportes_mensuales.py
├── ia_financiera.py
├── auditoria.py
├── alertas.py
├── metas.py
├── presupuestos.py
├── empresas.py
├── clientes.py
├── proveedores.py
├── configuracion_empresa.py
├── data_manager.py
├── modulos.py
│
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   ├── auditoria.json
│   ├── sesiones.json
│   ├── ingresos.json
│   ├── gastos.json
│   └── usuarios.json
│
└── web/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## Archivos principales

### app.py

`app.py` es el backend web principal construido con Flask.

Responsabilidades:

- Levantar el servidor Flask.
- Servir `web/index.html`.
- Inicializar la base de datos.
- Validar login web contra Neon.
- Listar usuarios desde Neon.
- Crear usuarios desde la web.
- Conectar frontend con PostgreSQL.

Rutas principales:

**`GET /`**
Sirve la página principal de FinFlow.

**`POST /api/login`**
Valida usuario y contraseña contra Neon.

**`GET /api/usuarios`**
Lista usuarios registrados en Neon.

**`POST /api/usuarios`**
Permite que un administrador cree usuarios nuevos desde el dashboard web.

### main.py

`main.py` es el punto de entrada para la aplicación de consola.

Responsabilidades:

- Mostrar el menú principal.
- Iniciar sesión.
- Mostrar opciones según rol.
- Ejecutar módulos.
- Registrar sesiones.
- Cerrar sesión.

### db.py

`db.py` administra la conexión con Neon PostgreSQL.

Responsabilidades:

- Cargar `DATABASE_URL`.
- Abrir conexión con Neon.
- Crear tablas si no existen.
- Agregar columnas nuevas si faltan.
- Insertar usuarios demo.
- Inicializar la base de datos.

Tablas creadas:

- `usuarios_db`
- `sesiones_db`
- `auditoria_db`
- `movimientos_db`

### usuarios.py

`usuarios.py` maneja autenticación y permisos.

Responsabilidades:

- Iniciar sesión desde consola.
- Validar usuario y contraseña contra Neon.
- Mostrar usuario actual.
- Validar permisos por rol.
- Mantener compatibilidad con roles anteriores.

Roles soportados:

- `admin`
- `administrador`
- `gerente`
- `contador`
- `empleado`

### admin_usuarios_db.py

`admin_usuarios_db.py` administra usuarios directamente en Neon.

Responsabilidades:

- Crear usuarios.
- Listar usuarios.
- Buscar usuarios.
- Activar usuarios.
- Desactivar usuarios.
- Generar carnets automáticos.
- Validar usuario duplicado.
- Validar correo duplicado.
- Normalizar roles.

Datos guardados por usuario:

- `nombre`
- `correo`
- `usuario`
- `password`
- `rol`
- `carnet`
- `empresa_id`
- `activo`
- `estado`
- `fecha_creacion`

Ejemplos de carnet:

- `ADM-0001`
- `GER-0001`
- `CON-0001`
- `EMP-0001`

### web/index.html

Archivo principal de la interfaz web.

Incluye:

- Login visual.
- Estructura del dashboard.
- Contenedores de módulos.
- Formularios.
- Panel visual de la aplicación.

### web/style.css

Archivo principal de estilos.

Incluye diseño para:

- Login.
- Dashboard.
- Tarjetas.
- Botones.
- Formularios.
- Módulos.
- Tablas.
- Experiencia responsive.
- Estilo visual premium.

### web/script.js

Archivo principal de lógica web.

Responsabilidades:

- Login conectado a Neon.
- Cierre de sesión.
- Dashboard visual por rol.
- Mostrar identidad real del usuario Neon.
- Administración web de usuarios.
- Crear usuarios desde el dashboard.
- Listar usuarios registrados.
- Manejo de módulos visuales.
- Reportes demo.
- Configuración de empresa.
- Interacción con formularios.
- Comunicación con Flask mediante `fetch`.

---

## Roles del sistema

FinFlow utiliza roles para controlar el acceso a módulos.

### Administrador

El administrador tiene acceso completo.

Puede:

- Ver dashboard general.
- Crear usuarios.
- Crear otros administradores.
- Crear gerentes.
- Crear contadores.
- Crear empleados.
- Registrar ingresos.
- Registrar gastos.
- Ver flujo de caja.
- Consultar reportes.
- Consultar reportes mensuales.
- Usar IA financiera.
- Administrar clientes.
- Administrar proveedores.
- Administrar empresas.
- Administrar presupuestos.
- Administrar metas.
- Ver alertas.
- Ver auditoría.
- Configurar módulos.
- Configurar empresa.

### Gerente

El gerente tiene acceso ejecutivo.

Puede:

- Ver dashboard ejecutivo.
- Consultar flujo de caja.
- Consultar reportes.
- Consultar reportes mensuales.
- Ver clientes.
- Ver proveedores.
- Revisar metas.
- Revisar alertas.
- Usar IA financiera.

### Contador

El contador tiene acceso financiero operativo.

Puede:

- Registrar ingresos.
- Registrar gastos.
- Consultar flujo de caja.
- Consultar reportes.
- Consultar reportes mensuales.
- Revisar presupuestos.
- Ver alertas.

### Empleado

El empleado tiene acceso limitado.

Puede:

- Ver dashboard básico.
- Registrar ingresos.
- Consultar reportes mensuales según permisos.

---

## Administración de usuarios

FinFlow permite administrar usuarios desde:

- Consola Python.
- Dashboard web.

Desde el dashboard web, cualquier usuario con rol administrador puede crear:

- Administradores.
- Gerentes.
- Contadores.
- Empleados.

El usuario creado se guarda directamente en Neon y puede iniciar sesión inmediatamente.

Ejemplo de usuario creado:

```text
Nombre: Pedro Carrillo
Correo: pedro@ufm.edu
Usuario: pedro2
Contraseña: 1234
Rol: Administrador
Empresa ID: vacío
```

Resultado esperado:

```text
Usuario creado correctamente con carnet ADM-0002.
```

Luego el usuario puede iniciar sesión con:

```text
Usuario: pedro2
Contraseña: 1234
```

---

## Login web conectado a Neon

El login web ya no depende únicamente de usuarios demo. Ahora valida contra Neon.

Flujo:

```text
Usuario escribe credenciales
        ↓
JavaScript envía datos a Flask
        ↓
Flask consulta Neon
        ↓
Neon valida usuario, password y estado
        ↓
Flask responde al frontend
        ↓
La página abre el dashboard correspondiente
```

Ruta utilizada: `POST /api/login`

Ejemplo de request:

```json
{
  "usuario": "cam1",
  "password": "1234"
}
```

Ejemplo de respuesta:

```json
{
  "success": true,
  "message": "Inicio de sesión exitoso.",
  "user": {
    "usuario": "cam1",
    "rol": "administrador",
    "estado": "activo",
    "carnet": "ADM-0001"
  }
}
```

---

## Usuarios demo

El sistema incluye usuarios iniciales para pruebas:

- `admin / 1234`
- `gerente / 1234`
- `contador / 1234`
- `empleado / 1234`

También se pueden crear nuevos usuarios desde la web usando un administrador.

---

## Base de datos

FinFlow utiliza Neon PostgreSQL.

### usuarios_db

Guarda usuarios del sistema.

Campos principales:

- `id`
- `nombre`
- `correo`
- `usuario`
- `password`
- `rol`
- `carnet`
- `empresa_id`
- `activo`
- `estado`
- `creado_en`
- `fecha_creacion`

### sesiones_db

Guarda eventos de sesión.

Campos principales:

- `id`
- `usuario`
- `accion`
- `fecha`

### auditoria_db

Guarda acciones importantes del sistema.

Campos principales:

- `id`
- `usuario`
- `accion`
- `detalle`
- `fecha`

### movimientos_db

Guarda ingresos y gastos.

Campos principales:

- `id`
- `tipo`
- `descripcion`
- `categoria`
- `monto`
- `usuario`
- `fecha`

---

## Módulos principales

### Dashboard

Muestra una vista general de la empresa y los módulos disponibles según el rol del usuario.

### Ingresos

Permite registrar ingresos financieros.

Datos comunes: descripción, categoría, monto, fecha, usuario.

### Gastos

Permite registrar gastos financieros.

Datos comunes: descripción, categoría, monto, fecha, usuario.

### Flujo de caja

Calcula:

- Total de ingresos.
- Total de gastos.
- Saldo final.

### Reportes

Muestra información financiera general.

### Reportes mensuales

Permite analizar información financiera por mes y año.

Ejemplo: *Reporte de julio 2026*

Mejoras planeadas:

- Filtro por mes.
- Filtro por año.
- Filtro por empresa.
- Filtro por usuario.
- Filtro por rol.
- Filtro por categoría.

### IA financiera

Módulo de análisis financiero simulado. Ayuda a interpretar datos y generar recomendaciones básicas para la empresa.

### Empresas

Permite administrar información de empresas.

### Clientes

Permite administrar clientes.

### Proveedores

Permite administrar proveedores.

### Presupuestos

Permite crear y analizar presupuestos.

### Metas financieras

Permite registrar metas de ventas, ahorro o utilidad.

### Alertas inteligentes

Permite mostrar alertas según movimientos, metas, gastos o presupuestos.

### Auditoría

Registra acciones importantes hechas por usuarios.

### Sesiones

Registra inicios y cierres de sesión.

### Configuración de empresa

Permite personalizar información general de la empresa en la experiencia web.

---

## Variables de entorno

El proyecto utiliza un archivo `.env` para guardar variables sensibles.

Ejemplo:

```text
DATABASE_URL=postgresql://usuario:password@host/neondb?sslmode=require
```

El archivo `.env` **no debe subirse a GitHub**. Debe estar en `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

---

## Instalación local

### 1. Clonar repositorio

```bash
git clone https://github.com/camilaortiz-cyber/proyecto-final-progra.git
cd proyecto-final-progra
```

### 2. Crear entorno virtual

En Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```bash
py -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Dependencias principales:

- `flask`
- `flask-cors`
- `psycopg[binary]`
- `python-dotenv`

### 4. Crear archivo .env

Crear un archivo `.env` en la raíz del proyecto:

```text
DATABASE_URL=tu_url_de_neon
```

### 5. Inicializar base de datos

En Mac:

```bash
python3 -c "from db import inicializar_base_datos; inicializar_base_datos()"
```

En Windows:

```bash
py -c "from db import inicializar_base_datos; inicializar_base_datos()"
```

### 6. Correr aplicación de consola

En Mac:

```bash
python3 main.py
```

En Windows:

```bash
py main.py
```

### 7. Correr aplicación web

```bash
python3 app.py
```

Abrir en navegador:

```text
http://127.0.0.1:5050
```

---

## Requirements

El archivo `requirements.txt` debe contener:

```text
flask
flask-cors
psycopg[binary]
python-dotenv
```

Para despliegue en Railway también se recomienda agregar:

```text
gunicorn
```

---

## Railway

FinFlow está preparado para desplegarse en Railway.

Railway permitirá que la aplicación se ejecute en la nube y no dependa de un entorno local.

Arquitectura esperada:

```text
GitHub
   ↓
Railway
   ↓
Flask app
   ↓
Neon PostgreSQL
```

### Variables en Railway

En Railway se debe configurar la variable:

```text
DATABASE_URL=postgresql://usuario:password@host/neondb?sslmode=require
```

No se debe subir el archivo `.env` al repositorio.

### Comando de inicio en Railway

Para despliegue básico:

```bash
python app.py
```

Para producción se recomienda usar:

```bash
gunicorn app:app
```

En ese caso `requirements.txt` debe incluir:

```text
gunicorn
```

### Puerto en Railway

Railway asigna el puerto mediante la variable de entorno `PORT`.

Para que Flask funcione correctamente en Railway, `app.py` puede usar:

```python
import os

port = int(os.environ.get("PORT", 5050))
app.run(host="0.0.0.0", port=port)
```

Esto permite que Railway levante la aplicación correctamente.

---

## Seguridad

Actualmente FinFlow es un MVP académico avanzado. Algunas decisiones fueron tomadas para facilitar desarrollo y demostración.

Limitaciones actuales de seguridad:

- Las contraseñas se guardan en texto plano.
- No hay hashing de contraseñas todavía.
- No hay recuperación de contraseña.
- No hay sesiones web seguras con cookies.
- Algunos permisos todavía se validan también desde frontend.
- Algunas funciones financieras siguen usando JSON.

Mejoras recomendadas:

- Usar `werkzeug.security` para encriptar contraseñas.
- Implementar sesiones seguras.
- Proteger endpoints administrativos desde backend.
- Agregar validación de correo.
- Agregar recuperación de contraseña.
- Migrar movimientos financieros completamente a Neon.
- Agregar logs de auditoría para acciones web.

---

## Limitaciones actuales

El sistema funciona como MVP académico avanzado, pero todavía puede mejorar en:

- Migración completa de ingresos y gastos a Neon.
- Reportes financieros completamente conectados a base de datos.
- Filtros avanzados en reportes mensuales.
- Seguridad de contraseñas.
- Sesiones web robustas.
- Exportación de reportes.
- Diseño final para producción.
- Configuración final de Railway.

---

## Próximas mejoras

Se planea agregar:

- Filtros mensuales avanzados.
- Reportes por empresa.
- Reportes por usuario.
- Reportes por rol.
- Reportes por categoría.
- Exportación a PDF.
- Exportación a Excel.
- Dashboard financiero completamente conectado a Neon.
- Movimientos financieros guardados en PostgreSQL.
- Gestión web completa de clientes.
- Gestión web completa de proveedores.
- Autenticación segura con contraseñas cifradas.
- Deploy final en Railway.
- Multiempresa real.
- Panel administrativo más completo.

---

## Flujo de Git

El proyecto utiliza el siguiente flujo:

```text
feature/... → dev → main
```

**main** — Rama principal y estable. Debe contener la versión final lista para presentación o despliegue.

**dev** — Rama de desarrollo donde se integran features terminadas y probadas.

**feature** — Ramas individuales para nuevas funcionalidades.

Ejemplos:

- `feature/admin-user-management`
- `feature/monthly-role-reports`
- `feature/monthly-report-filters`
- `feature/web-admin-user-management`

---

## Funcionalidad agregada recientemente

Se agregó administración web de usuarios conectada a Neon.

Incluye:

- Login web contra Neon.
- Cierre de sesión funcional.
- Dashboard visual por rol.
- Identidad real de usuario Neon.
- Botón de administración de usuarios visible para administradores.
- Formulario web para crear usuarios.
- Creación de administradores, gerentes, contadores y empleados.
- Guardado directo en Neon.
- Carnet automático.
- Listado de usuarios.
- Login inmediato del usuario creado.
- Nuevos administradores pueden crear más usuarios.

Archivos principales modificados:

- `app.py`
- `web/script.js`
- `requirements.txt`

---

## Pruebas recomendadas

Antes de hacer merge a `dev` o `main`, probar:

- `admin / 1234`
- `cam1 / 1234`
- `pedro2 / 1234`
- `gerente / 1234`
- `contador / 1234`
- `empleado / 1234`

También probar:

- Crear usuario administrador.
- Crear usuario gerente.
- Crear usuario contador.
- Crear usuario empleado.
- Cerrar sesión.
- Iniciar sesión con usuario nuevo.
- Ver dashboard según rol.
- Listar usuarios en web.

---

## Comandos útiles

Correr consola:

```bash
python3 main.py
```

Correr web:

```bash
python3 app.py
```

Compilar `app.py`:

```bash
python3 -m py_compile app.py
```

Revisar JavaScript:

```bash
node -c web/script.js
```

Matar puerto 5050 en Mac:

```bash
lsof -ti:5050 | xargs kill -9
```

Probar login con curl:

```bash
curl -X POST http://127.0.0.1:5050/api/login \
-H "Content-Type: application/json" \
-d '{"usuario":"cam1","password":"1234"}'
```

Probar creación de usuario con curl:

```bash
curl -X POST http://127.0.0.1:5050/api/usuarios \
-H "Content-Type: application/json" \
-d '{
  "nombre":"Pedro Carrillo",
  "correo":"pedro@ufm.edu",
  "usuario":"pedro2",
  "password":"1234",
  "rol":"administrador",
  "empresa_id":"",
  "admin_actual":{
    "usuario":"cam1",
    "rol":"administrador"
  }
}'
```

---

## Presentación del proyecto

FinFlow OS puede presentarse como:

> Una plataforma financiera modular para PYMES que integra gestión financiera, usuarios, roles, reportes, alertas, auditoría y administración empresarial, conectada a una base de datos PostgreSQL en la nube mediante Neon y preparada para despliegue en Railway.

---

## Equipo

Proyecto desarrollado por:

- Camila Ortíz
- Pedro Carrillo

Curso: Programación
Universidad Francisco Marroquín

---

## Conclusión

FinFlow OS representa una solución financiera modular pensada para pequeñas y medianas empresas.

El proyecto evolucionó desde una aplicación de consola hacia una plataforma web conectada a base de datos en la nube. Actualmente permite autenticación real, administración de usuarios desde web, roles diferenciados, módulos financieros, reportes y preparación para despliegue en Railway.

La arquitectura actual permite seguir creciendo hacia una aplicación financiera más completa, segura, escalable y profesional.

