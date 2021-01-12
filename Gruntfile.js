const parsers = require("./grunt/parsers");
const YAML = require("yaml");
const fs = require("fs");

const loader = (name) =>
  YAML.parse(fs.readFileSync("grunt/".concat(name, ".yml"), "utf8"));

module.exports = function (grunt) {
  grunt.initConfig({
    copy: loader("copy"),
    clean: loader("clean"),
    exec: parsers.parseKv(loader("exec"), parsers.parseExec),
  });

  grunt.loadNpmTasks("grunt-exec");
  grunt.loadNpmTasks("grunt-force-task");
  grunt.loadNpmTasks("grunt-contrib-copy");
  grunt.loadNpmTasks("grunt-contrib-clean");

  grunt.registerTask("lint", [
    "exec:pylint",
    "exec:bandit",
    "exec:mypy",
    "force:exec:eslint",
    "exec:cspell",
  ]);

  grunt.registerTask("format", [
    "exec:presort",
    "exec:autoflake",
    "exec:isort",
    "exec:black",
    "force:exec:prettier",
    "exec:csscomb",
  ]);

  grunt.registerTask("buildMaster", [
    "clean:dist",
    "copy:architects",
    "copy:static",
    "exec:buildbotInit",
    "clean:buildbot",
    "exec:buildbotStart",
  ]);
  
  grunt.registerTask("buildApp", [
    "clean:dist",
    "exec:compile",
  ]);
};

