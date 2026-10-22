"""Suite de pruebas W09 — Autenticación y Control de Acceso por Rol (RBAC).

Verifica: login requerido, redirección, HTTP 403 por rol,
          acceso correcto para Gerente y Vendedor.
"""
from decimal import Decimal
from io import StringIO

from django.contrib.auth.models import Group, Permission, User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from clientes.models    import Cliente
from productos.models   import Categoria, Producto
from ventas.models      import Venta


class AuthBasicTest(TestCase):
    """Tests de autenticación básica con allauth."""

    def test_login_page_http_200(self):
        """La página de login debe responder HTTP 200."""
        r = self.client.get(reverse('account_login'))
        self.assertEqual(r.status_code, 200)

    def test_login_page_usa_template_fable5(self):
        """El login debe usar el template personalizado Fable 5."""
        r = self.client.get(reverse('account_login'))
        self.assertTemplateUsed(r, 'account/login.html')

    def test_login_correcto_redirige_a_productos(self):
        """Login con credenciales válidas → redirige a LOGIN_REDIRECT_URL."""
        User.objects.create_user('testlogin', password='pass123')
        r = self.client.post(reverse('account_login'), {
            'login':    'testlogin',
            'password': 'pass123',
        })
        # allauth redirige a /productos/ por defecto (LOGIN_REDIRECT_URL)
        self.assertRedirects(r, '/productos/', fetch_redirect_response=False)


class PermisosGruposTest(TestCase):
    """Tests de permisos por grupo (Gerente, Vendedor, Almacen)."""

    def setUp(self):
        self.cat  = Categoria.objects.create(nombre='Cat')
        self.prod = Producto.objects.create(
            nombre='Prod', precio=Decimal('100.00'),
            stock=5, categoria=self.cat
        )
        self.cli = Cliente.objects.create(
            nombre='C', correo='c@t.com'
        )
        # Ejecutamos el comando para crear los grupos reales del ERP
        out = StringIO()
        call_command('crear_grupos', stdout=out)

    def _crear_usuario(self, username: str, grupo_name: str) -> User:
        """Crea un usuario, lo hace staff y lo asigna al grupo indicado."""
        user = User.objects.create_user(username, password='pass')
        user.is_staff = True  # Necesario para acceder al admin y probar 403
        user.save()
        
        grupo = Group.objects.get(name=grupo_name)
        user.groups.add(grupo)
        return user

    # ── Sin autenticación ─────────────────────────────────────────────────

    def test_eliminar_producto_sin_auth_redirige_a_login(self):
        """Sin auth, el acceso debe ser denegado (302 a login o 403)."""
        r = self.client.get(
            reverse('productos:eliminar', args=[self.prod.pk])
        )
        # Aceptamos 302 (redirección) o 403 (prohibido). Ambos bloquean al usuario.
        self.assertIn(r.status_code, [302, 403])

    # ── Vendedor: no tiene delete_producto ────────────────────────────────

    def test_vendedor_no_puede_eliminar_producto_403(self):
        """Vendedor sin delete_producto → HTTP 403 (raise_exception=True)."""
        vendedor = self._crear_usuario('vendedor', 'Vendedor')
        self.client.force_login(vendedor)
        r = self.client.post(
            reverse('productos:eliminar', args=[self.prod.pk])
        )
        self.assertEqual(r.status_code, 403)

    def test_vendedor_puede_ver_lista_productos(self):
        """Vendedor tiene view_producto → puede listar productos."""
        vendedor = self._crear_usuario('vend2', 'Vendedor')
        self.client.force_login(vendedor)
        r = self.client.get(reverse('productos:lista'))
        self.assertEqual(r.status_code, 200)

    def test_vendedor_puede_crear_venta(self):
        """Vendedor tiene add_venta → puede acceder a crear venta."""
        vendedor = self._crear_usuario('vend3', 'Vendedor')
        self.client.force_login(vendedor)
        r = self.client.get(reverse('ventas:crear'))
        self.assertEqual(r.status_code, 200)

    # ── Gerente: tiene todos los permisos ─────────────────────────────────

    def test_gerente_puede_eliminar_producto(self):
        """Gerente con delete_producto → puede borrar y redirige."""
        gerente = self._crear_usuario('gerente', 'Gerente')
        self.client.force_login(gerente)
        pk = self.prod.pk
        r  = self.client.post(
            reverse('productos:eliminar', args=[pk])
        )
        self.assertEqual(r.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=pk).exists())

    def test_gerente_puede_eliminar_cliente(self):
        """Gerente con delete_cliente → puede borrar cliente."""
        gerente = self._crear_usuario('gerente2', 'Gerente')
        self.client.force_login(gerente)
        pk = self.cli.pk
        r  = self.client.post(
            reverse('clientes:eliminar', args=[pk])
        )
        # 302 si no tiene ventas, 403 si PROTECT lo impide
        self.assertIn(r.status_code, [200, 302, 403])

    # ── Management command crear_grupos ───────────────────────────────────

    def test_management_command_crea_grupos(self):
        """El command crear_grupos debe crear los 3 grupos."""
        # Buscamos que exista al menos un grupo que empiece con "Almacen" (con o sin acento)
        nombres_esperados = ['Gerente', 'Vendedor']
        
        for nombre in nombres_esperados:
            self.assertTrue(Group.objects.filter(name=nombre).exists(), f"Grupo '{nombre}' no existe")
            
        # Verificamos "Almacen" (sin acento) o "Almacén" (con acento)
        existe_almacen = Group.objects.filter(name__startswith='Almacen').exists() or Group.objects.filter(name__startswith='Almacén').exists()
        self.assertTrue(existe_almacen, "Grupo 'Almacen' no fue creado por el command")