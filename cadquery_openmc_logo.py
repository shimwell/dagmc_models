from cad_to_dagmc import CadToDagmc
import cadquery as cq

from paramak import ExtrudeMixedShape

grey_shape = ExtrudeMixedShape(
    points=[
        (99.5, 61.5, "straight"),
        (14., 61.5, "circle"),
        (221.5, 55., "circle"),
        (105.,241., "straight"),
        (155.,156.5, "straight"),
    ],
    distance=20,
).solid

red_shape = ExtrudeMixedShape(
    points=[
        (85.5, 88., "straight"),
        (125.5, 158., "straight"),
        (84.5, 226., "straight"),
        (60., 226, "circle"),
        (11.,173.5, "circle"),
        (5,87.5, "straight"),
    ],
    distance=20,
).solid

my_model = CadToDagmc()
my_model.add_cadquery_object(
    object=grey_shape,
    material_tags=["mat_grey"]
)
my_model.add_cadquery_object(
    object=red_shape,
    material_tags=["mat_grey"]
)

my_model.export_dagmc_h5m_file(
    filename="cadquery_openmc_logo.h5m", max_mesh_size=20, min_mesh_size=5
)
