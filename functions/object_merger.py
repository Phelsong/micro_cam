"""Object Merger"""
# libs

# imports
from functions.mesh_config import Mesh_Config


class Object_Merger:
    def __init__(self, config) -> None:
        self.dont_remove = set()
        self.config: Mesh_Config = config

    # =============================================================

    def merge_objects(self) -> None:
        from .mesh_object import MESH_OBJECTS

        last_pass = 0
        while len(MESH_OBJECTS) > 6:
            print("virtual objects: ", len(MESH_OBJECTS))
            self.run_merge()
            to_remove: set = MESH_OBJECTS.keys() - self.dont_remove
            for id in to_remove:
                del MESH_OBJECTS[id]
            self.dont_remove = set()
            if len(MESH_OBJECTS) == last_pass:
                break
            last_pass = len(MESH_OBJECTS)
        print("no more objects to merge")

    # =============================================================

    def run_merge(self) -> bool:
        from .mesh_object import MESH_OBJECTS

        for ref_id, ref in MESH_OBJECTS.items():
            # ---
            # cache ref values
            ref.calc_dimensions()
            ref_min_x = ref.min_x()
            ref_max_x = ref.max_x()
            ref_min_y = ref.min_y()
            ref_max_y = ref.max_y()
            # ---

            for inner_id, inner_obj in MESH_OBJECTS.items():
                # --
                inner_obj.calc_dimensions()
                check_min_x = inner_obj.min_x() - self.config.x_width
                check_max_x = inner_obj.max_x() + self.config.x_width
                check_min_y = inner_obj.min_y() - self.config.y_width
                check_max_y = inner_obj.max_y() + self.config.y_width
                # ---

                if (
                    ref_min_x > check_min_x
                    and ref_max_x < check_max_x
                    and ref_min_y > check_min_y
                    and ref_max_y < check_max_y
                ):
                    # print(f"merging {inner_obj.id} and {ref.id}")
                    inner_obj.merge(ref)
                    self.dont_remove.update([inner_id])
                    break
                    # ------
                # -------
        else:
            return True


# =============================================================
