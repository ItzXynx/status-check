import sys
import urllib.request
import concurrent.futures

def check(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(req) as r:
            return url, r.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except:
        return url, 0

if __name__ == "__main__":
    urls = sys.argv[1:]
    with concurrent.futures.ThreadPoolExecutor() as ex:
        for url, status in ex.map(check, urls):
            ok = "ok" if status < 400 else "err"
            print(f"  {status} {ok} {url}")
