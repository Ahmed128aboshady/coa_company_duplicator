# -*- coding: utf-8 -*-
"""Writes index.html for coa_company_duplicator Odoo module description page."""

import os

OUTPUT_PATH = r'C:\Users\user\.gemini\antigravity\scratch\coa_addons_repo\coa_company_duplicator\static\description\index.html'

HTML = r'''<div style="font-family:'Inter',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;background:#F4F7FB;color:#1A2B3C;line-height:1.6;">

<!-- ═══════════════════════════════════════════════════════════════
     BOOTSTRAP 5 CDN
════════════════════════════════════════════════════════════════ -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

<!-- ═══════════════════════════════════════════════════════════════
     SECTION 1 · HERO HEADER
════════════════════════════════════════════════════════════════ -->
<section style="background:linear-gradient(135deg,#041F33 0%,#063153 50%,#0F5586 100%);padding:72px 0 0;position:relative;overflow:hidden;">

  <!-- subtle geometric decoration -->
  <div style="position:absolute;top:-120px;right:-120px;width:500px;height:500px;border-radius:50%;background:rgba(255,255,255,0.03);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;left:-80px;width:320px;height:320px;border-radius:50%;background:rgba(255,255,255,0.02);pointer-events:none;"></div>

  <div class="container" style="max-width:1160px;position:relative;z-index:2;">

    <!-- Top badge row -->
    <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:28px;">

      <!-- COA logo pill -->
      <div style="display:flex;align-items:center;gap:10px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);border-radius:999px;padding:6px 16px 6px 8px;backdrop-filter:blur(8px);">
        <img src="coa_logo.jpg" alt="COA Egypt Logo" style="width:32px;height:32px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,0.3);">
        <span style="color:#fff;font-size:13px;font-weight:600;letter-spacing:.3px;">COA Egypt</span>
      </div>

      <!-- Pulsing live badge -->
      <div style="display:flex;align-items:center;gap:8px;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.35);border-radius:999px;padding:5px 14px;">
        <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 3px rgba(34,197,94,0.35);animation:pulse 1.8s ease-in-out infinite;"></span>
        <span style="color:#86EFAC;font-size:12px;font-weight:600;letter-spacing:.5px;text-transform:uppercase;">Live &amp; Maintained</span>
      </div>

      <!-- Version badge -->
      <div style="background:linear-gradient(90deg,#8C1D22,#E61B21);border-radius:999px;padding:5px 16px;">
        <span style="color:#fff;font-size:12px;font-weight:700;letter-spacing:.5px;">Odoo 19 · 18 · 17 Ready</span>
      </div>
    </div>

    <!-- Main headline -->
    <h1 style="color:#fff;font-size:clamp(30px,4.5vw,54px);font-weight:900;line-height:1.1;margin:0 0 20px;max-width:780px;letter-spacing:-1px;">
      Duplicate Company Configurations<br>
      <span style="background:linear-gradient(90deg,#6EC3F5,#A5D8FF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Instantly &amp; Accurately</span>
    </h1>

    <!-- Subtitle -->
    <p style="color:#B0CBDF;font-size:clamp(15px,1.8vw,19px);font-weight:400;max-width:680px;margin:0 0 40px;line-height:1.7;">
      Seamlessly copy Chart of Accounts, Taxes, Journals, and Warehouse configurations from one company to another in your multi-company Odoo environment — eliminating manual re-entry and configuration errors.
    </p>

    <!-- Stat cards row -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:52px;">

      <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);border-radius:16px;padding:24px 20px;backdrop-filter:blur(6px);text-align:center;">
        <div style="font-size:36px;font-weight:900;color:#6EC3F5;line-height:1;">5+</div>
        <div style="color:#B0CBDF;font-size:13px;font-weight:500;margin-top:6px;">Config Types</div>
        <div style="color:rgba(176,203,223,0.6);font-size:11px;margin-top:4px;">CoA, Taxes, Journals, Warehouses &amp; more</div>
      </div>

      <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);border-radius:16px;padding:24px 20px;backdrop-filter:blur(6px);text-align:center;">
        <div style="font-size:36px;font-weight:900;color:#86EFAC;line-height:1;">1</div>
        <div style="color:#B0CBDF;font-size:13px;font-weight:500;margin-top:6px;">Click Wizard</div>
        <div style="color:rgba(176,203,223,0.6);font-size:11px;margin-top:4px;">Guided step-by-step duplication</div>
      </div>

      <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);border-radius:16px;padding:24px 20px;backdrop-filter:blur(6px);text-align:center;">
        <div style="font-size:36px;font-weight:900;color:#FCD34D;line-height:1;">∞</div>
        <div style="color:#B0CBDF;font-size:13px;font-weight:500;margin-top:6px;">Multi-Company</div>
        <div style="color:rgba(176,203,223,0.6);font-size:11px;margin-top:4px;">Unlimited company support</div>
      </div>

      <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);border-radius:16px;padding:24px 20px;backdrop-filter:blur(6px);text-align:center;">
        <div style="font-size:36px;font-weight:900;color:#F87171;line-height:1;">OPL</div>
        <div style="color:#B0CBDF;font-size:13px;font-weight:500;margin-top:6px;">Licensed</div>
        <div style="color:rgba(176,203,223,0.6);font-size:11px;margin-top:4px;">Odoo Proprietary License v1</div>
      </div>

    </div>

    <!-- Mac-style browser window screenshot -->
    <div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px 16px 0 0;overflow:hidden;max-width:960px;margin:0 auto;">

      <!-- Browser chrome bar -->
      <div style="background:#1A3A52;padding:12px 20px;display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,0.1);">
        <div style="display:flex;gap:7px;">
          <span style="width:12px;height:12px;border-radius:50%;background:#E61B21;display:inline-block;"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#F59E0B;display:inline-block;"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#22C55E;display:inline-block;"></span>
        </div>
        <div style="flex:1;background:rgba(255,255,255,0.08);border-radius:6px;padding:5px 14px;display:flex;align-items:center;gap:8px;">
          <span style="color:rgba(255,255,255,0.4);font-size:11px;">🔒</span>
          <span style="color:rgba(255,255,255,0.55);font-size:12px;font-family:monospace;">odoo.coa-egy.com/web#action=coa_company_duplicator</span>
        </div>
      </div>

      <!-- Screenshot -->
      <div style="background:#0A2740;">
        <img src="01_duplicate_wizard.png" alt="COA Company Duplicator Wizard" style="width:100%;display:block;border-radius:0;">
      </div>
    </div>

    <!-- Feature tags row -->
    <div style="display:flex;flex-wrap:wrap;gap:10px;padding:28px 0 0;justify-content:center;">
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Chart of Accounts</span>
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Tax Configuration</span>
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Journal Setup</span>
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Warehouse Config</span>
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Multi-Company</span>
      <span style="background:rgba(110,147,176,0.25);border:1px solid rgba(110,147,176,0.4);color:#A8C7DD;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># Odoo 19 Shared Accounts</span>
      <span style="background:rgba(140,29,34,0.3);border:1px solid rgba(230,27,33,0.4);color:#FCA5A5;border-radius:999px;padding:6px 16px;font-size:12px;font-weight:600;"># OPL-1 License</span>
    </div>

  </div><!-- /container -->

  <!-- Wave separator -->
  <div style="margin-top:52px;line-height:0;">
    <svg viewBox="0 0 1440 60" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" style="display:block;width:100%;height:60px;">
      <path d="M0,0 C360,60 1080,0 1440,60 L1440,60 L0,60 Z" fill="#F4F7FB"/>
    </svg>
  </div>

</section><!-- /hero -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 2 · PROBLEM VS SOLUTION
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:#F4F7FB;">
  <div class="container" style="max-width:1160px;">

    <!-- Section header -->
    <div style="text-align:center;margin-bottom:52px;">
      <div style="display:inline-flex;align-items:center;gap:8px;background:#E7EEF3;border:1px solid #C5D5E0;border-radius:999px;padding:5px 18px;margin-bottom:16px;">
        <span style="color:#0F5586;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">The Real Problem</span>
      </div>
      <h2 style="font-size:clamp(26px,3.5vw,40px);font-weight:800;color:#041F33;margin:0 0 14px;letter-spacing:-0.5px;">
        Why Manual Configuration Fails at Scale
      </h2>
      <p style="color:#4A6070;font-size:16px;max-width:580px;margin:0 auto;line-height:1.7;">
        Every new company in a multi-company Odoo setup demands hours of tedious configuration — until now.
      </p>
    </div>

    <!-- Two-column card grid -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;">

      <!-- WITHOUT card -->
      <div style="background:#fff;border-radius:20px;border:2px solid #FECACA;overflow:hidden;box-shadow:0 4px 24px rgba(230,27,33,0.08);">
        <div style="background:linear-gradient(90deg,#8C1D22,#E61B21);padding:20px 28px;display:flex;align-items:center;gap:12px;">
          <span style="font-size:22px;">❌</span>
          <div>
            <div style="color:#fff;font-size:18px;font-weight:800;">Without This Module</div>
            <div style="color:rgba(255,255,255,0.7);font-size:13px;">The painful old way</div>
          </div>
        </div>
        <div style="padding:28px;">
          <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:16px;">
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#FEE2E2;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;">✗</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Manual re-entry for every company</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Copy each account, tax, and journal by hand — one by one, company by company.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#FEE2E2;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;">✗</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Frequent tax &amp; journal mistakes</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Human error introduces mismatched tax codes, wrong journal types, broken fiscal positions.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#FEE2E2;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;">✗</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Hours of setup per company</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Configuring a new subsidiary from scratch takes 4–8 hours of consultant time.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#FEE2E2;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;">✗</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">No audit trail or history</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">No record of what was copied, when, or by whom — impossible to troubleshoot.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#FEE2E2;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;">✗</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Inconsistent configurations</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Different companies end up with different account structures, causing consolidation pain.</div>
              </div>
            </li>
          </ul>

          <div style="margin-top:24px;background:#FEF2F2;border:1px solid #FECACA;border-radius:12px;padding:16px;display:flex;align-items:center;gap:10px;">
            <span style="font-size:20px;">⏱️</span>
            <div style="color:#991B1B;font-weight:600;font-size:14px;">Average time per company: <strong>4–8 hours</strong> of manual work</div>
          </div>
        </div>
      </div><!-- /without card -->

      <!-- WITH card -->
      <div style="background:#fff;border-radius:20px;border:2px solid #BBF7D0;overflow:hidden;box-shadow:0 4px 24px rgba(34,197,94,0.08);">
        <div style="background:linear-gradient(90deg,#065F46,#059669);padding:20px 28px;display:flex;align-items:center;gap:12px;">
          <span style="font-size:22px;">✅</span>
          <div>
            <div style="color:#fff;font-size:18px;font-weight:800;">With COA Company Duplicator</div>
            <div style="color:rgba(255,255,255,0.7);font-size:13px;">The smart, accurate way</div>
          </div>
        </div>
        <div style="padding:28px;">
          <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:16px;">
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#D1FAE5;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;color:#059669;">✓</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">One-click duplication wizard</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Select source company, choose config types, click Execute — done in under 5 minutes.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#D1FAE5;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;color:#059669;">✓</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Accurate, validated configuration copy</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Intelligent mapping preserves relationships between accounts, taxes, and journals.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#D1FAE5;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;color:#059669;">✓</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">5-minute company setup</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Spin up a fully configured subsidiary in minutes, not hours — scale your Odoo footprint fast.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#D1FAE5;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;color:#059669;">✓</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Complete duplication history</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">Every operation is logged — who ran it, what was copied, when it happened.</div>
              </div>
            </li>
            <li style="display:flex;align-items:flex-start;gap:12px;">
              <span style="min-width:22px;height:22px;background:#D1FAE5;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px;color:#059669;">✓</span>
              <div>
                <div style="color:#1A2B3C;font-weight:600;font-size:14px;">Consistent cross-company structure</div>
                <div style="color:#6B8499;font-size:13px;margin-top:3px;">All companies share a perfectly synchronized accounting structure — consolidation made easy.</div>
              </div>
            </li>
          </ul>

          <div style="margin-top:24px;background:#ECFDF5;border:1px solid #BBF7D0;border-radius:12px;padding:16px;display:flex;align-items:center;gap:10px;">
            <span style="font-size:20px;">🚀</span>
            <div style="color:#065F46;font-weight:600;font-size:14px;">Average time per company: <strong>&lt; 5 minutes</strong> automated</div>
          </div>
        </div>
      </div><!-- /with card -->

    </div><!-- /grid -->
  </div><!-- /container -->
</section><!-- /problem-solution -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 3 · 6 FEATURE PILLARS
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:#fff;">
  <div class="container" style="max-width:1160px;">

    <div style="text-align:center;margin-bottom:52px;">
      <div style="display:inline-flex;align-items:center;gap:8px;background:#E7EEF3;border:1px solid #C5D5E0;border-radius:999px;padding:5px 18px;margin-bottom:16px;">
        <span style="color:#0F5586;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">Core Capabilities</span>
      </div>
      <h2 style="font-size:clamp(26px,3.5vw,40px);font-weight:800;color:#041F33;margin:0 0 14px;letter-spacing:-0.5px;">
        Six Powerful Feature Pillars
      </h2>
      <p style="color:#4A6070;font-size:16px;max-width:600px;margin:0 auto;line-height:1.7;">
        Every component of your accounting and inventory configuration is covered — from chart of accounts to warehouse locations.
      </p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:24px;">

      <!-- Pillar 1: Chart of Accounts -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;border-left:5px solid #0F5586;padding:28px;box-shadow:0 2px 16px rgba(15,85,134,0.07);transition:box-shadow .2s;">
        <div style="width:52px;height:52px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          📊
        </div>
        <h3 style="color:#041F33;font-size:18px;font-weight:700;margin:0 0 10px;">Chart of Accounts Duplication</h3>
        <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Duplicate the complete chart of accounts hierarchy from any source company to any target company. Preserves account codes, types, parent-child relationships, and all configuration properties automatically.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Full Hierarchy</span>
          <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Account Types</span>
          <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Tags &amp; Groups</span>
        </div>
      </div>

      <!-- Pillar 2: Tax Configuration -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;border-left:5px solid #063153;padding:28px;box-shadow:0 2px 16px rgba(6,49,83,0.07);">
        <div style="width:52px;height:52px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          🧾
        </div>
        <h3 style="color:#041F33;font-size:18px;font-weight:700;margin:0 0 10px;">Tax Configuration Copy</h3>
        <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Transfer all tax definitions — VAT, withholding, group taxes — with their account mappings, fiscal positions, and tax grids fully intact. No broken references or missing accounts after duplication.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:#E7EEF3;color:#063153;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Tax Groups</span>
          <span style="background:#E7EEF3;color:#063153;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Fiscal Positions</span>
          <span style="background:#E7EEF3;color:#063153;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Tax Grids</span>
        </div>
      </div>

      <!-- Pillar 3: Journal Setup -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;border-left:5px solid #6E93B0;padding:28px;box-shadow:0 2px 16px rgba(110,147,176,0.07);">
        <div style="width:52px;height:52px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          📒
        </div>
        <h3 style="color:#041F33;font-size:18px;font-weight:700;margin:0 0 10px;">Journal Setup Transfer</h3>
        <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Copy all journal configurations — Sales, Purchase, Bank, Cash, and Miscellaneous — including their default accounts, sequences, and payment method integrations. Bank accounts are linked correctly to the target company.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:#E7EEF3;color:#6E93B0;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">All Journal Types</span>
          <span style="background:#E7EEF3;color:#6E93B0;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Sequences</span>
          <span style="background:#E7EEF3;color:#6E93B0;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Bank Accounts</span>
        </div>
      </div>

      <!-- Pillar 4: Warehouse Config -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;border-left:5px solid #F59E0B;padding:28px;box-shadow:0 2px 16px rgba(245,158,11,0.07);">
        <div style="width:52px;height:52px;background:linear-gradient(135deg,#FEF3C7,#FDE68A);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          🏭
        </div>
        <h3 style="color:#041F33;font-size:18px;font-weight:700;margin:0 0 10px;">Warehouse &amp; Inventory Config</h3>
        <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Replicate warehouse structures including locations, routes, operation types, and inventory rules. Ensures the new company's stock module is ready to operate immediately after duplication.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:#FEF3C7;color:#92400E;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Locations</span>
          <span style="background:#FEF3C7;color:#92400E;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Routes</span>
          <span style="background:#FEF3C7;color:#92400E;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Operation Types</span>
        </div>
      </div>

      <!-- Pillar 5: Multi-Company Architecture -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;border-left:5px solid #8B5CF6;padding:28px;box-shadow:0 2px 16px rgba(139,92,246,0.07);">
        <div style="width:52px;height:52px;background:linear-gradient(135deg,#EDE9FE,#DDD6FE);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          🏢
        </div>
        <h3 style="color:#041F33;font-size:18px;font-weight:700;margin:0 0 10px;">Multi-Company Architecture Support</h3>
        <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Built natively for Odoo's multi-company framework. Respects company-level security rules, handles inter-company relationships, and works seamlessly with Odoo's native company switching mechanisms.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:#EDE9FE;color:#6D28D9;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Company Security</span>
          <span style="background:#EDE9FE;color:#6D28D9;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Any Source→Target</span>
          <span style="background:#EDE9FE;color:#6D28D9;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Unlimited Companies</span>
        </div>
      </div>

      <!-- Pillar 6: Odoo 19 Shared Accounts -->
      <div style="background:linear-gradient(135deg,#041F33,#063153);border-radius:18px;border:1px solid #0F5586;border-left:5px solid #6EC3F5;padding:28px;box-shadow:0 4px 24px rgba(4,31,51,0.2);">
        <div style="width:52px;height:52px;background:rgba(255,255,255,0.1);border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;font-size:24px;">
          🔗
        </div>
        <h3 style="color:#fff;font-size:18px;font-weight:700;margin:0 0 10px;">Odoo 19 Shared Accounts Ready</h3>
        <p style="color:#B0CBDF;font-size:14px;line-height:1.7;margin:0 0 16px;">
          Fully compatible with Odoo 19's revolutionary shared accounts architecture. The module intelligently handles shared vs. company-specific accounts, ensuring a clean duplication that respects the new account ownership model.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span style="background:rgba(110,195,245,0.2);color:#6EC3F5;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">v19 Compatible</span>
          <span style="background:rgba(110,195,245,0.2);color:#6EC3F5;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Shared Accounts</span>
          <span style="background:rgba(110,195,245,0.2);color:#6EC3F5;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Future-Proof</span>
        </div>
      </div>

    </div><!-- /pillars grid -->
  </div><!-- /container -->
</section><!-- /features -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 4 · 3-STEP WORKFLOW PIPELINE
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:linear-gradient(135deg,#041F33 0%,#063153 60%,#0A3D62 100%);position:relative;overflow:hidden;">

  <div style="position:absolute;inset:0;background-image:radial-gradient(circle at 20% 50%,rgba(15,85,134,0.3) 0%,transparent 50%),radial-gradient(circle at 80% 20%,rgba(110,147,176,0.15) 0%,transparent 40%);pointer-events:none;"></div>

  <div class="container" style="max-width:1160px;position:relative;z-index:2;">

    <div style="text-align:center;margin-bottom:60px;">
      <div style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:999px;padding:5px 18px;margin-bottom:16px;">
        <span style="color:#6EC3F5;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">How It Works</span>
      </div>
      <h2 style="font-size:clamp(26px,3.5vw,40px);font-weight:800;color:#fff;margin:0 0 14px;letter-spacing:-0.5px;">
        Three Steps to a Fully Configured Company
      </h2>
      <p style="color:#8AACBF;font-size:16px;max-width:560px;margin:0 auto;line-height:1.7;">
        Our guided wizard makes company configuration duplication foolproof and fast.
      </p>
    </div>

    <!-- Step pipeline -->
    <div style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:0;align-items:start;">

      <!-- STEP 1 -->
      <div style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:36px 28px;text-align:center;position:relative;">
        <div style="position:absolute;top:-18px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#0F5586,#6E93B0);border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;border:3px solid #063153;">1</div>
        <div style="font-size:48px;margin-bottom:18px;">🏗️</div>
        <h3 style="color:#fff;font-size:18px;font-weight:700;margin:0 0 12px;">Select Source Company</h3>
        <p style="color:#8AACBF;font-size:14px;line-height:1.7;margin:0;">
          Open the duplication wizard from the Settings menu. Choose any existing company as your source. The module displays a summary of available configurations — accounts, taxes, journals, and warehouses — ready to be copied.
        </p>
        <div style="margin-top:20px;background:rgba(15,85,134,0.3);border:1px solid rgba(110,195,245,0.3);border-radius:10px;padding:12px;">
          <span style="color:#6EC3F5;font-size:12px;font-weight:600;">⚡ Instant preview of source config</span>
        </div>
      </div>

      <!-- Arrow 1 -->
      <div style="display:flex;align-items:center;justify-content:center;padding:0 16px;padding-top:80px;">
        <div style="color:#6E93B0;font-size:28px;">→</div>
      </div>

      <!-- STEP 2 -->
      <div style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:36px 28px;text-align:center;position:relative;">
        <div style="position:absolute;top:-18px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#0F5586,#6E93B0);border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;border:3px solid #063153;">2</div>
        <div style="font-size:48px;margin-bottom:18px;">⚙️</div>
        <h3 style="color:#fff;font-size:18px;font-weight:700;margin:0 0 12px;">Choose Config Types to Copy</h3>
        <p style="color:#8AACBF;font-size:14px;line-height:1.7;margin:0;">
          Select which configuration types to duplicate using checkbox toggles. Mix and match: copy only the chart of accounts, or include taxes and journals too. Select the target company where the configuration will be applied.
        </p>
        <div style="margin-top:20px;background:rgba(15,85,134,0.3);border:1px solid rgba(110,195,245,0.3);border-radius:10px;padding:12px;">
          <span style="color:#6EC3F5;font-size:12px;font-weight:600;">✓ Granular per-type selection</span>
        </div>
      </div>

      <!-- Arrow 2 -->
      <div style="display:flex;align-items:center;justify-content:center;padding:0 16px;padding-top:80px;">
        <div style="color:#6E93B0;font-size:28px;">→</div>
      </div>

      <!-- STEP 3 -->
      <div style="background:linear-gradient(135deg,rgba(15,85,134,0.35),rgba(110,147,176,0.2));border:1px solid rgba(110,195,245,0.3);border-radius:20px;padding:36px 28px;text-align:center;position:relative;">
        <div style="position:absolute;top:-18px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#22C55E,#16A34A);border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;border:3px solid #063153;">3</div>
        <div style="font-size:48px;margin-bottom:18px;">✅</div>
        <h3 style="color:#fff;font-size:18px;font-weight:700;margin:0 0 12px;">Execute &amp; Verify</h3>
        <p style="color:#8AACBF;font-size:14px;line-height:1.7;margin:0;">
          Click Execute to start the duplication process. The system validates data integrity, copies all selected configurations to the target company, and generates a complete operation log. Switch to the target company and verify immediately.
        </p>
        <div style="margin-top:20px;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.35);border-radius:10px;padding:12px;">
          <span style="color:#86EFAC;font-size:12px;font-weight:600;">🎉 Company ready in &lt; 5 minutes</span>
        </div>
      </div>

    </div><!-- /pipeline grid -->

    <!-- Bottom summary bar -->
    <div style="margin-top:52px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:24px 32px;display:flex;align-items:center;justify-content:space-around;flex-wrap:wrap;gap:20px;">
      <div style="text-align:center;">
        <div style="color:#6EC3F5;font-size:28px;font-weight:800;">100%</div>
        <div style="color:#8AACBF;font-size:13px;">Configuration fidelity</div>
      </div>
      <div style="width:1px;height:40px;background:rgba(255,255,255,0.1);"></div>
      <div style="text-align:center;">
        <div style="color:#86EFAC;font-size:28px;font-weight:800;">&lt; 5 min</div>
        <div style="color:#8AACBF;font-size:13px;">Complete setup time</div>
      </div>
      <div style="width:1px;height:40px;background:rgba(255,255,255,0.1);"></div>
      <div style="text-align:center;">
        <div style="color:#FCD34D;font-size:28px;font-weight:800;">0 errors</div>
        <div style="color:#8AACBF;font-size:13px;">Manual data entry</div>
      </div>
      <div style="width:1px;height:40px;background:rgba(255,255,255,0.1);"></div>
      <div style="text-align:center;">
        <div style="color:#F87171;font-size:28px;font-weight:800;">Full</div>
        <div style="color:#8AACBF;font-size:13px;">Operation audit log</div>
      </div>
    </div>

  </div><!-- /container -->
</section><!-- /workflow -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 5 · LIVE SCREENSHOTS SHOWCASE
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:#F4F7FB;">
  <div class="container" style="max-width:1160px;">

    <div style="text-align:center;margin-bottom:52px;">
      <div style="display:inline-flex;align-items:center;gap:8px;background:#E7EEF3;border:1px solid #C5D5E0;border-radius:999px;padding:5px 18px;margin-bottom:16px;">
        <span style="color:#0F5586;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">Product Screenshots</span>
      </div>
      <h2 style="font-size:clamp(26px,3.5vw,40px);font-weight:800;color:#041F33;margin:0 0 14px;letter-spacing:-0.5px;">
        See It In Action
      </h2>
      <p style="color:#4A6070;font-size:16px;max-width:560px;margin:0 auto;line-height:1.7;">
        Real screenshots from the module running on Odoo 19 — no mockups.
      </p>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;">

      <!-- Screenshot 1: Duplicate Wizard -->
      <div style="background:#fff;border-radius:20px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 4px 20px rgba(15,85,134,0.08);">
        <div style="padding:20px 24px 16px;border-bottom:1px solid #F0F5F8;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0F5586;"></div>
            <h4 style="color:#041F33;font-size:16px;font-weight:700;margin:0;">Duplication Wizard</h4>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="background:#E7EEF3;color:#0F5586;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Step-by-Step</span>
            <span style="background:#E7EEF3;color:#0F5586;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Company Selection</span>
            <span style="background:#E7EEF3;color:#0F5586;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Config Toggles</span>
          </div>
        </div>
        <div style="padding:16px;">
          <div style="background:#F4F7FB;border-radius:12px;overflow:hidden;border:1px solid #E2EBF0;">
            <img src="01_duplicate_wizard.png" alt="COA Company Duplicator Wizard Interface" style="width:100%;display:block;">
          </div>
          <p style="color:#4A6070;font-size:13px;line-height:1.6;margin:14px 0 0;">
            The main duplication wizard allows you to select source and target companies, then toggle which configuration types to copy. A clear, intuitive interface with validation feedback before execution.
          </p>
        </div>
      </div>

      <!-- Screenshot 2: Company Config -->
      <div style="background:#fff;border-radius:20px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 4px 20px rgba(15,85,134,0.08);">
        <div style="padding:20px 24px 16px;border-bottom:1px solid #F0F5F8;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#063153;"></div>
            <h4 style="color:#041F33;font-size:16px;font-weight:700;margin:0;">Company Configuration Panel</h4>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="background:#E7EEF3;color:#063153;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Source Settings</span>
            <span style="background:#E7EEF3;color:#063153;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Target Preview</span>
            <span style="background:#E7EEF3;color:#063153;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Validation</span>
          </div>
        </div>
        <div style="padding:16px;">
          <div style="background:#F4F7FB;border-radius:12px;overflow:hidden;border:1px solid #E2EBF0;">
            <img src="02_company_config.png" alt="Company Configuration Settings Panel" style="width:100%;display:block;">
          </div>
          <p style="color:#4A6070;font-size:13px;line-height:1.6;margin:14px 0 0;">
            Detailed configuration panel showing the source company's accounting setup, with a live preview of what will be duplicated to the target. Smart conflict detection highlights potential issues before you execute.
          </p>
        </div>
      </div>

      <!-- Screenshot 3: Accounts List -->
      <div style="background:#fff;border-radius:20px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 4px 20px rgba(15,85,134,0.08);">
        <div style="padding:20px 24px 16px;border-bottom:1px solid #F0F5F8;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#6E93B0;"></div>
            <h4 style="color:#041F33;font-size:16px;font-weight:700;margin:0;">Chart of Accounts After Duplication</h4>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="background:#E7EEF3;color:#6E93B0;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Full CoA List</span>
            <span style="background:#E7EEF3;color:#6E93B0;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Hierarchy View</span>
            <span style="background:#E7EEF3;color:#6E93B0;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">All Types</span>
          </div>
        </div>
        <div style="padding:16px;">
          <div style="background:#F4F7FB;border-radius:12px;overflow:hidden;border:1px solid #E2EBF0;">
            <img src="03_accounts_list.png" alt="Chart of Accounts List After Duplication" style="width:100%;display:block;">
          </div>
          <p style="color:#4A6070;font-size:13px;line-height:1.6;margin:14px 0 0;">
            The target company's chart of accounts after a successful duplication. All accounts are correctly assigned to the new company, with proper hierarchy, codes, and account types preserved from the source.
          </p>
        </div>
      </div>

      <!-- Screenshot 4: Multi-Company -->
      <div style="background:#fff;border-radius:20px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 4px 20px rgba(15,85,134,0.08);">
        <div style="padding:20px 24px 16px;border-bottom:1px solid #F0F5F8;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#8B5CF6;"></div>
            <h4 style="color:#041F33;font-size:16px;font-weight:700;margin:0;">Multi-Company Overview</h4>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="background:#EDE9FE;color:#6D28D9;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">All Companies</span>
            <span style="background:#EDE9FE;color:#6D28D9;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Config Status</span>
            <span style="background:#EDE9FE;color:#6D28D9;border-radius:999px;padding:3px 10px;font-size:11px;font-weight:600;">Audit Log</span>
          </div>
        </div>
        <div style="padding:16px;">
          <div style="background:#F4F7FB;border-radius:12px;overflow:hidden;border:1px solid #E2EBF0;">
            <img src="04_multi_company.png" alt="Multi-Company Configuration Overview" style="width:100%;display:block;">
          </div>
          <p style="color:#4A6070;font-size:13px;line-height:1.6;margin:14px 0 0;">
            Bird's-eye view of all companies in the system with their configuration status. The audit log records every duplication operation — operator, timestamp, source company, target company, and configuration types copied.
          </p>
        </div>
      </div>

    </div><!-- /screenshots grid -->
  </div><!-- /container -->
</section><!-- /screenshots -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 6 · TECHNICAL SPECIFICATIONS TABLE
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:#fff;">
  <div class="container" style="max-width:1160px;">

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:start;">

      <!-- Left: Header + description -->
      <div>
        <div style="display:inline-flex;align-items:center;gap:8px;background:#E7EEF3;border:1px solid #C5D5E0;border-radius:999px;padding:5px 18px;margin-bottom:16px;">
          <span style="color:#0F5586;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">Technical Info</span>
        </div>
        <h2 style="font-size:clamp(24px,3vw,36px);font-weight:800;color:#041F33;margin:0 0 18px;letter-spacing:-0.5px;">
          Module Technical Specifications
        </h2>
        <p style="color:#4A6070;font-size:15px;line-height:1.7;margin:0 0 28px;">
          All technical details you need to evaluate compatibility, plan installation, and understand the module's footprint in your Odoo environment.
        </p>

        <!-- Compatibility badges -->
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="background:#E7EEF3;border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;">
            <div style="width:40px;height:40px;background:#0F5586;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;">🐍</div>
            <div>
              <div style="color:#041F33;font-weight:600;font-size:14px;">Python Compatibility</div>
              <div style="color:#4A6070;font-size:13px;">Python 3.10+ (Odoo 17), 3.11+ (Odoo 18/19)</div>
            </div>
          </div>
          <div style="background:#E7EEF3;border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;">
            <div style="width:40px;height:40px;background:#063153;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;">🗄️</div>
            <div>
              <div style="color:#041F33;font-weight:600;font-size:14px;">Database Support</div>
              <div style="color:#4A6070;font-size:13px;">PostgreSQL 14, 15, 16 (Odoo standard)</div>
            </div>
          </div>
          <div style="background:linear-gradient(90deg,#041F33,#063153);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;">
            <div style="width:40px;height:40px;background:rgba(255,255,255,0.15);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;">📦</div>
            <div>
              <div style="color:#fff;font-weight:600;font-size:14px;">OPL-1 License</div>
              <div style="color:#8AACBF;font-size:13px;">Odoo Proprietary License — single production instance</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right: Specs table -->
      <div style="background:#F4F7FB;border-radius:20px;border:1px solid #E2EBF0;overflow:hidden;">
        <div style="background:linear-gradient(90deg,#041F33,#063153);padding:18px 24px;">
          <div style="color:#fff;font-size:16px;font-weight:700;">📋 Module Metadata</div>
        </div>

        <table style="width:100%;border-collapse:collapse;">
          <tbody>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;width:45%;background:#F4F7FB;">Module Name</td>
              <td style="padding:16px 24px;color:#1A2B3C;font-size:13px;font-weight:500;background:#fff;">COA Duplicate Company Configuration PRO</td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">Technical ID</td>
              <td style="padding:16px 24px;background:#fff;">
                <code style="background:#E7EEF3;color:#0F5586;padding:3px 8px;border-radius:6px;font-size:12px;font-weight:700;">coa_company_duplicator</code>
              </td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">Odoo Versions</td>
              <td style="padding:16px 24px;background:#fff;">
                <div style="display:flex;gap:6px;flex-wrap:wrap;">
                  <span style="background:#0F5586;color:#fff;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:700;">17.0</span>
                  <span style="background:#063153;color:#fff;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:700;">18.0</span>
                  <span style="background:linear-gradient(90deg,#8C1D22,#E61B21);color:#fff;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:700;">19.0 ✨</span>
                </div>
              </td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">Editions</td>
              <td style="padding:16px 24px;background:#fff;">
                <div style="display:flex;gap:6px;flex-wrap:wrap;">
                  <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Community</span>
                  <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">Enterprise</span>
                </div>
              </td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">Dependencies</td>
              <td style="padding:16px 24px;background:#fff;">
                <div style="display:flex;gap:4px;flex-wrap:wrap;">
                  <code style="background:#E7EEF3;color:#063153;padding:2px 7px;border-radius:4px;font-size:11px;">base</code>
                  <code style="background:#E7EEF3;color:#063153;padding:2px 7px;border-radius:4px;font-size:11px;">account</code>
                  <code style="background:#E7EEF3;color:#063153;padding:2px 7px;border-radius:4px;font-size:11px;">stock</code>
                </div>
              </td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">License</td>
              <td style="padding:16px 24px;background:#fff;">
                <span style="background:linear-gradient(90deg,#8C1D22,#E61B21);color:#fff;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:700;">OPL-1</span>
                <span style="color:#4A6070;font-size:12px;margin-left:8px;">Odoo Proprietary</span>
              </td>
            </tr>
            <tr style="border-bottom:1px solid #E2EBF0;">
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;">Languages</td>
              <td style="padding:16px 24px;background:#fff;">
                <div style="display:flex;gap:6px;flex-wrap:wrap;">
                  <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">🇺🇸 English</span>
                  <span style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:11px;font-weight:600;">🇪🇬 Arabic</span>
                </div>
              </td>
            </tr>
            <tr>
              <td style="padding:16px 24px;color:#4A6070;font-size:13px;font-weight:600;background:#F4F7FB;border-radius:0 0 0 20px;">Author</td>
              <td style="padding:16px 24px;background:#fff;border-radius:0 0 20px 0;">
                <div style="display:flex;align-items:center;gap:10px;">
                  <img src="coa_logo.jpg" alt="COA Logo" style="width:28px;height:28px;border-radius:50%;object-fit:cover;">
                  <div>
                    <div style="color:#1A2B3C;font-weight:600;font-size:13px;">Community of Accountants</div>
                    <div style="color:#4A6070;font-size:11px;">COA-Egypt</div>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </div><!-- /2-col grid -->
  </div><!-- /container -->
</section><!-- /tech-specs -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 7 · FAQ
════════════════════════════════════════════════════════════════ -->
<section style="padding:80px 0;background:#F4F7FB;">
  <div class="container" style="max-width:800px;">

    <div style="text-align:center;margin-bottom:52px;">
      <div style="display:inline-flex;align-items:center;gap:8px;background:#E7EEF3;border:1px solid #C5D5E0;border-radius:999px;padding:5px 18px;margin-bottom:16px;">
        <span style="color:#0F5586;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">FAQ</span>
      </div>
      <h2 style="font-size:clamp(26px,3.5vw,40px);font-weight:800;color:#041F33;margin:0 0 14px;letter-spacing:-0.5px;">
        Frequently Asked Questions
      </h2>
      <p style="color:#4A6070;font-size:16px;margin:0 auto;line-height:1.7;">
        Answers to the most common questions about the COA Company Duplicator module.
      </p>
    </div>

    <!-- FAQ Items -->
    <div style="display:flex;flex-direction:column;gap:20px;">

      <!-- Q1 -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 2px 12px rgba(15,85,134,0.06);">
        <div style="padding:24px 28px;border-bottom:1px solid #F0F5F8;display:flex;align-items:flex-start;gap:16px;">
          <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#0F5586;font-weight:800;font-size:16px;margin-top:2px;">Q</div>
          <h3 style="color:#041F33;font-size:17px;font-weight:700;margin:0;line-height:1.4;">
            Will it overwrite existing accounts in the target company?
          </h3>
        </div>
        <div style="padding:20px 28px 24px 80px;">
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#0F5586,#6E93B0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:16px;flex-shrink:0;margin-top:2px;">A</div>
            <div>
              <p style="color:#1A2B3C;font-size:15px;line-height:1.7;margin:0 0 12px;">
                <strong>No — by default, existing records are preserved.</strong> The module uses a smart conflict resolution strategy. If an account with the same code already exists in the target company, it is <em>skipped</em> (not overwritten). Only accounts that don't yet exist in the target are created.
              </p>
              <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 12px;">
                This behavior protects you from accidentally replacing accounts that may already have journal entries or other financial records attached to them. If you specifically want to update an existing account's configuration, you can do so manually after the duplication completes.
              </p>
              <div style="background:#E7EEF3;border-left:4px solid #0F5586;border-radius:0 8px 8px 0;padding:12px 16px;">
                <span style="color:#0F5586;font-size:13px;font-weight:600;">💡 Tip: Run duplication on a fresh, empty company to get the cleanest results with zero conflicts.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Q2 -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 2px 12px rgba(15,85,134,0.06);">
        <div style="padding:24px 28px;border-bottom:1px solid #F0F5F8;display:flex;align-items:flex-start;gap:16px;">
          <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#0F5586;font-weight:800;font-size:16px;margin-top:2px;">Q</div>
          <h3 style="color:#041F33;font-size:17px;font-weight:700;margin:0;line-height:1.4;">
            Does it work with Odoo 19's shared accounts architecture?
          </h3>
        </div>
        <div style="padding:20px 28px 24px 80px;">
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#0F5586,#6E93B0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:16px;flex-shrink:0;margin-top:2px;">A</div>
            <div>
              <p style="color:#1A2B3C;font-size:15px;line-height:1.7;margin:0 0 12px;">
                <strong>Yes — full Odoo 19 shared accounts compatibility is a core feature.</strong> Odoo 19 introduced a major architectural change where accounts can be shared across multiple companies. Our module is specifically designed to handle this new paradigm.
              </p>
              <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 12px;">
                During duplication, the module intelligently distinguishes between:
              </p>
              <ul style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 12px;padding-left:20px;">
                <li style="margin-bottom:6px;"><strong style="color:#1A2B3C;">Shared accounts</strong> — linked to the target company without creating duplicates, respecting the shared ownership model.</li>
                <li style="margin-bottom:6px;"><strong style="color:#1A2B3C;">Company-specific accounts</strong> — duplicated individually with the target company as owner.</li>
              </ul>
              <div style="background:#D1FAE5;border-left:4px solid #059669;border-radius:0 8px 8px 0;padding:12px 16px;">
                <span style="color:#065F46;font-size:13px;font-weight:600;">✅ Fully tested on Odoo 19.0 — no broken references or duplicate shared accounts.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Q3 -->
      <div style="background:#fff;border-radius:18px;border:1px solid #E2EBF0;overflow:hidden;box-shadow:0 2px 12px rgba(15,85,134,0.06);">
        <div style="padding:24px 28px;border-bottom:1px solid #F0F5F8;display:flex;align-items:flex-start;gap:16px;">
          <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#E7EEF3,#C5D5E0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#0F5586;font-weight:800;font-size:16px;margin-top:2px;">Q</div>
          <h3 style="color:#041F33;font-size:17px;font-weight:700;margin:0;line-height:1.4;">
            Can I select specific configuration types to copy?
          </h3>
        </div>
        <div style="padding:20px 28px 24px 80px;">
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="min-width:36px;height:36px;background:linear-gradient(135deg,#0F5586,#6E93B0);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:16px;flex-shrink:0;margin-top:2px;">A</div>
            <div>
              <p style="color:#1A2B3C;font-size:15px;line-height:1.7;margin:0 0 12px;">
                <strong>Absolutely — granular selection is a first-class feature.</strong> The wizard presents each configuration type as an independent checkbox. You can select any combination:
              </p>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:14px;">
                <div style="background:#E7EEF3;border-radius:8px;padding:10px 14px;display:flex;align-items:center;gap:8px;">
                  <span style="color:#22C55E;font-weight:700;">☑</span>
                  <span style="color:#1A2B3C;font-size:13px;font-weight:500;">Chart of Accounts</span>
                </div>
                <div style="background:#E7EEF3;border-radius:8px;padding:10px 14px;display:flex;align-items:center;gap:8px;">
                  <span style="color:#22C55E;font-weight:700;">☑</span>
                  <span style="color:#1A2B3C;font-size:13px;font-weight:500;">Tax Configuration</span>
                </div>
                <div style="background:#E7EEF3;border-radius:8px;padding:10px 14px;display:flex;align-items:center;gap:8px;">
                  <span style="color:#22C55E;font-weight:700;">☑</span>
                  <span style="color:#1A2B3C;font-size:13px;font-weight:500;">Journal Setup</span>
                </div>
                <div style="background:#E7EEF3;border-radius:8px;padding:10px 14px;display:flex;align-items:center;gap:8px;">
                  <span style="color:#22C55E;font-weight:700;">☑</span>
                  <span style="color:#1A2B3C;font-size:13px;font-weight:500;">Warehouse Config</span>
                </div>
              </div>
              <p style="color:#4A6070;font-size:14px;line-height:1.7;margin:0 0 12px;">
                For example, if you already have taxes set up in the target company but need to copy only the chart of accounts, simply uncheck Taxes and Journals. The module handles dependency resolution automatically — if you copy journals, the required accounts will be included automatically.
              </p>
              <div style="background:#FEF3C7;border-left:4px solid #F59E0B;border-radius:0 8px 8px 0;padding:12px 16px;">
                <span style="color:#92400E;font-size:13px;font-weight:600;">⚠️ Note: Some config types have dependencies. The wizard will warn you if a required prerequisite type is not selected.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div><!-- /faq items -->
  </div><!-- /container -->
</section><!-- /faq -->


<!-- ═══════════════════════════════════════════════════════════════
     SECTION 8 · FOOTER CTA
════════════════════════════════════════════════════════════════ -->
<section style="background:linear-gradient(135deg,#041F33 0%,#063153 55%,#0F5586 100%);padding:80px 0;position:relative;overflow:hidden;">

  <div style="position:absolute;top:-60px;right:-60px;width:320px;height:320px;border-radius:50%;background:rgba(255,255,255,0.04);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;left:-80px;width:400px;height:400px;border-radius:50%;background:rgba(255,255,255,0.03);pointer-events:none;"></div>

  <div class="container" style="max-width:1160px;position:relative;z-index:2;text-align:center;">

    <!-- COA Logo + name -->
    <div style="display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:28px;">
      <img src="coa_logo.jpg" alt="COA Egypt Logo" style="width:64px;height:64px;border-radius:50%;object-fit:cover;border:3px solid rgba(255,255,255,0.25);box-shadow:0 4px 20px rgba(0,0,0,0.3);">
      <div style="text-align:left;">
        <div style="color:#fff;font-size:20px;font-weight:800;line-height:1.2;">Community of Accountants</div>
        <div style="color:#8AACBF;font-size:14px;font-weight:400;">COA-Egypt · Premium Odoo Modules</div>
      </div>
    </div>

    <!-- Headline -->
    <h2 style="color:#fff;font-size:clamp(26px,4vw,46px);font-weight:800;line-height:1.15;margin:0 0 16px;letter-spacing:-0.5px;max-width:700px;margin-left:auto;margin-right:auto;">
      Ready to Eliminate Manual<br>Company Configuration?
    </h2>
    <p style="color:#8AACBF;font-size:16px;max-width:520px;margin:0 auto 40px;line-height:1.7;">
      Install the COA Company Duplicator module today and start configuring new companies in minutes instead of hours.
    </p>

    <!-- Contact info cards -->
    <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:20px;margin-bottom:48px;">

      <a href="mailto:info@coa-egy.com" style="text-decoration:none;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:16px 24px;color:#fff;transition:background .2s;">
        <div style="width:40px;height:40px;background:rgba(15,85,134,0.5);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;">✉️</div>
        <div style="text-align:left;">
          <div style="font-size:11px;color:#8AACBF;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-bottom:2px;">Email Support</div>
          <div style="font-size:14px;font-weight:600;">info@coa-egy.com</div>
        </div>
      </a>

      <a href="https://www.coa-egy.com" target="_blank" style="text-decoration:none;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:16px 24px;color:#fff;transition:background .2s;">
        <div style="width:40px;height:40px;background:rgba(15,85,134,0.5);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;">🌐</div>
        <div style="text-align:left;">
          <div style="font-size:11px;color:#8AACBF;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-bottom:2px;">Website</div>
          <div style="font-size:14px;font-weight:600;">www.coa-egy.com</div>
        </div>
      </a>

    </div>

    <!-- Version badges row -->
    <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin-bottom:40px;">
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#B0CBDF;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">Odoo 17 ✓</span>
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#B0CBDF;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">Odoo 18 ✓</span>
      <span style="background:rgba(230,27,33,0.3);border:1px solid rgba(230,27,33,0.5);color:#FCA5A5;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">Odoo 19 ✨ NEW</span>
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#B0CBDF;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">Community Edition</span>
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#B0CBDF;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">Enterprise Edition</span>
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#B0CBDF;border-radius:999px;padding:6px 18px;font-size:12px;font-weight:600;">OPL-1 License</span>
    </div>

    <!-- Divider -->
    <div style="width:100%;height:1px;background:rgba(255,255,255,0.1);margin-bottom:28px;"></div>

    <!-- Bottom copyright row -->
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;">
      <div style="color:#4A7090;font-size:13px;">
        &copy; 2024–2026 Community of Accountants (COA-Egypt). All rights reserved.
      </div>
      <div style="display:flex;gap:20px;">
        <span style="color:#4A7090;font-size:12px;">Odoo App Store Module</span>
        <span style="color:#4A7090;font-size:12px;">•</span>
        <span style="color:#4A7090;font-size:12px;">coa_company_duplicator</span>
        <span style="color:#4A7090;font-size:12px;">•</span>
        <span style="color:#4A7090;font-size:12px;">OPL-1</span>
      </div>
    </div>

  </div><!-- /container -->
</section><!-- /footer -->

</div><!-- /root div -->
'''

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"File written: {OUTPUT_PATH}")
print(f"Size: {len(HTML.encode('utf-8')):,} bytes")

# Verify no BOM
with open(OUTPUT_PATH, 'rb') as f:
    raw = f.read(8)
print(f"First raw bytes (hex): {raw.hex()}")
if raw[:3] == b'\xef\xbb\xbf':
    print("ERROR: BOM DETECTED!")
else:
    print("OK: No BOM detected.")

# Print first 5 lines
with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"\nTotal lines: {len(lines)}")
print("--- First 5 lines ---")
for i, line in enumerate(lines[:5], 1):
    print(f"{i}: {line.rstrip()}")
