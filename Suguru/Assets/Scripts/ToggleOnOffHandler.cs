using UnityEngine;
using UnityEngine.UI;

public class ToggleOnOffHandler : MonoBehaviour
{
    [SerializeField] private LevelManager manager;
    [SerializeField] private Toggle toggle;
    
    public void OnNumberChange(int n) => manager.SetInsertNumber(toggle.isOn ? n : 0);
    
    public void OnCandidateModeChange()
    {
        if (toggle.isOn)
        {
            manager.CandidateMode();
        }
        else
        {
            manager.WriteMode();
        }
    }
    
    public void OnEraseModeChange()
    {
        if (toggle.isOn)
        {
            manager.EraseMode();
        }
        else
        {
            manager.WriteMode();
        }
    }
}
