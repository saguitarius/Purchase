# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1301558060.2579999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/campaign/new.html'
_template_uri='/derived/campaign/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading']


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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(escape(h.form_start(h.url(controller='campaign', action='create'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 4
        __M_writer(escape(h.field(
        u"Дата начала",
        h.text(name='start_date'),
        required=True,
    )))
        # SOURCE LINE 8
        __M_writer(u'\r\n    ')
        # SOURCE LINE 9
        __M_writer(escape(h.field(
        u"Дата окончания",
        h.text(name='end_date'),
        required=True,
    )))
        # SOURCE LINE 13
        __M_writer(u'\r\n    ')
        # SOURCE LINE 14
        __M_writer(escape(h.field(
        u"Описание",
        h.textarea(name='description', rows=7, cols=40),
        required=True,
    )))
        # SOURCE LINE 18
        __M_writer(u'\r\n    ')
        # SOURCE LINE 19
        __M_writer(escape(h.field(field=h.submit(value=u"Создать", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 20
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\r\n    <h1 class="main">\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u043e\u0439 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


