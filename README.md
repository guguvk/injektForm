![banner][1]

>[!WARNING]
> **Usar bajo tu propia responsabilidad ya que el uso de este script puede causar daños graves en los sistemas.**

## Requirements

- Tener instalada la libreria `mechanize`
- Asegurarse de que esta señalado el formulario el cual se probara (`nr=0`), en este caso el **0** se refiere al formulario principal y puede ser modificado siempre y cuando haya otro formulario

![form][2]

- cambiar el `password` en el **"br"** por el id del formulario, en este caso se llama `password`

![var][3] 

![id][4]

- Por defecto viene esta inyección sql pero puedes modificarla

![sqli][5]

## Preview

- Tenemos un login de prueba donde haremos la inyección en el campo de contraseña

![login][6]

- Y al ejecutar el script obtendremos que se realizó con exito la inyección en el campo

![script][7]

[1]: https://github.com/user-attachments/assets/de8d4363-4f06-4ab2-975f-9e20f99292ab
[2]: https://github.com/user-attachments/assets/5ab7ffe0-a342-4f0f-bb9c-e754dcc35477
[3]: https://github.com/user-attachments/assets/da74b298-12f1-458c-9aa6-65615bea4045
[4]: https://github.com/user-attachments/assets/7a6d8b77-6d42-4814-953f-2c886a87ec63
[5]: https://github.com/user-attachments/assets/3b76946c-d5b5-4f4d-82b0-5b275f6ec2c6
[6]: https://github.com/user-attachments/assets/fbb06428-a5f7-4c66-aa2b-e2153761c22b
[7]: https://github.com/user-attachments/assets/c2da3567-e2db-4a7e-8b5f-3599c63d048b
