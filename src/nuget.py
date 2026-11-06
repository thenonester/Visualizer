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
    if deps["range"]:
      print(f" - {dep["id"]} {dep["range"]}")
    else:
      print(f" - {dep["id"]}")

def info(source, package, version=None):
  """получение информации о пакете"""
  base = base_url(source)
  vers = get_verse(base, pack)
  if version is None:
    version = latest(vers)
  elif version not in vers:
    raise ValueError(f"Version {vers} not found")
  dep = getdeps(base, pack, vers)
  return vers, dep

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
      if vers:
        versions.append(vers)
  return versions

def latest(vers): 
  if not vers:
    raise ValueError("No Versions Found")
  return versions[-1]

def getdeps(base_url, pack, vers):
  url = url_pack(base_url, pack, vers)
  data = jsonu(url)
  entry = entr(data.get("items", []), vers)
  if entry is None:
    raise ValueError(f"Version {vers} not found")
  return deps(entry)

def entr(items, vers):
  for item in items:
    entry = item.get("catalogEntry", {})
    if entry.get("version") == version:
      return entry
  return None

def deps(entry):
  deps = []
  seen = set()
  for group in entry.get("dependencyGroups", []):
    for dep in group.get("dependencies", []):
      id = dep.get("id")
      if id and id not in seen:
        seen.add(id)
        dep.append({"id": id, "range": dep.get("range", "")})
  return dep

def jsonu(url):
  try:
    with urllib.request.urlopen(url, timeout=10):
      data = r.read().decode("utf-8")
      return json.loads(data)
  except urllib.error.HTTPError as e:
    raise ValueError(f"HTTP {e.code}: {e.reason}")
  except urllib.error.UELError as e:
    raise ValueError(f"URL error: {e.reason}")
  except json.JSONDecodeError as e:
    raise ValueError(f"Invalid JSON: {e}")
