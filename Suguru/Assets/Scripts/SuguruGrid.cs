using System;
using Suguru.Utils;
using TMPro;
using UnityEngine;

public class SuguruGrid
{
    private readonly Cell[,] gridArray;
    private readonly Region[] regions;
    private readonly int width;
    private readonly int height;
    private Vector3 originPosition;
    private float cellSize;

    public SuguruGrid(int width, int height, Region[] regions)
    {
        this.width = width;
        this.height = height;
        this.regions = regions;

        gridArray = new Cell[width, height];
        for (int i = 0; i < gridArray.GetLength(0); i++)
        {
            for (int j = 0; j < gridArray.GetLength(1); j++)
            {
                gridArray[i, j] = new Cell();
            }
        }
    }

    public void DrawGrid(float cellSize, Vector3 originPosition, GameObject background, Material mat)
    {
        this.cellSize = cellSize;
        this.originPosition = originPosition;
        ShowGrid(background, mat);
    }
    
    public void SetValue(Vector3 worldPosition, int value)
    {
        Vector2Int index = GetXY(worldPosition);

        if (IsValid(index))
        {
            SetValue(index, value);
        }
        
    }

    public void SetCandidate(Vector3 worldPosition, int value)
    {
        Vector2Int index = GetXY(worldPosition);

        if (IsValid(index))
        {
            SetCandidate(index, value);
        }
    }
    
    public void Erase(Vector3 worldPosition, int value)
    {
        Vector2Int index = GetXY(worldPosition);

        if (IsValid(index))
        {
            Erase(index.x, index.y);
        }
    }



    private void ShowGrid(GameObject background, Material mat)
    {
        TextMeshPro textMesh;
        var numbersGO = new GameObject("Numbers");
        var linesGO = new GameObject("Lines");
        Transform linesTransform = linesGO.transform;

        for (var i = 0; i < gridArray.GetLength(0); i++) {
            for (var j = 0; j < gridArray.GetLength(1); j++) {
                textMesh = UtilsClass.CreateWorldText("", numbersGO.transform, 
                    GetWorldPosition(i, j) + new Vector3(cellSize, cellSize) * .5f, 
                    new Vector2(cellSize, cellSize), 10,  Color.black, TextAnchor.MiddleCenter, TextAlignmentOptions.Center);
                
                gridArray[i, j].textMesh = textMesh;
                gridArray[i, j].fontSize = 10;
                UtilsClass.DrawLine(GetWorldPosition(i, j), GetWorldPosition(i, j + 1), Color.black, mat, linesTransform);
                UtilsClass.DrawLine(GetWorldPosition(i, j), GetWorldPosition(i + 1, j), Color.black, mat, linesTransform);
            }
        }
        UtilsClass.DrawLine(GetWorldPosition(0, height), GetWorldPosition(width, height), Color.black, mat, linesTransform);
        UtilsClass.DrawLine(GetWorldPosition(width, 0), GetWorldPosition(width, height), Color.black, mat, linesTransform);

        Transform bTransform = background.transform;
        bTransform.localScale = new Vector3(width, height) * cellSize;
        bTransform.position = originPosition + bTransform.localScale/2;
    }

    private Vector3 GetWorldPosition(int x, int y)
    {
        return new Vector3(x, y) * cellSize + originPosition;
    }

    private Vector2Int GetXY(Vector3 worldPosition)
    {
        int x = Mathf.FloorToInt((worldPosition - originPosition).x / cellSize);
        int y = Mathf.FloorToInt((worldPosition - originPosition).y / cellSize);

        return new Vector2Int(x, y);
    }

    private bool IsValid(Vector2Int index)
    {
        int x = index.x;
        int y = index.y;

        return x >= 0 && y >= 0 && x < gridArray.GetLength(0) && y < gridArray.GetLength(1);
    }

    private void SetValue(Vector2Int index, int value) => SetValue(index.x, index.y, value);
    
    private void SetValue(int x, int y, int value)
    {
        try
        {
            if (!gridArray[x, y].initial)
            {
                gridArray[x, y].SetValue(value);
            }
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine(e);
            throw;
        }
    }
    
    private void SetCandidate(Vector2Int index, int value) => SetCandidate(index.x, index.y, value);
    
    private void SetCandidate(int x, int y, int value)
    {
        try
        {
            if (!gridArray[x, y].initial)
            {
                gridArray[x, y].SwitchCandidate(value);
            }
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine(e);
            throw;
        }
    }

    private void Erase(int x, int y)
    {
        try
        {
            if (!gridArray[x, y].initial)
            {
                gridArray[x, y].Erase();
            }
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine(e);
            throw;
        }
    }
}
