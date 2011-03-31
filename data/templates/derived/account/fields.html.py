# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1298885650.575
_template_filename=u'D:\\PyProjects\\Purchase\\purchase\\templates/derived/account/fields.html'
_template_uri=u'/derived/account/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Username",
    h.text(name='username'),
    required=True,
)))
        # SOURCE LINE 5
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Password",
    h.password(name='password'),
    required=True,
)))
        return ''
    finally:
        context.caller_stack._pop_frame()


