//
//  DriverOrdersCell.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 5/7/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DriverOrdersCell: UITableViewCell {


    @IBOutlet weak var idLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var userLabel: UILabel!
    
    func configure(orders: [DriverOrderStruct]) {
        nameLabel.text = orders[0].name
        idLabel.text = ("\(String(orders[0].id))")
        userLabel.text = orders[0].user.username
        
    }
}
