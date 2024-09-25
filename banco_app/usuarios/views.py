from django.shortcuts import render, get_object_or_404, redirect
from .models import UsuarioBanco
from .forms import UsuarioForm
from .forms import SaldoForm


# Listar usuarios
def listar_usuarios(request):
    usuarios = UsuarioBanco.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

#crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('cuenta_usuario', usuario_id=usuario.id)
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})


# Actualizar usuario
def actualizar_usuario(request, id):
    usuario = get_object_or_404(UsuarioBanco, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/actualizar_usuario.html', {'form': form})

# Eliminar usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(UsuarioBanco, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

def cuenta_usuario(request, usuario_id):
    usuario = get_object_or_404(UsuarioBanco, id=usuario_id)
    transacciones = usuario.transacciones.all()
    if request.method == 'POST':
        form = SaldoForm(request.POST)
        if form.is_valid():
            monto = form.cleaned_data['monto']
            # Actualizar el saldo del usuario
            usuario.saldo += monto
            usuario.save()

            # Registrar la transacción
            Transaccion.objects.create(usuario=usuario, tipo_transaccion='Ingreso', monto=monto)

            return redirect('cuenta_usuario', usuario_id=usuario.id)
    else:
        form = SaldoForm()

    return render(request, 'usuarios/cuenta_usuario.html', {
        'usuario': usuario,
        'transacciones': transacciones,
        'form': form,
    })
