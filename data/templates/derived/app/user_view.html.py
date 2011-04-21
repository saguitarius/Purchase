# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1303317328.5250001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/user_view.html'
_template_uri='/derived/app/user_view.html'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n<h2>\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430</h2>\r\n<b>id:</b> ')
        # SOURCE LINE 7
        __M_writer(escape(c.current_app.id))
        __M_writer(u'<br />\r\n<b>author_id:</b> ')
        # SOURCE LINE 8
        __M_writer(escape(c.current_app.author_id))
        __M_writer(u'<br />\r\n')
        # SOURCE LINE 10
        __M_writer(u'<b>\u0441\u0442\u0430\u0442\u0443\u0441:</b> ')
        __M_writer(escape(c.current_app.status))
        __M_writer(u'<br />\r\n<b>campaign_id:</b> ')
        # SOURCE LINE 11
        __M_writer(escape(c.current_app.campaign_id))
        __M_writer(u'<br />\r\n')
        # SOURCE LINE 15
        __M_writer(u'\r\n<h2>\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u0437\u0430\u044f\u0432\u043a\u0438</h2>\r\n\r\n')
        # SOURCE LINE 18
        __M_writer(escape(h.form_start(h.url(controller='app', action='save_user_app', id=c.current_app.id), method="post")))
        __M_writer(u'\r\n\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n                <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n                <th colspan="4">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n                <th rowspan="2" width="70">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n                <th rowspan="2" width="70">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="70">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n                <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="120">    \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435</th>\r\n                <th rowspan="2" width="120">    \u0421\u0442\u0430\u0442\u0443\u0441</th>\r\n            </tr>\r\n            <tr>\r\n                <th width="50">1</th> \r\n                <th width="50">2</th>\r\n                <th width="50">3</th>\r\n                <th width="50">4</th>               \r\n            </tr>\r\n')
        # SOURCE LINE 40
        for app_element in c.current_app_elements:
            # SOURCE LINE 41
            __M_writer(u'            <tr>\r\n                <td>')
            # SOURCE LINE 42
            __M_writer(escape(app_element.id))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u' \r\n')
            # SOURCE LINE 43
            if (c.current_app.status == 1) or (h.auth.authorized(h.auth.has_director_role)):
                # SOURCE LINE 44
                __M_writer(u'                        (<a href="')
                __M_writer(escape(h.url(controller='app', action='delete_item', id=app_element.id)))
                __M_writer(u'">\u0443\u0434\u0430\u043b\u0438\u0442\u044c</a>)\r\n')
                pass
            # SOURCE LINE 46
            __M_writer(u'                </td>\r\n                <td>')
            # SOURCE LINE 47
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 48
            __M_writer(escape(h.text(name='quarter1_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 49
            __M_writer(escape(h.text(name='quarter2_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 50
            __M_writer(escape(h.text(name='quarter3_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 51
            __M_writer(escape(h.text(name='quarter4_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 52
            __M_writer(escape(c.element_amount[app_element.id]))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 53
            __M_writer(escape(app_element.items.price))
            __M_writer(u'</td>\r\n')
            # SOURCE LINE 54
            if app_element.status == 3:
                # SOURCE LINE 55
                __M_writer(u'                    <td><i><b>')
                __M_writer(escape(c.element_price[app_element.id]))
                __M_writer(u'</b></i></td>\r\n')
                # SOURCE LINE 56
            else:
                # SOURCE LINE 57
                __M_writer(u'                    <td>')
                __M_writer(escape(c.element_price[app_element.id]))
                __M_writer(u'</td>\r\n')
                pass
            # SOURCE LINE 59
            __M_writer(u'                <td>')
            __M_writer(escape(h.select(name='finsource_el%s'%(app_element.id), options=c.available_finsource, selected_values=[],)))
            __M_writer(u'</td>                \r\n                <td>')
            # SOURCE LINE 60
            __M_writer(escape(h.select(name='needs_el%s'%(app_element.id), options=c.available_needs, selected_values=[],)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 61
            __M_writer(escape(h.select(name='place_el%s'%(app_element.id), options=c.available_groups, selected_values=[],)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 62
            __M_writer(escape(h.textarea(name='note_el%s'%(app_element.id), rows=3, cols=10)))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 64
            if app_element.status == 1:
                # SOURCE LINE 65
                __M_writer(u'                        \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 67
            if app_element.status == 2:
                # SOURCE LINE 68
                __M_writer(u'                        \u0417\u0430\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 70
            if app_element.status == 3:
                # SOURCE LINE 71
                __M_writer(u'                        \u0423\u0434\u0430\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 73
            if app_element.status == 4:
                # SOURCE LINE 74
                __M_writer(u'                        \u0423\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 76
            if app_element.status == 5:
                # SOURCE LINE 77
                __M_writer(u'                        \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 79
            if app_element.status == 6:
                # SOURCE LINE 80
                __M_writer(u'                        \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e, \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 82
            if app_element.status == 7:
                # SOURCE LINE 83
                __M_writer(u'                        \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e, \u0437\u0430\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 85
            if app_element.status == 8:
                # SOURCE LINE 86
                __M_writer(u'                        \u041d\u0435 \u0437\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 88
            __M_writer(u'                </td>\r\n            </tr>\r\n')
            pass
        # SOURCE LINE 91
        __M_writer(u'        \r\n            <tr>\r\n                <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td>')
        # SOURCE LINE 101
        __M_writer(escape(c.total_price))
        __M_writer(u'</td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n            </tr>\r\n        </table>\r\n        \r\n<br />\r\n')
        # SOURCE LINE 111
        if (c.current_app.status == 1) or (h.auth.authorized(h.auth.has_director_role)):
            # SOURCE LINE 112
            __M_writer(u'    ')
            __M_writer(escape(h.field(field=h.submit(value=u"Внести изменения в заявку", name='submit'))))
            __M_writer(u'\r\n')
            pass
        # SOURCE LINE 114
        if c.current_app.status == 1 and (not h.auth.authorized(h.auth.has_director_role)):
            # SOURCE LINE 115
            __M_writer(u'    <p><a href="')
            __M_writer(escape(h.url(controller='app', action='app_to_boss')))
            __M_writer(u'">\u041f\u0435\u0440\u0435\u0434\u0430\u0447\u0430 \u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u0438\u0435</a></p>\r\n')
            pass
        # SOURCE LINE 117
        __M_writer(u'<p>\r\n')
        # SOURCE LINE 118
        if c.current_app.status == 2:
            # SOURCE LINE 119
            __M_writer(u'    \u0412\u0430\u0448\u0430 \u0437\u0430\u044f\u0432\u043a\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0430 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u0438\u0435.\r\n')
            pass
        # SOURCE LINE 121
        if c.current_app.status == 3:
            # SOURCE LINE 122
            __M_writer(u'    \u0412\u0430\u0448\u0430 \u0437\u0430\u044f\u0432\u043a\u0430 \u0443\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430 \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u0443.\r\n')
            pass
        # SOURCE LINE 124
        if (c.current_app.status == 4) and not (h.auth.authorized(h.auth.has_director_role)):
            # SOURCE LINE 125
            __M_writer(u'    \u0412\u0430\u0448\u0430 \u0437\u0430\u044f\u0432\u043a\u0430 \u0443\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430 \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e.\r\n')
            pass
        # SOURCE LINE 127
        __M_writer(u'</p>\r\n')
        # SOURCE LINE 128
        if h.auth.authorized(h.auth.has_director_role):
            # SOURCE LINE 129
            __M_writer(u'    <p><a href="')
            __M_writer(escape(h.url(controller='app', action='director_app_to_global')))
            __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a \u043e\u0431\u0449\u0435\u0439 \u0437\u0430\u044f\u0432\u043a\u0435</a></p>\r\n')
            pass
        # SOURCE LINE 131
        __M_writer(u'\r\n<h2>\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438</h2>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0417\u0430\u044f\u0432\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430')
        return ''
    finally:
        context.caller_stack._pop_frame()


