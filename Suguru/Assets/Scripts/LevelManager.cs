using System;
using JetBrains.Annotations;
using Suguru.Utils;
using UnityEngine;

public class LevelManager : MonoBehaviour
{
    [SerializeField] private Camera cam;
    [SerializeField] private GameObject background;
    [SerializeField] private Material mat;
    
    private GridMethod gridMethod;
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
        gridMethod = grid.SetValue;
    }

    private void Update()
    {
        if (!Input.GetMouseButtonDown(0) || gridMethod != grid.Erase && insertNumber == 0 || 
            UtilsClass.IsPointerOverUI()) return;
        
        gridMethod(UtilsClass.GetMouseWorldPosition(), insertNumber);
    }

    public void WriteMode()
    {
        gridMethod = grid.SetValue;
    }
    
    public void CandidateMode()
    {
        gridMethod = grid.SetCandidate;
    }
    
    public void EraseMode()
    {
        gridMethod = grid.Erase;
    }

    public void SetInsertNumber(int n)
    {
        insertNumber = n;
    }

    
}
