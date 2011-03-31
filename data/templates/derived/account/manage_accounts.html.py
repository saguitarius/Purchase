# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1299090509.7279999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/account/manage_accounts.html'
_template_uri='/derived/account/manage_accounts.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['roles_list', 'user_list', 'heading', 'group_list', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def user_list():
            return render_user_list(context.locals_(__M_locals))
        def group_list():
            return render_group_list(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(user_list()))
        __M_writer(u'\r\n')
        # SOURCE LINE 7
        __M_writer(escape(group_list()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 45
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 85
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_roles_list(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\r\n    <h2>\u041f\u0440\u0430\u0432\u0430</h2>\r\n    <table border="1" width="100%">\r\n        <tr>\r\n            <th>\u2116</th>\r\n            <th>\u0418\u043c\u044f</th>\r\n            <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n        </tr>\r\n    ')
        # SOURCE LINE 95
        counter=0 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 96
        for group in c.users.list_roles():
            # SOURCE LINE 97
            __M_writer(u'        ')
            counter += 1 
            
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 99
            __M_writer(escape(counter))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 100
            __M_writer(escape(group))
            __M_writer(u'</td>    \r\n            <td><a href="')
            # SOURCE LINE 101
            __M_writer(escape(h.url(controller='account', action='edit_role')))
            __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a> |\r\n                <a href="')
            # SOURCE LINE 102
            __M_writer(escape(h.url(controller='account', action='delete_role')))
            __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a>\r\n            </td>\r\n        </tr>\r\n')
            pass
        # SOURCE LINE 106
        __M_writer(u'    </table>\r\n    <p><a href="')
        # SOURCE LINE 107
        __M_writer(escape(h.url(controller='account', action='add_role')))
        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0430\u0432\u0430</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_list(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\r\n    <h2>\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438</h2>\r\n    \r\n    <table border="1" width="100%">\r\n        <tr>\r\n            <th>\u2116</th>\r\n            <th>\u0418\u043c\u044f</th>\r\n            <th>\u0413\u0440\u0443\u043f\u043f\u0430</th>\r\n            <th>\u041f\u0440\u0430\u0432\u0430</th>\r\n            <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n        </tr>\r\n    ')
        # SOURCE LINE 20
        counter=0 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 21
        for user in c.users.list_users():
            # SOURCE LINE 22
            __M_writer(u'        ')
            counter += 1 
            
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 24
            __M_writer(escape(counter))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 25
            __M_writer(escape(user))
            __M_writer(u'</td>     \r\n            ')
            # SOURCE LINE 26

            try:
                group = c.users.user_group(user)
            except:
                group = ''
                        
            
            # SOURCE LINE 31
            __M_writer(u'\r\n            <td>')
            # SOURCE LINE 32
            __M_writer(escape(group))
            __M_writer(u'</td>\r\n            <td>\r\n')
            # SOURCE LINE 34
            for role in c.users.user_roles(user):
                # SOURCE LINE 35
                __M_writer(u'                    ')
                __M_writer(escape(role))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 37
            __M_writer(u'            </td>\r\n            <td><a href="')
            # SOURCE LINE 38
            __M_writer(escape(h.url(username=user, controller='account', action='edit_user_form')))
            __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a> |\r\n                <a href="')
            # SOURCE LINE 39
            __M_writer(escape(h.url(username=user, controller='account', action='delete_user')))
            __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a>\r\n            </td>\r\n        </tr>\r\n')
            pass
        # SOURCE LINE 43
        __M_writer(u'    </table>\r\n    <p><a href="')
        # SOURCE LINE 44
        __M_writer(escape(h.url(controller='account', action='add_user_form')))
        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_group_list(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\r\n    <h2>\u0413\u0440\u0443\u043f\u043f\u044b</h2>\r\n    <table border="1" width="100%">\r\n        <tr>\r\n            <th>\u2116</th>\r\n            <th>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</th>\r\n            <th>\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a</th>\r\n            <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n        </tr>\r\n    ')
        # SOURCE LINE 56
        counter=0 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 57
        for group in c.users.list_groups():
            # SOURCE LINE 58
            __M_writer(u'        ')
            counter += 1 
            
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 60
            __M_writer(escape(counter))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 61
            __M_writer(escape(group))
            __M_writer(u'</td>   \r\n                ')
            # SOURCE LINE 62

            try:
                boss = c.boss_list[group]
            except:
                boss = ''
                            
            
            # SOURCE LINE 67
            __M_writer(u'\r\n                    <td>')
            # SOURCE LINE 68
            __M_writer(escape(boss))
            __M_writer(u'</td>\r\n            <td><a href="')
            # SOURCE LINE 69
            __M_writer(escape(h.url(controller='account', action='edit_group_form', group=group)))
            __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a> |\r\n                <a href="')
            # SOURCE LINE 70
            __M_writer(escape(h.url(controller='account', action='delete_group', group=group)))
            __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a>\r\n            </td>\r\n        </tr>\r\n')
            pass
        # SOURCE LINE 74
        __M_writer(u'    </table>\r\n    \r\n    <h3>\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443</h3>\r\n    ')
        # SOURCE LINE 77
        __M_writer(escape(h.form_start(h.url(controller='account', action='add_group'), method="post")))
        __M_writer(u'\r\n        ')
        # SOURCE LINE 78
        __M_writer(escape(h.field(
            "Название",
            h.text(name='group'),
            required=True,
        )))
        # SOURCE LINE 82
        __M_writer(u'\r\n        ')
        # SOURCE LINE 83
        __M_writer(escape(h.field(field=h.submit(value="Добавить группу", name='submit'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 84
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438')
        return ''
    finally:
        context.caller_stack._pop_frame()


