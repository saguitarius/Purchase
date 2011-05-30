# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306413643.257
_template_filename=u'D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/catalog.html'
_template_uri=u'/derived/catalog/catalog.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'section_description', 'main_sections', 'breadcrumbs', 'subsections', 'search', 'section_actions', 'show_subsection', 'section_items', 'all_sections', 'heading', 'item_actions']


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
        # SOURCE LINE 30
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 34
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 45
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 92
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 98
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 108
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 121
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 133
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 145
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 159
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 173
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 183
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\r\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/reset-fonts-grids/reset-fonts-grids.css'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 7
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/base/base-min.css'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 8
        __M_writer(escape(h.stylesheet_link(h.url('/css/main.css'))))
        __M_writer(u'  \r\n    \r\n    <script type="text/javascript" src="/jquery.js"></script>          \r\n    <script type="text/javascript">       \r\n       # \u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u044b\r\n     $(document).ready(function() {\r\n \r\n       $(\'#toggleli\').click(function(){\r\n         $(\'div.showhide,li.child\').toggle();\r\n       });\r\n     });       \r\n    \r\n')
        # SOURCE LINE 21
        __M_writer(u"    function hide_all() {\r\n        $('div.showhide,li.child').hide();\r\n    }\r\n    \r\n")
        # SOURCE LINE 26
        __M_writer(u'    window.onload = function() {\r\n       hide_all();\r\n     };                                                    \r\n    </script>  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_description(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_sections(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 135
        __M_writer(u'\r\n')
        # SOURCE LINE 136
        for section in c.section:
            # SOURCE LINE 137
            if section.parent_section_id == 1:
                # SOURCE LINE 138
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 140
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
        # SOURCE LINE 110
        __M_writer(u'\r\n    <h3>\r\n    <a href="')
        # SOURCE LINE 112
        __M_writer(escape(h.url(controller='catalog', action='section', id='1')))
        __M_writer(u'">\u041a\u0430\u0442\u0430\u043b\u043e\u0433</a> >\r\n')
        # SOURCE LINE 113
        for section in c.breadcrumbs:
            # SOURCE LINE 114
            if section == c.breadcrumbs[-1]:
                # SOURCE LINE 115
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', id=section[1])))
                __M_writer(u'">')
                __M_writer(escape(section[0]))
                __M_writer(u'</a>\r\n')
                # SOURCE LINE 116
            else:
                # SOURCE LINE 117
                __M_writer(u'            <a href="')
                __M_writer(escape(h.url(controller='catalog', action='section', id=section[1])))
                __M_writer(u'">')
                __M_writer(escape(section[0]))
                __M_writer(u'</a> >\r\n')
                pass
            pass
        # SOURCE LINE 120
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
        # SOURCE LINE 123
        __M_writer(u'\r\n')
        # SOURCE LINE 124
        for subsection in c.section:
            # SOURCE LINE 125
            if subsection.parent_section_id == c.current_section.id:
                # SOURCE LINE 126
                __M_writer(u'        <ul>\r\n        <li>\r\n        <a href="')
                # SOURCE LINE 128
                __M_writer(escape(h.url(controller='catalog', action='section', id=subsection.id)))
                __M_writer(u'">')
                __M_writer(escape(subsection.name))
                __M_writer(u'</a>\r\n        </li>\r\n        </ul>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 175
        __M_writer(u'\r\n')
        # SOURCE LINE 176
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='search_item'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 177
        __M_writer(escape(h.field(
        u"Поиск",
        h.text(name='search_string'),
    )))
        # SOURCE LINE 180
        __M_writer(u'\r\n    ')
        # SOURCE LINE 181
        __M_writer(escape(h.field(field=h.submit(value=u"Найти", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 182
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_actions(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\r\n    <p>\r\n')
        # SOURCE LINE 102
        if h.auth.authorized(h.auth.has_admin_role):
            # SOURCE LINE 103
            __M_writer(u'        <a href="')
            __M_writer(escape(h.url(controller='catalog', action='new_section')))
            __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>  |\r\n        <a href="')
            # SOURCE LINE 104
            __M_writer(escape(h.url(controller='catalog', action='edit_section', id=c.current_section.id)))
            __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a> |\r\n        <a href="')
            # SOURCE LINE 105
            __M_writer(escape(h.url(controller='catalog', action='delete_section', id=c.current_section.id)))
            __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b</a>\r\n')
            pass
        # SOURCE LINE 107
        __M_writer(u'    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_show_subsection(context,section):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        def show_subsection(section):
            return render_show_subsection(context,section)
        __M_writer = context.writer()
        # SOURCE LINE 161
        __M_writer(u'\r\n')
        # SOURCE LINE 162
        for subsection in c.section:
            # SOURCE LINE 163
            if subsection.parent_section_id == section.id:
                # SOURCE LINE 164
                __M_writer(u"              <dl>\r\n              <li class='child'+")
                # SOURCE LINE 165
                __M_writer(escape(subsection.parent_section_id))
                __M_writer(u'+')
                __M_writer(escape(subsection.id))
                __M_writer(u'>\r\n              <input type="image" src="/plus.gif" id="toggleli" />\r\n              <a href="')
                # SOURCE LINE 167
                __M_writer(escape(h.url(controller='catalog', action='section', id=subsection.id)))
                __M_writer(u'">')
                __M_writer(escape(subsection.name))
                __M_writer(u'</a>\r\n              ')
                # SOURCE LINE 168
                __M_writer(escape(show_subsection(subsection)))
                __M_writer(u'\r\n              </li>\r\n              </dl>\r\n')
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
        # SOURCE LINE 47
        __M_writer(u'\r\n')
        # SOURCE LINE 48
        if c.section_items:
            # SOURCE LINE 50
            __M_writer(u'        <table border="1" width="100%">\r\n            <tr>\r\n                <th>\u2116</th>\r\n                <th>\u041c\u0430\u0440\u043a\u0430</th>\r\n                <th>\u041c\u043e\u0434\u0435\u043b\u044c</th>\r\n                <th>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</th>\r\n                <th>\u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f</th>\r\n')
            # SOURCE LINE 58
            if (c.current_app_status == 1) and h.auth.authorized(h.auth.is_valid_user) and (not h.auth.authorized(h.auth.has_admin_role)):
                # SOURCE LINE 59
                __M_writer(u'                    <th>\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c<br />\u0432 \u0437\u0430\u044f\u0432\u043a\u0443</th>\r\n')
                pass
            # SOURCE LINE 61
            if h.auth.authorized(h.auth.has_admin_role):
                # SOURCE LINE 62
                __M_writer(u'                    <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n')
                pass
            # SOURCE LINE 64
            __M_writer(u'            </tr>\r\n        ')
            # SOURCE LINE 65
 
            count = 0
                    
            
            # SOURCE LINE 67
            __M_writer(u'\r\n')
            # SOURCE LINE 68
            for item in c.section_items:
                # SOURCE LINE 69
                if item.deleted != 1:
                    # SOURCE LINE 70
                    __M_writer(u'                ')
 
                    count += 1
                                    
                    
                    # SOURCE LINE 72
                    __M_writer(u'\r\n                <tr>\r\n                    <td>')
                    # SOURCE LINE 74
                    __M_writer(escape(count))
                    __M_writer(u'</td>\r\n                    <td>')
                    # SOURCE LINE 75
                    __M_writer(escape(item.brand))
                    __M_writer(u'</td>\r\n                    <td>')
                    # SOURCE LINE 76
                    __M_writer(escape(item.model))
                    __M_writer(u'</td>\r\n                    <td>')
                    # SOURCE LINE 77
                    __M_writer(escape(item.description))
                    __M_writer(u'</td>\r\n                    <td align="right">')
                    # SOURCE LINE 78
                    __M_writer(escape(item.price))
                    __M_writer(u'</td>\r\n                    <td>')
                    # SOURCE LINE 79
                    __M_writer(escape(item.edited))
                    __M_writer(u'</td>\r\n')
                    # SOURCE LINE 80
                    if (c.current_app_status == 1) and h.auth.authorized(h.auth.is_valid_user) and (not h.auth.authorized(h.auth.has_admin_role)):
                        # SOURCE LINE 81
                        __M_writer(u'                        <th><a href="')
                        __M_writer(escape(h.url(controller='app', action='add_item', id=item.id,)))
                        __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c</a></th>\r\n')
                        pass
                    # SOURCE LINE 83
                    if h.auth.authorized(h.auth.has_admin_role):
                        # SOURCE LINE 84
                        __M_writer(u'                        <td><a href="')
                        __M_writer(escape(h.url(controller='catalog', action='edit_item', id=item.id)))
                        __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a>\r\n                            <a href="')
                        # SOURCE LINE 85
                        __M_writer(escape(h.url(controller='catalog', action='delete_item', id=item.id)))
                        __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>\r\n')
                        pass
                    # SOURCE LINE 87
                    __M_writer(u'                </tr>\r\n')
                    pass
                pass
            # SOURCE LINE 90
            __M_writer(u'        </table>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_all_sections(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        def show_subsection(section):
            return render_show_subsection(context,section)
        __M_writer = context.writer()
        # SOURCE LINE 147
        __M_writer(u'\r\n')
        # SOURCE LINE 148
        for section in c.section:
            # SOURCE LINE 149
            if section.parent_section_id == 1:
                # SOURCE LINE 150
                __M_writer(u'            <dl>\r\n            <li>\r\n            <input type="image" src="/plus.gif" id="toggleli" />\r\n            <a href="')
                # SOURCE LINE 153
                __M_writer(escape(h.url(controller='catalog', action='section', id=section.id)))
                __M_writer(u'">')
                __M_writer(escape(section.name))
                __M_writer(u'</a>\r\n            ')
                # SOURCE LINE 154
                __M_writer(escape(show_subsection(section)))
                __M_writer(u'\r\n            </li>\r\n            </dl>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
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
        # SOURCE LINE 36
        __M_writer(u'\r\n    <p>\r\n')
        # SOURCE LINE 38
        if h.auth.authorized(h.auth.has_admin_role):
            # SOURCE LINE 39
            __M_writer(u'        <a href="')
            __M_writer(escape(h.url(controller='catalog', action='new_item', name=c.current_section.name)))
            __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442</a> \r\n')
            pass
        # SOURCE LINE 41
        if h.auth.authorized(h.auth.has_user_role):
            # SOURCE LINE 42
            __M_writer(u'        <a href="')
            __M_writer(escape(h.url(controller='catalog', action='propose_item', name=c.current_section.name)))
            __M_writer(u'">\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442</a>\r\n')
            pass
        # SOURCE LINE 44
        __M_writer(u'    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


