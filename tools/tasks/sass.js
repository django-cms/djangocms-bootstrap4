const autoprefixer = require('autoprefixer');
const cleanCSS = require('gulp-clean-css');
const concat = require('gulp-concat-util');
const gulpif = require('gulp-if');
const gutil = require('gulp-util');
const postcss = require('gulp-postcss');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
const styleLint = require('gulp-stylelint');
const { importer } = require('npm-sass');


module.exports = function (gulp, opts) {
    return function () {
        return gulp.src(opts.PROJECT_PATTERNS.sass)
            .pipe(styleLint({
                reporters: [{
                    formatter: (opts.argv.debug) ? 'verbose' : 'string',
                    console: true,
                }],
            }))
            .on('error', function () {
                this.emit('end');
            })
            .pipe(gulpif(opts.argv.debug, sourcemaps.init()))
            .pipe(sass({
                importer: importer,
                precision: 10,
            }))
            .on('error', function (error) {
                gutil.log(gutil.colors.red(
                    'Error (' + error.plugin + '): ' + error.messageFormatted)
                );
                // in dev mode - just continue
                this.emit('end');
            })
            .pipe(
                postcss([
                    autoprefixer({
                        // browsers are coming from browserslist file
                        cascade: false,
                    }),
                ])
            )
            .pipe(gulpif(!opts.argv.debug, cleanCSS({
                rebase: false,
            })))
            // this information is added on top of the generated .css file
            .pipe(concat.header(
                '/*\n    This file is generated.\n' +
                '    Do not edit directly.\n' +
                '    Edit original files in\n' +
                '    /private/sass instead\n */ \n\n'
            ))
            .pipe(gulpif(opts.argv.debug, sourcemaps.write()))
            .pipe(gulp.dest(opts.PROJECT_PATH.css));
    };
};
