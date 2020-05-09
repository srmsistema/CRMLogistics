//
//  ClientProfileViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/26/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DriverProfileViewController: UIViewController {
    
    @IBOutlet weak var phoneLabel: UILabel!
    @IBOutlet weak var lnameLabel: UILabel!
    @IBOutlet weak var fnameLabel: UILabel!
    @IBOutlet weak var autoLabel: UILabel!
    
    var profile: DriverProfileStruct?
    override func viewDidLoad() {
        super.viewDidLoad()

        ServerManager.shared.getDriverProfileInfo(token: UserDefaults.standard.value(forKey: "token") as! String, { (data) in
            self.profile = data
            self.lnameLabel.text = data.last_name
            self.phoneLabel.text = data.phone
            self.fnameLabel.text = data.first_name
            switch data.auto_type{
            case 1:
                self.autoLabel.text = "Рефрижераторный фургон"
            case 2:
                self.autoLabel.text = "Jumbo"
            default:
                self.autoLabel.text =  "Тентованный полуприцеп (еврофура)"
            }
            
        }) { (error) in
            print(error)
        }
    }
    
  
    @IBAction func signOutButton(_ sender: Any) {
    createAlert(title: "Выход", message: "Вы уверены что хотите выйти?")
    
    }
    
    func nextVC(identifier: String) {
           let storyboard = UIStoryboard(name: "Main", bundle: nil)
               let nextVC = storyboard.instantiateViewController(withIdentifier: identifier)
           nextVC.modalPresentationStyle = .fullScreen
               self.present(nextVC, animated: false, completion: nil)
    }
    
    func createAlert(title: String, message: String)
    {
        let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertController.Style.alert)
        alert.addAction(UIAlertAction(title: "Отмена", style: UIAlertAction.Style.default, handler: {(action) in alert.dismiss(animated: true, completion: nil)}))
        alert.addAction(UIAlertAction(title: "Выйти", style: UIAlertAction.Style.destructive, handler: {(action) in
            self.nextVC(identifier: "SelectVC")
            UserDefaults.standard.set(nil, forKey: "token")
            alert.dismiss(animated: true, completion: nil)}))
            self.present(alert, animated: true, completion: nil)
    }
}
