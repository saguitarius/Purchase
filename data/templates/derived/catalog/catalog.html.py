# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1300888086.3870001
_template_filename=u'D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/catalog.html'
_template_uri=u'/derived/catalog/catalog.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['section_description', 'main_sections', 'breadcrumbs', 'subsections', 'section_actions', 'all_sec', 'section_items', 'heading', 'item_actions']


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
        def main_sections():
            return render_main_sections(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(escape(main_sections()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 13
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 42
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 48
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 56
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 69
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 81
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 93
        __M_writer(u'\r\n\r\n\r\n\r\n')
        # SOURCE LINE 109
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_description(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\r\n    <p><b>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</b>: ')
        # SOURCE LINE 45
        __M_writer(escape(c.current_section.description))
        __M_writer(u'</p>\r\n    <p><i>\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f: ')
        # SOURCE LINE 46
        __M_writer(escape(c.current_section.created))
        __M_writer(u'</i><br />\r\n    <i>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f: ')
        # SOURCE LINE 47
        __M_writer(escape(c.current_section.edited))
        __M_writer(u'</i></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_sections(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 83
        __M_writer(u'\r\n')
        # SOURCE LINE 84
        for section in c.section:
            # SOURCE LINE 85
            if section.parent_section_id == 1:
                # SOURCE LINE 86
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 88
                __M_writer(escape(h.url(controller='catalog', action='section', id=section.id)))
                __M_writer(u'">')
                __M_writer(escape(section.name))
                __M_writer(u'</a>\r\n        </li>\r\n        </ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\r\n    <h3>\r\n    <a href="')
        # SOURCE LINE 60
        __M_writer(escape(h.url(controller='catalog', action='section', id='1')))
        __M_writer(u'">\u041a\u0430\u0442\u0430\u043b\u043e\u0433</a> =>\r\n')
        # SOURCE LINE 61
        for section in c.breadcrumbs:
            # SOURCE LINE 62
            if section == c.breadcrumbs[-1]:
                # SOURCE LINE 63
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', id=section[1])))
                __M_writer(u'">')
                __M_writer(escape(section[0]))
                __M_writer(u'</a>\r\n')
                # SOURCE LINE 64
            else:
                # SOURCE LINE 65
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', id=section[1])))
                __M_writer(u'">')
                __M_writer(escape(section[0]))
                __M_writer(u'</a> =>\r\n')
                pass
            pass
        # SOURCE LINE 68
        __M_writer(u'    </h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subsections(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\r\n')
        # SOURCE LINE 72
        for subsection in c.section:
            # SOURCE LINE 73
            if subsection.parent_section_id == c.current_section.id:
                # SOURCE LINE 74
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 76
                __M_writer(escape(h.url(controller='catalog', action='section', id=subsection.id)))
                __M_writer(u'">')
                __M_writer(escape(subsection.name))
                __M_writer(u'</a>\r\n        </li>\r\n        </ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_actions(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\r\n    <p>\r\n    <a href="')
        # SOURCE LINE 52
        __M_writer(escape(h.url(controller='catalog', action='new_section')))
        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>  |\r\n    <a href="')
        # SOURCE LINE 53
        __M_writer(escape(h.url(controller='catalog', action='edit_section', id=c.current_section.id)))
        __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a> |\r\n    <a href="')
        # SOURCE LINE 54
        __M_writer(escape(h.url(controller='catalog', action='delete_section', id=c.current_section.id)))
        __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>\r\n    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_all_sec(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\r\n')
        # SOURCE LINE 98
        for section in c.section:
            # SOURCE LINE 99
            if section.parent_section_id == 1:
                # SOURCE LINE 100
                __M_writer(u'            <ul><li>')
                __M_writer(escape(section.name))
                __M_writer(u'\r\n')
                # SOURCE LINE 101
                for subsection in c.section:
                    # SOURCE LINE 102
                    if subsection.parent_section_id == section.id:
                        # SOURCE LINE 103
                        __M_writer(u'                    <ul><li>')
                        __M_writer(escape(subsection.name))
                        __M_writer(u'</li></ul>\r\n')
                        pass
                    pass
                # SOURCE LINE 106
                __M_writer(u'            </li></ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_items(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\r\n')
        # SOURCE LINE 16
        if c.section_items:
            # SOURCE LINE 17
            __M_writer(u'        <p><b>\u041e\u0431\u044a\u0435\u043a\u0442\u044b \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0430:</b></p>\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th>\u041c\u0430\u0440\u043a\u0430</th>\r\n                <th>\u041c\u043e\u0434\u0435\u043b\u044c</th>\r\n                <th>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</th>\r\n                <th>\u0426\u0435\u043d\u0430</th>\r\n                <th>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f</th>\r\n                <th>\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c<br />\u0432 \u0437\u0430\u044f\u0432\u043a\u0443</th>\r\n                <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n            </tr>\r\n')
            # SOURCE LINE 28
            for item in c.section_items:
                # SOURCE LINE 29
                __M_writer(u'            <tr>\r\n                <td>')
                # SOURCE LINE 30
                __M_writer(escape(item.brand))
                __M_writer(u'</td>\r\n                <td>')
                # SOURCE LINE 31
                __M_writer(escape(item.model))
                __M_writer(u'</td>\r\n                <td>')
                # SOURCE LINE 32
                __M_writer(escape(item.description))
                __M_writer(u'</td>\r\n                <td>')
                # SOURCE LINE 33
                __M_writer(escape(item.price))
                __M_writer(u'</td>\r\n                <td>')
                # SOURCE LINE 34
                __M_writer(escape(item.edited))
                __M_writer(u'</td>\r\n                <td><a href="')
                # SOURCE LINE 35
                __M_writer(escape(h.url(controller='application', action='add_item')))
                __M_writer(u'">X</a></td>\r\n                <td><a href="')
                # SOURCE LINE 36
                __M_writer(escape(h.url(id=item.id, controller='catalog', action='edit_item')))
                __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a>\r\n                    <a href="')
                # SOURCE LINE 37
                __M_writer(escape(h.url(controller='catalog', action='delete_item', id=item.id)))
                __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>\r\n            </tr>\r\n')
                pass
            # SOURCE LINE 40
            __M_writer(u'        </table>\r\n')
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


def render_item_actions(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\r\n    <p>\r\n    <a href="')
        # SOURCE LINE 11
        __M_writer(escape(h.url(controller='catalog', action='new_item', name=c.current_section.name)))
        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442</a>\r\n    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


