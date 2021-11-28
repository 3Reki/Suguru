using TMPro;
using UnityEngine;

public static class Utils
{
    public static TextMeshPro CreateWorldText(string text, Transform parent = null, Vector3 localPosition = default(Vector3),
        Vector2 sizeDelta = default(Vector2), int fontSize = 40, Color? color = null, TextAnchor anchor = TextAnchor.UpperLeft, 
        TextAlignmentOptions alignment = TextAlignmentOptions.Left, int sortingOrder = 5000)
    {
        color ??= Color.white;

        return CreateWorldText(parent, text, localPosition, sizeDelta, fontSize, (Color) color, anchor, alignment, sortingOrder);
    }
    
    public static TextMeshPro CreateWorldText(Transform parent, string text, Vector3 localPosition, Vector2 sizeDelta, 
        int fontSize, Color color, TextAnchor anchor, TextAlignmentOptions alignment, int sortingOrder)
    {
        var go = new GameObject("World Text", typeof(TextMeshPro));
        var transform = (RectTransform) go.transform;
        transform.SetParent(parent, false);
        transform.localPosition = localPosition;
        transform.sizeDelta = sizeDelta;
        var textMesh = go.GetComponent<TextMeshPro>();
        
        textMesh.alignment = alignment;
        textMesh.text = text;
        textMesh.fontSize = fontSize;
        textMesh.color = color;
        textMesh.GetComponent<MeshRenderer>().sortingOrder = sortingOrder;
        return textMesh;
    }
    
    public static void DrawLine(Vector3 start, Vector3 end, Color color, Material mat, Transform parent = null)
    {
        var lineGO = new GameObject("Line");
        var transform = lineGO.transform;
        transform.position = start;
        transform.SetParent(parent);
        lineGO.AddComponent<LineRenderer>();
        var lr = lineGO.GetComponent<LineRenderer>();
        lr.material = mat;
        lr.startColor = color;
        lr.endColor = color;
        lr.startWidth = 0.1f;
        lr.endWidth = 0.1f;
        lr.SetPosition(0, start);
        lr.SetPosition(1, end);
    }
}
