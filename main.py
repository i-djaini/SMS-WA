#Encrypt by SC Ismail Djaini

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))
