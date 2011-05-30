# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306412160.9159999
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/campaign/settings.html'
_template_uri='/derived/campaign/settings.html'
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
        __M_writer(u'\r\n\r\n<h2>\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f</h2>\r\n    <table border="1" width="400">\r\n    <tr>\r\n        <th>\u2116</th>\r\n        <th>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</th>\r\n        <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435</th>\r\n    </tr>\r\n    ')
        # SOURCE LINE 13
 
        count = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 15
        __M_writer(u'\r\n')
        # SOURCE LINE 16
        for unit in c.available_units:
            # SOURCE LINE 17
            __M_writer(u'        ')
 
            count += 1
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 19
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 21
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 22
            __M_writer(escape(unit[1]))
            __M_writer(u'</td>\r\n            <td><a href="">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>   \r\n        </tr>\r\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'    \r\n')
        # SOURCE LINE 27
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='add_unit'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 28
        __M_writer(escape(h.field(
        u"Единица измерения",
        h.text(name='brand'),
        required=True,
    )))
        # SOURCE LINE 32
        __M_writer(u'\r\n    ')
        # SOURCE LINE 33
        __M_writer(escape(h.field(field=h.submit(value=u"Добавить", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 34
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n<h2>\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438 \u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</h2>\r\n    <table border="1" width="400">\r\n    <tr>\r\n        <th>\u2116</th>\r\n        <th>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</th>\r\n        <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435</th>\r\n    </tr>\r\n    ')
        # SOURCE LINE 43
 
        count = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 45
        __M_writer(u'\r\n')
        # SOURCE LINE 46
        for finsource in c.available_finsource:
            # SOURCE LINE 47
            __M_writer(u'        ')
 
            count += 1
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 49
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 51
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 52
            __M_writer(escape(finsource[1]))
            __M_writer(u'</td>\r\n            <td><a href="">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>   \r\n        </tr>\r\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'    \r\n')
        # SOURCE LINE 57
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='add_finsource'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 58
        __M_writer(escape(h.field(
        u"Источник финансирования",
        h.text(name='brand'),
        required=True,
    )))
        # SOURCE LINE 62
        __M_writer(u'\r\n    ')
        # SOURCE LINE 63
        __M_writer(escape(h.field(field=h.submit(value=u"Добавить", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 64
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n<h2>\u041d\u0443\u0436\u0434\u044b</h2>\r\n    <table border="1" width="400">\r\n    <tr>\r\n        <th>\u2116</th>\r\n        <th>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</th>\r\n        <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435</th>\r\n    </tr>\r\n    ')
        # SOURCE LINE 73
 
        count = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 75
        __M_writer(u'\r\n')
        # SOURCE LINE 76
        for need in c.available_needs:
            # SOURCE LINE 77
            __M_writer(u'        ')
 
            count += 1
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 79
            __M_writer(u'\r\n        <tr>\r\n            <td>')
            # SOURCE LINE 81
            __M_writer(escape(count))
            __M_writer(u'</td>\r\n            <td>')
            # SOURCE LINE 82
            __M_writer(escape(need[1]))
            __M_writer(u'</td>\r\n            <td><a href="">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>   \r\n        </tr>\r\n')
            pass
        # SOURCE LINE 86
        __M_writer(u'    \r\n')
        # SOURCE LINE 87
        __M_writer(escape(h.form_start(h.url(controller='catalog', action='add_need'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 88
        __M_writer(escape(h.field(
        u"Нужды",
        h.text(name='brand'),
        required=True,
    )))
        # SOURCE LINE 92
        __M_writer(u'\r\n    ')
        # SOURCE LINE 93
        __M_writer(escape(h.field(field=h.submit(value=u"Добавить", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 94
        __M_writer(escape(h.form_end()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438')
        return ''
    finally:
        context.caller_stack._pop_frame()


