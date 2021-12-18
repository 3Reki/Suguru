using System;
using TMPro;

public class Cell
{
    public readonly bool initial;
    private readonly bool[] candidates;
    private readonly TextMeshPro textMesh;
    private readonly int fontSize;
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
        if (initial) throw new Exception("Initial value can't be changed");

        value = value == v ? 0 : v;
        
        Show();
    }

    public void SwitchCandidate(int v)
    {
        if (initial) throw new Exception("Initial value can't be changed");
        
        candidates[v - 1] = !candidates[v - 1];
        Show();
    }
    
    public void Erase()
    {
        if (initial) throw new Exception("Initial value can't be changed");

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
