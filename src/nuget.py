"""Клиент для работы с API v3"""
import json
import urllib.error
import urllib.request

def norm(pack):
  return pack.lower()

def url(url, pack):
  n=norm(pack)
  return f"{url}/{n}/index.json"

def url_vers(url, pack, vers):
  n=norm(pack)
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
