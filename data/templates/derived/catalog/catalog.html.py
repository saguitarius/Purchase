# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1298485287.973
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/catalog.html'
_template_uri='/derived/catalog/catalog.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['current_section', 'description', 'breadcrumbs', 'actions', 'sections', 'heading']


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
        def sections():
            return render_sections(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(escape(sections()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 13
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 19
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 32
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 44
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_current_section(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\r\n')
        # SOURCE LINE 35
        for subsection in c.section:
            # SOURCE LINE 36
            if subsection.parent_section_id == c.current_section.id:
                # SOURCE LINE 37
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 39
                __M_writer(escape(h.url(controller='catalog', action='section', name=subsection.name)))
                __M_writer(u'">')
                __M_writer(escape(subsection.name))
                __M_writer(u'</a>\r\n        </li>\r\n        </ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_description(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\r\n    <p><b>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</b>: ')
        # SOURCE LINE 10
        __M_writer(escape(c.current_section.description))
        __M_writer(u'</p>\r\n    <p><i>\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f: ')
        # SOURCE LINE 11
        __M_writer(escape(c.current_section.created))
        __M_writer(u'</i><br />\r\n    <i>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f: ')
        # SOURCE LINE 12
        __M_writer(escape(c.current_section.edited))
        __M_writer(u'</i></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\r\n    <h3>\r\n    \u041a\u0430\u0442\u0430\u043b\u043e\u0433 =>\r\n')
        # SOURCE LINE 24
        for item in c.breadcrumbs:
            # SOURCE LINE 25
            if item == c.breadcrumbs[-1]:
                # SOURCE LINE 26
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', name=item)))
                __M_writer(u'">')
                __M_writer(escape(item))
                __M_writer(u'</a>\r\n')
                # SOURCE LINE 27
            else:
                # SOURCE LINE 28
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', name=item)))
                __M_writer(u'">')
                __M_writer(escape(item))
                __M_writer(u'</a> =>\r\n')
                pass
            pass
        # SOURCE LINE 31
        __M_writer(u'    </h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_actions(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\r\n    <a href="')
        # SOURCE LINE 16
        __M_writer(escape(h.url(controller='catalog', action='new_section')))
        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>  |\r\n    <a href="')
        # SOURCE LINE 17
        __M_writer(escape(h.url(controller='catalog', action='edit_section', name=c.current_section.name)))
        __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a> |\r\n    <a href="')
        # SOURCE LINE 18
        __M_writer(escape(h.url(controller='catalog', action='delete_section', name=c.current_section.name)))
        __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sections(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\r\n')
        # SOURCE LINE 47
        for section in c.section:
            # SOURCE LINE 48
            if section.parent_section_id == 1:
                # SOURCE LINE 49
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 51
                __M_writer(escape(h.url(controller='catalog', action='section', name=section.name)))
                __M_writer(u'">')
                __M_writer(escape(section.name))
                __M_writer(u'</a>\r\n        </li>\r\n        </ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\r\n    <h1 class="main">\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0442\u043e\u0432\u0430\u0440\u043e\u0432</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


