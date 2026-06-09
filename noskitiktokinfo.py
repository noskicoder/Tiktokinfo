import webbrowser
import requests
import datetime
import json
import secrets
import uuid
import binascii
import os
import time
import random
import re
import sys

try:
    import pyfiglet
    from pyfiglet import Figlet
except ImportError:
    print("Kurulum: pip install pyfiglet")
    sys.exit(1)

def xor_encode(email):
    try:
        key = 5
        encoded = []
        for char in email:
            encoded.append(hex(ord(char) ^ key)[2:])
        return "".join(encoded)
    except:
        return ""

def generate_user_agent():
    return "Mozilla/5.0 (Linux; Android 13; Infinix X6528) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"

def flag_emoji(country_code):
    if not country_code or country_code == 'Bilinmiyor':
        return '🏳️'
    return ''.join(chr(127397 + ord(c)) for c in country_code.upper())

def noski_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    f = Figlet(font='slant')
    noski_yazi = f.renderText('Noski')

    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    print("\033[1;32m" + "═" * terminal_width + "\033[0m")
    for line in noski_yazi.split('\n'):
        if line.strip():
            print("\033[1;31m" + line.center(terminal_width) + "\033[0m")
    
    print("\033[1;36m" + "TikTok User Info Tool".center(terminal_width) + "\033[0m")
    print("\033[1;33m" + f"Dev : Noski".center(terminal_width) + "\033[0m")
    print("\033[1;34m" + f"YouTube: youtube.com/@noskicoder".center(terminal_width) + "\033[0m")
    print("\033[1;32m" + "═" * terminal_width + "\033[0m\n")

def get_tiktok_profile_api(username, email=""):
    try:
        secret = secrets.token_hex(16)
        
        headers = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\"Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": generate_user_agent(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
        }
    
        try:
            response = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, timeout=10)
            
            if response.status_code == 200:
                match = re.search(r'<script[^>]*id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', response.text, re.DOTALL)
                if match:
                    data = json.loads(match.group(1))
                    user_info = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
                    user = user_info.get('user', {})
                    stats = user_info.get('stats', {})
                    
                    unique_id = user.get('uniqueId', '')
                    nickname = user.get('nickname', '')
                    user_id = user.get('id', '')
                    sec_uid = user.get('secUid', '')
                    bio = user.get('signature', '')[:150] if user.get('signature') else ''
                    
                    followers = stats.get('followerCount', 0)
                    following = stats.get('followingCount', 0)
                    hearts = stats.get('heartCount', 0)
                    videos = stats.get('videoCount', 0)
                    diggs = stats.get('diggCount', 0)
                    
                    country = user.get('region', 'Bilinmiyor')
                    flag = user.get('flag', country)
                    
                    create_time = user.get('createTime', 0)
                    if create_time:
                        created_date = datetime.datetime.fromtimestamp(create_time).strftime('%d.%m.%Y')
                        created_full = datetime.datetime.fromtimestamp(create_time).strftime('%d.%m.%Y %H:%M:%S')
                    else:
                        created_date = 'Bilinmiyor'
                        created_full = 'Bilinmiyor'
                    
                    is_private = user.get('privateAccount', False)
                    is_verified = user.get('verified', False)
                    account_type = "Özel" if is_private else "Açık"
                    if is_verified:
                        account_type += " | Doğrulanmış"
                    
                    bio_links = user.get('bioLink', {}).get('link', '') if user.get('bioLink') else ''
                    
                    return {
                        'username': unique_id,
                        'user_id': user_id,
                        'sec_uid': sec_uid,
                        'nickname': nickname,
                        'bio': bio,
                        'bio_links': bio_links,
                        'followers': followers,
                        'following': following,
                        'hearts': hearts,
                        'videos': videos,
                        'diggs': diggs,
                        'is_private': is_private,
                        'is_verified': is_verified,
                        'account_type': account_type,
                        'country': country,
                        'flag': flag,
                        'created_date': created_date,
                        'created_full': created_full
                    }
        except:
            pass
        
        return None
    except Exception as e:
        return None

def get_tiktok_info(username):
    return get_tiktok_profile_api(username)

def noski_tiktok_info(username):
    """Noski TikTok bilgi gösterici"""
    info = get_tiktok_profile_api(username)
    
    # Terminal genişliğini al
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    
    print("\033[1;36m" + "═" * terminal_width + "\033[0m")
    print("\033[1;33m" + "NOSKİ TİKTOK INFO".center(terminal_width) + "\033[0m")
    print("\033[1;36m" + "═" * terminal_width + "\033[0m")
    
    if info:
        print(f"""
\033[1;32m┌─────────────────────────────────────────────────────────────┐\033[0m
\033[1;32m│\033[1;33m Kullanıcı Adı:\033[0m @{info['username']}
\033[1;32m│\033[1;33m İsim:\033[0m {info['nickname']}
\033[1;32m│\033[1;33m Kullanıcı ID:\033[0m {info['user_id']}
\033[1;32m│\033[1;33m Takipçi:\033[0m {info['followers']:,}
\033[1;32m│\033[1;33m Takip:\033[0m {info['following']:,}
\033[1;32m│\033[1;33m Beğeni:\033[0m {info['hearts']:,}
\033[1;32m│\033[1;33m Video:\033[0m {info['videos']:,}
\033[1;32m│\033[1;33m Bio:\033[0m {info['bio'][:100]}...
\033[1;32m│\033[1;33m Hesap Türü:\033[0m {info['account_type']}
\033[1;32m│\033[1;33m Ülke:\033[0m {info['country']} {flag_emoji(info['flag'])}
\033[1;32m│\033[1;33m Kuruluş:\033[0m {info['created_full']}
\033[1;32m└─────────────────────────────────────────────────────────────┘\033[0m
        """)
    else:
        print(f"""
\033[1;31m┌────────────────────────────────────────────────────────────────┐\033[0m
\033[1;31m│\033[1;33m Kullanıcı Adı:\033[0m @{username}
\033[1;31m│\033[1;31m ✗ Hesap bulunamadı veya silinmiş olabilir!\033[0m
\033[1;31m└────────────────────────────────────────────────────────────────┘\033[0m
        """)
    
    print("\033[1;36m" + "═" * terminal_width + "\033[0m")
    print("\033[1;34m" + f"YouTube: youtube.com/@noskicoder".center(terminal_width) + "\033[0m")
    print("\033[1;36m" + "═" * terminal_width + "\033[0m\n")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    while True:
        clear_screen()
        noski_banner()
        
        # Terminal genişliğini al
        try:
            terminal_width = os.get_terminal_size().columns
        except:
            terminal_width = 80
        
        print("\033[1;36m" + "═" * terminal_width + "\033[0m")
        print("\033[1;33m" + "[?] TikTok kullanıcı adını girin:".center(terminal_width) + "\033[0m")
        print("\033[1;36m" + "═" * terminal_width + "\033[0m")
        username = input("\033[1;32m  >> \033[0m").strip()
        
        if not username:
            print("\n\033[1;31m[!] Kullanıcı adı boş olamaz!\033[0m")
            time.sleep(1.5)
            continue
        
        username = username.replace('@', '')
        
        noski_tiktok_info(username)
        
        print("\033[1;36m" + "═" * terminal_width + "\033[0m")
        print("\033[1;33m" + "[?] Tekrar arama yapmak ister misiniz? (e/h):".center(terminal_width) + "\033[0m")
        print("\033[1;36m" + "═" * terminal_width + "\033[0m")
        devam = input("\033[1;32m  >> \033[0m").strip().lower()
        
        if devam != 'e' and devam != 'evet':
            clear_screen()
            print("\033[1;32m" + "═" * terminal_width + "\033[0m")
            print("\033[1;33m" + "Noski TikTok User Info kullandığınız için teşekkürler!".center(terminal_width) + "\033[0m")
            print("\033[1;34m" + f"YouTube: youtube.com/@noskicoder".center(terminal_width) + "\033[0m")
            print("\033[1;32m" + "═" * terminal_width + "\033[0m\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;31m[!] Kullanıcı tarafından durduruldu.\033[0m")
        sys.exit(0)