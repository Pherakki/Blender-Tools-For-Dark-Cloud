from .CHRInterface import CHRInterface
from ..CFG.CFGInterface import CFGInterface

class Model:
    def __init__(self):
        self.submodels = []

    @classmethod
    def from_chr(cls, chr_interface):
        instance = cls()
        
        # Locate CFG files
        cfgs = []
        for nm, file in chr_interface.files.items():
            if type(file) == CFGInterface:
                cfgs.append(file)
        
        for cfg in cfgs:
            submodel = SubModel()
            submodel.mds = chr_interface.files.get(cfg.mds) if cfg.mds is not None else None
            submodel.bbp = chr_interface.files.get(cfg.bbp) if cfg.bbp is not None else None
            submodel.wgt = chr_interface.files.get(cfg.wgt) if cfg.wgt is not None else None
            submodel.mot = chr_interface.files.get(cfg.mot) if cfg.mot is not None else None
            submodel.shadow_mds = chr_interface.files.get(cfg.shadow_mds) if cfg.shadow_mds is not None else None
            submodel.shadow_bbp = chr_interface.files.get(cfg.shadow_bbp) if cfg.shadow_bbp is not None else None
            submodel.shadow_wgt = chr_interface.files.get(cfg.shadow_wgt) if cfg.shadow_wgt is not None else None
            submodel.shadow_mot = chr_interface.files.get(cfg.shadow_mot) if cfg.shadow_mot is not None else None
            submodel.imgs = [chr_interface.files.get(img_name) if img_name is not None else None for img_name in cfg.imgs]
            instance.submodels.append(submodel)
        
        return instance
        
    def to_chr(self):
        raise NotImplementedError

class SubModel:
    def __init__(self):
        self.mds = None
        self.bbp = None
        self.wgt = None
        self.mot = None
        self.shadow_mds = None
        self.shadow_bbp = None
        self.shadow_wgt = None
        self.shadow_mot = None
        self.imgs = []
