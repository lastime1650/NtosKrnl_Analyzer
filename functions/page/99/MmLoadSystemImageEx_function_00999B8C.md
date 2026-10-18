# MmLoadSystemImageEx

- RVA: `0x00999B8C`–`0x0099A1C5` (길이 `1,593` bytes)
- VA: `0x0000000140999B8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099540`
- 디코드: `422`개 명령, `1,593/1,593` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00999C0C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00999C25` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x00999C2D` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x00999C5A` → [MiGenerateSystemImageNames](../AD/MiGenerateSystemImageNames_function_00AD8CFC.md) (function, `0x00AD8CFC`)
- `0x00999C77` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (function, `0x004DC2A0`)
- `0x00999C97` → [MiObtainSectionForDriver](../A2/MiObtainSectionForDriver_function_00A24494.md) (function, `0x00A24494`)
- `0x00999CAD` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00999D02` → [MiUnloadSystemImage](../AA/MiUnloadSystemImage_function_00AA2FD4.md) (function, `0x00AA2FD4`)
- `0x00999D13` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)
- `0x00999D2E` → [MiLogFailedDriverLoad](../A2/MiLogFailedDriverLoad_function_00A24ACC.md) (function, `0x00A24ACC`)
- `0x00999D3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00999D4C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x00999D76` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00999D8E` → [MiGetSystemAddressForImage](../A7/MiGetSystemAddressForImage_function_00A74EEC.md) (function, `0x00A74EEC`)
- `0x00999DAC` → [MiCheckPurgeAndUpMapCount](../../text/41/MiCheckPurgeAndUpMapCount_function_004186B0.md) (function, `0x004186B0`)
- `0x00999DCD` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (function, `0x004318DC`)
- `0x00999DDA` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x00999DFE` → [MiReferenceActiveSubsection](../../text/32/MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x00999E1F` → [MiMapSystemImage](../AA/MiMapSystemImage_function_00AA3558.md) (function, `0x00AA3558`)
- `0x00999E48` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00999E97` → [MiValidateStrongCodeDriverImage](../A8/MiValidateStrongCodeDriverImage_function_00A8E69C.md) (function, `0x00A8E69C`)
- `0x00999EC7` → [MiLogStrongCodeDriverLoadFailure](../AC/MiLogStrongCodeDriverLoadFailure_function_00AC2E6C.md) (function, `0x00AC2E6C`)
- `0x00999EE8` → [MiConstructLoaderEntry](../AA/MiConstructLoaderEntry_function_00AAA264.md) (function, `0x00AAA264`)
- `0x00999F0D` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (function, `0x004318DC`)
- `0x00999F17` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00999F22` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00999F2E` → [KasanDriverLoadImage](../../text/4C/KasanDriverLoadImage_function_004C2820.md) (function, `0x004C2820`)
- `0x00999F7B` → [MiResolveImageImports](../7F/MiResolveImageImports_function_007F8144.md) (function, `0x007F8144`)
- `0x00999FA7` → [MiProcessLoadConfigForDriver](../A7/MiProcessLoadConfigForDriver_function_00A7FCE4.md) (function, `0x00A7FCE4`)
- `0x00999FBC` → [MiFinalizeKernelScpForSystemImage](../AA/MiFinalizeKernelScpForSystemImage_function_00AA02F8.md) (function, `0x00AA02F8`)
- `0x0099A00E` → [MiSetImageProtection](../../text/38/MiSetImageProtection_function_003843D0.md) (function, `0x003843D0`)
- `0x0099A016` → [MiRelocateAmount](../A9/MiRelocateAmount_function_00A96F4C.md) (function, `0x00A96F4C`)
- `0x0099A041` → [MiSetImageProtection](../../text/38/MiSetImageProtection_function_003843D0.md) (function, `0x003843D0`)
- `0x0099A055` → [VfDriverLoadImage](../../pagevrfy/BB/VfDriverLoadImage_function_00BB7DE4.md) (function, `0x00BB7DE4`)
- `0x0099A06E` → [KseDriverLoadImage](../95/KseDriverLoadImage_function_009588C0.md) (function, `0x009588C0`)
- `0x0099A090` → [MiApplyImportOptimizationToRuntimeDriver](../A9/MiApplyImportOptimizationToRuntimeDriver_function_00A9F93C.md) (function, `0x00A9F93C`)
- `0x0099A0AE` → [MiCompactServiceTable](../80/MiCompactServiceTable_function_0080C63C.md) (function, `0x0080C63C`)
- `0x0099A0C6` → [MiHandleDriverNonPagedSections](../A4/MiHandleDriverNonPagedSections_function_00A4AEA8.md) (function, `0x00A4AEA8`)
- `0x0099A0ED` → [MiFinalizeDriverCfgState](../A4/MiFinalizeDriverCfgState_function_00A4AD54.md) (function, `0x00A4AD54`)
- `0x0099A0FF` → [MiApplyRequiredDriverHotPatches](../70/MiApplyRequiredDriverHotPatches_function_007053D4.md) (function, `0x007053D4`)
- `0x0099A118` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x0099A128` → [MiCallImageNotify](../AD/MiCallImageNotify_function_00ADB9CC.md) (function, `0x00ADB9CC`)
- `0x0099A138` → [MiCacheImageSymbols](../AD/MiCacheImageSymbols_function_00AD9410.md) (function, `0x00AD9410`)
- `0x0099A141` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x0099A15E` → [MiProtectSystemImage](../AA/MiProtectSystemImage_function_00AA7D74.md) (function, `0x00AA7D74`)
- `0x0099A166` → [VfDriverLoadSucceeded](../../text/4B/VfDriverLoadSucceeded_function_004BD418.md) (function, `0x004BD418`)
- `0x0099A176` → [MmCallDllInitialize](../7F/MmCallDllInitialize_function_007F836C.md) (function, `0x007F836C`)
- `0x0099A184` → [MiFreeDriverInitialization](../A4/MiFreeDriverInitialization_function_00A4B120.md) (function, `0x00A4B120`)

### Direct callers
- [IopLoadCrashdumpDriver](../../text/4E/IopLoadCrashdumpDriver_function_004E2F70.md) at `0x004E2FD6`
- [MiApplyHotPatchToLoadedDriver](../80/MiApplyHotPatchToLoadedDriver_function_00802078.md) at `0x008021B6`
- [IopLoadDriver](IopLoadDriver_function_00997B54.md) at `0x00997DB1`
- [MmLoadSystemImage](MmLoadSystemImage_function_0099A9A0.md) at `0x0099A9C9`
- [IopLoadCrashdmpImage](../AD/IopLoadCrashdmpImage_function_00ADA790.md) at `0x00ADA7B4`
- [sub_00B37A8C](../B3/Unknown_function_00B37A8C.md) at `0x00B37B9D`
- [sub_00B37A8C](../B3/Unknown_function_00B37A8C.md) at `0x00B37C34`

### Static image references
- `0x00999C14` → RVA `0x00E0A74C` (`.data`; read)
- `0x00999E7D` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00999EA9` → RVA `0x00B09ED0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x00999C0C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00999C25` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x00999C2D` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x00999C77` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (`PAGE` → `.text`)
  - `0x00999CAD` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00999D13` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`PAGE` → `.text`)
  - `0x00999D3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00999D4C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x00999D76` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00999DAC` → [MiCheckPurgeAndUpMapCount](../../text/41/MiCheckPurgeAndUpMapCount_function_004186B0.md) (`PAGE` → `.text`)
  - `0x00999DCD` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (`PAGE` → `.text`)
  - `0x00999DDA` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (`PAGE` → `.text`)
  - `0x00999DFE` → [MiReferenceActiveSubsection](../../text/32/MiReferenceActiveSubsection_function_00325060.md) (`PAGE` → `.text`)
  - `0x00999E48` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00999F0D` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (`PAGE` → `.text`)
  - `0x00999F17` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00999F22` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00999F2E` → [KasanDriverLoadImage](../../text/4C/KasanDriverLoadImage_function_004C2820.md) (`PAGE` → `.text`)
  - `0x0099A00E` → [MiSetImageProtection](../../text/38/MiSetImageProtection_function_003843D0.md) (`PAGE` → `.text`)
  - `0x0099A041` → [MiSetImageProtection](../../text/38/MiSetImageProtection_function_003843D0.md) (`PAGE` → `.text`)
  - `0x0099A055` → [VfDriverLoadImage](../../pagevrfy/BB/VfDriverLoadImage_function_00BB7DE4.md) (`PAGE` → `PAGEVRFY`)
  - `0x0099A118` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x0099A141` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x0099A166` → [VfDriverLoadSucceeded](../../text/4B/VfDriverLoadSucceeded_function_004BD418.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00999B8C  48 8B C4                        mov rax, rsp
00999B8F  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00999B93  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00999B97  48 89 48 08                     mov qword ptr [rax + 8], rcx
00999B9B  55                              push rbp
00999B9C  56                              push rsi
00999B9D  57                              push rdi
00999B9E  41 54                           push r12
00999BA0  41 55                           push r13
00999BA2  41 56                           push r14
00999BA4  41 57                           push r15
00999BA6  48 8D 68 B9                     lea rbp, [rax - 0x47]
00999BAA  48 81 EC A0 00 00 00            sub rsp, 0xa0
00999BB1  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00999BB5  0F 57 C0                        xorps xmm0, xmm0
00999BB8  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
00999BBC  4C 8B F1                        mov r14, rcx
00999BBF  33 C9                           xor ecx, ecx
00999BC1  C6 45 6F 01                     mov byte ptr [rbp + 0x6f], 1
00999BC5  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
00999BC9  0F 57 C9                        xorps xmm1, xmm1
00999BCC  48 89 08                        mov qword ptr [rax], rcx
00999BCF  49 8B F1                        mov rsi, r9
00999BD2  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00999BD6  49 8B F8                        mov rdi, r8
00999BD9  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00999BDD  4C 8B EA                        mov r13, rdx
00999BE0  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00999BE4  44 8B F9                        mov r15d, ecx
00999BE7  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00999BEB  8B D9                           mov ebx, ecx
00999BED  48 89 08                        mov qword ptr [rax], rcx
00999BF0  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00999BF4  0F 11 4D D7                     movups xmmword ptr [rbp - 0x29], xmm1
00999BF8  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00999BFC  41 F6 C4 01                     test r12b, 1
00999C00  74 0A                           je 0x140999c0c
00999C02  B8 55 04 00 C0                  mov eax, 0xc0000455
00999C07  E9 47 01 00 00                  jmp 0x140999d53
00999C0C  E8 DF 45 96 FF                  call 0x1402fe1f0
00999C11  48 8B D0                        mov rdx, rax
00999C14  8B 05 32 0B 47 00               mov eax, dword ptr [rip + 0x470b32]
00999C1A  0F B7 C8                        movzx ecx, ax
00999C1D  39 8A 38 05 00 00               cmp dword ptr [rdx + 0x538], ecx
00999C23  73 16                           jae 0x140999c3b
00999C25  E8 96 61 AF FF                  call 0x14048fdc0
00999C2A  48 8B C8                        mov rcx, rax
00999C2D  E8 8E 8C AA FF                  call 0x1404428c0
00999C32  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00999C36  BB 01 00 00 00                  mov ebx, 1
00999C3B  48 8D 45 E7                     lea rax, [rbp - 0x19]
00999C3F  4C 8B C7                        mov r8, rdi
00999C42  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00999C47  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00999C4B  48 8D 45 F7                     lea rax, [rbp - 9]
00999C4F  49 8B D5                        mov rdx, r13
00999C52  49 8B CE                        mov rcx, r14
00999C55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00999C5A  E8 9D F0 13 00                  call 0x140ad8cfc
00999C5F  8B F8                           mov edi, eax
00999C61  85 C0                           test eax, eax
00999C63  0F 88 8D 00 00 00               js 0x140999cf6
00999C69  44 8B F3                        mov r14d, ebx
00999C6C  41 83 CE 02                     or r14d, 2
00999C70  4D 85 ED                        test r13, r13
00999C73  44 0F 44 F3                     cmove r14d, ebx
00999C77  E8 24 26 B4 FF                  call 0x1404dc2a0
00999C7C  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
00999C80  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00999C84  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00999C89  45 8B CC                        mov r9d, r12d
00999C8C  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00999C90  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00999C94  4C 8B C6                        mov r8, rsi
00999C97  E8 F8 A7 08 00                  call 0x140a24494
00999C9C  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
00999CA0  8B F8                           mov edi, eax
00999CA2  41 8B DE                        mov ebx, r14d
00999CA5  4D 85 FF                        test r15, r15
00999CA8  74 4C                           je 0x140999cf6
00999CAA  49 8B CF                        mov rcx, r15
00999CAD  E8 82 00 B4 FF                  call 0x1404d9d34
00999CB2  48 8B F0                        mov rsi, rax
00999CB5  F7 80 B8 00 00 00 00 01 00 00   test dword ptr [rax + 0xb8], 0x100
00999CBF  0F 85 AA 00 00 00               jne 0x140999d6f
00999CC5  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00999CC9  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00999CCD  4C 89 38                        mov qword ptr [rax], r15
00999CD0  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
00999CD4  48 89 01                        mov qword ptr [rcx], rax
00999CD7  49 8D 47 68                     lea rax, [r15 + 0x68]
00999CDB  8B 08                           mov ecx, dword ptr [rax]
00999CDD  45 33 FF                        xor r15d, r15d
00999CE0  81 E1 00 00 00 04               and ecx, 0x4000000
00999CE6  F7 D9                           neg ecx
00999CE8  1B FF                           sbb edi, edi
00999CEA  81 E7 8F 00 00 00               and edi, 0x8f
00999CF0  81 C7 0E 01 00 C0               add edi, 0xc000010e
00999CF6  85 FF                           test edi, edi
00999CF8  79 0D                           jns 0x140999d07
00999CFA  4D 85 FF                        test r15, r15
00999CFD  74 08                           je 0x140999d07
00999CFF  49 8B CF                        mov rcx, r15
00999D02  E8 CD 92 10 00                  call 0x140aa2fd4
00999D07  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00999D0B  48 85 C0                        test rax, rax
00999D0E  74 08                           je 0x140999d18
00999D10  48 8B C8                        mov rcx, rax
00999D13  E8 B8 99 B3 FF                  call 0x1404d36d0
00999D18  85 FF                           test edi, edi
00999D1A  79 17                           jns 0x140999d33
00999D1C  80 7D 6F 00                     cmp byte ptr [rbp + 0x6f], 0
00999D20  75 11                           jne 0x140999d33
00999D22  48 8B 4D 4F                     mov rcx, qword ptr [rbp + 0x4f]
00999D26  44 8B CF                        mov r9d, edi
00999D29  45 33 C0                        xor r8d, r8d
00999D2C  33 D2                           xor edx, edx
00999D2E  E8 99 AD 08 00                  call 0x140a24acc
00999D33  F6 C3 02                        test bl, 2
00999D36  74 0B                           je 0x140999d43
00999D38  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00999D3C  33 D2                           xor edx, edx
00999D3E  E8 2D 8B 1E 00                  call 0x140b82870
00999D43  F6 C3 01                        test bl, 1
00999D46  74 09                           je 0x140999d51
00999D48  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00999D4C  E8 6F FD AA FF                  call 0x140449ac0
00999D51  8B C7                           mov eax, edi
00999D53  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00999D5B  48 81 C4 A0 00 00 00            add rsp, 0xa0
00999D62  41 5F                           pop r15
00999D64  41 5E                           pop r14
00999D66  41 5D                           pop r13
00999D68  41 5C                           pop r12
00999D6A  5F                              pop rdi
00999D6B  5E                              pop rsi
00999D6C  5D                              pop rbp
00999D6D  C3                              ret
00999D6E  CC                              int3
00999D6F  4D 8B 6F 70                     mov r13, qword ptr [r15 + 0x70]
00999D73  49 8B CD                        mov rcx, r13
00999D76  E8 35 AF 8F FF                  call 0x140294cb0
00999D7B  41 8B D4                        mov edx, r12d
00999D7E  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00999D82  48 8B D8                        mov rbx, rax
00999D85  48 8B 08                        mov rcx, qword ptr [rax]
00999D88  8B 79 08                        mov edi, dword ptr [rcx + 8]
00999D8B  49 8B CF                        mov rcx, r15
00999D8E  E8 59 B1 0D 00                  call 0x140a74eec
00999D93  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00999D97  48 85 C0                        test rax, rax
00999D9A  75 0D                           jne 0x140999da9
00999D9C  BF 9A 00 00 C0                  mov edi, 0xc000009a
00999DA1  41 8B DE                        mov ebx, r14d
00999DA4  E9 51 FF FF FF                  jmp 0x140999cfa
00999DA9  48 8B CB                        mov rcx, rbx
00999DAC  E8 FF E8 A7 FF                  call 0x1404186b0
00999DB1  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00999DB5  41 B9 01 00 00 00               mov r9d, 1
00999DBB  0F BA AE B8 00 00 00 13         bts dword ptr [rsi + 0xb8], 0x13
00999DC3  49 8B CF                        mov rcx, r15
00999DC6  48 C1 E7 0C                     shl rdi, 0xc
00999DCA  4C 8B C7                        mov r8, rdi
00999DCD  E8 0A 7B A9 FF                  call 0x1404318dc
00999DD2  BA 02 00 00 00                  mov edx, 2
00999DD7  48 8B CB                        mov rcx, rbx
00999DDA  E8 ED 98 A1 FF                  call 0x1403b36cc
00999DDF  85 C0                           test eax, eax
00999DE1  75 07                           jne 0x140999dea
00999DE3  BF 0B 06 00 C0                  mov edi, 0xc000060b
00999DE8  EB B7                           jmp 0x140999da1
00999DEA  83 F8 02                        cmp eax, 2
00999DED  75 29                           jne 0x140999e18
00999DEF  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
00999DF6  41 B0 11                        mov r8b, 0x11
00999DF9  BA 88 00 00 00                  mov edx, 0x88
00999DFE  E8 5D B2 98 FF                  call 0x140325060
00999E03  8B F8                           mov edi, eax
00999E05  41 8B DE                        mov ebx, r14d
00999E08  85 C0                           test eax, eax
00999E0A  0F 88 E6 FE FF FF               js 0x140999cf6
00999E10  0F BA AE B8 00 00 00 0B         bts dword ptr [rsi + 0xb8], 0xb
00999E18  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00999E1C  49 8B CD                        mov rcx, r13
00999E1F  E8 34 97 10 00                  call 0x140aa3558
00999E24  8B F8                           mov edi, eax
00999E26  41 8B DE                        mov ebx, r14d
00999E29  85 C0                           test eax, eax
00999E2B  0F 88 C5 FE FF FF               js 0x140999cf6
00999E31  0F BA AE B8 00 00 00 0E         bts dword ptr [rsi + 0xb8], 0xe
00999E39  40 32 F6                        xor sil, sil
00999E3C  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00999E40  40 88 75 6F                     mov byte ptr [rbp + 0x6f], sil
00999E44  40 88 75 9F                     mov byte ptr [rbp - 0x61], sil
00999E48  E8 13 9D AA FF                  call 0x140443b60
00999E4D  48 8B D8                        mov rbx, rax
00999E50  48 85 C0                        test rax, rax
00999E53  75 0A                           jne 0x140999e5f
00999E55  BF 21 02 00 C0                  mov edi, 0xc0000221
00999E5A  E9 42 FF FF FF                  jmp 0x140999da1
00999E5F  B8 64 86 00 00                  mov eax, 0x8664
00999E64  66 39 43 04                     cmp word ptr [rbx + 4], ax
00999E68  0F 85 4D 03 00 00               jne 0x14099a1bb
00999E6E  B8 0B 02 00 00                  mov eax, 0x20b
00999E73  66 39 43 18                     cmp word ptr [rbx + 0x18], ax
00999E77  0F 85 3E 03 00 00               jne 0x14099a1bb
00999E7D  48 F7 05 00 CC 62 00 00 80 00 00  test qword ptr [rip + 0x62cc00], 0x8000
00999E88  74 47                           je 0x140999ed1
00999E8A  41 8B C4                        mov eax, r12d
00999E8D  25 00 00 00 40                  and eax, 0x40000000
00999E92  75 3D                           jne 0x140999ed1
00999E94  48 8B CB                        mov rcx, rbx
00999E97  E8 00 48 0F 00                  call 0x140a8e69c
00999E9C  8B F8                           mov edi, eax
00999E9E  85 C0                           test eax, eax
00999EA0  79 2F                           jns 0x140999ed1
00999EA2  0F 10 45 D7                     movups xmm0, xmmword ptr [rbp - 0x29]
00999EA6  49 8B D7                        mov rdx, r15
00999EA9  48 8D 0D 20 00 17 00            lea rcx, [rip + 0x170020]
00999EB0  F3 41 0F 7F 47 58               movdqu xmmword ptr [r15 + 0x58], xmm0
00999EB6  8B 43 58                        mov eax, dword ptr [rbx + 0x58]
00999EB9  41 89 47 78                     mov dword ptr [r15 + 0x78], eax
00999EBD  8B 43 08                        mov eax, dword ptr [rbx + 8]
00999EC0  41 89 87 9C 00 00 00            mov dword ptr [r15 + 0x9c], eax
00999EC7  E8 A0 8F 12 00                  call 0x140ac2e6c
00999ECC  E9 D0 FE FF FF                  jmp 0x140999da1
00999ED1  48 8D 45 B7                     lea rax, [rbp - 0x49]
00999ED5  45 8B CC                        mov r9d, r12d
00999ED8  4C 8D 45 E7                     lea r8, [rbp - 0x19]
00999EDC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00999EE1  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00999EE5  49 8B CF                        mov rcx, r15
00999EE8  E8 77 03 11 00                  call 0x140aaa264
00999EED  8B F8                           mov edi, eax
00999EEF  41 8B DE                        mov ebx, r14d
00999EF2  85 C0                           test eax, eax
00999EF4  0F 88 FC FD FF FF               js 0x140999cf6
00999EFA  48 8B 75 B7                     mov rsi, qword ptr [rbp - 0x49]
00999EFE  4D 8B C4                        mov r8, r12
00999F01  48 8B CE                        mov rcx, rsi
00999F04  41 B9 02 00 00 00               mov r9d, 2
00999F0A  49 8B D7                        mov rdx, r15
00999F0D  E8 CA 79 A9 FF                  call 0x1404318dc
00999F12  33 D2                           xor edx, edx
00999F14  49 8B CF                        mov rcx, r15
00999F17  E8 54 89 1E 00                  call 0x140b82870
00999F1C  48 8B CE                        mov rcx, rsi
00999F1F  4C 8B FE                        mov r15, rsi
00999F22  E8 0D FE B3 FF                  call 0x1404d9d34
00999F27  4C 8B E8                        mov r13, rax
00999F2A  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00999F2E  E8 ED 88 B2 FF                  call 0x1404c2820
00999F33  8B F8                           mov edi, eax
00999F35  85 C0                           test eax, eax
00999F37  0F 88 B9 FD FF FF               js 0x140999cf6
00999F3D  41 0F BA AD B8 00 00 00 11      bts dword ptr [r13 + 0xb8], 0x11
00999F46  45 8B EC                        mov r13d, r12d
00999F49  41 81 E5 00 00 00 40            and r13d, 0x40000000
00999F50  41 0F BA E4 1D                  bt r12d, 0x1d
00999F55  72 39                           jb 0x140999f90
00999F57  48 8B 55 57                     mov rdx, qword ptr [rbp + 0x57]
00999F5B  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00999F5F  33 C0                           xor eax, eax
00999F61  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00999F66  45 85 ED                        test r13d, r13d
00999F69  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00999F6D  4C 8D 45 F7                     lea r8, [rbp - 9]
00999F71  48 8B CE                        mov rcx, rsi
00999F74  0F 95 C0                        setne al
00999F77  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00999F7B  E8 C4 E1 E5 FF                  call 0x1407f8144
00999F80  8B F8                           mov edi, eax
00999F82  85 C0                           test eax, eax
00999F84  8A 45 9F                        mov al, byte ptr [rbp - 0x61]
00999F87  88 45 6F                        mov byte ptr [rbp + 0x6f], al
00999F8A  0F 88 66 FD FF FF               js 0x140999cf6
00999F90  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00999F94  48 83 E8 80                     sub rax, -0x80
00999F98  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00999F9C  45 85 ED                        test r13d, r13d
00999F9F  75 18                           jne 0x140999fb9
00999FA1  48 8B D0                        mov rdx, rax
00999FA4  48 8B CE                        mov rcx, rsi
00999FA7  E8 38 5D 0E 00                  call 0x140a7fce4
00999FAC  8B F8                           mov edi, eax
00999FAE  41 8B DE                        mov ebx, r14d
00999FB1  85 C0                           test eax, eax
00999FB3  0F 88 3D FD FF FF               js 0x140999cf6
00999FB9  48 8B CE                        mov rcx, rsi
00999FBC  E8 37 63 10 00                  call 0x140aa02f8
00999FC1  8B F8                           mov edi, eax
00999FC3  41 8B DE                        mov ebx, r14d
00999FC6  85 C0                           test eax, eax
00999FC8  0F 88 28 FD FF FF               js 0x140999cf6
00999FCE  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00999FD2  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00999FD6  0F BA A8 B8 00 00 00 12         bts dword ptr [rax + 0xb8], 0x12
00999FDE  48 8B 03                        mov rax, qword ptr [rbx]
00999FE1  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00999FE5  F6 41 2E 40                     test byte ptr [rcx + 0x2e], 0x40
00999FE9  75 5B                           jne 0x14099a046
00999FEB  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
00999FEF  41 B9 04 00 00 00               mov r9d, 4
00999FF5  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00999FF9  48 8B CE                        mov rcx, rsi
00999FFC  45 8D 41 04                     lea r8d, [r9 + 4]
0099A000  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
0099A004  8B 78 3C                        mov edi, dword ptr [rax + 0x3c]
0099A007  48 03 7D A7                     add rdi, qword ptr [rbp - 0x59]
0099A00B  48 8B D7                        mov rdx, rdi
0099A00E  E8 BD A3 9E FF                  call 0x1403843d0
0099A013  48 8B CB                        mov rcx, rbx
0099A016  E8 31 CF 0F 00                  call 0x140a96f4c
0099A01B  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0099A01F  48 2B C8                        sub rcx, rax
0099A022  48 89 0F                        mov qword ptr [rdi], rcx
0099A025  48 83 BB 90 00 00 00 00         cmp qword ptr [rbx + 0x90], 0
0099A02D  74 17                           je 0x14099a046
0099A02F  41 B9 00 01 00 00               mov r9d, 0x100
0099A035  41 B8 08 00 00 00               mov r8d, 8
0099A03B  48 8B D7                        mov rdx, rdi
0099A03E  48 8B CE                        mov rcx, rsi
0099A041  E8 8A A3 9E FF                  call 0x1403843d0
0099A046  45 85 ED                        test r13d, r13d
0099A049  75 56                           jne 0x14099a0a1
0099A04B  44 21 6D A3                     and dword ptr [rbp - 0x5d], r13d
0099A04F  45 33 C0                        xor r8d, r8d
0099A052  48 8B CE                        mov rcx, rsi
0099A055  E8 8A DD 21 00                  call 0x140bb7de4
0099A05A  4C 8B 6D AF                     mov r13, qword ptr [rbp - 0x51]
0099A05E  48 8D 55 A3                     lea rdx, [rbp - 0x5d]
0099A062  48 8B CE                        mov rcx, rsi
0099A065  41 0F BA AD B8 00 00 00 0F      bts dword ptr [r13 + 0xb8], 0xf
0099A06E  E8 4D E8 FB FF                  call 0x1409588c0
0099A073  8B F8                           mov edi, eax
0099A075  41 8B DE                        mov ebx, r14d
0099A078  85 C0                           test eax, eax
0099A07A  0F 88 76 FC FF FF               js 0x140999cf6
0099A080  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0099A084  48 8B CE                        mov rcx, rsi
0099A087  41 0F BA AD B8 00 00 00 10      bts dword ptr [r13 + 0xb8], 0x10
0099A090  E8 A7 58 10 00                  call 0x140a9f93c
0099A095  8B F8                           mov edi, eax
0099A097  85 C0                           test eax, eax
0099A099  0F 88 57 FC FF FF               js 0x140999cf6
0099A09F  EB 04                           jmp 0x14099a0a5
0099A0A1  4C 8B 6D AF                     mov r13, qword ptr [rbp - 0x51]
0099A0A5  41 F6 C4 04                     test r12b, 4
0099A0A9  74 15                           je 0x14099a0c0
0099A0AB  48 8B CE                        mov rcx, rsi
0099A0AE  E8 89 25 E7 FF                  call 0x14080c63c
0099A0B3  8B F8                           mov edi, eax
0099A0B5  41 8B DE                        mov ebx, r14d
0099A0B8  85 C0                           test eax, eax
0099A0BA  0F 88 36 FC FF FF               js 0x140999cf6
0099A0C0  41 8B D4                        mov edx, r12d
0099A0C3  48 8B CE                        mov rcx, rsi
0099A0C6  E8 DD 0D 0B 00                  call 0x140a4aea8
0099A0CB  8B F8                           mov edi, eax
0099A0CD  41 8B DE                        mov ebx, r14d
0099A0D0  85 C0                           test eax, eax
0099A0D2  0F 88 1E FC FF FF               js 0x140999cf6
0099A0D8  41 0F BA E4 1E                  bt r12d, 0x1e
0099A0DD  0F 82 88 00 00 00               jb 0x14099a16b
0099A0E3  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
0099A0E7  41 8B D4                        mov edx, r12d
0099A0EA  48 8B CE                        mov rcx, rsi
0099A0ED  E8 62 0C 0B 00                  call 0x140a4ad54
0099A0F2  8B F8                           mov edi, eax
0099A0F4  85 C0                           test eax, eax
0099A0F6  0F 88 FA FB FF FF               js 0x140999cf6
0099A0FC  48 8B CE                        mov rcx, rsi
0099A0FF  E8 D0 B2 D6 FF                  call 0x1407053d4
0099A104  8B F8                           mov edi, eax
0099A106  85 C0                           test eax, eax
0099A108  0F 88 E8 FB FF FF               js 0x140999cf6
0099A10E  81 4E 68 00 40 00 41            or dword ptr [rsi + 0x68], 0x41004000
0099A115  48 8B CE                        mov rcx, rsi
0099A118  E8 17 FC B3 FF                  call 0x1404d9d34
0099A11D  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
0099A121  83 88 B8 00 00 00 02            or dword ptr [rax + 0xb8], 2
0099A128  E8 9F 18 14 00                  call 0x140adb9cc
0099A12D  4C 8D 45 D7                     lea r8, [rbp - 0x29]
0099A131  48 8B CE                        mov rcx, rsi
0099A134  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0099A138  E8 D3 F2 13 00                  call 0x140ad9410
0099A13D  48 8B 4E 70                     mov rcx, qword ptr [rsi + 0x70]
0099A141  E8 6A AB 8F FF                  call 0x140294cb0
0099A146  48 83 B8 90 00 00 00 00         cmp qword ptr [rax + 0x90], 0
0099A14E  74 09                           je 0x14099a159
0099A150  F7 46 68 00 00 00 08            test dword ptr [rsi + 0x68], 0x8000000
0099A157  75 0A                           jne 0x14099a163
0099A159  33 D2                           xor edx, edx
0099A15B  48 8B CE                        mov rcx, rsi
0099A15E  E8 11 DC 10 00                  call 0x140aa7d74
0099A163  48 8B CE                        mov rcx, rsi
0099A166  E8 AD 32 B2 FF                  call 0x1404bd418
0099A16B  33 FF                           xor edi, edi
0099A16D  41 F6 C4 08                     test r12b, 8
0099A171  74 18                           je 0x14099a18b
0099A173  48 8B CE                        mov rcx, rsi
0099A176  E8 F1 E1 E5 FF                  call 0x1407f836c
0099A17B  8B F8                           mov edi, eax
0099A17D  85 C0                           test eax, eax
0099A17F  78 0A                           js 0x14099a18b
0099A181  48 8B CE                        mov rcx, rsi
0099A184  E8 97 0F 0B 00                  call 0x140a4b120
0099A189  EB 0B                           jmp 0x14099a196
0099A18B  41 8B DE                        mov ebx, r14d
0099A18E  85 FF                           test edi, edi
0099A190  0F 88 64 FB FF FF               js 0x140999cfa
0099A196  41 0F BA B5 B8 00 00 00 08      btr dword ptr [r13 + 0xb8], 8
0099A19F  41 8B DE                        mov ebx, r14d
0099A1A2  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0099A1A6  33 FF                           xor edi, edi
0099A1A8  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0099A1AC  48 89 30                        mov qword ptr [rax], rsi
0099A1AF  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0099A1B3  48 89 01                        mov qword ptr [rcx], rax
0099A1B6  E9 4C FB FF FF                  jmp 0x140999d07
0099A1BB  BF 30 01 00 C0                  mov edi, 0xc0000130
0099A1C0  E9 DC FB FF FF                  jmp 0x140999da1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmLoadSystemImageEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    a1 = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 111) = 1;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 81) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 71 - 9) = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))) & (1)) == 0) goto loc_00999C0C;
    goto loc_00999D53;
loc_00999C0C:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = (unsigned int)(*(unsigned int *)(v_rip + 4655922));
    v_rbx = 0;
    if ((*(unsigned int *)(result + 1336)) < ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4655922)))))) {
        result = HalAdjustResourceList((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4655922))), result, a3, a4);
        a1 = result;
        result = PsAttachSiloToCurrentThread(a1, result, a3, a4);
        *(unsigned __int64 *)(v_rsp - 71 - 49) = result;
        v_rbx = 1;
    }
    v_stack_mB0 = v_rsp - 71 - 25;
    v_stack_mB8 = v_rsp - 71 - 9;
    result = MiGenerateSystemImageNames(a1, a2, a3, v_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | (2));
    if (a2 == 0) { v_r14 = (unsigned int)(v_rbx); }
    result = MmAcquireLoadLock(a1, a2, a3, v_rsp - 71 - 41);
    v_stack_mB8 = v_rsp - 71 - 81;
    *(unsigned __int64 *)(v_rsp - 71 - 57) = result;
    result = MiObtainSectionForDriver(v_rsp - 71 - 25, *(unsigned __int64 *)(v_rsp - 71 + 79), a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))));
    if (*(unsigned __int64 *)(v_rsp - 71 - 81) == 0) goto loc_00999CF6;
    result = MiGetBaseLoaderPortion(*(unsigned __int64 *)(v_rsp - 71 - 81), *(unsigned __int64 *)(v_rsp - 71 + 79), a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))));
    if (((*(unsigned int *)(result + 184)) & (256)) != 0) goto loc_00999D6F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = *(unsigned __int64 *)(v_rsp - 71 - 81);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 48);
    v_r15 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 104))) & (0x4000000ULL));
    a1 = (unsigned int)(-(a1));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) & (143));
    v_rdi = (unsigned int)((v_rdi) + (0xC000010EULL));
loc_00999CF6:
    if (!sign_flag) goto loc_00999D07;
loc_00999CFA:
    result = *(unsigned __int64 *)(v_rsp - 71 - 81) + 104;
    if (0 != 0) {
        a1 = 0;
        result = MiUnloadSystemImage(a1, *(unsigned __int64 *)(v_rsp - 71 + 79), a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))));
    }
    result = *(unsigned __int64 *)(v_rsp - 71 - 57);
    if (*(unsigned __int64 *)(v_rsp - 71 - 57) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 57);
        result = MmReleaseLoadLock(a1, *(unsigned __int64 *)(v_rsp - 71 + 79), a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))));
    }
    if (!sign_flag) goto loc_00999D33;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 111)) == 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 + 79);
        a4 = (unsigned int)(v_rdi);
        a3 = 0;
        a2 = 0;
        result = MiLogFailedDriverLoad(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 17);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 49);
        result = PsDetachSiloFromCurrentThread(a1, a2, a3, a4);
    }
loc_00999D53:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)((unsigned int)(v_rdi));
loc_00999D6F:
    result = MiSectionControlArea(*(unsigned __int64 *)(v_r15 + 112), a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 71 - 65) = result;
    result = MiGetSystemAddressForImage(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), a3, a4);
    *(unsigned __int64 *)(v_rsp - 71 - 89) = result;
    if (result != 0) goto loc_00999DA9;
loc_00999DA1:
    goto loc_00999CFA;
loc_00999DA9:
    result = MiCheckPurgeAndUpMapCount((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), a3, a4);
    v_rdi = ((unsigned int)(0xC000009AULL)) << (12);
    result = MiUpdateDriverLoadInProgress(0, *(unsigned __int64 *)(v_rsp - 71 - 89), v_rdi, 1);
    result = MiControlAreaRequiresCharge((unsigned int)((unsigned int)(v_r14)), 2, v_rdi, 1);
    if ((unsigned int)(result) != 0) goto loc_00999DEA;
    goto loc_00999DA1;
loc_00999DEA:
    if (((unsigned int)(result)) != 2) goto loc_00999E18;
    result = MiReferenceActiveSubsection((unsigned int)((unsigned int)(v_r14)) + 128, 136, 17, 1);
    if (sign_flag) goto loc_00999CF6;
loc_00999E18:
    result = MiMapSystemImage(*(unsigned __int64 *)(v_r15 + 112), *(unsigned __int64 *)(v_rsp - 71 - 89), 17, 1);
    if (sign_flag) goto loc_00999CF6;
    v_rsi = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 111) = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 97) = 0;
    result = RtlImageNtHeader(*(unsigned __int64 *)(v_rsp - 71 - 89), *(unsigned __int64 *)(v_rsp - 71 - 89), 17, 1);
    if (result != 0) goto loc_00999E5F;
    goto loc_00999DA1;
loc_00999E5F:
    if ((*(unsigned __int16 *)(result + 4)) != ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_0099A1BB;
    if ((*(unsigned __int16 *)(result + 24)) != 523) goto loc_0099A1BB;
    if (((*(unsigned __int64 *)(v_rip + 6474752)) & (0x8000ULL)) == 0) goto loc_00999ED1;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111))))) & (0x40000000ULL));
    if (condition_is_not_equal) goto loc_00999ED1;
    result = MiValidateStrongCodeDriverImage(result, *(unsigned __int64 *)(v_rsp - 71 - 89), 17, 1);
    if (!sign_flag) goto loc_00999ED1;
    *(unsigned __int64 *)(v_r15 + 88) = v_xmm0;
    *(unsigned int *)(v_r15 + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 88)));
    *(unsigned int *)(v_r15 + 156) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = MiLogStrongCodeDriverLoadFailure(v_rip + 1507360, 0, 17, 1);
    goto loc_00999DA1;
loc_00999ED1:
    v_stack_p20 = v_rsp - 71 - 73;
    result = MiConstructLoaderEntry(0, v_rsp - 71 - 41, v_rsp - 71 - 25, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))));
    if (sign_flag) goto loc_00999CF6;
    result = MiUpdateDriverLoadInProgress(*(unsigned __int64 *)(v_rsp - 71 - 73), 0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)), 2);
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)), 2);
    result = MiGetBaseLoaderPortion(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)), 2);
    *(unsigned __int64 *)(v_rsp - 71 - 81) = result;
    result = KasanDriverLoadImage(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)), 2);
    if (sign_flag) goto loc_00999CF6;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111))))) & (0x40000000ULL));
    if (condition_is_below) goto loc_00999F90;
    result = 0;
    v_stack_p28 = v_rsp - 71 - 97;
    result = ((unsigned int)(v_r13) != 0) ? 1 : 0;
    v_stack_p20 = (unsigned int)(result);
    result = MiResolveImageImports(*(unsigned __int64 *)(v_rsp - 71 - 73), *(unsigned __int64 *)(v_rsp - 71 + 87), v_rsp - 71 - 9, v_rsp - 71 - 41);
    *(unsigned __int8 *)(v_rsp - 71 + 111) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 - 97));
    if (sign_flag) goto loc_00999CF6;
loc_00999F90:
    result = (*(unsigned __int64 *)(v_rsp - 71 - 65)) - (-128);
    *(unsigned __int64 *)(v_rsp - 71 - 73) = result;
    if ((unsigned int)(v_r13) != 0) goto loc_00999FB9;
    result = MiProcessLoadConfigForDriver(*(unsigned __int64 *)(v_rsp - 71 - 73), result, v_rsp - 71 - 9, v_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
loc_00999FB9:
    result = MiFinalizeKernelScpForSystemImage(*(unsigned __int64 *)(v_rsp - 71 - 73), result, v_rsp - 71 - 9, v_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65)) + 56) + 46)) & (64)) != 0) goto loc_0099A046;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + 96)) & (-8);
    v_rdi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 60))) + (*(unsigned __int64 *)(v_rsp - 71 - 89));
    result = MiSetImageProtection(*(unsigned __int64 *)(v_rsp - 71 - 73), v_rdi, 4 + 4, 4);
    result = MiRelocateAmount(*(unsigned __int64 *)(v_rsp - 71 - 65), v_rdi, 4 + 4, 4);
    a1 = (*(unsigned __int64 *)(v_rsp - 71 - 89)) - (result);
    *(unsigned __int64 *)(v_rdi) = a1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + 144)) != 0) {
        a4 = 256;
        a3 = 8;
        a2 = v_rdi;
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 73);
        result = MiSetImageProtection(a1, a2, a3, a4);
    }
    if ((unsigned int)(v_r13) != 0) goto loc_0099A0A1;
    a3 = 0;
    result = VfDriverLoadImage(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, a3, a4);
    result = KseDriverLoadImage(*(unsigned __int64 *)(v_rsp - 71 - 73), v_rsp - 71 - 93, a3, a4);
    if (sign_flag) goto loc_00999CF6;
    result = MiApplyImportOptimizationToRuntimeDriver(*(unsigned __int64 *)(v_rsp - 71 - 73), *(unsigned __int64 *)(v_rsp - 71 - 65), a3, a4);
    if (sign_flag) goto loc_00999CF6;
    goto loc_0099A0A5;
loc_0099A0A1:
loc_0099A0A5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))) & (4)) == 0) goto loc_0099A0C0;
    result = MiCompactServiceTable(*(unsigned __int64 *)(v_rsp - 71 - 73), *(unsigned __int64 *)(v_rsp - 71 - 65), a3, a4);
    if (sign_flag) goto loc_00999CF6;
loc_0099A0C0:
    result = MiHandleDriverNonPagedSections(*(unsigned __int64 *)(v_rsp - 71 - 73), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), a3, a4);
    if (sign_flag) goto loc_00999CF6;
    if (condition_is_below) goto loc_0099A16B;
    result = MiFinalizeDriverCfgState(*(unsigned __int64 *)(v_rsp - 71 - 73), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), *(unsigned __int64 *)(v_rsp - 71 - 73), a4);
    if (sign_flag) goto loc_00999CF6;
    result = MiApplyRequiredDriverHotPatches(*(unsigned __int64 *)(v_rsp - 71 - 73), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), *(unsigned __int64 *)(v_rsp - 71 - 73), a4);
    if (sign_flag) goto loc_00999CF6;
    result = MiGetBaseLoaderPortion(*(unsigned __int64 *)(v_rsp - 71 - 73), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))), *(unsigned __int64 *)(v_rsp - 71 - 73), a4);
    result = MiCallImageNotify(*(unsigned __int64 *)(v_rsp - 71 - 73), *(unsigned __int64 *)(v_rsp - 71 + 79), *(unsigned __int64 *)(v_rsp - 71 - 73), a4);
    result = MiCacheImageSymbols(*(unsigned __int64 *)(v_rsp - 71 - 73), v_rsp - 71 - 25, v_rsp - 71 - 41, a4);
    result = MiSectionControlArea(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 112), v_rsp - 71 - 25, v_rsp - 71 - 41, a4);
    if ((*(unsigned __int64 *)(result + 144)) == 0) goto loc_0099A159;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 104)) & (0x8000000ULL)) == 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 73);
        result = MiProtectSystemImage(a1, a2, v_rsp - 71 - 41, a4);
    }
    result = VfDriverLoadSucceeded(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, v_rsp - 71 - 41, a4);
loc_0099A16B:
    v_rdi = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)))) & (8)) == 0) goto loc_0099A18B;
    result = MmCallDllInitialize(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, v_rsp - 71 - 41, a4);
    if (sign_flag) goto loc_0099A18B;
    result = MiFreeDriverInitialization(*(unsigned __int64 *)(v_rsp - 71 - 73), a2, v_rsp - 71 - 41, a4);
    goto loc_0099A196;
loc_0099A18B:
    if (sign_flag) goto loc_00999CFA;
loc_0099A196:
    v_rdi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = *(unsigned __int64 *)(v_rsp - 71 - 73);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = *(unsigned __int64 *)(v_rsp - 71 - 89);
    goto loc_00999D07;
loc_0099A1BB:
    goto loc_00999DA1;
}
```

## 5. (Beta) C Style

```c
int64_t MmLoadSystemImageEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    Arg1 = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x6F) = 1;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))) & (1)) == 0) goto loc_00999C0C;
    goto loc_00999D53;
loc_00999C0C:
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x470B32));
    local_rbx = 0;
    if ((*(uint32_t *)(result + 0x538)) < ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x470B32)))))) {
        result = HalAdjustResourceList((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x470B32))), result, Arg3, Arg4);
        Arg1 = result;
        result = PsAttachSiloToCurrentThread(Arg1, result, Arg3, Arg4);
        *(uint64_t *)(local_rsp - 0x47 - 0x31) = result;
        local_rbx = 1;
    }
    v_stack_mB0 = local_rsp - 71 - 25;
    v_stack_mB8 = local_rsp - 71 - 9;
    result = MiGenerateSystemImageNames(Arg1, Arg2, Arg3, local_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | (2));
    if (Arg2 == 0) { local_r14 = (uint32_t)(local_rbx); }
    result = MmAcquireLoadLock(Arg1, Arg2, Arg3, local_rsp - 71 - 41);
    v_stack_mB8 = local_rsp - 71 - 81;
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = result;
    result = MiObtainSectionForDriver(local_rsp - 71 - 25, *(uint64_t *)(local_rsp - 0x47 + 0x4F), Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))));
    if (*(uint64_t *)(local_rsp - 0x47 - 0x51) == 0) goto loc_00999CF6;
    result = MiGetBaseLoaderPortion(*(uint64_t *)(local_rsp - 0x47 - 0x51), *(uint64_t *)(local_rsp - 0x47 + 0x4F), Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))));
    if (((*(uint32_t *)(result + 0xB8)) & (256)) != 0) goto loc_00999D6F;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = *(uint64_t *)(local_rsp - 0x47 - 0x51);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x30);
    local_r15 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x68))) & (0x4000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) & (143));
    local_rdi = (uint32_t)((local_rdi) + (0xC000010EULL));
loc_00999CF6:
    if (!sign_flag) goto loc_00999D07;
loc_00999CFA:
    result = *(uint64_t *)(local_rsp - 0x47 - 0x51) + 104;
    if (0 != 0) {
        Arg1 = 0;
        result = MiUnloadSystemImage(Arg1, *(uint64_t *)(local_rsp - 0x47 + 0x4F), Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))));
    }
    result = *(uint64_t *)(local_rsp - 0x47 - 0x39);
    if (*(uint64_t *)(local_rsp - 0x47 - 0x39) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x39);
        result = MmReleaseLoadLock(Arg1, *(uint64_t *)(local_rsp - 0x47 + 0x4F), Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))));
    }
    if (!sign_flag) goto loc_00999D33;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x6F)) == 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 + 0x4F);
        Arg4 = (uint32_t)(local_rdi);
        Arg3 = 0;
        Arg2 = 0;
        result = MiLogFailedDriverLoad(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r14)))) & (2)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x11);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r14)))) & (1)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x31);
        result = PsDetachSiloFromCurrentThread(Arg1, Arg2, Arg3, Arg4);
    }
loc_00999D53:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)((uint32_t)(local_rdi));
loc_00999D6F:
    result = MiSectionControlArea(*(uint64_t *)(local_r15 + 0x70), Arg2, Arg3, Arg4);
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = result;
    result = MiGetSystemAddressForImage(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), Arg3, Arg4);
    *(uint64_t *)(local_rsp - 0x47 - 0x59) = result;
    if (result != 0) goto loc_00999DA9;
loc_00999DA1:
    goto loc_00999CFA;
loc_00999DA9:
    result = MiCheckPurgeAndUpMapCount((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), Arg3, Arg4);
    local_rdi = ((uint32_t)(0xC000009AULL)) << (12);
    result = MiUpdateDriverLoadInProgress(0, *(uint64_t *)(local_rsp - 0x47 - 0x59), local_rdi, 1);
    result = MiControlAreaRequiresCharge((uint32_t)((uint32_t)(local_r14)), 2, local_rdi, 1);
    if ((uint32_t)(result) != 0) goto loc_00999DEA;
    goto loc_00999DA1;
loc_00999DEA:
    if (((uint32_t)(result)) != 2) goto loc_00999E18;
    result = MiReferenceActiveSubsection((uint32_t)((uint32_t)(local_r14)) + 128, 136, 17, 1);
    if (sign_flag) goto loc_00999CF6;
loc_00999E18:
    result = MiMapSystemImage(*(uint64_t *)(local_r15 + 0x70), *(uint64_t *)(local_rsp - 0x47 - 0x59), 17, 1);
    if (sign_flag) goto loc_00999CF6;
    local_rsi = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x6F) = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x61) = 0;
    result = RtlImageNtHeader(*(uint64_t *)(local_rsp - 0x47 - 0x59), *(uint64_t *)(local_rsp - 0x47 - 0x59), 17, 1);
    if (result != 0) goto loc_00999E5F;
    goto loc_00999DA1;
loc_00999E5F:
    if ((*(uint16_t *)(result + 0x4)) != ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_0099A1BB;
    if ((*(uint16_t *)(result + 0x18)) != 523) goto loc_0099A1BB;
    if (((*(uint64_t *)(v_rip + 0x62CC00)) & (0x8000ULL)) == 0) goto loc_00999ED1;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F))))) & (0x40000000ULL));
    if (condition_is_not_equal) goto loc_00999ED1;
    result = MiValidateStrongCodeDriverImage(result, *(uint64_t *)(local_rsp - 0x47 - 0x59), 17, 1);
    if (!sign_flag) goto loc_00999ED1;
    *(uint64_t *)(local_r15 + 0x58) = v_xmm0;
    *(uint32_t *)(local_r15 + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x58)));
    *(uint32_t *)(local_r15 + 0x9C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = MiLogStrongCodeDriverLoadFailure(v_rip + 1507360, 0, 17, 1);
    goto loc_00999DA1;
loc_00999ED1:
    v_stack_p20 = local_rsp - 71 - 73;
    result = MiConstructLoaderEntry(0, local_rsp - 71 - 41, local_rsp - 71 - 25, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))));
    if (sign_flag) goto loc_00999CF6;
    result = MiUpdateDriverLoadInProgress(*(uint64_t *)(local_rsp - 0x47 - 0x49), 0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)), 2);
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)), 2);
    result = MiGetBaseLoaderPortion(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)), 2);
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = result;
    result = KasanDriverLoadImage(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)), 2);
    if (sign_flag) goto loc_00999CF6;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F))))) & (0x40000000ULL));
    if (condition_is_below) goto loc_00999F90;
    result = 0;
    v_stack_p28 = local_rsp - 71 - 97;
    result = ((uint32_t)(local_r13) != 0) ? 1 : 0;
    v_stack_p20 = (uint32_t)(result);
    result = MiResolveImageImports(*(uint64_t *)(local_rsp - 0x47 - 0x49), *(uint64_t *)(local_rsp - 0x47 + 0x57), local_rsp - 71 - 9, local_rsp - 71 - 41);
    *(uint8_t *)(local_rsp - 0x47 + 0x6F) = (uint8_t)(*(uint8_t *)(local_rsp - 0x47 - 0x61));
    if (sign_flag) goto loc_00999CF6;
loc_00999F90:
    result = (*(uint64_t *)(local_rsp - 0x47 - 0x41)) - (-128);
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = result;
    if ((uint32_t)(local_r13) != 0) goto loc_00999FB9;
    result = MiProcessLoadConfigForDriver(*(uint64_t *)(local_rsp - 0x47 - 0x49), result, local_rsp - 71 - 9, local_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
loc_00999FB9:
    result = MiFinalizeKernelScpForSystemImage(*(uint64_t *)(local_rsp - 0x47 - 0x49), result, local_rsp - 71 - 9, local_rsp - 71 - 41);
    if (sign_flag) goto loc_00999CF6;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41)) + 0x38) + 0x2E)) & (64)) != 0) goto loc_0099A046;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + 0x60)) & (-8);
    local_rdi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x3C))) + (*(uint64_t *)(local_rsp - 0x47 - 0x59));
    result = MiSetImageProtection(*(uint64_t *)(local_rsp - 0x47 - 0x49), local_rdi, 4 + 4, 4);
    result = MiRelocateAmount(*(uint64_t *)(local_rsp - 0x47 - 0x41), local_rdi, 4 + 4, 4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x47 - 0x59)) - (result);
    *(uint64_t *)(local_rdi) = Arg1;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + 0x90)) != 0) {
        Arg4 = 256;
        Arg3 = 8;
        Arg2 = local_rdi;
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x49);
        result = MiSetImageProtection(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)(local_r13) != 0) goto loc_0099A0A1;
    Arg3 = 0;
    result = VfDriverLoadImage(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, Arg3, Arg4);
    result = KseDriverLoadImage(*(uint64_t *)(local_rsp - 0x47 - 0x49), local_rsp - 71 - 93, Arg3, Arg4);
    if (sign_flag) goto loc_00999CF6;
    result = MiApplyImportOptimizationToRuntimeDriver(*(uint64_t *)(local_rsp - 0x47 - 0x49), *(uint64_t *)(local_rsp - 0x47 - 0x41), Arg3, Arg4);
    if (sign_flag) goto loc_00999CF6;
    goto loc_0099A0A5;
loc_0099A0A1:
loc_0099A0A5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))) & (4)) == 0) goto loc_0099A0C0;
    result = MiCompactServiceTable(*(uint64_t *)(local_rsp - 0x47 - 0x49), *(uint64_t *)(local_rsp - 0x47 - 0x41), Arg3, Arg4);
    if (sign_flag) goto loc_00999CF6;
loc_0099A0C0:
    result = MiHandleDriverNonPagedSections(*(uint64_t *)(local_rsp - 0x47 - 0x49), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), Arg3, Arg4);
    if (sign_flag) goto loc_00999CF6;
    if (condition_is_below) goto loc_0099A16B;
    result = MiFinalizeDriverCfgState(*(uint64_t *)(local_rsp - 0x47 - 0x49), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), *(uint64_t *)(local_rsp - 0x47 - 0x49), Arg4);
    if (sign_flag) goto loc_00999CF6;
    result = MiApplyRequiredDriverHotPatches(*(uint64_t *)(local_rsp - 0x47 - 0x49), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), *(uint64_t *)(local_rsp - 0x47 - 0x49), Arg4);
    if (sign_flag) goto loc_00999CF6;
    result = MiGetBaseLoaderPortion(*(uint64_t *)(local_rsp - 0x47 - 0x49), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))), *(uint64_t *)(local_rsp - 0x47 - 0x49), Arg4);
    result = MiCallImageNotify(*(uint64_t *)(local_rsp - 0x47 - 0x49), *(uint64_t *)(local_rsp - 0x47 + 0x4F), *(uint64_t *)(local_rsp - 0x47 - 0x49), Arg4);
    result = MiCacheImageSymbols(*(uint64_t *)(local_rsp - 0x47 - 0x49), local_rsp - 71 - 25, local_rsp - 71 - 41, Arg4);
    result = MiSectionControlArea(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x70), local_rsp - 71 - 25, local_rsp - 71 - 41, Arg4);
    if ((*(uint64_t *)(result + 0x90)) == 0) goto loc_0099A159;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x68)) & (0x8000000ULL)) == 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x49);
        result = MiProtectSystemImage(Arg1, Arg2, local_rsp - 71 - 41, Arg4);
    }
    result = VfDriverLoadSucceeded(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, local_rsp - 71 - 41, Arg4);
loc_0099A16B:
    local_rdi = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)))) & (8)) == 0) goto loc_0099A18B;
    result = MmCallDllInitialize(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, local_rsp - 71 - 41, Arg4);
    if (sign_flag) goto loc_0099A18B;
    result = MiFreeDriverInitialization(*(uint64_t *)(local_rsp - 0x47 - 0x49), Arg2, local_rsp - 71 - 41, Arg4);
    goto loc_0099A196;
loc_0099A18B:
    if (sign_flag) goto loc_00999CFA;
loc_0099A196:
    local_rdi = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = *(uint64_t *)(local_rsp - 0x47 - 0x49);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = *(uint64_t *)(local_rsp - 0x47 - 0x59);
    goto loc_00999D07;
loc_0099A1BB:
    goto loc_00999DA1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00999B8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
