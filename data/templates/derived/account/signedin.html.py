# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1302680437.9200001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/account/signedin.html'
_template_uri='/derived/account/signedin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 5
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(u'\r\n\r\n<p>\u0412\u044b \u0432\u043e\u0448\u043b\u0438 \u043a\u0430\u043a ')
        # SOURCE LINE 8
        __M_writer(escape(request.environ['REMOTE_USER']))
        __M_writer(u'.\r\n<a href="')
        # SOURCE LINE 9
        __M_writer(escape(h.url(controller='account', action='signout')))
        __M_writer(u'">\u0412\u044b\u0439\u0442\u0438</a></p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'<h1>\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u0451\u043d</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u0451\u043d')
        return ''
    finally:
        context.caller_stack._pop_frame()


