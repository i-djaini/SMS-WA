#Encrypt by SC Ismail Djaini

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))