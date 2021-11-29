using UnityEngine;
using UnityEngine.UI;

public class NumberToggles : MonoBehaviour
{
    [SerializeField] private LevelManager manager;
    
    public void OnValueChanged(int n)
    {
        if (GetComponent<Toggle>().isOn)
        {
            manager.DelegateToSet(n);
        }
        else
        {
            manager.DelegateUnset();
        }
    }
}
