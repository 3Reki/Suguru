using System;
using TMPro;

public class Cell
{
    private readonly bool[] candidates;
    private readonly bool initial;
    private TextMeshPro textMesh;
    private int fontSize;
    private int value;

    public Cell(TextMeshPro textMesh, int fontSize, int value = 0, bool initial = false)
    {
        this.textMesh = textMesh;
        this.fontSize = fontSize;
        this.value = value;
        this.initial = initial;

        candidates = new bool[9];
        for (int i = 0; i < 9; i++)
        {
            candidates[i] = false;
        }
        
        if (initial)
        {
            textMesh.fontStyle = FontStyles.Bold;
        }
    }

    public void SetValue(int v)
    {
        if (initial)
        {
            throw new Exception("Value can't be changed");
        }
        
        value = v;
        Show();
    }

    public void SwitchCandidate(int v)
    {
        candidates[v - 1] = !candidates[v - 1];
    }

    public int GetValue()
    {
        return value;
    }

    public void Show()
    {
        if (initial) return;
        
        if (value != 0)
        {
            textMesh.fontSize = fontSize;
            textMesh.text = value.ToString();
        }
        else
        {
            textMesh.fontSize = fontSize * 0.5f;
            // TODO : finish
        }

    }

    public override string ToString()
    {
        return value == 0 ? candidates.ToString() : value.ToString();
    }
}
