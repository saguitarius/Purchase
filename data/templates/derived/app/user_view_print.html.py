# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306406116.957
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/user_view_print.html'
_template_uri='/derived/app/user_view_print.html'
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
        # SOURCE LINE 8
        __M_writer(u' \r\n\r\n\r\n')
        # SOURCE LINE 11
        __M_writer(escape(h.form_start(h.url(controller='app', action='save_user_app', id=c.current_app.id), method="post")))
        __M_writer(u'\r\n\r\n    <table border="1" width="100%">\r\n        <tr>\r\n            <th rowspan="2" width="15">     \u2116</th>\r\n            <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n            <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n            <th colspan="4">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n            <th rowspan="2" width="50">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n            <th rowspan="2" width="40">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n            <th rowspan="2" width="50">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n            <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n            <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n            <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n            <th rowspan="2" width="90">     \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435</th>\r\n            <th rowspan="2" width="90">     \u0421\u0442\u0430\u0442\u0443\u0441</th>\r\n        </tr>\r\n        <tr>\r\n            <th width="70">1</th> \r\n            <th width="70">2</th>\r\n            <th width="70">3</th>\r\n            <th width="70">4</th>               \r\n        </tr>\r\n    ')
        # SOURCE LINE 34
 
        count = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 36
        __M_writer(u'\r\n')
        # SOURCE LINE 37
        for app_element in c.current_app_elements:
            # SOURCE LINE 38
            __M_writer(u'        ')
 
            count += 1
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 40
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 42
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 43
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 44
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n')
            # SOURCE LINE 45
            if c.current_app.status == 1:
                # SOURCE LINE 46
                __M_writer(u'                <td align="right">')
                __M_writer(escape(app_element.quarter1))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 47
                __M_writer(escape(app_element.quarter2))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 48
                __M_writer(escape(app_element.quarter3))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 49
                __M_writer(escape(app_element.quarter4))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 50
                __M_writer(escape(c.element_amount[app_element.id]))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 51
                __M_writer(escape(app_element.items.price))
                __M_writer(u'</td>\r\n')
                # SOURCE LINE 52
                if app_element.status == 3:
                    # SOURCE LINE 53
                    __M_writer(u'                    <td align="right"><i><b>')
                    __M_writer(escape(c.element_price[app_element.id]))
                    __M_writer(u' / ')
                    __M_writer(escape(c.element_pricep[app_element.id]))
                    __M_writer(u'</b></i></td>\r\n')
                    # SOURCE LINE 54
                else:
                    # SOURCE LINE 55
                    __M_writer(u'                    <td align="right">')
                    __M_writer(escape(c.element_price[app_element.id]))
                    __M_writer(u'</td>\r\n')
                    pass
                pass
            # SOURCE LINE 58
            if c.current_app.status in (2,3,4):
                # SOURCE LINE 59
                __M_writer(u'                <td align="right">')
                __M_writer(escape(app_element.quarter1))
                __M_writer(u' / ')
                __M_writer(escape(app_element.quarter1p))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 60
                __M_writer(escape(app_element.quarter2))
                __M_writer(u' / ')
                __M_writer(escape(app_element.quarter2p))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 61
                __M_writer(escape(app_element.quarter3))
                __M_writer(u' / ')
                __M_writer(escape(app_element.quarter3p))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 62
                __M_writer(escape(app_element.quarter4))
                __M_writer(u' / ')
                __M_writer(escape(app_element.quarter4p))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 63
                __M_writer(escape(c.element_amount[app_element.id]))
                __M_writer(u' / ')
                __M_writer(escape(c.element_amountp[app_element.id]))
                __M_writer(u'</td>\r\n                <td align="right">')
                # SOURCE LINE 64
                __M_writer(escape(app_element.items.price))
                __M_writer(u'</td>\r\n')
                # SOURCE LINE 65
                if app_element.status == 3:
                    # SOURCE LINE 66
                    __M_writer(u'                    <td align="right"><i><b>')
                    __M_writer(escape(c.element_price[app_element.id]))
                    __M_writer(u' / ')
                    __M_writer(escape(c.element_pricep[app_element.id]))
                    __M_writer(u'</b></i></td>\r\n')
                    # SOURCE LINE 67
                else:
                    # SOURCE LINE 68
                    __M_writer(u'                    <td align="right">')
                    __M_writer(escape(c.element_price[app_element.id]))
                    __M_writer(u' / ')
                    __M_writer(escape(c.element_pricep[app_element.id]))
                    __M_writer(u'</td>\r\n')
                    pass
                pass
            # SOURCE LINE 71
            __M_writer(u'            <td>')
            __M_writer(escape(app_element.finsources.name))
            __M_writer(u'</td>                \r\n            <td>')
            # SOURCE LINE 72
            __M_writer(escape(app_element.needss.name))
            __M_writer(u'</td>\r\n            <td>\r\n')
            # SOURCE LINE 74
            for place in c.available_groups:
                # SOURCE LINE 75
                if place[0] == app_element.place:
                    # SOURCE LINE 76
                    __M_writer(u'                            ')
                    __M_writer(escape(place[1]))
                    __M_writer(u'\r\n')
                    pass
                pass
            # SOURCE LINE 79
            __M_writer(u'            </td>\r\n            <td>')
            # SOURCE LINE 80
            __M_writer(escape(app_element.note))
            __M_writer(u'</td>\r\n            <td>\r\n')
            # SOURCE LINE 82
            if app_element.status == 1:
                # SOURCE LINE 83
                __M_writer(u'                    \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 85
            if app_element.status == 2:
                # SOURCE LINE 86
                __M_writer(u'                    \u0417\u0430\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 88
            if app_element.status == 3:
                # SOURCE LINE 89
                __M_writer(u'                    \u0423\u0434\u0430\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 91
            if app_element.status == 4:
                # SOURCE LINE 92
                __M_writer(u'                    \u0423\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 94
            if app_element.status == 5:
                # SOURCE LINE 95
                __M_writer(u'                    \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 97
            if app_element.status == 6:
                # SOURCE LINE 98
                __M_writer(u'                    \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e, \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 100
            if app_element.status == 7:
                # SOURCE LINE 101
                __M_writer(u'                    \u0417\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e, \u0437\u0430\u043c\u0435\u043d\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 103
            if app_element.status == 8:
                # SOURCE LINE 104
                __M_writer(u'                    \u041d\u0435 \u0437\u0430\u043a\u0443\u043f\u043b\u0435\u043d\u043e\r\n')
                pass
            # SOURCE LINE 106
            __M_writer(u'            </td>\r\n        </tr>\r\n')
            pass
        # SOURCE LINE 109
        __M_writer(u'    \r\n        <tr>\r\n            <td></td>\r\n            <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n')
        # SOURCE LINE 120
        if c.current_app.status == 1:
            # SOURCE LINE 121
            __M_writer(u'                <td align="right">')
            __M_writer(escape(c.total_price))
            __M_writer(u'</td>\r\n')
            pass
        # SOURCE LINE 123
        if c.current_app.status in (2,3,4):
            # SOURCE LINE 124
            __M_writer(u'                <td align="right">')
            __M_writer(escape(c.total_price))
            __M_writer(u' / ')
            __M_writer(escape(c.total_pricep))
            __M_writer(u'</td>\r\n')
            pass
        # SOURCE LINE 126
        __M_writer(u'            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n        </tr>\r\n    </table>\r\n        \r\n<br />')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        app_globals = context.get('app_globals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n    <h2>\u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 ')
        # SOURCE LINE 5
        __M_writer(escape(c.year))
        __M_writer(u' \u0433\u043e\u0434.</h2>\r\n    <b>\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a: ')
        # SOURCE LINE 6
        __M_writer(escape(app_globals.user_view))
        __M_writer(u'</b><br />\r\n    <b>\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435: ')
        # SOURCE LINE 7
        __M_writer(escape(app_globals.user_group))
        __M_writer(u'</b>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043a\u0430')
        return ''
    finally:
        context.caller_stack._pop_frame()


