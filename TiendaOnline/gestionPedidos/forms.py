from django import forms

class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()

#>>> from gestionPedidos.forms import FormularioContacto
#>>> miFormulario=FormularioContacto()
#>>>print(miFormulario)
#>>>print(miFormulario.as_p())
#>>>print(miFormulario.as_ul())