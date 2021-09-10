/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/divio/djangocms-boilerplate-webpack
 */

// INFO:
// - The minimatch/graceful-fs warnings are from gulp, needs upgrade to 4.0 once released.

// #############################################################################
// IMPORTS
const argv = require('minimist')(process.argv.slice(2));
const gulp = require('gulp');

// #############################################################################
// SETTINGS
const PROJECT_ROOT = __dirname;
const PROJECT_STATIC = '/djangocms_bootstrap5/static/djangocms_bootstrap5/'
const PROJECT_PATH = {
    css: PROJECT_ROOT + PROJECT_STATIC + '/css',
    js: PROJECT_ROOT + PROJECT_STATIC + '/js',
    sprites: PROJECT_ROOT + PROJECT_STATIC + '/sprites',
    sass: PROJECT_ROOT + '/private/sass',
    webpack: PROJECT_ROOT + '/private/js',
    svg: PROJECT_ROOT + '/private/svg',
};
const PROJECT_PATTERNS = {
    css: [
        PROJECT_PATH.css + '/*base*.css',
    ],
    js: [
        '*.js',
        './tools/tasks/**/*.js',
        PROJECT_PATH.webpack + '*.config.js',
        PROJECT_PATH.webpack + '/**/*.js',
        '!' + PROJECT_PATH.webpack + '/*.min.js',
        '!' + PROJECT_PATH.webpack + '/**/*.min.js',
    ],
    sass: [
        PROJECT_PATH.sass + '/**/*.{scss,sass}',
        '!' + PROJECT_PATH.sass + '/libs/_svgsprite.scss',
    ],
    svg: {
        icons: [PROJECT_PATH.svg + '/**/*.svg'],
    },
};

/**
 * Generic utility to import gulp tasks and pass options to them
 *
 * @param {String} id - task name
 * @param {Object} [extra] - optional options to pass
 * @returns {Function} - task definition
 */
function task(id, extra) {
    return require('./tools/tasks/' + id)(
        gulp,
        Object.assign(
            {
                PROJECT_ROOT: PROJECT_ROOT,
                PROJECT_PATH: PROJECT_PATH,
                PROJECT_PATTERNS: PROJECT_PATTERNS,
                argv: argv,
            },
            extra
        )
    );
}


// #############################################################################
// TASKS
gulp.task('sass', task('sass'));
gulp.task('webpack', task('webpack'));
gulp.task('webpack:watch', task('webpack', { watch: true }));

gulp.task('lint', task('lint'));
gulp.task('icons', task('svg', { svg: 'icons' }));

gulp.task('default', ['sass', 'webpack', 'watch']);

gulp.task('watch', function () {
    gulp.start('webpack:watch');
    gulp.watch(PROJECT_PATTERNS.sass, ['sass']);
    gulp.watch(PROJECT_PATTERNS.js, ['lint']);
});
