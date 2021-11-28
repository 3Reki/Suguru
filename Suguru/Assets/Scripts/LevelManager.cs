using UnityEngine;

public class LevelManager : MonoBehaviour
{
    [SerializeField] private Camera cam;
    [SerializeField] private GameObject background;
    [SerializeField] private Material mat;
    
    private void Start()
    {
        int width = 5;
        int height = 7;
        float screenUnitWidth = cam.orthographicSize * Screen.width / Screen.height * 1.6f;
        float cellSize = screenUnitWidth/width;
        var originPosition = new Vector3(-cellSize * width * 0.5f, -cellSize * height * 0.5f);
        var grid = new SuguruGrid(width, height, cellSize, originPosition, background, mat);
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            Debug.Log("Screen Width : " + Screen.width);
        }
    }
}
