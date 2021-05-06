from androguard.core.analysis.analysis import Analysis
from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.decompiler.decompiler import DecompilerDAD

d = DalvikVMFormat(APK("dosya"))
da = Analysis(d)

decompiler = DecompilerDAD(d,da)

d.set_decompiler(decompiler)
d.set_vmanalysis(da)

for c in d.get_classes()[:5]:
    print(c,decompiler.get_source_class(c),sep="\n")