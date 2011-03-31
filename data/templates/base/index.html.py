# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1301580488.05
_template_filename=u'D:\\PyProjects\\Purchase\\purchase\\templates/base/index.html'
_template_uri=u'/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['account', 'campaign', 'title', 'footer', 'head', 'header', 'heading']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\r\n"http://www.w3.org/TR/html4/strict.dtd">\r\n<html>\r\n<head>\r\n    <title>')
        # SOURCE LINE 7
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\r\n    ')
        # SOURCE LINE 8
        __M_writer(escape(self.head()))
        __M_writer(u'\r\n</head>\r\n<body>\r\n    ')
        # SOURCE LINE 11
        __M_writer(escape(self.account()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 12
        __M_writer(escape(self.campaign()))
        __M_writer(u'\r\n    <hr>\r\n    ')
        # SOURCE LINE 14
        __M_writer(escape(self.heading()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 15
        __M_writer(escape(self.header()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 16
        __M_writer(escape(next.body()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 17
        __M_writer(escape(self.footer()))
        __M_writer(u'\r\n</body>\r\n</html>\r\n\r\n\r\n')
        # SOURCE LINE 29
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 38
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 42
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 45
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 49
        __M_writer(u'\r\n\r\n\r\n')
        # SOURCE LINE 54
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\r\n')
        # SOURCE LINE 23
        if h.auth.authorized(h.auth.is_valid_user) and not (request.urlvars['controller'] == 'account' and request.urlvars['action'] == 'signout'):
            # SOURCE LINE 24
            __M_writer(u'        <p>\u0412\u044b \u0432\u043e\u0448\u043b\u0438 \u043a\u0430\u043a <b><a href="')
            __M_writer(escape(h.url(controller='account', action='cabinet')))
            __M_writer(u'">')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u'</a></b>,\r\n            <a href="')
            # SOURCE LINE 25
            __M_writer(escape(h.url('signout')))
            __M_writer(u'">\u0412\u044b\u0439\u0442\u0438</a></p>\r\n')
            # SOURCE LINE 26
        else:
            # SOURCE LINE 27
            __M_writer(u'        <p><a href="')
            __M_writer(escape(h.url('signin')))
            __M_writer(u'">\u0412\u043e\u0439\u0442\u0438</a></p>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_campaign(context):
    context.caller_stack._push_frame()
    try:
        app_globals = context.get('app_globals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\r\n    \r\n')
        # SOURCE LINE 33
        if (app_globals.current_campaign_id == 0):
            # SOURCE LINE 34
            __M_writer(u'        <p>\u0412 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u043d\u0435 \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0439, id = ')
            __M_writer(escape(app_globals.current_campaign_id))
            __M_writer(u'</p>\r\n')
            # SOURCE LINE 35
        else:
            # SOURCE LINE 36
            __M_writer(u'        <p>\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u0430 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u0430\u044f \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044f, id = ')
            __M_writer(escape(app_globals.current_campaign_id))
            __M_writer(u'. \u0421\u0440\u043e\u043a \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f: \u0441 <b>')
            __M_writer(escape(app_globals.current_campaign_start_date))
            __M_writer(u'</b> \u043f\u043e <b>')
            __M_writer(escape(app_globals.current_campaign_end_date))
            __M_writer(u'</b>.</p>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\r\n    \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043a\u0443\u043f\u043a\u0430\u043c\u0438\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\r\n    <p>\r\n        <a href="')
        # SOURCE LINE 58
        __M_writer(escape(h.url('/')))
        __M_writer(u'">[\u041a\u0430\u0442\u0430\u043b\u043e\u0433]</a> |\r\n        <a href="')
        # SOURCE LINE 59
        __M_writer(escape(h.url(controller='app', action='index')))
        __M_writer(u'">[\u0417\u0430\u044f\u0432\u043a\u0430]</a> |  \r\n        <a href="')
        # SOURCE LINE 60
        __M_writer(escape(h.url(controller='campaign', action='index')))
        __M_writer(u'">[\u041a\u0430\u043c\u043f\u0430\u043d\u0438\u0438]</a> |     \r\n        <a href="')
        # SOURCE LINE 61
        __M_writer(escape(h.url(controller='account', action='index')))
        __M_writer(u'">[\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438]</a> |  \r\n        <a href="#top">[\u041d\u0430\u0432\u0435\u0440\u0445]</a>\r\n    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\r\n    <a name="top"></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\r\n    <h1>')
        # SOURCE LINE 53
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


