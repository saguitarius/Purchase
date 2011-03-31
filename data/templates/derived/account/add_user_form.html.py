# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1300868102.6129999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/account/add_user_form.html'
_template_uri='/derived/account/add_user_form.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['user_exists_print', 'user_exists', 'heading', 'title']


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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        def user_exists():
            return render_user_exists(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(user_exists()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 8
        __M_writer(escape(h.form_start(h.url(controller='account', action='add_user'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 9
        __M_writer(escape(h.field(
        "Имя",
        h.text(name='username'),
        required=True,
    )))
        # SOURCE LINE 13
        __M_writer(u'\r\n    ')
        # SOURCE LINE 14
        __M_writer(escape(h.field(
        "Пароль",
        h.password(name='password'),
        required=True,
    )))
        # SOURCE LINE 18
        __M_writer(u'    \r\n    ')
        # SOURCE LINE 19
        __M_writer(escape(h.field(
        u"Группа",
        h.select(
            "group",
            id='group',
            options=c.available_groups,
            selected_values=[],
        ),
        required=True
    )))
        # SOURCE LINE 28
        __M_writer(u'\r\n    ')
        # SOURCE LINE 29
        __M_writer(escape(h.field(
        u"Права",
        h.select(
            "roles",
            id='roles',
            ##options=[''] + c.available_roles,
            options=c.available_roles,
            selected_values=[],
            #multiple = True,
        ),
    )))
        # SOURCE LINE 39
        __M_writer(u'\r\n    ')
        # SOURCE LINE 40
        __M_writer(escape(h.field(field=h.submit(value="Добавить", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 41
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n    \r\n')
        # SOURCE LINE 45
        __M_writer(u'    \r\n    \r\n')
        # SOURCE LINE 55
        __M_writer(u'    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_exists_print(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\r\n    <p>Username <b>')
        # SOURCE LINE 44
        __M_writer(escape(c.username))
        __M_writer(u'</b> already exists.</p>    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_exists(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def user_exists_print():
            return render_user_exists_print(context)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\r\n    ')
        # SOURCE LINE 48

        try:
            c.username
            user_exists_print()
        except:
            pass
            
        
        # SOURCE LINE 54
        __M_writer(u'     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f')
        return ''
    finally:
        context.caller_stack._pop_frame()


