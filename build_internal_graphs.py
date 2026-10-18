"""Publish immutable per-function CFG data from the existing PE/PDB graph reports."""
from pathlib import Path
import argparse
import json

def build(root: Path):
    sim = root / 'simulator'
    text = (sim / 'catalog.js').read_text(encoding='utf-8')
    catalog = json.loads(text.split('=', 1)[1].strip().rstrip(';'))
    wanted = set(catalog['calls']) | {e['rva'] for e in catalog['exports'] if e.get('callable')}
    for calls in catalog['calls'].values():
        wanted.update(c['target'] for c in calls if c.get('target') and c.get('kind') == 'direct')
    dest = sim / 'internal-graphs'
    dest.mkdir(exist_ok=True)
    index = {}
    for partition in sorted((root / 'graphs').glob('*.js')):
        source = partition.read_text(encoding='utf-8')
        try:
            graphs = json.loads(source.split('=', 1)[1].strip().rstrip(';'))
        except (ValueError, IndexError):
            continue
        for rva in wanted.intersection(graphs):
            graph = graphs[rva]
            graph = {**graph, 'readonly': True, 'sha256': catalog['sha256'], 'evidence': 'static-pe-pdb-cfg'}
            filename = rva[2:] + '.json'
            (dest / filename).write_text(json.dumps(graph, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
            index[rva] = {'name': graph['name'], 'file': filename, 'report': graph.get('report'), 'blocks': graph.get('blocks', 0)}
        del graphs, source
    (sim / 'internal-index.json').write_text(json.dumps({'schema': 1, 'sha256': catalog['sha256'], 'functions': index}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'Read-only internal graphs: {len(index):,} functions; {catalog["sha256"]}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True, type=Path)
    build(parser.parse_args().root)
