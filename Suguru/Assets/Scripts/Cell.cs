using TMPro;
using UnityEngine;

public class Cell
{
    public readonly bool initial;

    public TextMeshPro textMesh
    {
        get
        {
            if (pTextMesh == null)
            {
                Debug.LogError("TextMesh not set.");
            }

            return pTextMesh;
        }

        set
        {
            pTextMesh = value;
            
            if (initial)
            {
                pTextMesh.fontStyle = FontStyles.Bold;
            }
        }
    }

    public int fontSize
    {
        get => pFontSize == 0 ? 10 : pFontSize;

        set => pFontSize = value;
    }

    private readonly bool[] candidates;
    private TextMeshPro pTextMesh;
    private int value;
    private int pFontSize;

    public Cell(int value = 0)
    {
        this.value = value;
        initial = value != 0;

        candidates = new bool[9];
        for (int i = 0; i < 9; i++)
        {
            candidates[i] = false;
        }
    }

    public void SetValue(int v)
    {
        if (initial) Debug.LogError("Initial value can't be changed");

        value = value == v ? 0 : v;
        
        Show();
    }

    public void SwitchCandidate(int v)
    {
        if (initial) Debug.LogError("Initial value can't be changed");
        
        candidates[v - 1] = !candidates[v - 1];
        Show();
    }
    
    public void Erase()
    {
        if (initial) Debug.LogError("Initial value can't be changed");

        value = 0;
        for (int i = 0; i < candidates.Length; i++)
        {
            candidates[i] = false;
        }
    }

    public int GetValue()
    {
        return value;
    }

    private void Show()
    {
        if (initial) return;
        
        if (value != 0)
        {
            textMesh.fontSize = fontSize;
            textMesh.alignment = TextAlignmentOptions.Center;
            textMesh.text = value.ToString();
        }
        else
        {
            textMesh.fontSize = fontSize * 0.48f;
            textMesh.alignment = TextAlignmentOptions.Flush;

            textMesh.text = " ";
            for (int i = 0; i < candidates.Length; i++)
            {
                if (candidates[i])
                {
                    textMesh.text += i+1 + " ";
                }
                else
                {
                    textMesh.text += "   ";
                }

                if (i%3 == 2)
                {
                    textMesh.text += "\n";
                }
            }
        }

    }

    public override string ToString()
    {
        return value == 0 ? candidates.ToString() : value.ToString();
    }
}
