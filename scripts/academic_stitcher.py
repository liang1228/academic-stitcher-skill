import argparse
import json
import re
import sys
from typing import Dict, List, Any

class AcademicStitcher:
    """
    Implements the 'Scientific Innovation Stitching' workflow following top-tier 
    (Nature/Science/Cell) rigor and anti-AI-style writing standards.
    """

    BUZZWORDS = [
        "revolutionary", "game-changing", "paradigm shift", "in recent years",
        "it is worth noting that", "a comprehensive study", "groundbreaking",
        "unprecedented", "delve into", "pivotal", "transformative"
    ]

    def __init__(self):
        self.rules = {
            "phases": ["Nature-Rigor", "Brainstorming Gate", "AI-Style Reduction"],
            "model": "A (Object) + B (Catalyst/Method) -> C (Scenario/Solution)"
        }

    def phase_1_nature_rigor(self, target: str, catalyst: str) -> str:
        """
        Validates if the combination has potential for top-tier publication.
        Checks for genericness and obvious incrementalism.
        Returns "SUCCESS" or "FAILED".
        """
        t_low = target.lower()
        c_low = catalyst.lower()

        incremental_patterns = [
            r"machine learning for",
            r"deep learning for",
            r"standard ai for",
            r"standard neural networks for",
            r"regression to predict"
        ]
        
        for pattern in incremental_patterns:
            if re.search(pattern, f"{c_low} for {t_low}"):
                return "FAILED"

        if len(target.strip()) < 10 or len(catalyst.strip()) < 3:
            return "FAILED"

        return "SUCCESS"

    def phase_2_brainstorming_gate(self, abstract: str) -> Dict[str, str]:
        """
        Deconstructs input into Object, Method, and Scenario.
        Includes robust fallbacks when regex heuristic fails.
        """
        deconstruction = {
            "Object": "Unknown Target Domain",
            "Method": "Unknown baseline approach",
            "Scenario": "General research environment"
        }
        
        obj_match = re.search(r"(?:focused on|study of|targeting|investigating|analysis of) ([\w\s\-]+?)(?:\.|\s+utilizing|\s+using|\s+via|\s+in\s+electric|\s+in\s+a|\s+for\s+[\w\s]+|$)", abstract, re.I)
        if obj_match:
            deconstruction["Object"] = obj_match.group(1).strip()
        else:
            first_clause = abstract.split(',')[0].split(' utilizing')[0].split(' using')[0]
            deconstruction["Object"] = first_clause.strip()

        method_match = re.search(r"(?:using|via|utilizing|employing|based on) ([\w\s\-]+?)(?:\s+in\s+electric|\s+in\s+a|\s+for\s+[\w\s]+|\s+to\s+[\w\s]+|\.|$)", abstract, re.I)
        if method_match:
            deconstruction["Method"] = method_match.group(1).strip()
        else:
            methods_db = ["spectroscopy", "microscopy", "simulation", "dft", "quantum", "modeling", "chromatography"]
            for m in methods_db:
                if m in abstract.lower():
                    deconstruction["Method"] = m
                    break

        scenario_match = re.search(r"(?:in|for|under|during) ([\w\s\-]+?)(?:\.|\s+utilizing|\s+using|\s+via|$)", abstract, re.I)
        if scenario_match:
            deconstruction["Scenario"] = scenario_match.group(1).strip()
        else:
            if "ev" in abstract.lower() or "electric vehicle" in abstract.lower():
                deconstruction["Scenario"] = "electric vehicle operations"
            elif "battery" in abstract.lower():
                deconstruction["Scenario"] = "battery degradation monitoring"

        return deconstruction

    def phase_3_ai_style_reduction(self, text: str) -> str:
        """
        Removes AI-style fluff and replaces it with direct academic prose.
        """
        cleaned_text = text
        for word in self.BUZZWORDS:
            cleaned_text = re.sub(rf"(?i)\b{word}\b", "", cleaned_text)
            cleaned_text = re.sub(rf"(?i){word}", "", cleaned_text)
        
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        cleaned_text = cleaned_text.replace(" .", ".").replace(" ,", ",")
        return cleaned_text

    def stitch(self, target_abstract: str, catalyst: str) -> Dict[str, Any]:
        """
        Executes the full 3-phase stitching workflow.
        """
        rigor_status = self.phase_1_nature_rigor(target_abstract, catalyst)
        if rigor_status == "FAILED":
            return {
                "status": "FAILED",
                "reason": "Fails Nature-Rigor criteria due to incrementalism or insufficient technical novelty."
            }

        decon = self.phase_2_brainstorming_gate(target_abstract)

        title = f"High-Fidelity {catalyst} for {decon['Object']} Optimization"
        core_logic = f"We integrate {catalyst} directly into the {decon['Scenario']} workflow, replacing traditional {decon['Method']} to bypass the classic transport-limit bottleneck."
        evidence_claim = f"Physical mapping of the {catalyst} variables models the non-linear degradation kinetics of the {decon['Object']} under operando conditions."

        refined_core_logic = self.phase_3_ai_style_reduction(core_logic)
        refined_evidence_claim = self.phase_3_ai_style_reduction(evidence_claim)

        return {
            "status": "SUCCESS",
            "deconstruction": decon,
            "idea": {
                "title": title,
                "core_logic": refined_core_logic,
                "evidence_claim": refined_evidence_claim
            }
        }

def main():
    parser = argparse.ArgumentParser(description="Academic Stitcher CLI Tool (Datawhale Standard)")
    parser.add_argument("--target", type=str, help="Research abstract or topic")
    parser.add_argument("--catalyst", type=str, help="New technology or method")
    parser.add_argument("--test", action="store_true", help="Run with default Battery MPGNN example")
    parser.add_argument("--json", action="store_true", help="Output raw JSON data directly to stdout")
    
    args = parser.parse_args()

    stitcher = AcademicStitcher()

    if args.test:
        target = "Current study of Lithium-ion battery degradation utilizing standard electrochemical impedance spectroscopy in electric vehicle scenarios."
        catalyst = "Multi-scale Physics-informed Graph Neural Networks (MPGNN)"
    elif args.target and args.catalyst:
        target = args.target
        catalyst = args.catalyst
    else:
        parser.print_help()
        sys.exit(1)

    results = stitcher.stitch(target, catalyst)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\n--- Starting Academic Stitcher Workflow ---")
        print(f"Target: {target[:100]}...")
        print(f"Catalyst: {catalyst}\n")
        
        print(f"--- [Phase 1] Nature-Rigor: {results['status']} ---")
        if results['status'] == "FAILED":
            print(f"Reason: {results['reason']}")
            sys.exit(1)
            
        print("\n--- [Phase 2] Brainstorming Gate Deconstruction ---")
        for k, v in results['deconstruction'].items():
            print(f"  {k}: {v}")
            
        print("\n--- [Phase 3] Refined Stitched Research Idea (Nature-Rigor Compliant) ---")
        print(f"Title: {results['idea']['title']}")
        print(f"Core Logic: {results['idea']['core_logic']}")
        print(f"Evidence Claim: {results['idea']['evidence_claim']}")

if __name__ == '__main__':
    main()
