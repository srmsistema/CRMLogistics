//
//  StatusViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/3/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class StatusViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    @IBOutlet weak var statusImage: UIImageView!
    
    @IBAction func finishButton(_ sender: UIButton) {
        statusImage.image = UIImage(named: "checkmark.seal.fill")
    }
    
}
