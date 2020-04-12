////
////  MainViewController.swift
////  CRMClient
////
////  Created by Nurzhan Ababakirov on 2/22/20.
////  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
////
//
//
//import UIKit
//
//var list = [String]()
//var sList = [String]()
//
//var indexAt = 0
//let defaults = UserDefaults.standard
//
//
//class TakeOrderViewController: UIViewController, UITableViewDataSource, UITableViewDelegate{
//    
//    private let defaults = UserDefaults.standard
//    
//    var list = ["Su", "ls"]
//    var sList = ["I am", "Hello"]
//    
//    @IBOutlet weak var tableView: UITableView!
//    
//    override func viewDidLoad() {
//        super.viewDidLoad()
//         sList = defaults.stringArray(forKey: "sList") ?? [String]()
//        list = defaults.stringArray(forKey: "list") ?? [String]()
//        tableView.delegate = self
//        tableView.dataSource = self
//        tableView.reloadData()
//        
//    }
//    
//    override func viewDidAppear(_ animated: Bool) {
//        tableView.reloadData()
//    }
//    
//
//    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
//        return 1
//    }
//
//    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
//        return list.count
//    }
//    
//    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
//        let cell = tableView.dequeueReusableCell(withIdentifier: "TextCell", for: indexPath)
//        let row = indexPath.row
//        cell.textLabel?.text = list[row]
//        cell.detailTextLabel!.text = sList[row]
//       
//        return cell
//    }
//    
//    func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath) {
//        indexAt = indexPath.row
//        let storyboard = UIStoryboard(name: "Main", bundle: nil)
//        let secondViewController = storyboard.instantiateViewController(withIdentifier: "info") as UIViewController
//        present(secondViewController, animated: true, completion: nil)
//    }
//
//    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath){
//        if editingStyle == .delete{
//            list.remove(at: indexPath.row)
//            sList.remove(at: indexPath.row)
//
//
//            tableView.deleteRows(at: [indexPath], with: UITableView.RowAnimation.fade)
//            self.tableView.reloadData()
//        }
//    }
//
//
//
//    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
//        tableView.deselectRow(at: indexPath, animated: true)
//
//        let row = indexPath.row
//        print(list[row])
//    }
//
//}
//
//
