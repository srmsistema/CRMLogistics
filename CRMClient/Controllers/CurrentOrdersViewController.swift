//
//  CurrentOrdersViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//


import UIKit
import Alamofire
import SwiftyJSON

class CurrentOrdersViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var tableView: UITableView!
    
    var orders = [OrderStruct]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        ServerManager.shared.getOrderList(token: UserDefaults.standard.value(forKey: "token") as! String, { (ordersList) in
            self.orders = ordersList
            self.tableView.reloadData()
        })
        {(error) in print(error)}
    }

    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return orders.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let order = orders[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "OrdersCell", for: indexPath) as! OrdersCell
        cell.configure(orders:order)
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let order = orders[indexPath.row]
        print(order.name)
        let storyboard = UIStoryboard(name: "Main", bundle: nil)

        if let detailsViewController = storyboard.instantiateViewController(withIdentifier: "DetailVC") as? DetailsViewController{
            detailsViewController.configure(order: order)
            detailsViewController.modalPresentationStyle = .fullScreen
            present(detailsViewController, animated: false, completion: nil)
        }
    }
}
    


