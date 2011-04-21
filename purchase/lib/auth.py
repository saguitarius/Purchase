## -*- coding: utf-8 -*-

from authkit.authorize.pylons_adaptors import authorized

from authkit.permissions import ValidAuthKitUser
is_valid_user = ValidAuthKitUser()

from authkit.permissions import HasAuthKitRole
has_admin_role = HasAuthKitRole(['admin'])
has_director_role = HasAuthKitRole(['director'])
has_boss_role = HasAuthKitRole(['boss'])
has_user_role = HasAuthKitRole(['user'])


from pylons.templating import render_mako as render
def render_signin():
    return render('/derived/account/signin.html')