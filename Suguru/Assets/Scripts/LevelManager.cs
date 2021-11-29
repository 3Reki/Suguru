using System;
using JetBrains.Annotations;
using Suguru.Utils;
using UnityEngine;

public class LevelManager : MonoBehaviour
{
    [SerializeField] private Camera cam;
    [SerializeField] private GameObject background;
    [SerializeField] private Material mat;
    
    [CanBeNull] private GridMethod gridMethod;
    private SuguruGrid grid;
    private int insertNumber;

    private delegate void GridMethod(Vector3 worldPosition, int value);

    private void Start()
    {
        const int width = 5;
        const int height = 7;
        float screenUnitHeight = cam.orthographicSize * 2;
        float screenUnitWidth = screenUnitHeight * cam.aspect;
        float cellSize = Mathf.Min(screenUnitHeight * 0.7f * 0.8f / height, screenUnitWidth * 0.8f / width);
        var originPosition = new Vector3(-cellSize * width * 0.5f, -cellSize * height * 0.5f + screenUnitHeight * 0.15f);
        grid = new SuguruGrid(width, height, cellSize, originPosition, background, mat);
    }

    private void Update()
    {
        if (gridMethod != null && Input.GetMouseButtonDown(0) && !UtilsClass.IsPointerOverUI()) {
            gridMethod(UtilsClass.GetMouseWorldPosition(), insertNumber);
        }
    }

    public void DelegateToSet(int n)
    {
        insertNumber = n;
        gridMethod = grid.SetValue;
    }

    public void DelegateUnset()
    {
        gridMethod = null;
    }
}
