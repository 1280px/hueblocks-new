import antfu from '@antfu/eslint-config'

export default antfu(
    {
        ignores: [
            '**/node_modules',
            'package.*.json',
            '.github/*',
            '.vscode/*',
        ],

        stylistic: {
            indent: 4,
            quotes: 'single',
        },

        typescript: true,
        vue: true,
    },
    {
        rules: {
            'antfu/consistent-list-newline': ['warn', { ObjectExpression: false }],
            'no-console': ['warn', { allow: ['info', 'warn', 'error'] }],
            'style/max-statements-per-line': ['warn', { max: 3 }],
            'style/member-delimiter-style': ['error', { multiline: { delimiter: 'comma' }, singleline: { delimiter: 'comma' } }],
        },
    },
)
