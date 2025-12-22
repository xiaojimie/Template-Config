import requests
import re

# 源文件地址 (AdGuardHome 规则)
SOURCE_URL = "https://raw.githubusercontent.com/miaoermua/AdguardFilter/main/rule.txt"
# 输出文件名
OUTPUT_FILE = "smartdns_ad_rules.conf"

def convert_rules():
    print("正在下载规则...")
    try:
        response = requests.get(SOURCE_URL)
        response.raise_for_status()
        content = response.text
    except Exception as e:
        print(f"下载失败: {e}")
        return

    print("正在转换规则...")
    smartdns_rules = []
    
    # 写入文件头
    smartdns_rules.append("# SmartDNS Block List")
    smartdns_rules.append(f"# Source: {SOURCE_URL}")
    smartdns_rules.append("# Converted by GitHub Actions")
    smartdns_rules.append("")

    lines = content.splitlines()
    count = 0

    for line in lines:
        line = line.strip()
        # 忽略空行和注释
        if not line or line.startswith('!'):
            continue

        if line.startswith('||') and line.endswith('^'):
            domain = line[2:-1] # 去掉开头的 || 和结尾的 ^
            # 转换为 SmartDNS 格式: address /domain/#
            smartdns_rules.append(f"address /ads.{domain}/#")
            # 更通用的转换逻辑：
            smartdns_rules.append(f"address /{domain}/#")
            count += 1

    # 写入结果文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(smartdns_rules))
    
    print(f"转换完成! 共处理 {count} 条规则。")

if __name__ == "__main__":
    convert_rules()
