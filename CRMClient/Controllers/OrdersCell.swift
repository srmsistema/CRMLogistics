//
//  OrderCell.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 4/16/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class OrdersCell: UITableViewCell {

    @IBOutlet weak var idLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var dateLabel: UILabel!
    
    func configure(orders: OrderStruct) {
        
        nameLabel.text = ("Название: \(orders.name)")
        idLabel.text = ("№\(String(orders.id))")
        //dateLabel.text = orders.fromOrder

        
    }
}
