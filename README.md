# FinFlow

FinFlow es una plataforma financiera modular para pequeñas y medianas empresas. El proyecto permite administrar ingresos, gastos, flujo de caja, reportes básicos, roles de usuario y módulos personalizables desde una aplicación desarrollada en Python, acompañada de una página web demostrativa publicada con Vercel.

## Descripción general

Muchas PYMES manejan sus finanzas con hojas de cálculo, apuntes o herramientas demasiado complejas. FinFlow propone una solución más simple: una plataforma modular donde cada empresa puede activar únicamente las funciones que necesita.

El sistema está diseñado para adaptarse a diferentes tipos de negocios, como tiendas, restaurantes, agencias, empresas familiares o consultorías.

## Objetivo del proyecto

Crear una plataforma financiera modular que permita:

- Registrar ingresos.
- Registrar gastos.
- Consultar flujo de caja.
- Generar reportes básicos.
- Manejar roles de usuario.
- Activar y desactivar módulos.
- Simular un asistente financiero.
- Presentar el proyecto en una página web pública.

## Funciones principales

### Login y roles

El sistema permite iniciar sesión con diferentes usuarios y asigna permisos según el rol.

Roles incluidos:

- Administrador.
- Gerente.
- Contador.
- Empleado.

### Módulos personalizables

El administrador puede activar o desactivar módulos del sistema. Esto permite que cada empresa tenga una experiencia diferente según sus necesidades.

Módulos funcionales del MVP:

- Dashboard.
- Ingresos.
- Gastos.
- Flujo de caja.
- Reportes.
- IA financiera simulada.
- Configuración de módulos.

Módulos futuros:

- Inventario.
- Facturación.
- Clientes.
- Proveedores.
- Nómina.
- Préstamos.
- OCR.
- IA avanzada.

### Finanzas

El sistema permite registrar ingresos y gastos con:

- Descripción.
- Categoría.
- Monto.
- Fecha.
- Usuario que creó el registro.

### Reportes

FinFlow genera reportes básicos como:

- Total de ingresos.
- Total de gastos.
- Utilidad actual.
- Movimientos registrados.
- Gastos por categoría.

### IA financiera simulada

El proyecto incluye un asistente financiero simulado que responde preguntas como:

- ¿En qué gasté más?
- ¿Cuánto he ganado?
- ¿Cuál es mi utilidad?
- Dame una recomendación.

## Usuarios de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | 1234 | administrador |
| gerente | 1234 | gerente |
| contador | 1234 | contador |
| empleado | 1234 | empleado |

## Cómo ejecutar el programa en Python

1. Clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal en la raíz del proyecto.
4. Ejecutar:

```bash
python main.py