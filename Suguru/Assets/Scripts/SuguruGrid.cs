using System;
using TMPro;
using UnityEngine;

public class SuguruGrid
{
    private int width;
    private int height;
    private float cellSize;
    private Vector3 originPosition;
    private int[,] gridArray;

    public SuguruGrid(int width, int height, float cellSize, Vector3 originPosition, GameObject background, Material mat) {
        this.width = width;
        this.height = height;
        this.cellSize = cellSize;
        this.originPosition = originPosition;

        gridArray = new int[width, height];
        ShowGrid(background, mat);
    }

    public void ShowGrid(GameObject background, Material mat)
    {
        var debugTextArray = new TextMeshPro[width, height];
        var numbersGO = new GameObject("Numbers");
        var linesGO = new GameObject("Lines");
        var linesTransform = linesGO.transform;

        for (var i = 0; i < gridArray.GetLength(0); i++) {
            for (var j = 0; j < gridArray.GetLength(1); j++) {
                //debugTextArray[x, y] = UtilsClass.CreateWorldText(gridArray[x, y].ToString(), null, GetWorldPosition(x, y) + new Vector3(cellSize, cellSize) * .5f, 30, Color.white, TextAnchor.MiddleCenter);
                debugTextArray[i, j] = Utils.CreateWorldText(gridArray[i, j].ToString(), numbersGO.transform, 
                    GetWorldPosition(i, j) + new Vector3(cellSize, cellSize) * .5f, new Vector2(cellSize, cellSize), 10, 
                    Color.black, TextAnchor.MiddleCenter, TextAlignmentOptions.Center);
                Utils.DrawLine(GetWorldPosition(i, j), GetWorldPosition(i, j + 1), Color.black, mat, linesTransform);
                Utils.DrawLine(GetWorldPosition(i, j), GetWorldPosition(i + 1, j), Color.black, mat, linesTransform);
            }
        }
        Utils.DrawLine(GetWorldPosition(0, height), GetWorldPosition(width, height), Color.black, mat, linesTransform);
        Utils.DrawLine(GetWorldPosition(width, 0), GetWorldPosition(width, height), Color.black, mat, linesTransform);

        /*OnGridValueChanged += (object sender, Grid.OnGridValueChangedEventArgs eventArgs) => {
            debugTextArray[eventArgs.x, eventArgs.y].text = gridArray[eventArgs.x, eventArgs.y].ToString();
        };*/

        var bTransform = background.transform;
        bTransform.localScale = new Vector3(width, height) * cellSize;
        bTransform.position = originPosition + bTransform.localScale/2;
    }
    
    

    public int GetWidth() {
        return width;
    }

    public int GetHeight() {
        return height;
    }

    public float GetCellSize() {
        return cellSize;
    }

    public Vector3 GetWorldPosition(int x, int y) {
        return new Vector3(x, y) * cellSize + originPosition;
    }

    private Vector2Int GetXY(Vector3 worldPosition) {
        int x = Mathf.FloorToInt((worldPosition - originPosition).x / cellSize);
        int y = Mathf.FloorToInt((worldPosition - originPosition).y / cellSize);

        return new Vector2Int(x, y);
    }

    public void SetValue(int x, int y, int value)
    {
        try
        {
            gridArray[x, y] = value;
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine(e);
            throw;
        }
        //if (OnGridValueChanged != null) OnGridValueChanged(this, new Grid.OnGridValueChangedEventArgs { x = x, y = y });
    }

    public void SetValue(Vector3 worldPosition, int value) {
        Vector2Int index = GetXY(worldPosition);
        SetValue(index.x, index.y, value);
    }

    public int GetValue(int x, int y) {
        try {
            return gridArray[x, y];
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine(e);
            throw;
        }
    }

    public int GetValue(Vector3 worldPosition) {
        Vector2Int index = GetXY(worldPosition);
        return GetValue(index.x, index.y);
    }
}
