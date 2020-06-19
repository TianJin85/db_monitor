# # Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# # Copyright: (c) <spug.dev@gmail.com>
# # Released under the MIT License.
# from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter
# from consumer import routing, executors
#
# application = ProtocolTypeRouter({
#     'channel': ChannelNameRouter({
#         'ssh_exec': executors.SSHExecutor,
#     }),
#     'websocket': URLRouter(
#         routing.websocket_urlpatterns
#     )
# })



from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
import pxectrl.routing
import webssh.routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # 【channels】（第6步）添加路由配置指向应用的路由模块
    'websocket': SessionMiddlewareStack(  # 使用Session中间件，可以请求中session的值
        # 一个url
        # URLRouter(
        #     pxectrl.routing.websocket_urlpatterns,
        # ),
        # 多个url合并一起使用，多个子路由列表相加
        URLRouter(
            pxectrl.routing.websocket_urlpatterns + webssh.routing.websocket_urlpatterns,
        ),
    ),
})