# if __name__ == "__main__":
# test_bundle = np.array(
#     [
#         [13.1231, 1, 1.6123],
#         [7.81233, 1, 55.5123],
#         [2.1237, 1, 12.1442],
#         [4.1231, 1, 77.124],
#         [1.4243, 2, 23.12354],
#         [243.112, 2, 123.1234],
#         [55.44, 2, 11.32],
#     ],
#     dtype=np.float16,
# )
# print("testing")
# generate_lines(test_bundle)
# for key in LINES.keys():
#     print("------------------------")
#     print(key)
#     print(LINES[key])


# -------------------------------------------------------------------
# elif abs(abs(LINES[self.id][-1][0]) - self.points[0]) > 100:
#     if LINES2.get(self.id2) is None:
#         LINES2.setdefault(
#             self.id2, np.array(self.points, ndmin=2, dtype=np.float16)
#         )
#     else:
#         LINES2[self.id2] = np.vstack((LINES2[self.id2], self.points))
