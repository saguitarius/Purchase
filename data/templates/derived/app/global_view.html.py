# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1303294422.9579999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/global_view.html'
_template_uri='/derived/app/global_view.html'
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
        __M_writer(u'\r\n\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n                <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n                <th colspan="4">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n                <th rowspan="2" width="70">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n                <th rowspan="2" width="70">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="70">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n                <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n')
        # SOURCE LINE 18
        __M_writer(u'            </tr>\r\n            <tr>\r\n                <th width="50">1</th> \r\n                <th width="50">2</th>\r\n                <th width="50">3</th>\r\n                <th width="50">4</th>               \r\n            </tr>\r\n')
        # SOURCE LINE 25
        for app_element in c.global_app_elements:
            # SOURCE LINE 26
            __M_writer(u'            <tr>\r\n                <td>\r\n                    ')
            # SOURCE LINE 28
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u'\r\n                </td>\r\n                <td>')
            # SOURCE LINE 30
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 31
            __M_writer(escape(app_element.quarter1))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 32
            __M_writer(escape(app_element.quarter2))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 33
            __M_writer(escape(app_element.quarter3))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 34
            __M_writer(escape(app_element.quarter4))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 35
            __M_writer(escape(app_element.amount))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 36
            __M_writer(escape(app_element.items.price))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 38
            if app_element.status == 3:
                # SOURCE LINE 39
                __M_writer(u'                        <i><b>')
                __M_writer(escape(app_element.price))
                __M_writer(u'</b></i>\r\n')
                # SOURCE LINE 40
            else:
                # SOURCE LINE 41
                __M_writer(u'                        ')
                __M_writer(escape(app_element.price))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 43
            __M_writer(u'                </td>\r\n                <td>')
            # SOURCE LINE 44
            __M_writer(escape(app_element.finsources.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 45
            __M_writer(escape(app_element.needss.name))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 48
            for place in c.available_groups:
                # SOURCE LINE 49
                if place[0] == app_element.place:
                    # SOURCE LINE 50
                    __M_writer(u'                            ')
                    __M_writer(escape(place[1]))
                    __M_writer(u'\r\n')
                    pass
                pass
            # SOURCE LINE 53
            __M_writer(u'                </td>\r\n')
            # SOURCE LINE 55
            __M_writer(u'            </tr>\r\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'        \r\n            <tr>\r\n                <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td>')
        # SOURCE LINE 67
        __M_writer(escape(c.total_price))
        __M_writer(u'</td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n')
        # SOURCE LINE 72
        __M_writer(u'            </tr>\r\n        </table>\r\n        \r\n<p><a href="')
        # SOURCE LINE 75
        __M_writer(escape(h.url(controller='app', action='approve_global_app')))
        __M_writer(u'">\u0423\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e</a></p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e')
        return ''
    finally:
        context.caller_stack._pop_frame()


