#include <iostream>
#include <cstring>

using namespace std;

struct PayComponent {
    char desc[30];
    float amount;
};

// Abstract base class
class CompCalculator {
public:
    virtual float compute(const PayComponent* comps, int n) = 0;
    virtual ~CompCalculator() {}
};

// Salary Calculator: sum of all components
class SalaryCalculator : public CompCalculator {
public:
    float compute(const PayComponent* comps, int n) override {
        float total = 0;
        for (int i = 0; i < n; ++i) {
            total += comps[i].amount;
        }
        return total;
    }
};

// Commission Calculator: 10% of each component
class CommissionCalculator : public CompCalculator {
public:
    float compute(const PayComponent* comps, int n) override {
        float commission = 0;
        for (int i = 0; i < n; ++i) {
            commission += comps[i].amount * 0.10f;
        }
        return commission;
    }
};

// Add new component
void addComponent(PayComponent*& comps, int& n, const PayComponent& newComp) {
    PayComponent* temp = new PayComponent[n + 1];
    for (int i = 0; i < n; ++i) {
        temp[i] = comps[i];
    }
    temp[n] = newComp;
    delete[] comps;
    comps = temp;
    ++n;
}

// Remove a component by index
void removeComponent(PayComponent*& comps, int& n, int index) {
    if (index < 0 || index >= n) return;
    PayComponent* temp = new PayComponent[n - 1];
    for (int i = 0, j = 0; i < n; ++i) {
        if (i != index) {
            temp[j++] = comps[i];
        }
    }
    delete[] comps;
    comps = temp;
    --n;
}

// Show all pay components
void showComponents(const PayComponent* comps, int n) {
    if (n == 0) {
        cout << "No components found.\n";
        return;
    }
    for (int i = 0; i < n; ++i) {
        cout << i << ". " << comps[i].desc << " - $" << comps[i].amount << endl;
    }
}

int main() {
    int numComponents = 0;
    PayComponent* comps = nullptr;

    CompCalculator* salaryCalc = new SalaryCalculator();
    CompCalculator* commissionCalc = new CommissionCalculator();

    int choice;
    do {
        cout << "\n--- Employee Compensation Menu ---\n";
        cout << "1. Add a pay component\n";
        cout << "2. Remove a component by index\n";
        cout << "3. Show all components\n";
        cout << "4. Compute total salary\n";
        cout << "5. Compute total commission\n";
        cout << "6. Compute total compensation (salary + commission)\n";
        cout << "0. Exit\n";
        cout << "Choose an option: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                PayComponent newComp;
                cout << "Enter description: ";
                cin.ignore();
                cin.getline(newComp.desc, 30);
                cout << "Enter amount: ";
                cin >> newComp.amount;
                addComponent(comps, numComponents, newComp);
                cout << "Component added!\n";
                break;
            }
            case 2: {
                showComponents(comps, numComponents);
                int index;
                cout << "Enter index to remove: ";
                cin >> index;
                removeComponent(comps, numComponents, index);
                cout << "Component removed.\n";
                break;
            }
            case 3: {
                showComponents(comps, numComponents);
                break;
            }
            case 4: {
                float total = salaryCalc->compute(comps, numComponents);
                cout << "Total Salary: $" << total << endl;
                break;
            }
            case 5: {
                float commission = commissionCalc->compute(comps, numComponents);
                cout << "Total Commission (10%): $" << commission << endl;
                break;
            }
            case 6: {
                float salary = salaryCalc->compute(comps, numComponents);
                float commission = commissionCalc->compute(comps, numComponents);
                cout << "Total Salary: $" << salary << endl;
                cout << "Total Commission: $" << commission << endl;
                cout << "Total Compensation: $" << (salary + commission) << endl;
                break;
            }
            case 0:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid option! Try again.\n";
        }

    } while (choice != 0);

    delete[] comps;
    delete salaryCalc;
    delete commissionCalc;

    return 0;
}

