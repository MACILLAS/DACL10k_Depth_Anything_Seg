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
        # palette=[[128, 64, 128]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_0.png', **kwargs) -> None:
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
        # palette=[[190, 153, 153]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_4.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kSpall(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('Spalling', 'Background'),
        # palette=[[107, 142, 35]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_8.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)


@DATASETS.register_module()
class Dacl10kPE(BaseSegDataset):
    """DACL10K dataset for semantic segmentation.

    The img_suffix is '.jpg' and 'seg_map_suffix' is '.png' for the dacl10k dataset
    """
    METAINFO = dict(
        classes=('PEquipment', 'Background'),
        # palette=[[0, 80, 100]]
    )

    def __init__(self, img_suffix='.jpg', seg_map_suffix='_cls_16.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
