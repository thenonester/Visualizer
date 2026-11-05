"""Клиент для работы с API v3"""
import json
import urllib.error
import urllib.request

def norm(pack):
  return pack.lower()

def url_pack(url, pack, vers=None):
  n=norm(pack)
  if not vers:
    return f"{url}/{n}/index.json"
  return f"{url}/{n}/{vers}.json"

def print_dep(pack, vers, deps):
  print(f"Package: {pack} {vers}")
  print(f"Direct dependencies ({len(deps)})")
  for dep in deps:
    print(f" - {form(dep)}")

def info(source, package, version=None):
  """получение информации о пакете"""
  if version:''

def base_url(source):
  """Определяет базовый URL"""
  if not source.endwith("/index.json"):
    return source.rstrip("/")
  data = jsonu(source)
  for res in data.get("resources", []):
    t = res.get("@type", "")
    if t.startswith("RegistrationBaseUrl"):
      return res["@id"].rstrip("/")
  raise ValueError("RegistrationBaseUrl not found")

def get_verse(base, pack):
  url = url_pack(base, pack)
  data = jsonu(url)
  versions=[]
  for page in data.get("items", []):
    if "items" in page:
      items = page["items"]
    else:
      p_url = page.get("@id")
      if not p_url:
        continue
      p_data = jsonu(p_url)
      items = p_data.get("items", [])
    for item in items:
      entry = item.get("catalogEntry", {})
      vers = entry.get("version")
      if v:
        versions.append(vers)
  return versions

def latest(vers): 
  if not vers:
    raise ValueError("No Versions Found")
  return versions[-1]

def getdeps(url, pack, vers):''

def jsonu(url):
  try:
    urllib.request.urlopen(url, timeout=10):
    data = r.read().decode("utf-8")
    return json.loads(data)
  except urllib.error.HTTPError as e:
    raise ValueError(f"HTTP {e.code}: {e.reason}")
  except urllib.error.UELError as e:
    raise ValueError(f"URL error: {e.reason}")
  except json.JSONDecodeError as e:
    raise ValueError(f"Invalid JSON: {e}")
