
1. Solicitar al @BotFather la creación de un nuevo bot
```
/newbot
<bot_name>
<bot_username ending with bot>
```
2. Solicitar vuestro propio ID de telegram a @userinfobot
```
/start
```
3. Enviar mensaje a Telgram mediante Python
4. Agregar esta funcionalidad a un endpoint de nuestra aplicación
5. Guardar un log de cada uno de los mensajes enviados en la db
6. **Crear un formulario HTML para enviar mensajes**
   - Añadir un campo para el ID del destinatario y otro para el texto del mensaje.
   - Incorporar un botón «Enviar» que llame al endpoint de nuestra aplicación.
   - Validar que ambos campos estén completos.
   - Mostrar si el mensaje se ha enviado correctamente o se ha producido un error.
   - Guardar el envío en la base de datos utilizando la funcionalidad del punto 5.

7. **Consultar el historial de mensajes**
   - Crear un endpoint `GET /mensajes` que devuelva los registros de la base de datos.
   - Permitir filtrar por destinatario y estado.
   - Ordenar los resultados del más reciente al más antiguo.
   - Mostrar el historial en una tabla HTML debajo del formulario.

8. **Guardar conversaciones completas**
Ahora el historial debe incluir tanto los mensajes recibidos como las respuestas enviadas.
- Registrar el ID del chat, el texto, la fecha y la dirección: entrante o saliente.
- Indicar quién genera cada mensaje: usuario o IA

9. Añadir memoria a la IA
Hacer que la IA pueda mantener una conversación de varios turnos.
- Recuperar los últimos mensajes de ese chat antes de consultar a la IA.
- Enviarlos como contexto, respetando el orden cronológico y el rol de cada participante.
- Limitar el contexto a los últimos diez mensajes.
- Mantener separado el historial de cada chat.