{
	'targets': [{
		'target_name': 'api',
		'sources': ["src/api.cc", "src/myobject.cc"],

		'include_dirs' : [
			# Include NAN
			"<!(node -e \"require('nan')\")",
            "lib/tensorflow"
		],
        'libraries': [
            '<!(pwd)/lib/tensorflow/bazel-bin/tensorflow/cc/libtensorflow.so'
        ]
        }]
}
