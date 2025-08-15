# Template-Config  

自用Mihomo、Singbox配置模板及分流规则，不提供Fake-ip配置  

因为我使用的是docker版的控制面板，所以模板没有ui名称、路径、下载地址等信息，如有需要请自行查看内核文档进行添加  

[Mihomo配置模板](https://github.com/xiaojimie/Template-Config/blob/main/config/mihomo/smart-ruleset.yaml)  

[Singbox配置模板](https://github.com/xiaojimie/Template-Config/blob/main/config/singbox/momo-ruleset.json)  

Singbox配置的思路和Mihomo基本一致，区别在于Singbox规则没有no-resolve功能，因此某些谷歌/CF CDN网站可能会命中谷歌/Cloudflare策略组，而Mihomo会命中兜底策略组  

如果想保持一致可以删掉Mihomo模板规则里相应的no-resolve字段，或者删掉singbox模板中google_ip和cloudflare_ip规则集，我懒得改了（

# Mihomo-Config  

仅支持[smart内核](https://github.com/vernesong/mihomo/releases)使用  

不支持`裸核`运行，仅支持`Nikki`、`Openclash`等插件配置防火墙使用，或配置`TUN`字段  

需要自行修改`订阅链接`、`鉴权`、`DNS`等信息  

# Singbox-Config  

不支持`裸核`运行，仅支持`momo`插件配置防火墙使用，需要使用[sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe)进行订阅转换  

`http://转换后端/config/订阅&file=配置文件地址`  

需要自行修改`鉴权`、`DNS`等信息  
