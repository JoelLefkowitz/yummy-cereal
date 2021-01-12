module.exports = {
  parseExec: function parseExec(kv) {
    const [cwd, execs] = kv;
    return Object.fromEntries(
      Object.entries(execs).map((kv) => {
        const [name, cmd] = kv;
        return [name, { cmd: cmd.join(" "), cwd }];
      })
    );
  },
  parseKv: function parseKv(kv, parser) {
    return Object.entries(kv).reduce(
      (acc, x) => ({ ...acc, ...parser(x) }),
      {}
    );
  },
};
