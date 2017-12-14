import  tensorflow as tf

t = tf.constant(
                    [
                        [
                            [1, 1, 1], [2, 2, 2]
                        ],
                        [
                            [3, 3, 3], [4, 4, 4]
                        ],
                        [
                            [5, 5, 5], [6, 6, 6]
                        ]
                    ]
                )
print(tf.slice(t, [1, 0, 0], [1, 1, 3]))  # [[[3, 3, 3]]]
print(tf.slice(t, [1, 0, 0], [1, 2, 3]))  # [[[3, 3, 3],  [4, 4, 4]]]
print(tf.slice(t, [1, 0, 0], [2, 1, 3]))  # [[[3, 3, 3]], [[5, 5, 5]]]