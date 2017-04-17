%include('header.tpl')
<br>
	<form action="/eventfull" method="post">
		<label>ciudad:</label>
		<input type="text" name="ciudad" required/>
		<label>tipo:</label>
		<input type="text" name="tipo" required/>
		<input type="submit" value="Enviar">
	</form>
<br>
%include('footer.tpl')