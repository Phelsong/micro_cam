from base64 import b64encode


# NOTE: from stl_mesh.py, need to write a wrapper function here
# if __name__ == "__main__":
#     print("-----------------------------")
# Raw Mesh data
# source_mesh = Mesh.from_file("X:\\0.code_projects\\precisionfit\\data\\33_FLAT.STL")
# print(source_mesh.normals)
# ------------
# The mesh normals (calculated automatically)
# print("normals:")
# print(source_mesh.normals[0])
# print(source_mesh.normals[1])
# print(source_mesh.normals[2])

# mesh16 = np.array(source_mesh.normals, dtype=np.float16)
# print(mesh16)
# print("-----------------------------")
# print("normals min-max:")
# print(source_mesh.normals.min())
# print(source_mesh.normals.max())
# print(source_mesh.y[0])
# print("-----------------------------")
# The mesh vectors
# print(source_mesh.v0[0])
# print(source_mesh.v1[0])
# print(source_mesh.v2[0])
# print("-----------------------------")
# print("X:", X.min(), X.max())
# print("Y:", Y.min(), Y.max())
# print("Z:", Z.min(), Z.max())
# generate_raw_visual(source_mesh)
# print(source_mesh.min_)
# print(source_mesh.max_)
