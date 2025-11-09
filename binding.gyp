{
	"variables": {
		"module_name%": "pcsclite",
		"module_path%": "lib"
	},
	"targets": [
		{
			"target_name": "action_after_build",
			"type": "none",
			"dependencies": [
				"<(module_name)"
			],
			"copies": [
				{
					"files": [
						"<(PRODUCT_DIR)/<(module_name).node"
					],
					"destination": "<(module_path)"
				}
			]
		},
		{
			"target_name": "pcsclite",
			"sources": [
				"src/addon.cpp",
				"src/pcsclite.cpp",
				"src/cardreader.cpp"
			],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			"defines": [
				"NAPI_VERSION=8"
			],
			"cflags": [
				"-Wall",
				"-Wextra",
				"-Wno-unused-parameter",
				"-fPIC",
				"-fno-strict-aliasing",
				"-pedantic"
			],
			"cflags_cc": [
				"-std=c++17"
			],
			"conditions": [
				[
					"OS=='linux'",
					{
						"include_dirs": [
							"/usr/include/PCSC"
						],
						"link_settings": {
							"libraries": [
								"-lpcsclite"
							],
							"library_dirs": [
								"/usr/lib"
							]
						}
					}
				],
				[
					"OS=='mac'",
					{
						"libraries": [
							"-framework",
							"PCSC"
						],
						"xcode_settings": {
							"GCC_ENABLE_CPP_EXCEPTIONS": "YES",
							"CLANG_CXX_LIBRARY": "libc++",
							"MACOSX_DEPLOYMENT_TARGET": "10.15"
						}
					}
				],
				[
					"OS=='win'",
					{
						"libraries": [
							"-lWinSCard"
						],
						"msvs_settings": {
							"VCCLCompilerTool": {
								"ExceptionHandling": 1
							}
						}
					}
				]
			]
		}
	]
}