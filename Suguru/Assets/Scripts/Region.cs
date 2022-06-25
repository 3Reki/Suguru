using UnityEngine;

public class Region
{
    public Vector2[] cellIndexes { get; private set; }

    public Region(Vector2[] cellIndexes)
    {
        this.cellIndexes = cellIndexes;
    }
}
