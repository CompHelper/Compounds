module.exports = {
  root: true,

  env: {
    node: true
  },

  extends: ["plugin:vue/essential", "eslint:recommended", "@vue/prettier"],

  parserOptions: {
    parser: 'babel-eslint'
  },

  rules: {
    'no-prototype-builtins': 'off',
    'no-console': 'off',
    'no-debugger': 'off',
    'vue/attribute-hyphenation': 'error',
    'vue/html-quotes': 'warn',
    'vue/html-self-closing': 'warn',
    'vue/prop-name-casing': 'error',
    'vue/require-default-prop': 'warn',
    'vue/require-prop-types': 'warn',
    'vue/v-bind-style': 'warn',
    'vue/v-on-style': 'warn',
    'vue/no-confusing-v-for-v-if': 'warn',
    'vue/this-in-template': 'warn',
    'vue/component-definition-name-casing': 'warn',
    'vue/no-static-inline-styles': 'warn',
    'vue/require-name-property': 'off',
    'vue/v-on-function-call': 'error',
    'vue/valid-v-bind-sync': 'warn',
    'vue/valid-v-slot': 'warn'
  },

  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ],

  'extends': [
    'plugin:vue/essential',
    'eslint:recommended',
    '@vue/prettier'
  ]
};
