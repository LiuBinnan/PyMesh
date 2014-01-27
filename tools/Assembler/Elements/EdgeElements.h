#pragma once

#include <Mesh.h>

#include "Elements.h"

class EdgeElements : public Elements {
    public:
        EdgeElements(Mesh::Ptr mesh);

    public:
        virtual size_t getDim() const;

        virtual size_t getNbrNodes() const;
        virtual VectorF getNodes() const;
        virtual VectorF getNode(size_t vi) const;

        virtual size_t getNbrElements() const;
        virtual VectorI getElements() const;
        virtual VectorI getElement(size_t ei) const;

    private:
        void check_mesh();
        void extract_boundary_edges();

    private:
        Mesh::Ptr m_mesh;
        MatrixIr m_edges;
};
