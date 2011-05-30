# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306738705.5039999
_template_filename=u'D:\\PyProjects\\Purchase\\purchase\\templates/base/index_print.html'
_template_uri=u'/base/index_print.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['account', 'campaign', 'title', 'tabs', 'head', 'header', 'heading']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\r\n"http://www.w3.org/TR/html4/strict.dtd">\r\n<html>\r\n<head>\r\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n    <title>')
        # SOURCE LINE 8
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\r\n    ')
        # SOURCE LINE 9
        __M_writer(escape(self.head()))
        __M_writer(u'\r\n    \r\n</head>\r\n<body class="yui-skin-sam">\r\n    <div id="doc3" class="yui-t3">\r\n        <div id="hd">        \r\n            ')
        # SOURCE LINE 15
        __M_writer(escape(self.heading()))
        __M_writer(u'\r\n        </div>\r\n\r\n        <div id="bd">\r\n            ')
        # SOURCE LINE 19
        __M_writer(escape(next.body()))
        __M_writer(u'\r\n        </div>\r\n    </div>\r\n</body>\r\n</html>\r\n\r\n\r\n')
        # SOURCE LINE 34
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 48
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 52
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 58
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 62
        __M_writer(u'\r\n\r\n\r\n')
        # SOURCE LINE 67
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app_globals = context.get('app_globals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\r\n')
        # SOURCE LINE 27
        if h.auth.authorized(h.auth.is_valid_user) and not (request.urlvars['controller'] == 'account' and request.urlvars['action'] == 'signout'):
            # SOURCE LINE 28
            __M_writer(u'        <p>\u0412\u044b \u0432\u043e\u0448\u043b\u0438 \u043a\u0430\u043a <b>')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u'</b>,\r\n            ')
            # SOURCE LINE 29
            __M_writer(escape(app_globals.user_view))
            __M_writer(u'. \u0413\u0440\u0443\u043f\u043f\u0430: ')
            __M_writer(escape(app_globals.user_group))
            __M_writer(u'. \r\n            <a href="')
            # SOURCE LINE 30
            __M_writer(escape(h.url('signout')))
            __M_writer(u'"><b>\u0412\u044b\u0439\u0442\u0438</b></a></p>\r\n')
            # SOURCE LINE 31
        else:
            # SOURCE LINE 32
            __M_writer(u'        <p><a href="')
            __M_writer(escape(h.url('signin')))
            __M_writer(u'"><b>\u0412\u043e\u0439\u0442\u0438</b></a></p>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_campaign(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app_globals = context.get('app_globals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\r\n')
        # SOURCE LINE 37
        if h.auth.authorized(h.auth.is_valid_user):
            # SOURCE LINE 38
            if (app_globals.current_campaign_id == 0) and (app_globals.finished_active_campaign_id == 0):
                # SOURCE LINE 39
                __M_writer(u'                <p>\u0412 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u043d\u0435 \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0439.</p>\r\n')
                pass
            # SOURCE LINE 41
            if (app_globals.current_campaign_id != 0) and (app_globals.finished_active_campaign_id == 0):
                # SOURCE LINE 42
                __M_writer(u'                <p>\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u0430 \u0437\u0430\u044f\u0432\u043e\u0447\u043d\u0430\u044f \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044f \u2116 ')
                __M_writer(escape(app_globals.current_campaign_id))
                __M_writer(u'. \u0421\u0440\u043e\u043a \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f: \u0441 <b>')
                __M_writer(escape(app_globals.current_campaign_start_date))
                __M_writer(u'</b> \u043f\u043e <b>')
                __M_writer(escape(app_globals.current_campaign_end_date))
                __M_writer(u'</b>.</p>\r\n')
                pass
            # SOURCE LINE 44
            if app_globals.finished_active_campaign_id != 0:
                # SOURCE LINE 45
                __M_writer(u'                <p>\u0417\u0430\u044f\u0432\u043e\u0447\u043d\u0430\u044f \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u044f \u2116 ')
                __M_writer(escape(app_globals.finished_active_campaign_id))
                __M_writer(u' \u043e\u043a\u043e\u043d\u0447\u0435\u043d\u0430. \u0421\u0440\u043e\u043a \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f: \u0441 <b>')
                __M_writer(escape(app_globals.finished_active_campaign_start_date))
                __M_writer(u'</b> \u043f\u043e <b>')
                __M_writer(escape(app_globals.finished_active_campaign_end_date))
                __M_writer(u'</b>.</p>\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\r\n    \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043a\u0443\u043f\u043a\u0430\u043c\u0438\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app_globals = context.get('app_globals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\r\n<div id="maintabs">\r\n<ul class="draglist">\r\n\r\n')
        # SOURCE LINE 73
        if h.auth.authorized(h.auth.is_valid_user):
            # SOURCE LINE 74
            __M_writer(u'        <li><a href="')
            __M_writer(escape(h.url('/')))
            __M_writer(u'">\u041a\u0430\u0442\u0430\u043b\u043e\u0433</a></li>\r\n')
            # SOURCE LINE 75
            if not h.auth.authorized(h.auth.has_admin_role):
                # SOURCE LINE 76
                if app_globals.current_campaign_id != 0:
                    # SOURCE LINE 77
                    __M_writer(u'                <li><a href="')
                    __M_writer(escape(h.url(controller='app', action='user_app')))
                    __M_writer(u'">\u0417\u0430\u044f\u0432\u043a\u0430</a></li>\r\n')
                    pass
                # SOURCE LINE 79
                if app_globals.current_campaign_id == 0:
                    # SOURCE LINE 80
                    __M_writer(u'                <li>\u0417\u0430\u044f\u0432\u043a\u0430</li>\r\n')
                    pass
                pass
            # SOURCE LINE 83
            if h.auth.authorized(h.auth.has_admin_role):
                # SOURCE LINE 84
                __M_writer(u'            <li><a href="')
                __M_writer(escape(h.url(controller='account', action='index')))
                __M_writer(u'">\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438</a></li> \r\n')
                pass
            # SOURCE LINE 86
            if h.auth.authorized(h.auth.has_boss_role):
                # SOURCE LINE 87
                if app_globals.current_campaign_id != 0:
                    # SOURCE LINE 88
                    __M_writer(u'                <li><a href="')
                    __M_writer(escape(h.url(controller='app', action='group_app')))
                    __M_writer(u'">\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u0443</a></li> \r\n')
                    pass
                # SOURCE LINE 90
                if app_globals.current_campaign_id == 0:
                    # SOURCE LINE 91
                    __M_writer(u'                <li>\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u0443</li>\r\n')
                    pass
                pass
            # SOURCE LINE 94
            if h.auth.authorized(h.auth.has_director_role):
                # SOURCE LINE 95
                if app_globals.current_campaign_id != 0:
                    # SOURCE LINE 96
                    __M_writer(u'                <li><a href="')
                    __M_writer(escape(h.url(controller='app', action='global_app')))
                    __M_writer(u'">\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e</a></li>\r\n                <li><a href="')
                    # SOURCE LINE 97
                    __M_writer(escape(h.url(controller='app', action='sale_app')))
                    __M_writer(u'">\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438</a></li>\r\n')
                    pass
                # SOURCE LINE 99
                if app_globals.current_campaign_id == 0:
                    # SOURCE LINE 100
                    __M_writer(u'                <li>\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044e</li>\r\n                <li>\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438</li>\r\n')
                    pass
                # SOURCE LINE 103
                __M_writer(u'            <li><a href="')
                __M_writer(escape(h.url(controller='campaign', action='index')))
                __M_writer(u'">\u041a\u0430\u043c\u043f\u0430\u043d\u0438\u0438</a></li>\r\n')
                pass
            pass
        # SOURCE LINE 106
        __M_writer(u'</ul>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\r\n    ')
        # SOURCE LINE 55
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/reset-fonts-grids/reset-fonts-grids.css'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 56
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/base/base-min.css'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 57
        __M_writer(escape(h.stylesheet_link(h.url('/css/main_print.css'))))
        __M_writer(u'                                     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\r\n    <a name="top"></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\r\n    <h1>')
        # SOURCE LINE 66
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


