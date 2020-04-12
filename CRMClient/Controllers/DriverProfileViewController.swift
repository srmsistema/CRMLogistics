//
//  ClientProfileViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/26/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DriverProfileViewController: UIViewController {
    @IBOutlet weak var emailLabel: UILabel!
    @IBOutlet weak var loginLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    func profile(user: UserInfo){

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
            self.nextVC(identifier: "LoginDVC")
            alert.dismiss(animated: true, completion: nil)}))
        
        self.present(alert, animated: true, completion: nil)
        
        
    }

    
    }
    
