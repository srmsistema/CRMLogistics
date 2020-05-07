//
//  HistoryViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class HistoryViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
    
    @IBAction func exitButton(_ sender: Any) {
        showAlert(title: "Alert!", message: "Вы уверены что хотите выйти?")
    }
}

