# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1298540672.777
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/test.html'
_template_uri='/derived/catalog/test.html'
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
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='crea'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 2
        __M_writer(escape(h.field(
        u"Раздел",
        h.select(
            "parent_section",
            id='parent_section',
            options=[
                ['1', 'Chief Investigator', ['2', '4']],
                ['2', 'Assistant'],
                ['3', 'Student'],
            ],
            selected_values=[],
        ),
        required=True
    )))
        # SOURCE LINE 15
        __M_writer(u'\r\n    ')
        # SOURCE LINE 16
        __M_writer(escape(h.field(field=h.submit(value=u"Создать", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 17
        __M_writer(escape(h.form_end()))
        return ''
    finally:
        context.caller_stack._pop_frame()


