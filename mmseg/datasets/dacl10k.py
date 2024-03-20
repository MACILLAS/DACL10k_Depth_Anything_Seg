from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class Dacl10k(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Crack', 'ACrack', 'Wetspot', 'Efflorescence', 'Rust', 'Rockpocket', 'Hollowareas', 'Cavity',
                 'Spalling', 'Graffiti', 'Weathering', 'Restformwork', 'ExposedRebars',
                 'Bearing', 'EJoint', 'Drainage', 'PEquipment', 'JTape', 'WConccor'),
        palette=[[128, 64, 128], [244, 35, 232], [70, 70, 70], [102, 102, 156],
                 [190, 153, 153], [153, 153, 153], [250, 170, 30], [220, 220, 0],
                 [107, 142, 35], [152, 251, 152], [70, 130, 180],
                 [220, 20, 60], [255, 0, 0], [0, 0, 142], [0, 0, 70],
                 [0, 60, 100], [0, 80, 100], [0, 0, 230], [119, 11, 32]])

    def __init__(self, img_suffix='.jpg', seg_map_suffix='.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kCrack(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Crack', 'Background'),
        palette=[[128, 64, 128], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_0.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kAcrack(BaseSegDataset):

    METAINFO = dict(
        classes=('ACrack', 'Background'),
        palette=[[244, 35, 232], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_1_.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kWetspot(BaseSegDataset):

    METAINFO = dict(
        classes=('Wetspot', 'Background'),
        palette=[[70, 70, 70], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_2_.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kEfflor(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Efflorescence', 'Background'),
        palette=[[102, 102, 156], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_3.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kRust(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Rust', 'Background'),
        palette=[[190, 153, 153], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_4.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kRockpocket(BaseSegDataset):

    METAINFO = dict(
        classes=('Rockpocket', 'Background'),
        palette=[[153, 153, 153], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_5.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kHollowareas(BaseSegDataset):

    METAINFO = dict(
        classes=('Hollowareas', 'Background'),
        palette=[[250, 170, 30], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_6.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kCavity(BaseSegDataset):

    METAINFO = dict(
        classes=('Cavity', 'Background'),
        palette=[[220, 220, 0], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_7.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kSpall(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Spalling', 'Background'),
        palette=[[107, 142, 35], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_8.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kGraffiti(BaseSegDataset):

    METAINFO = dict(
        classes=('Graffiti', 'Background'),
        palette=[[152, 251, 152], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_9.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kWeathering(BaseSegDataset):

    METAINFO = dict(
        classes=('Weathering', 'Background'),
        palette=[[70, 130, 180], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_10.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kRestformwork(BaseSegDataset):

    METAINFO = dict(
        classes=('Restformwork', 'Background'),
        palette=[[220, 20, 60], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_11.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kExposedrebars(BaseSegDataset):

    METAINFO = dict(
        classes=('ExposedRebars', 'Background'),
        palette=[[255, 0, 0], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_12.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kBearing(BaseSegDataset):

    METAINFO = dict(
        classes=('Bearing', 'Background'),
        palette=[[0, 0, 142], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_13.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kEjoint(BaseSegDataset):

    METAINFO = dict(
        classes=('EJoint', 'Background'),
        palette=[[0, 0, 70], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_14.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kDrainage(BaseSegDataset):

    METAINFO = dict(
        classes=('Drainage', 'Background'),
        palette=[[0, 60, 100], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_15.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kPE(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('PEquipment', 'Background'),
        palette=[[0, 80, 100], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_16.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kJtape(BaseSegDataset):

    METAINFO = dict(
        classes=('EJoint', 'Background'),
        palette=[[0, 0, 230], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_17.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

@DATASETS.register_module()
class Dacl10kWconccor(BaseSegDataset):

    METAINFO = dict(
        classes=('WConccor', 'Background'),
        palette=[[119, 11, 32], [0, 0, 0]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_18.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)