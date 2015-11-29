Go to lib and execute this

`git clone --recurse-submodules https://github.com/tensorflow/tensorflow`

Patch lib/tensorflow/tensorflow/cc/BUILD with

```
cc_binary(
    name = "libtensorflow.so",
    copts = tf_copts(),
    linkshared = 1,
    deps = [
        ":cc_ops",
        "//tensorflow/core:kernels",
        "//tensorflow/core:tensorflow",
    ],
)
```

Execute this in lib/tensorflow

`bazel build -c opt //tensorflow/cc:libtensorflow.so`

Then
`node-gyp configure`
`node-gyp build`
`node index.js`
