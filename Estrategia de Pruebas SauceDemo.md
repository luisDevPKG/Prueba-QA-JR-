Tester:  Luis Fernando Mosquera Imbachi 

# Estrategia de Pruebas:

Plataforma: https://www.saucedemo.com/

## Objetivo:
Asegurar que la plataforma Saucedemo cuente con funcionalidad adecuada, que sea acorde a la lógica de negocio, esto permitirá identificar cada uno de los posibles problemas y bugs garantizando que la experiencia de usuario sea completamente agradable y que la plataforma tenga altos estándares de calidad.

## Alcance:
Los tipos y casos de pruebas detallados en este documento se van a realizar para cada uno de los usuarios de prueba suministrados; las funcionalidades a priorizar (sin limitación) de la plataforma se describen a continuación:


#### Componente	y funcionalidad
- Formulario login: 
    Ingreso exitoso con credenciales correctas y validaciones ante credenciales erróneas o formulario incompleto.

- Select Name (A to Z): 
    Ordene adecuadamente conforme a la opción seleccionada.

- Botón Add to Cart:
    Agregue el producto al carrito de compras.

- Botón Remove:
    Remueva el producto del carrito de compras.

- Botón Carrito compras:
    Se llene a medida que se agreguen productos y muestre la información de cada producto agregado.

- Botón checkout: 
    Redirija al usuario al formulario de ingreso de información personal

- Formulario Checkout Your Information y Botón Continue: 
    Requiera la información de los tres campos para continuar con la compra.
    Si se llena el formulario correctamente, al hacer continue redirija al usuario a la sección de Overview

- Sección Overview: 	
    Presentar la información completa de los productos a comprar, así como el totalizado de la compra en caso de ser más de un producto

- Botón Finish: 
    Finalizar la compra y redirigir al usuario a la sección de checkout Complete

- Sección checkout Complete: 	
    Presentar al usuario información indicando que la compra finalizó de forma exitosa

- Botón back home: 
    Redirija al usuario a la página principal donde se visualizan los productos


## Tipos de Pruebas:

    1.	Pruebas de Funcionalidad:
-   Asegurar que los usuarios puedan iniciar sesión correctamente.
-   Comprobar la funcionalidad de ordenamiento de productos.
-   Validar que los productos se puedan agregar al carrito sin problemas.
-   Confirmar que el proceso de pago se complete correctamente.
-   Verificar que todas las funciones principales del sitio estén operativas.
-   Verificar cada una de las validaciones presentes ante una mala ejecución de procedimientos.


    2.	Pruebas de Usabilidad:
-   Evaluar la navegación general del sitio.
-   Verificar la legibilidad y comprensión de las traducciones y mensajes de confirmación.
-   Asegurar que las páginas sean de fácil comprensión. 


    3.	Pruebas de Compatibilidad:
-   Testear compatibilidad de la plataforma en los navegadores con mayor uso por parte de los usuarios como Chrome, Firefox, Safari.
-   Verificar la responsividad del sitio en dispositivos móviles y tabletas para que la experiencia de usuario sea agradable.


    4.	Pruebas de Rendimiento:	
-   Evaluar la velocidad de carga de las páginas en diferentes dispositivos y conexiones.
-   Realizar pruebas de estrés para determinar la capacidad del sitio.
-   Verificar la respuesta del sitio a situaciones de tráfico intenso.


    5.	Pruebas de Seguridad:
-   Verificar que la información del usuario esté protegida durante la transmisión.


    6.	Pruebas de Regresión:
-   Desarrollar y ejecutar los casos de prueba cada vez que se realice alguna modificación en los procesos funcionales del sistema para garantizar que las nuevas funcionalidades o modificaciones no afecten el flujo de trabajo e intercambio de información con las interfaces existentes.


### Casos de Prueba:

    Caso 1: Inicio de Sesión Exitoso
    Ingresar credenciales válidas y verificar que el inicio de sesión sea exitoso.

    Caso 2: Inicio de Sesión fallido con credenciales No validas
    Ingresar credenciales NO válidas y verificar que NO se puede iniciar sesión.

    Caso 3: Inicio de Sesión fallido, validación del campo Username requerido
    Dejar el campo Username  vacío y en el campo Password ingresar una contraseña valida, al momento de hacer clic en login verificar que el campo Username es requerido.

    Caso 4: Inicio de Sesión fallido, validación del campo Password requerido
    En el campo Username ingresar un usuario valido y el campo Password se deja vacío, al momento de hacer clic en login verificar que el campo Password es requerido.

    Caso 5: Inicio de Sesión fallido, validación de campos requeridos
    Dejar los campos Username y Password vacíos al momento de hacer clic en login y validar que los campos sean requeridos.

    Caso 6: Inicio de Sesión, validación de usuario bloqueado
    Ingresar credenciales válidas de un usuario registrado pero que está bloqueado y verificar que no se pueda iniciar sesión y se indique que el usuario está bloqueado

    Caso 7: Ordenamiento de productos de acuerdo con el filtro
    Seleccionar cada una de las opciones del select que trae por defecto Name (A to Z) y verificar que los productos se ordenen de acuerdo con cada opción seleccionada.

    Caso 8: Agregar producto al carrito de compras
    Seleccionar un producto y agregarlo al carrito de compras mediante el botón Add to Cart verificando que se agregue correctamente.

    Caso 9: Remover producto del carrito de compras desde la página principal
    Seleccionar un producto y agregarlo al carrito de compras, posteriormente mediante el botón Remove verificando que se remueva dicho producto.

    Caso 10: Verificar Carrito de compras
    Verificar que el carrito de compras se vaya llenando a medida que se agreguen productos y que al cliquearlo muestre la lista de productos agregados.

    Caso 11: Remover producto directamente en el carrito de compras
    Seleccionar un producto y agregarlo al carrito de compras, posteriormente mediante el botón Remove verificando que se remueva dicho producto.

    Caso 12: Redireccionamiento a la página principal desde el listado de productos en el carrito de compras 
    Cliquear el botón de Continue Shopping visible en el listado del carrito de compras, verificar que redirija al usuario a la página principal.

    Caso 13: Redireccionamiento al formulario de información personal
    Cliquear el botón de checkout visible en el listado carrito de compras, verificar que redirija al usuario al formulario de información personal.

    Caso 14: Registro de información en el formulario Checkout: Your Information exitoso
    Ingresar la información de First Name, Last Name y Zip/Postal code de forma correcta y hacer clic en continue, verificar que al llenar todos los campos se redirija a la sección de Checkout Overview

    Caso 15: Validación del campo First Name requerido en el formulario Checkout: Your Information
    Dejar el campo First Name, vacío al momento de hacer clic en continue y validar que sea requerido.

    Caso 16: Validación del campo Last Name requerido en el formulario Checkout: Your Information
    Dejar el campo Last Name, vacío al momento de hacer clic en continue y validar que sea requerido.

    Caso 17: Validación del campo Zip/Postal requerido en el formulario Checkout: Your Information
    Dejar el campo Zip/Postal, vacío al momento de hacer clic en continue y validar que sea requerido.

    Caso 18: Validación de campos requeridos en el formulario Checkout: Your Information
    Dejar los campos First Name, Last Name y Zip/Postal vacíos al momento de hacer clic en continue y validar que los campos sean requeridos.

    Caso 19: Retornar al listado del carrito de compras desde el formulario Checkout: Your Information
    Ingresar la información de First Name, Last Name y Zip/Postal code de forma correcta y hacer clic en Cancel, verificar que al hacer clic en Cancel se redirija al usuario a la lista del carrito de compras.

    Caso 20: Visualización de información de compra en la sección Checkout: Overview 
    Posterior a la selección de productos, registro de información y clic en continue, se debe visualizar la información de la compra. Verificar si corresponde realmente a los productos seleccionados y no a otros.

    Caso 21: Retornar al listado del carrito de compras desde la sección Checkout: Overview 
    Posterior a la selección de productos, registro de información y clic en continue, se debe visualizar la información de la compra, en la parte inferior izquierda se visualizará el botón Cancel. Verificar si al hacer clic en Cancel debe retornar al usuario a la página principal donde se listen los productos.

    Caso 22: Finalizar compra
    Posterior a la selección de productos, registro de información y clic en continue; cliquear el botón de finish para proceder a finalizar compra. Verificar que el evento al hacer clic funcione adecuadamente y redirija al usuario a la sección de Checkout: Complete.

    Caso 23: Retornar a la página principal 
    Cliquear el botón de Back Home visible en la sección de Checkout: Complete, verificar que redirija al usuario a la página principal, la cual presenta todos los productos de la plataforma.

    Caso 24: Integración – Simular el completo procedimiento de compra:
    Simular todo el proceso de compra desde el inicio de sesión hasta visualizar la sección de Checkout: Complete indicando la compra exitosa. Verificar que todo este proceso integrando los diferentes componentes se complete de forma exitosa.


## Entregables:
Informe de pruebas detallado que incluya resultados, problemas encontrados y recomendaciones.
Registro de casos de prueba ejecutados y su estado.

## Plan de Ejecución:
Fecha de Inicio: 11 noviembre 2023
Fecha de Finalización: 15 noviembre 2023
Tester responsable: Luis Fernando Mosquera Imbachi 
Ambiente de Pruebas: https://www.saucedemo.com/ 
