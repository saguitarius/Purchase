# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306414379.6800001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/group_view.html'
_template_uri='/derived/app/group_view.html'
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
        __M_writer(u'\r\n\r\n    <table border="1" width="100%">\r\n        <tr>\r\n            <th rowspan="2" width="15">     \u2116</th>\r\n            <th rowspan="2" width="200">    \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</th>\r\n            <th rowspan="2" width="50">     \u0415\u0434. \u0418\u0437\u043c</th>\r\n            <th colspan="4">                \u041a\u0432\u0430\u0440\u0442\u0430\u043b</th>\r\n            <th rowspan="2" width="70">     \u041e\u0431\u0449\u0435\u0435<br />\u043a\u043e\u043b-\u0432\u043e</th>\r\n            <th rowspan="2" width="40">     \u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)</th>\r\n            <th rowspan="2" width="70">     \u0421\u0443\u043c\u043c\u0430 (\u0440\u0443\u0431.)</th>\r\n            <th rowspan="2" width="80">     \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a<br />\u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</th>\r\n            <th rowspan="2" width="80">     \u0414\u043b\u044f \u043a\u0430\u043a\u0438\u0445 \u043d\u0443\u0436\u0434</th>\r\n            <th rowspan="2" width="80">     \u041c\u0435\u0441\u0442\u043e<br />\u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f</th>\r\n            <th rowspan="2" width="120">    \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435</th>\r\n            <th rowspan="2" width="120">    \u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n        </tr>\r\n        <tr>\r\n            <th width="50">1</th> \r\n            <th width="50">2</th>\r\n            <th width="50">3</th>\r\n            <th width="50">4</th>               \r\n        </tr>\r\n    ')
        # SOURCE LINE 27
 
        count = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 29
        __M_writer(u'\r\n')
        # SOURCE LINE 30
        for app_element in c.group_app_elements:
            # SOURCE LINE 31
            __M_writer(u'        ')
 
            count += 1
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 33
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 35
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n            <td>\r\n                ')
            # SOURCE LINE 37
            __M_writer(escape(app_element.items.brand))
            __M_writer(u' ')
            __M_writer(escape(app_element.items.model))
            __M_writer(u'\r\n            </td>\r\n            <td>')
            # SOURCE LINE 39
            __M_writer(escape(app_element.items.units.name))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 40
            __M_writer(escape(app_element.quarter1))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 41
            __M_writer(escape(app_element.quarter2))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 42
            __M_writer(escape(app_element.quarter3))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 43
            __M_writer(escape(app_element.quarter4))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 44
            __M_writer(escape(app_element.amount))
            __M_writer(u'</td>\r\n            <td align="right">')
            # SOURCE LINE 45
            __M_writer(escape(app_element.items.price))
            __M_writer(u'</td>\r\n            <td align="right">\r\n')
            # SOURCE LINE 47
            if app_element.status == 3:
                # SOURCE LINE 48
                __M_writer(u'                    <i><b>')
                __M_writer(escape(app_element.price))
                __M_writer(u'</b></i>\r\n')
                # SOURCE LINE 49
            else:
                # SOURCE LINE 50
                __M_writer(u'                    ')
                __M_writer(escape(app_element.price))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 52
            __M_writer(u'            </td>\r\n            <td>')
            # SOURCE LINE 53
            __M_writer(escape(app_element.finsources.name))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 54
            __M_writer(escape(app_element.needss.name))
            __M_writer(u'</td>\r\n            <td>\r\n')
            # SOURCE LINE 57
            for place in c.available_groups:
                # SOURCE LINE 58
                if place[0] == app_element.place:
                    # SOURCE LINE 59
                    __M_writer(u'                        ')
                    __M_writer(escape(place[1]))
                    __M_writer(u'\r\n')
                    pass
                pass
            # SOURCE LINE 62
            __M_writer(u'            </td>\r\n            <td>')
            # SOURCE LINE 63
            __M_writer(escape(app_element.note))
            __M_writer(u'</td>\r\n            <th>\r\n')
            # SOURCE LINE 65
            if (app_element.status == 0) or (app_element.status == 1) or (app_element.status == 2):
                # SOURCE LINE 66
                __M_writer(u'                    <a href="')
                __M_writer(escape(h.url(controller='app', action='edit_item_group_form', id=app_element.id)))
                __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a> \r\n                    <a href="')
                # SOURCE LINE 67
                __M_writer(escape(h.url(controller='app', action='change_item_group_form', id=app_element.id)))
                __M_writer(u'">\u0417\u0430\u043c\u0435\u043d\u0438\u0442\u044c</a><br />\r\n                    <a href="')
                # SOURCE LINE 68
                __M_writer(escape(h.url(controller='app', action='delete_item_group', id=app_element.id)))
                __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a><br />\r\n')
                pass
            # SOURCE LINE 70
            __M_writer(u'                </form>\r\n')
            # SOURCE LINE 71
            if app_element.status == 3:
                # SOURCE LINE 72
                __M_writer(u'                    <a href="')
                __M_writer(escape(h.url(controller='app', action='restore_item_group', id=app_element.id)))
                __M_writer(u'">\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c</a><br />\r\n')
                pass
            # SOURCE LINE 74
            __M_writer(u'            </th>           \r\n        </tr>\r\n')
            pass
        # SOURCE LINE 77
        __M_writer(u'    \r\n        <tr>\r\n            <td></td>\r\n            <th>\u0418\u0442\u043e\u0433\u043e:</th>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td align="right">')
        # SOURCE LINE 88
        __M_writer(escape(c.total_price))
        __M_writer(u'</td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n            <td></td>\r\n        </tr>\r\n    </table>\r\n        \r\n<p>\u041b\u0438\u043c\u0438\u0442 \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044e ')
        # SOURCE LINE 97
        __M_writer(escape(c.boss_group_view))
        __M_writer(u' \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442: <b>')
        __M_writer(escape(c.limit.limit_value))
        __M_writer(u' \u0440\u0443\u0431</b>.</p><br />\r\n        \r\n<p><a href="')
        # SOURCE LINE 99
        __M_writer(escape(h.url(controller='app', action='app_to_director')))
        __M_writer(u'">\u0423\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443 \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044e ')
        __M_writer(escape(c.boss_group_view))
        __M_writer(u'</a></p>\r\n<p><img src="/print.png"></img> <a href="')
        # SOURCE LINE 100
        __M_writer(escape(h.url(controller='app', action='group_app_print')))
        __M_writer(u'">\u0412\u0435\u0440\u0441\u0438\u044f \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044e ')
        __M_writer(escape(c.boss_group_view))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044e ')
        __M_writer(escape(c.boss_group_view))
        return ''
    finally:
        context.caller_stack._pop_frame()


