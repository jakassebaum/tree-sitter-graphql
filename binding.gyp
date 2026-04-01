{
  "targets": [
    {
      "target_name": "tree_sitter_graphql_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "src",
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
      ],
      "conditions": [
        ["OS!='win'", {
          "cflags_c": [
            "-std=c11",
          ],
        }, { # OS == "win"
          "cflags_c": [
            "/std:c11",
            "/utf-8",
          ],
        }],
      ],
      "cflags_cc": ["-std=c++20"],
      "xcode_settings": {
        "CLANG_CXX_LANGUAGE_STANDARD": "c++20"
      },
    }
  ]
}
