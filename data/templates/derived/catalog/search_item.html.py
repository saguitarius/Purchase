# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306330540.4360001
_template_filename='D:\\PyProjects\\Purchase\\purchase\\templates/derived/catalog/search_item.html'
_template_uri='/derived/catalog/search_item.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'search_results']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'catalog', context._clean_inheritance_tokens(), templateuri=u'/derived/catalog/catalog.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'catalog')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'catalog')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        search = _import_ns.get('search', context.get('search', UNDEFINED))
        all_sections = _import_ns.get('all_sections', context.get('all_sections', UNDEFINED))
        def search_results():
            return render_search_results(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n<h3><a href="')
        # SOURCE LINE 4
        __M_writer(escape(h.url(controller='catalog', action='section', id='1')))
        __M_writer(u'">\u041a\u0430\u0442\u0430\u043b\u043e\u0433</a> > \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430</h3>\r\n    <div id="yui-main">\r\n        <div class="yui-b">\r\n             ')
        # SOURCE LINE 7
        __M_writer(escape(search_results()))
        __M_writer(u'     \r\n        </div>\r\n    </div>\r\n    <div class="yui-b">\r\n        ')
        # SOURCE LINE 11
        __M_writer(escape(all_sections()))
        __M_writer(u'\r\n        ')
        # SOURCE LINE 12
        __M_writer(escape(search()))
        __M_writer(u'\r\n    </div>\r\n\r\n')
        # SOURCE LINE 17
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'catalog')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\r\n    <h1 class="main">\u041a\u0430\u0442\u0430\u043b\u043e\u0433</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_results(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'catalog')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\r\n        <p><b>\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430:</b></p>\r\n        <table border="1" width="100%">\r\n            <tr>\r\n                <th>\u041c\u0430\u0440\u043a\u0430</th>\r\n                <th>\u041c\u043e\u0434\u0435\u043b\u044c</th>\r\n                <th>\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</th>\r\n                <th>\u0426\u0435\u043d\u0430</th>\r\n                <th>\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f</th>\r\n')
        # SOURCE LINE 28
        if (c.current_app_status == 1) and h.auth.authorized(h.auth.is_valid_user) and (not h.auth.authorized(h.auth.has_admin_role)):
            # SOURCE LINE 29
            __M_writer(u'                    <th>\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c<br />\u0432 \u0437\u0430\u044f\u0432\u043a\u0443</th>\r\n')
            pass
        # SOURCE LINE 31
        if h.auth.authorized(h.auth.has_admin_role):
            # SOURCE LINE 32
            __M_writer(u'                    <th>\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f</th>\r\n')
            pass
        # SOURCE LINE 34
        __M_writer(u'            </tr>\r\n')
        # SOURCE LINE 35
        for item in c.search_results :
            # SOURCE LINE 36
            __M_writer(u'            <tr>\r\n                <td>')
            # SOURCE LINE 37
            __M_writer(escape(item.brand))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 38
            __M_writer(escape(item.model))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 39
            __M_writer(escape(item.description))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 40
            __M_writer(escape(item.price))
            __M_writer(u'</td>\r\n                <td>')
            # SOURCE LINE 41
            __M_writer(escape(item.edited))
            __M_writer(u'</td>\r\n')
            # SOURCE LINE 42
            if (c.current_app_status == 1) and h.auth.authorized(h.auth.is_valid_user) and (not h.auth.authorized(h.auth.has_admin_role)):
                # SOURCE LINE 43
                __M_writer(u'                    <th><a href="')
                __M_writer(escape(h.url(controller='app', action='add_item', id=item.id,)))
                __M_writer(u'">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c</a></th>\r\n')
                pass
            # SOURCE LINE 45
            if h.auth.authorized(h.auth.has_admin_role):
                # SOURCE LINE 46
                __M_writer(u'                    <td><a href="')
                __M_writer(escape(h.url(controller='catalog', action='edit_item', id=item.id)))
                __M_writer(u'">\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c</a>\r\n                        <a href="')
                # SOURCE LINE 47
                __M_writer(escape(h.url(controller='catalog', action='delete_item', id=item.id)))
                __M_writer(u'">\u0423\u0434\u0430\u043b\u0438\u0442\u044c</a></td>\r\n')
                pass
            # SOURCE LINE 49
            __M_writer(u'            </tr>\r\n')
            pass
        # SOURCE LINE 51
        __M_writer(u'        </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


