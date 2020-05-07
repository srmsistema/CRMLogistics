//
//  Extension.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/25/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import Foundation
import UIKit

extension UIViewController {
    func showAlert(title: String, message: String)
    {
        let alert =  UIAlertController(title: title, message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "OK", style: .cancel, handler: nil)
        alert.addAction(action)
        DispatchQueue.main.async {
            self.present(alert, animated: true, completion: nil)
        }
    }
}


