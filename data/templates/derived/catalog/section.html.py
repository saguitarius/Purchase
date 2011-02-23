# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1298479271.171
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/section.html'
_template_uri='/derived/catalog/section.html'
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
    ns = runtime.Namespace(u'catalog', context._clean_inheritance_tokens(), templateuri=u'/derived/catalog/catalog.html', callables=None, calling_uri=_template_uri, module=None)
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
        breadcrumbs = _import_ns.get('breadcrumbs', context.get('breadcrumbs', UNDEFINED))
        current_section = _import_ns.get('current_section', context.get('current_section', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        actions = _import_ns.get('actions', context.get('actions', UNDEFINED))
        sections = _import_ns.get('sections', context.get('sections', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 5
        __M_writer(escape(sections()))
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(breadcrumbs()))
        __M_writer(u'\r\n')
        # SOURCE LINE 7
        __M_writer(escape(current_section()))
        __M_writer(u'\r\n')
        # SOURCE LINE 8
        __M_writer(escape(description()))
        __M_writer(u'\r\n')
        # SOURCE LINE 9
        __M_writer(escape(actions()))
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
        # SOURCE LINE 11
        __M_writer(u'\r\n    <h1 class="main">\u0420\u0430\u0437\u0434\u0435\u043b\u044b \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


