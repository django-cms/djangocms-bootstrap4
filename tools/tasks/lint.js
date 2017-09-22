const eslint = require('gulp-eslint');
const styleLint = require('gulp-stylelint');


module.exports = function (gulp, opts) {
    return function () {
        return gulp.src(opts.PROJECT_PATTERNS.js)
            .pipe(eslint())
            .pipe(eslint.format())
            .pipe(eslint.failAfterError());
    };
};

module.exports = function (gulp, opts) {
    return function () {
        return gulp.src(opts.PROJECT_PATTERNS.sass)
            .pipe(styleLint({
                reporters: [{
                    formatter: (opts.argv.debug) ? 'verbose' : 'string',
                    console: true,
                }],
            }));
    };
};
