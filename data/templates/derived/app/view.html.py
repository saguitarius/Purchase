# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1301594330.4530001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/app/view.html'
_template_uri='/derived/app/view.html'
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
        __M_writer(u'<br />\r\n<b>\u0413\u043e\u0434:</b> ')
        # SOURCE LINE 9
        __M_writer(escape(c.current_app.year))
        __M_writer(u'<br />\r\n<b>\u0421\u0442\u0430\u0442\u0443\u0441:</b> ')
        # SOURCE LINE 10
        __M_writer(escape(c.current_app.status))
        __M_writer(u'<br />\r\n<b>campaign_id:</b> ')
        # SOURCE LINE 11
        __M_writer(escape(c.current_app.campaign_id))
        __M_writer(u'<br />\r\n<b>\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:</b> ')
        # SOURCE LINE 12
        __M_writer(escape(c.current_app.info))
        __M_writer(u'<br />\r\n<b>\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f:</b> ')
        # SOURCE LINE 13
        __M_writer(escape(c.current_app.created))
        __M_writer(u'<br />\r\n<b>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f:</b> ')
        # SOURCE LINE 14
        __M_writer(escape(c.current_app.edited))
        __M_writer(u'<br />\r\n\r\n<h2>\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438</h2>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0417\u0430\u044f\u0432\u043a\u0430</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043a\u0438')
        return ''
    finally:
        context.caller_stack._pop_frame()


