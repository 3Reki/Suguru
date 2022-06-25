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
        /******** Debug Vars ********/
        const int width = 3;
        const int height = 4;
        var regions = new Region[3];
        regions[0] = new Region(new[] {new Vector2(0, 0), new Vector2(1, 0), new Vector2(2, 0), new Vector2(0, 1)});
        regions[1] = new Region(new[] {new Vector2(1, 1), new Vector2(1, 2), new Vector2(2, 1), new Vector2(2, 2), new Vector2(2, 3)});
        regions[2] = new Region(new[] {new Vector2(0, 2), new Vector2(0, 3), new Vector2(1, 3)});
        /****************************/
        
        float screenUnitHeight = cam.orthographicSize * 2;
        float screenUnitWidth = screenUnitHeight * cam.aspect;
        float cellSize = Mathf.Min(screenUnitHeight * 0.7f * 0.8f / height, screenUnitWidth * 0.8f / width);
        var originPosition = new Vector3(-cellSize * width * 0.5f, -cellSize * height * 0.5f + screenUnitHeight * 0.15f);
        grid = new SuguruGrid(width, height, regions);
        grid.DrawGrid(cellSize, originPosition, background, mat);
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
