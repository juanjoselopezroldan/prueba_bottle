%include('header.tpl')
<br>
	<h1>En {{ciudad}} con la modalidad {{tipo}} hay los siguientes eventos: </h1>
	% for a,e,i in zip(titulo,empezar,lugar):
		<li>Evento: {{a}}</li>
		<li>Fecha: {{e}}</li>
		<li>Sitio: {{i}}</li>
		<br>
	%end
<br>
%include('footer.tpl')