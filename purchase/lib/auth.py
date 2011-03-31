from authkit.authorize.pylons_adaptors import authorized

from authkit.permissions import ValidAuthKitUser
is_valid_user = ValidAuthKitUser()

from authkit.permissions import HasAuthKitRole
has_delete_role = HasAuthKitRole(['delete'])