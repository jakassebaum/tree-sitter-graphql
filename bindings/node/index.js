let binding;
try {
  binding = require("../../build/Release/tree_sitter_graphql_binding");
} catch (error1) {
  if (error1.code !== 'MODULE_NOT_FOUND') {
    throw error1;
  }
  try {
    binding = require("../../build/Debug/tree_sitter_graphql_binding");
  } catch (error2) {
    if (error2.code !== 'MODULE_NOT_FOUND') {
      throw error2;
    }
    throw error1
  }
}

// Export the language directly for compatibility
module.exports = binding.language;

// Also export other properties for full compatibility
module.exports.name = binding.name;
try {
  module.exports.nodeTypeInfo = require("../../src/node-types.json");
} catch (_) {}
