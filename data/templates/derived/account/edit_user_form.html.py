# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1302788538.0320001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/account/edit_user_form.html'
_template_uri='/derived/account/edit_user_form.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['user_exists_print', 'heading', 'title']


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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.form_start(h.url(controller='account', action='edit_user', username=c.username), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 7
        __M_writer(escape(h.field(
        "Имя",
        h.text(name='view'),
        required=True,
    )))
        # SOURCE LINE 11
        __M_writer(u'\r\n    ')
        # SOURCE LINE 12
        __M_writer(escape(h.field(
        "E-mail",
        h.text(name='mail'),
        required=True,
    )))
        # SOURCE LINE 16
        __M_writer(u'\r\n    ')
        # SOURCE LINE 17
        __M_writer(escape(h.field(
        "Пароль",
        h.password(name='password'),
        required=True,
    )))
        # SOURCE LINE 21
        __M_writer(u'    \r\n    ')
        # SOURCE LINE 22
        __M_writer(escape(h.field(
        u"Группа",
        h.select(
            "group",
            id='group',
            options=c.available_groups,
            selected_values=c.group,
        ),
        required=True
    )))
        # SOURCE LINE 31
        __M_writer(u'\r\n')
        # SOURCE LINE 42
        __M_writer(u'    ')
        __M_writer(escape(h.field(field=h.submit(value="Изменить", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 43
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n    \r\n')
        # SOURCE LINE 47
        __M_writer(u'    \r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_exists_print(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\r\n    <p>Username <b>')
        # SOURCE LINE 46
        __M_writer(escape(c.username))
        __M_writer(u'</b> already exists.</p>    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f ')
        __M_writer(escape(c.username))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f ')
        return ''
    finally:
        context.caller_stack._pop_frame()


