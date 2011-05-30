# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306410381.849
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/campaign/new.html'
_template_uri='/derived/campaign/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading']


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
        __M_writer(u'\r\n\r\n<p>\u0424\u043e\u0440\u043c\u0430\u0442 \u0434\u0430\u0442\u044b: <i>\u0434\u0434.\u043c\u043c.\u0433\u0433\u0433\u0433</i></p>\r\n\r\n')
        # SOURCE LINE 5
        __M_writer(escape(h.form_start(h.url(controller='campaign', action='create'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
        u"Дата начала",
        h.text(name='start_date'),
        required=True,
    )))
        # SOURCE LINE 10
        __M_writer(u'\r\n    ')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
        u"Дата окончания",
        h.text(name='end_date'),
        required=True,
    )))
        # SOURCE LINE 15
        __M_writer(u'\r\n    ')
        # SOURCE LINE 16
        __M_writer(escape(h.field(
        u"Описание",
        h.textarea(name='description', rows=3, cols=40),
        required=True,
    )))
        # SOURCE LINE 20
        __M_writer(u'  \r\n    \r\n    <table border="1" width="500">\r\n    <h3>\u041b\u0438\u043c\u0438\u0442\u044b \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f\u043c</h3>\r\n        <tr>\r\n            <th>\u2116</th>\r\n            <th>\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435</th>\r\n            <th width="100">\u041b\u0438\u043c\u0438\u0442 (\u0440\u0443\u0431.)</th>\r\n        </tr>\r\n    ')
        # SOURCE LINE 29
        counter=0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\r\n')
        # SOURCE LINE 30
        for group in c.users.list_groups():
            # SOURCE LINE 31
            if not (c.users.group_name(group) == 'admin'):
                # SOURCE LINE 32
                __M_writer(u'            ')
                counter += 1 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\r\n            <tr>\r\n                <td>')
                # SOURCE LINE 34
                __M_writer(escape(counter))
                __M_writer(u'</td>\r\n                <td>')
                # SOURCE LINE 35
                __M_writer(escape(c.users.group_view(group)))
                __M_writer(u'</td>\r\n                <td>\r\n                    ')
                # SOURCE LINE 37
                __M_writer(escape(h.text(name='limit%s'%(c.users.group_uid(group)), required=True,)))
                __M_writer(u'           \r\n                </td>\r\n            </tr>\r\n')
                pass
            pass
        # SOURCE LINE 42
        __M_writer(u'    </table>\r\n    \r\n    ')
        # SOURCE LINE 44
        __M_writer(escape(h.field(field=h.submit(value=u"Создать", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 45
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\r\n    <h1 class="main">\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u043e\u0439 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


