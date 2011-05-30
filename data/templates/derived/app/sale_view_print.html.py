# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306387516.8800001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/sale_view_print.html'
_template_uri='/derived/app/sale_view_print.html'
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
    return runtime._inherit_from(context, u'/base/index_print.html', _template_uri)
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
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.form_start(h.url(controller='app', action='save_sale_app',), method="post")))
        __M_writer(u'\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th rowspan="2" width="30">     \u2116</th>\r\n                <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n                <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n                <th colspan="8">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n                <th rowspan="2" width="50" colspan="2">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n                <th rowspan="2" width="40">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="80" colspan="2">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n                <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n                <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n                <th rowspan="2" width="80">     \u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435</th>\r\n')
        # SOURCE LINE 21
        __M_writer(u'            </tr>\r\n            <tr>\r\n                <th width="20" colspan="2">1</th> \r\n                <th width="20" colspan="2">2</th>\r\n                <th width="20" colspan="2">3</th>\r\n                <th width="20" colspan="2">4</th>               \r\n            </tr>\r\n        ')
        # SOURCE LINE 28
 
        count = 0
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 30
        __M_writer(u'\r\n')
        # SOURCE LINE 31
        for app_element in c.global_app_elements:
            # SOURCE LINE 32
            __M_writer(u'            ')
 
            count += 1
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 34
            __M_writer(u'\r\n            <tr>\r\n                <td>')
            # SOURCE LINE 36
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n                <td>\r\n                    ')
            # SOURCE LINE 38
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u'\r\n                </td>\r\n                <td>')
            # SOURCE LINE 40
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n                <td >')
            # SOURCE LINE 41
            __M_writer(escape(app_element.quarter1))
            __M_writer(u'</td>\r\n                    <td>')
            # SOURCE LINE 42
            __M_writer(escape(app_element.quarter1p))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 43
            __M_writer(escape(app_element.quarter2))
            __M_writer(u'</td>\r\n                    <td>')
            # SOURCE LINE 44
            __M_writer(escape(app_element.quarter2p))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 45
            __M_writer(escape(app_element.quarter3))
            __M_writer(u'</td>\r\n                    <td>')
            # SOURCE LINE 46
            __M_writer(escape(app_element.quarter3p))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 47
            __M_writer(escape(app_element.quarter4))
            __M_writer(u'</td>\r\n                    <td>')
            # SOURCE LINE 48
            __M_writer(escape(app_element.quarter4p))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 49
            __M_writer(escape(app_element.amount))
            __M_writer(u'</td>\r\n                    <td>')
            # SOURCE LINE 50
            __M_writer(escape(app_element.amountp))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 51
            __M_writer(escape(app_element.items.price))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 53
            if app_element.status == 3:
                # SOURCE LINE 54
                __M_writer(u'                        <i><b>')
                __M_writer(escape(app_element.price))
                __M_writer(u'/b></i>\r\n')
                # SOURCE LINE 55
            else:
                # SOURCE LINE 56
                __M_writer(u'                        ')
                __M_writer(escape(app_element.price))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 58
            __M_writer(u'                </td>\r\n                <td>\r\n')
            # SOURCE LINE 60
            if app_element.status == 3:
                # SOURCE LINE 61
                __M_writer(u'                        <i><b>')
                __M_writer(escape(app_element.pricep))
                __M_writer(u'</b></i>\r\n')
                # SOURCE LINE 62
            else:
                # SOURCE LINE 63
                __M_writer(u'                        ')
                __M_writer(escape(app_element.pricep))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 65
            __M_writer(u'                </td>\r\n                <td>')
            # SOURCE LINE 66
            __M_writer(escape(app_element.finsources.name))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 67
            __M_writer(escape(app_element.needss.name))
            __M_writer(u'</td>\r\n                <td>\r\n')
            # SOURCE LINE 70
            for place in c.available_groups:
                # SOURCE LINE 71
                if place[0] == app_element.place:
                    # SOURCE LINE 72
                    __M_writer(u'                            ')
                    __M_writer(escape(place[1]))
                    __M_writer(u'\r\n')
                    pass
                pass
            # SOURCE LINE 75
            __M_writer(u'                </td>\r\n                <td>\r\n')
            # SOURCE LINE 77
            if app_element.status == 5:
                # SOURCE LINE 78
                __M_writer(u'                    \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 80
            if app_element.status == 6:
                # SOURCE LINE 81
                __M_writer(u'                    \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 83
            if app_element.status == 7:
                # SOURCE LINE 84
                __M_writer(u'                    \u0417\u0430\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 86
            if app_element.status == 8:
                # SOURCE LINE 87
                __M_writer(u'                    \u041d\u0435 \u0437\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 89
            __M_writer(u'                </td>            \r\n')
            # SOURCE LINE 91
            __M_writer(u'            </tr>\r\n')
            pass
        # SOURCE LINE 93
        __M_writer(u'        \r\n            <tr>\r\n                <td></td>\r\n                <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n                <td></td>\r\n                <td colspan="2"></td>\r\n                <td colspan="2"></td>\r\n                <td colspan="2"></td>\r\n                <td colspan="2"></td>\r\n                <td colspan="2"></td>\r\n                <td></td>\r\n                <td>')
        # SOURCE LINE 104
        __M_writer(escape(c.total_price))
        __M_writer(u'</td>\r\n                    <td>')
        # SOURCE LINE 105
        __M_writer(escape(c.total_pricep))
        __M_writer(u'</td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n                <td></td>\r\n')
        # SOURCE LINE 111
        __M_writer(u'            </tr>\r\n        </table>\r\n<br />        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h2>\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438 ')
        __M_writer(escape(c.year))
        __M_writer(u' \u0433\u043e\u0434\u0430</h2>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438')
        return ''
    finally:
        context.caller_stack._pop_frame()


