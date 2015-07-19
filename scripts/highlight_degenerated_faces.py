#!/usr/bin/env python

import argparse
import numpy as np
import pymesh

def parse_args():
    parser = argparse.ArgumentParser(
            description="highlight degenerated faces");
    parser.add_argument("input_mesh", help="input mesh");
    parser.add_argument("output_mesh", help="output mesh");
    return parser.parse_args();

def main():
    args = parse_args();
    mesh = pymesh.load_mesh(args.input_mesh);

    f_indices = pymesh.get_degenerated_faces(mesh);
    v_indices = mesh.faces[f_indices].ravel();
    degenerated_faces = np.zeros(mesh.num_faces);
    degenerated_faces[f_indices] = 1.0;
    degenerated = np.zeros(mesh.num_vertices);
    degenerated[v_indices] = 1.0;
    mesh.add_attribute("degenerated_faces");
    mesh.set_attribute("degenerated_faces", degenerated_faces);
    mesh.add_attribute("degenerated");
    mesh.set_attribute("degenerated", degenerated);

    print("{} degenerated faces, consisting of {} vertices.".format(
        len(f_indices), np.count_nonzero(degenerated)));

    pymesh.save_mesh(args.output_mesh, mesh, "degenerated", "degenerated_faces");

if __name__ == "__main__":
    main();
