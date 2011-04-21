# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1303306065.188
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/sale_view.html'
_template_uri='/derived/app/sale_view.html'
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
        __M_writer(u'\r\n<h3>\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</h3>\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(escape(h.form_start(h.url(controller='app', action='save_sale_app',), method="post")))
        __M_writer(u'\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n                <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n                <th colspan="4">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n                <th rowspan="2" width="70">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n                <th rowspan="2" width="70">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="70">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n                <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435</th>\r\n')
        # SOURCE LINE 21
        __M_writer(u'            </tr>\r\n            <tr>\r\n                <th width="50">1</th> \r\n                <th width="50">2</th>\r\n                <th width="50">3</th>\r\n                <th width="50">4</th>               \r\n            </tr>\r\n')
        # SOURCE LINE 28
        for app_element in c.global_app_elements:
            # SOURCE LINE 29
            __M_writer(u'            <tr>\r\n                <td>\r\n                    ')
            # SOURCE LINE 31
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u'\r\n                </td>\r\n                <td>')
            # SOURCE LINE 33
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 34
            __M_writer(escape(h.text(name='quarter1_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 35
            __M_writer(escape(h.text(name='quarter2_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 36
            __M_writer(escape(h.text(name='quarter3_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 37
            __M_writer(escape(h.text(name='quarter4_el%s'%(app_element.id), size=2)))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 38
            __M_writer(escape(app_element.amount))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 39
            __M_writer(escape(app_element.items.price))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 41
            if app_element.status == 3:
                # SOURCE LINE 42
                __M_writer(u'                        <i><b>')
                __M_writer(escape(app_element.price))
                __M_writer(u'</b></i>\r\n')
                # SOURCE LINE 43
            else:
                # SOURCE LINE 44
                __M_writer(u'                        ')
                __M_writer(escape(app_element.price))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 46
            __M_writer(u'                </td>\r\n                <td>')
            # SOURCE LINE 47
            __M_writer(escape(app_element.finsources.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 48
            __M_writer(escape(app_element.needss.name))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 51
            for place in c.available_groups:
                # SOURCE LINE 52
                if place[0] == app_element.place:
                    # SOURCE LINE 53
                    __M_writer(u'                            ')
                    __M_writer(escape(place[1]))
                    __M_writer(u'\r\n')
                    pass
                pass
            # SOURCE LINE 56
            __M_writer(u'                </td>\r\n                <td>')
            # SOURCE LINE 57
            __M_writer(escape(h.select(name='action_el%s'%(app_element.id), options=c.available_actions, selected_values=[],)))
            __M_writer(u'</td>\r\n')
            # SOURCE LINE 59
            __M_writer(u'            </tr>\r\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'        \r\n            <tr>\r\n                <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td>')
        # SOURCE LINE 71
        __M_writer(escape(c.total_price))
        __M_writer(u'</td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n')
        # SOURCE LINE 77
        __M_writer(u'            </tr>\r\n        </table>\r\n<br />        \r\n')
        # SOURCE LINE 80
        __M_writer(escape(h.field(field=h.submit(value=u"Внести изменения в заявку", name='submit'))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e')
        return ''
    finally:
        context.caller_stack._pop_frame()


