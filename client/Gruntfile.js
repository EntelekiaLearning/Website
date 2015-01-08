module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    jade: {
      compile: {
        options: {
          client: false,
          pretty: true
        },
        files: [{
          cwd: './',
          src: [
            '**/*.jade'
          ],
          dest: './',
          expand: true,
          ext: '.html'
        }]
      }
    },

    browserify: {
      './app.pre.js': [
        './!Gruntfile.js',
        './index.js',
        './conf.js',
        './ViewModels/*.js',
        './Models/*.js',
        './node_modules/crossroads/node_modules/signals/dist/signals.js',
        './node_modules/crossroads/dist/crossroads.js',
        './node_modules/knockout/build/output/knockout-latest.js',
        './node_modules/jquery/dist/jquery.js'
      ]
    },

    uglify: {
      build: {
        src: [
          './node_modules/jquery/dist/jquery.js',
          './node_modules/semantic-ui/dist/semantic.js',
          'app.pre.js'
        ],
        dest: 'app.min.js'
      }
    },

    cssmin: {
      target: {
        files: {
          './app.min.css': [
            './Styles/*.css',
            './node_modules/semantic-ui/dist/semantic.css'
          ]
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jade');
  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('default', [
    'jade',
    'browserify',
    'uglify',
    'cssmin'
  ]);
};