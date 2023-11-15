#### Tester: Luis Fernando Mosquera Imbachi.

# Casos de Prueba:

A continuación, se detallan los casos de prueba a ejecutar:

### Caso de prueba N1:  Inicio Sesión exitoso usuario standard_user

Scenario: 
Verificar que el usuario standard_user pueda iniciar sesión con credenciales válidas.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces debería estar en la página principal donde se visualizan todos los productos.


### Caso de prueba N2:  Inicio de Sesión fallido con credenciales No validas

Scenario: Verificar que el usuario standard_user NO pueda iniciar sesión con credenciales no válidas. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuarios:
standard_user

Contraseña:
Hola123;

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “Hola123;”
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces el usuario debería permanecer en el formulario login y debe visualizar una alerta indicando que la información de usuario y contraseña NO son validos 


### Caso de prueba N3:  Inicio de Sesión fallido, validación del campo Username requerido

Scenario: Verificar que el campo Username sea requerido para iniciar sesión. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/

Datos de prueba:
Usuarios:
Campo vacío

Contraseña
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando no ingreso ninguna información en el campo Username
- Y en el campo Password ingreso “secret_sauce”
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces se debería permanecer en el formulario login y debe visualizar una alerta indicando que el campo Username es obligatorio 


### Caso de prueba N4:  Inicio de Sesión fallido, validación del campo Password requerido

Scenario: Verificar que el campo Password sea requerido para iniciar sesión. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuarios:
standard_user

Contraseña:
Campo vacío

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y no ingreso ninguna información en el campo Password
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces se debería permanecer en el formulario login y debe visualizar una alerta indicando que el campo Password es obligatorio 


### Caso de prueba N5:  Inicio de Sesión fallido, validación de campos Userame y Password requeridos

Scenario: Verificar que los campos Username y Password sean requeridos al iniciar sesión. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuarios:
Campo vacío

Contraseña para todos los usuarios:
Campo vacío

Ejecución o pasos:

- Dado como usuario abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando no ingreso ninguna información en el campo Username
- Y no ingreso información en el campo Password 
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces el usuario debería permanecer en el formulario login y debe visualizar una alerta indicando que la información de usuario y contraseña son obligatorios 


### Caso de prueba N6:  Inicio de Sesión, validación de usuario bloqueado

Scenario: Verificar que al iniciar sesión con el usuario locked_out_user se valide que está bloqueado.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
locked_out_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como locked_out_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “locked_out_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"


##### Resultado esperado:
Entonces usuario “locked_out_user” deberá visualizar una alerta indicando que el usuario está bloqueado.


### Caso de prueba N7:  Ordenamiento de productos de acuerdo con el filtro

Scenario: Verificar que el usuario standard_user pueda realizar ordenamiento de los productos de acuerdo a su criterio.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el select que tiene por defecto Name (A to Z)
- Y selecciono Name (Z to A)
- Y luego selecciono Price (low to high)
- Y luego selecciono Price (high to low)


##### Resultado esperado:
Entonces se debe organizar la presentación de productos de acuerdo con la opción indicada.


### Caso de prueba N8:  Visualizar información del producto

Scenario: Verificar que al hacer clic sobre el nombre o imagen del producto el usuario sea redirigido una sección donde solo visualice información de dicho producto. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el nombre del Producto o imagen


##### Resultado esperado:
Entonces se debe redirigir al usuario a una sección donde solo visualizará la información de dicho producto.


### Caso de prueba N9:  Agregar producto

Scenario: Verificar que al hacer clic sobre el boton Add to Cart que se visualiza en la sección de información de producto, se agregue al carrito de compras. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el nombre del Producto o imagen
- Y hago clic en agregar


##### Resultado esperado:
Entonces se debe llenar el carrito de compras con el producto agregado
Y se debe visualizar el botón remove después de agregar el producto.


### Caso de prueba N10:  Remover producto

Scenario: Verificar que al hacer clic sobre el botón Remove que se visualiza en la sección de información de producto, se remueva el producto del carrito de compras.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el nombre del Producto o imagen
- Y hago clic en agregar
- Y hago clic en Remove


##### Resultado esperado:
Entonces se debe remover el producto del carrito de compras y se debe habilitar de nuevo el botón Add to cart.


### Caso de prueba N11:  Retornar a la pagina principal desde la sección de producto individual

Scenario: Verificar que al hacer clic sobre el botón Back to Products que se visualiza en la sección de información de producto, se retorne a la página principal donde se visualizan todos los productos.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el nombre del Producto o imagen
- Y hago clic en Back to products


##### Resultado esperado:
Entonces se debe redirigir al usuario a la página principal donde se visualizan todos los productos


### Caso de prueba N12:  Agregar producto al carrito de compras desde la pagina principal

Scenario: Verificar que se puedan agregar productos al carrito de compras. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar


##### Resultado esperado:
Entonces se debe ir llenando el carrito de compras a medida que se haga clic en el botón en add to cart.
Y se debe visualizar el botón remove en aquellos productos agregados.


### Caso de prueba N13:  Remover producto del carrito de compras desde la página principal

Scenario: Verificar que se puedan remover productos del carrito de compras desde la página principal. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y luego hago clic en el botón Remove


##### Resultado esperado:
Entonces se debe ir removiendo o quitando el producto agregado del carrito de compras.
Y se debe actualizar la cantidad de productos en el carrito de compras.


### Caso de prueba N14:  Verificar Carrito de compras

Scenario: Verificar que el carrito de compras se llene conforme se agregan productos y que adicionalmente al cliquearlo se visualice la lista de productos agregados. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras


##### Resultado esperado:
Entonces se debe ir llenando el carrito de compras a medida que se haga clic en el botón en add to cart.
Entonces al hacer clic en el icono de carrito de compras se debe listar la información de los productos agregados.


### Caso de prueba N15: Remover producto directamente en el carrito de compras

Scenario: Verificar que se puedan remover productos del carrito de compras desde el listado de productos visible en el carrito de compras.

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el boton remove


##### Resultado esperado:
Entonces al hacer clic en el icono de carrito de compras se debe listar la información de los productos agregados.
Entonces al hacer clic en el botón Remove, se debe eliminar el producto de la lista del carrito de compras.


### Caso de prueba N16:  Redireccionamiento a la página principal desde el listado de productos en el carrito de compras

Scenario: Verificar que ser visualice el botón Continue Shopping en el listado de ítems a comprar y que este redirija al usuario a la página principal. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón Continue Shopping


##### Resultado esperado:
Entonces al hacer clic en el icono de carrito de compras se debe listar la información de los productos agregados y en la parte inferior izquierda el boton Continue Shopping.
Entonces al hacer clic en el botón Continue Shopping, se debe redirigir al usuario la página principal.
Entonces visualizará todos los productos incluyendo los que ya están agregados al carrito. 


### Caso de prueba N17:  Redireccionamiento al formulario de información personal

Scenario: Verificar que ser visualice el botón checkout en el listado de ítems a comprar y que este redirija al usuario al formulario de información personal. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout


##### Resultado esperado:
Entonces al hacer clic en el icono de carrito de compras se debe listar la información de los productos agregados y en la parte inferior el boton checkout.
Entonces al hacer clic en el botón Checkout, se debe redirigir al usuario al formulario de Checkout: Your Information


### Caso de prueba N18:  Registro de información en el formulario Checkout: Your Information exitoso

Scenario: Verificar que al llenar la información completa del formulario Checkout: Your Information y hacer clic en continue se redirija al usuario a la sección Checkour Overview. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el formulario de Checkout: Your Information
- Y hago clic en el botón continue 


##### Resultado esperado:
Entonces al hacer llenar por completo el formulario Checkout: Your Information y hacer clic en continue debe redirigir al usuario a la sección Checkout: Overview.


### Caso de prueba N19:  Validación del campo First Name requerido en el formulario Checkout: Your Information

Scenario: Verificar que al dejar el campo First Name vacío y hacer clic en continue se valide que es un campo requerido. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Last Name:
mosquera

Zip/Postal Code:
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y dejo vacío el campo First Name
- Y lleno el campo Last Name
- Y lleno el campo Zip/Postal Code
- Y hago clic en el botón Continue


##### Resultado esperado:
Entonces al dejar vacío el campo First Name del formulario Checkout: Your Information y hacer clic en continue se debe validar que es un campo requerido 


### Caso de prueba N20:  Validación del campo Last Name requerido en el formulario Checkout: Your Information

Scenario: Verificar que al dejar el campo First Name vacío y hacer clic en continue se valide que es un campo requerido. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
Luis

Zip/Postal Code:
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el campo First Name
- Y dejo vacío el campo Last Name
- Y lleno el campo Zip/Postal Code
- Y hago clic en el botón Continue


##### Resultado esperado:
Entonces al dejar vacío el campo Last Name del formulario Checkout: Your Information y hacer clic en continue se debe validar que es un campo requerido 


### Caso de prueba N21:  Validación del campo Zip/Postal Code requerido en el formulario Checkout: Your Information

Scenario: Verificar que al dejar el campo Zip/Postal Code vacío y hacer clic en continue se valide que es un campo requerido. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
Luis

Last Name:
mosquera

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el campo First Name
- Y lleno el campo Last Name
- Y dejo vacío el campo Zip/Postal Code
- Y hago clic en el botón Continue


##### Resultado esperado:
Entonces al dejar vacío el campo Zip/Postal Code del formulario Checkout: Your Information y hacer clic en continue se debe validar que es un campo requerido 


### Caso de prueba N22:  Validación de campos requeridos en el formulario Checkout: Your Information

Scenario: Verificar que al dejar los campos First Name, Last Name y Zip/Postal vacíos y hacer clic en continue se valide que son campos requeridos. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/

Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y dejo vacío el formulario de Checkout: Your Information
- Y hago clic en el botón Continue


##### Resultado esperado:
Entonces al dejar vacío el formulario Checkout: Your Information y hacer clic en continue se debe validar que los campos First Name, Last Name y Zip/Postal son requeridos


### Caso de prueba N23:  Retornar al listado del carrito de compras desde el formulario Checkout: Your Information

Scenario: Verificar que ser visualice el botón Cancel en la sección Checkout: Your y que este redirija al usuario al listado de los productos agregados al carrito de compras. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y hago clic en el botón Cancel


##### Resultado esperado:
Entonces al hacer clic en el icono de carrito de compras se debe listar la información de los productos agregados y en la parte inferior el botón checkout.
Entonces al hacer clic en el botón Checkout, se debe redirigir al usuario al formulario de Checkout: Your Information y en la parte inferior el botón cancel
Entonces al hacer clic en el botón Cancel, se debe redirigir al usuario al listado de productos agregados al carrito de compras.


### Caso de prueba N24:  Visualización de información de compra en la sección Checkout: Overview

Scenario: Verificar que se visualice la información de los productos, métodos de pago, envió y el total la compra a realizar en la sección Checkout: Overview y que este redirija al usuario al listado de los productos agregados al carrito de compras. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
luis

Last Name:
mosquera

Zip/Postal Code
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el formulario Checkout: Your Information
- Y hago clic en continue


##### Resultado esperado:
Entonces al hacer clic en el botón Continue, se debe redirigir al usuario a la sección de Checkout: Overview 
Entonces en esta sección se visualizará la Información de cada producto a comprar, el método de pago, información de envío y el total de la compra.


### Caso de prueba N25:  Retornar al listado del carrito de compras desde la sección Checkout: Overview

Scenario: Verificar que ser visualice el botón Cancel en la sección Checkout: Overview y que este redirija al usuario al listado de productos en la página principal. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
luis

Last Name:
mosquera

Zip/Postal Code
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el formulario Checkout: Your Information
- Y hago clic en continue
- Y hago clic en el botón Cancel


##### Resultado esperado:
Entonces al hacer clic en el botón Continue, se debe redirigir al usuario a la sección de Checkout: Overview 
Entonces al hacer clic en el botón Cancel, se debe redirigir al usuario a la página principal donde se listan todos los productos.


### Caso de prueba N26:  Finalizar Compra

Scenario: Verificar que ser visualice el botón Finish en la sección Checkout: Overview y que este redirija al usuario a la sección Checkout Complete. 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
luis

Last Name:
mosquera

Zip/Postal Code
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el formulario Checkout: Your Information
- Y hago clic en continue
- Y hago clic en el botón Finish


##### Resultado esperado:
Entonces al hacer clic en el botón Continue, se debe redirigir al usuario a la sección de Checkout: Overview 
Entonces al hacer clic en el botón Finish, se debe redirigir al usuario a sección Checkout Complete.


### Caso de prueba N27:  Retornar a la página principal (al listado de productos)

Scenario: Verificar que ser visualice el botón Back Home en la sección Checkout: Complete, que este redirija al usuario a la página principal donde se visualizan todos los productos y que la cantidad de productos del carrito de compras quede en cero (0) . 

Precondiciones:
Ambiente de Prueba https://www.saucedemo.com/
	
Datos de prueba:
Usuario:
standard_user

Contraseña:
secret_sauce

First Name:
luis

Last Name:
mosquera

Zip/Postal Code
410001

Ejecución o pasos:

- Dado como standard_user abro el navegador e ingreso a https://www.saucedemo.com/
- Cuando ingreso el nombre de usuario “standard_user”
- Y ingreso la contraseña “secret_sauce”
- Y hago clic en el botón "Login"
- Y visualizo la lista de productos
- Y hago clic en el botón Add to Cart en aquellos productos que deseo comprar
- Y hago clic en el icono de carrito de compras
- Y hago clic en el botón checkout
- Y lleno el formulario Checkout: Your Information
- Y hago clic en continue
- Y hago clic en el botón Finish
- Y hago clic en el botón back home


##### Resultado esperado:
Entonces al hacer clic en el botón Finish, se debe redirigir al usuario a sección Checkout Complete y se debe visualizar la notificación de compra exitosa y el botón Back Home.
Entonces al hacer clic en el botón Back Home, se debe redirigir al usuario a la página principal donde visualizará todos los productos disponibles en la tienda y el carrito de compras debe quedar seteado en cero (0) productos.









