# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1304520060.358
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/campaign/view.html'
_template_uri='/derived/campaign/view.html'
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
        __M_writer(u'\r\n\r\n<h2>\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044f</h2>\r\n')
        # SOURCE LINE 7
        if c.current_campaign:
            # SOURCE LINE 8
            __M_writer(u'    <p>\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430: ')
            __M_writer(escape(c.current_campaign.start_date))
            __M_writer(u'</p>\r\n    <p>\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f: ')
            # SOURCE LINE 9
            __M_writer(escape(c.current_campaign.end_date))
            __M_writer(u'</p>\r\n    <p>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: ')
            # SOURCE LINE 10
            __M_writer(escape(c.current_campaign.description))
            __M_writer(u'</p>\r\n    <p><a href="')
            # SOURCE LINE 11
            __M_writer(escape(h.url(controller='campaign', action='info', id=c.current_campaign.id)))
            __M_writer(u'">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</a></p>\r\n')
            # SOURCE LINE 12
            if c.current_campaign.status == 1:
                # SOURCE LINE 13
                __M_writer(u'        <p><a href="')
                __M_writer(escape(h.url(controller='campaign', action='stop', id=c.current_campaign.id)))
                __M_writer(u'">\u041f\u0440\u0435\u043a\u0440\u0430\u0442\u0438\u0442\u044c \u043f\u043e\u0434\u0430\u0447\u0443 \u0437\u0430\u044f\u0432\u043e\u043a</a></p>\r\n')
                pass
            # SOURCE LINE 15
        else:
            # SOURCE LINE 16
            if c.finished_active_campaign:
                # SOURCE LINE 17
                if c.finished_active_campaign.status == 2:
                    # SOURCE LINE 18
                    __M_writer(u'            <p><a href="')
                    __M_writer(escape(h.url(controller='campaign', action='end', id=c.finished_active_campaign.id)))
                    __M_writer(u'">\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044e</a></p>\r\n')
                    pass
                # SOURCE LINE 20
            else:
                # SOURCE LINE 21
                __M_writer(u'    \u0412 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u0430\u044f \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044f \u043d\u0435 \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u0430. <a href="')
                __M_writer(escape(h.url(controller='campaign', action='new')))
                __M_writer(u'">\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u043e\u0439 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</a>\r\n')
                pass
            pass
        # SOURCE LINE 24
        __M_writer(u'<br />\r\n\r\n<h3>\u041f\u0440\u043e\u0448\u0435\u0434\u043d\u0438\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</h3>\r\n')
        # SOURCE LINE 27
        if c.finished_inactive_campaign == []:
            # SOURCE LINE 28
            __M_writer(u'    \u041d\u0435\u0442 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0439 \u0434\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\r\n')
            # SOURCE LINE 29
        else:
            # SOURCE LINE 30
            for campaign in c.finished_inactive_campaign:
                # SOURCE LINE 31
                __M_writer(u'        <p>\r\n            <b>\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:</b> ')
                # SOURCE LINE 32
                __M_writer(escape(campaign.id))
                __M_writer(u'<br />\r\n            <b>\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430:</b> ')
                # SOURCE LINE 33
                __M_writer(escape(campaign.start_date))
                __M_writer(u'<br />\r\n            <b>\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f:</b> ')
                # SOURCE LINE 34
                __M_writer(escape(campaign.end_date))
                __M_writer(u'<br />\r\n            <b>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:</b> ')
                # SOURCE LINE 35
                __M_writer(escape(campaign.description))
                __M_writer(u'<br />\r\n            <a href="')
                # SOURCE LINE 36
                __M_writer(escape(h.url(controller='campaign', action='info', id=campaign.id)))
                __M_writer(u'">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</a>\r\n        </p>\r\n        <br />\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>\u0417\u0430\u044f\u0432\u043e\u0447\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u0417\u0430\u044f\u0432\u043e\u0447\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438')
        return ''
    finally:
        context.caller_stack._pop_frame()


