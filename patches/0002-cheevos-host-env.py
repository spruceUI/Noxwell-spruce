#!/usr/bin/env python3
# DS_CHEEVOS_HOST=host:port sends RetroAchievements requests there (spruce's RAOfflineProxy).
import sys
p = "src/cheevos/cheevos_client.cpp"
s = open(p).read()
old = "  rc_client_set_userdata(c, this);\n"
new = old + ("  if (const char* h = std::getenv(\"DS_CHEEVOS_HOST\")) {\n"
             "    if (*h) rc_client_set_host(c, h);\n"
             "  }\n")
if s.count(old) != 1:
    sys.exit(f"{p}: rc_client_set_userdata line not found; upstream moved it")
open(p, "w").write(s.replace(old, new))
print("cheevos_client.cpp: DS_CHEEVOS_HOST applied")
