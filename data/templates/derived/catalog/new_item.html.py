# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1298974331.8499999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/new_item.html'
_template_uri='/derived/catalog/new_item.html'
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
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'catalog', context._clean_inheritance_tokens(), templateuri=u'/derived/catalog/catalog.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'catalog')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'catalog')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 5
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='create_item'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
        u"Раздел",
        h.select(
            "section_id",
            id='section_id',
            options=c.available_sections,
            selected_values=[],
        ),
        required=True
    )))
        # SOURCE LINE 15
        __M_writer(u'\r\n    ')
        # SOURCE LINE 16
        __M_writer(escape(h.field(
        u"Марка",
        h.text(name='brand'),
        required=True,
    )))
        # SOURCE LINE 20
        __M_writer(u'\r\n    ')
        # SOURCE LINE 21
        __M_writer(escape(h.field(
        u"Модель",
        h.text(name='model'),
        required=True,
    )))
        # SOURCE LINE 25
        __M_writer(u'\r\n    ')
        # SOURCE LINE 26
        __M_writer(escape(h.field(
        u"Описание",
        h.textarea(name='description', rows=7, cols=40),
        required=True,
    )))
        # SOURCE LINE 30
        __M_writer(u'\r\n    ')
        # SOURCE LINE 31
        __M_writer(escape(h.field(
        u"Ед. изм.",
        h.select(
            "unit_id",
            id='unit_id',
            options=c.available_units,
            selected_values=[],
        ),
        required=True
    )))
        # SOURCE LINE 40
        __M_writer(u'\r\n    ')
        # SOURCE LINE 41
        __M_writer(escape(h.field(
        u"Цена (руб.)",
        h.text(name='price'),
        required=True,
    )))
        # SOURCE LINE 45
        __M_writer(u'\r\n    ')
        # SOURCE LINE 46
        __M_writer(escape(h.field(field=h.submit(value=u"Создать", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 47
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'catalog')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\r\n    <h1 class="main">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


