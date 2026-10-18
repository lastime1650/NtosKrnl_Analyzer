# AuthzBasepEvaluateAceCondition

- RVA: `0x002FEBD0`–`0x002FFD81` (길이 `4,529` bytes)
- VA: `0x00000001402FEBD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072E68`
- 디코드: `1,044`개 명령, `4,529/4,529` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002FEC48` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002FEC63` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002FEE35` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FEE47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FEE6B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FEF22` → [AuthzBasepMemAlloc](AuthzBasepMemAlloc_function_002FFD90.md) (function, `0x002FFD90`)
- `0x002FEF3D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FEFAA` → [AuthzBasepQuerySecurityAttributeAndValues](../30/AuthzBasepQuerySecurityAttributeAndValues_function_00300090.md) (function, `0x00300090`)
- `0x002FEFF1` → [AuthzBasepQuerySecurityAttributeAndValues](../30/AuthzBasepQuerySecurityAttributeAndValues_function_00300090.md) (function, `0x00300090`)
- `0x002FF099` → [AuthzBasepSupportSetOperation](../30/AuthzBasepSupportSetOperation_function_0030054C.md) (function, `0x0030054C`)
- `0x002FF0AF` → [AuthzBasepSupportSetOperation](../30/AuthzBasepSupportSetOperation_function_0030054C.md) (function, `0x0030054C`)
- `0x002FF0DC` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF0F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF119` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF18A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF1D1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF232` → [AuthzBasepSupportSetOperation](../30/AuthzBasepSupportSetOperation_function_0030054C.md) (function, `0x0030054C`)
- `0x002FF28D` → [AuthzBasepSupportSetOperation](../30/AuthzBasepSupportSetOperation_function_0030054C.md) (function, `0x0030054C`)
- `0x002FF2D1` → [AuthzBasepEvaluateExpression](../30/AuthzBasepEvaluateExpression_function_00300578.md) (function, `0x00300578`)
- `0x002FF353` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF40B` → [SepPotentialGlobalTableAttribute](../3A/SepPotentialGlobalTableAttribute_function_003A8828.md) (function, `0x003A8828`)
- `0x002FF436` → [SepValidateAndCopyGlobalEntry](../4F/SepValidateAndCopyGlobalEntry_function_004F825C.md) (function, `0x004F825C`)
- `0x002FF4B5` → [AuthzBasepIsValidExpression](../30/AuthzBasepIsValidExpression_function_00300390.md) (function, `0x00300390`)
- `0x002FF505` → [AuthzBasepResetOperands](../30/AuthzBasepResetOperands_function_00301190.md) (function, `0x00301190`)
- `0x002FF575` → [AuthzBasepFreeSecurityAttributesList](../30/AuthzBasepFreeSecurityAttributesList_function_00301230.md) (function, `0x00301230`)
- `0x002FF582` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF5D2` → [AuthzBasepIsValidExpression](../30/AuthzBasepIsValidExpression_function_00300390.md) (function, `0x00300390`)
- `0x002FF666` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF69C` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF6CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF74C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002FF7B1` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF7BD` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF80B` → [AuthzBasepIsValidExpression](../30/AuthzBasepIsValidExpression_function_00300390.md) (function, `0x00300390`)
- `0x002FF848` → [AuthzBasepIsValidExpression](../30/AuthzBasepIsValidExpression_function_00300390.md) (function, `0x00300390`)
- `0x002FF89F` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FF8CF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FF94F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002FF9AB` → [_report_rangecheckfailure](../4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x002FFA65` → [AuthzBasepMemberOf](../4E/AuthzBasepMemberOf_function_004E3584.md) (function, `0x004E3584`)
- `0x002FFACA` → [AuthzBasepDeviceMemberOf](../4E/AuthzBasepDeviceMemberOf_function_004E3694.md) (function, `0x004E3694`)
- `0x002FFB10` → [AuthzBasepIsValidExpression](../30/AuthzBasepIsValidExpression_function_00300390.md) (function, `0x00300390`)
- `0x002FFB3C` → [AuthzBasepOperandValueTypesCompatible](../30/AuthzBasepOperandValueTypesCompatible_function_00300708.md) (function, `0x00300708`)
- `0x002FFB7C` → [AuthzBasepResetOperands](../30/AuthzBasepResetOperands_function_00301190.md) (function, `0x00301190`)
- `0x002FFBA9` → [AuthzBasepEvaluateAttribute](../30/AuthzBasepEvaluateAttribute_function_0030137C.md) (function, `0x0030137C`)
- `0x002FFCFF` → [AuthzBasepComputeBitwise](../69/AuthzBasepComputeBitwise_function_0069D83C.md) (function, `0x0069D83C`)
- `0x002FFD54` → [AuthzBasepQuerySecurityAttributeAndValues](../30/AuthzBasepQuerySecurityAttributeAndValues_function_00300090.md) (function, `0x00300090`)

### Direct callers
- [SepMaximumAccessCheck](../30/SepMaximumAccessCheck_function_00300BF0.md) at `0x00300F62`
- [sub_00301B88](../30/Unknown_function_00301B88.md) at `0x00301C8D`
- [sub_00301ECC](../30/Unknown_function_00301ECC.md) at `0x00301F78`
- [SeAccessCheckWithHint](../3A/SeAccessCheckWithHint_function_003A6C30.md) at `0x003A72F5`
- [SeAccessCheckWithHint](../3A/SeAccessCheckWithHint_function_003A6C30.md) at `0x003A739C`
- [SepNormalAccessCheckEx](../3C/SepNormalAccessCheckEx_function_003CFD8C.md) at `0x003D00FB`
- [SepNormalAccessCheckEx](../3C/SepNormalAccessCheckEx_function_003CFD8C.md) at `0x003D02C5`
- [SepNormalAccessCheck](../3D/SepNormalAccessCheck_function_003D0688.md) at `0x003D0A95`
- [SeAccessCheckByType](../44/SeAccessCheckByType_function_00440BC8.md) at `0x00441E9B`
- [SeAccessCheckByType](../44/SeAccessCheckByType_function_00440BC8.md) at `0x00441F61`
- [SepCommonAccessCheckEx](../47/SepCommonAccessCheckEx_function_0047602C.md) at `0x00476AFD`
- [SepCommonAccessCheckEx](../47/SepCommonAccessCheckEx_function_0047602C.md) at `0x00476BA1`
- [SepMaximumAccessCheckEx](../60/SepMaximumAccessCheckEx_function_00606D78.md) at `0x006072B4`
- [SepMaximumAccessCheckEx](../60/SepMaximumAccessCheckEx_function_00606D78.md) at `0x0060743E`
- [sub_006E6B3A](../6E/Unknown_function_006E6B3A.md) at `0x006E6BBA`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1C11A`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1C1EE`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1C9CD`
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1CAA1`
- [SepExamineSaclEx](../../page/A2/SepExamineSaclEx_function_00A2F39C.md) at `0x00A2F6A1`
- [sub_00B2940C](../../page/B2/Unknown_function_00B2940C.md) at `0x00B294A5`

### Static image references
- `0x002FEBEF` → RVA `0x00E0A740` (`.data`; read)
- `0x002FED26` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002FEFBD` → RVA `0x00E08960` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x002FEE35` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FEE47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF0F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF119` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF18A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF1D1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF353` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF582` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF6CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FF8CF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002FF9F4` → [sub_006DFF48](../6D/Unknown_function_006DFF48.md) (`tail-transfer`)
  - `0x002FFA2D` → [sub_006DFF48](../6D/Unknown_function_006DFF48.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FEBD0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002FEBD5  55                              push rbp
002FEBD6  56                              push rsi
002FEBD7  57                              push rdi
002FEBD8  41 54                           push r12
002FEBDA  41 55                           push r13
002FEBDC  41 56                           push r14
002FEBDE  41 57                           push r15
002FEBE0  48 8D AC 24 80 FB FF FF         lea rbp, [rsp - 0x480]
002FEBE8  48 81 EC 80 05 00 00            sub rsp, 0x580
002FEBEF  48 8B 05 4A BB B0 00            mov rax, qword ptr [rip + 0xb0bb4a]
002FEBF6  48 33 C4                        xor rax, rsp
002FEBF9  48 89 85 70 04 00 00            mov qword ptr [rbp + 0x470], rax
002FEC00  48 8B 85 F8 04 00 00            mov rax, qword ptr [rbp + 0x4f8]
002FEC07  48 8B F1                        mov rsi, rcx
002FEC0A  48 8B BD 18 05 00 00            mov rdi, qword ptr [rbp + 0x518]
002FEC11  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002FEC15  33 C0                           xor eax, eax
002FEC17  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
002FEC1B  8B D8                           mov ebx, eax
002FEC1D  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
002FEC21  41 B8 80 00 00 00               mov r8d, 0x80
002FEC27  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
002FEC2B  33 D2                           xor edx, edx
002FEC2D  48 8D 4D F0                     lea rcx, [rbp - 0x10]
002FEC31  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
002FEC35  44 8B F8                        mov r15d, eax
002FEC38  89 45 E0                        mov dword ptr [rbp - 0x20], eax
002FEC3B  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
002FEC3F  4C 89 4D C0                     mov qword ptr [rbp - 0x40], r9
002FEC43  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002FEC48  E8 F3 7F 3C 00                  call 0x1406c6c40
002FEC4D  33 C0                           xor eax, eax
002FEC4F  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
002FEC54  33 D2                           xor edx, edx
002FEC56  66 89 44 24 55                  mov word ptr [rsp + 0x55], ax
002FEC5B  88 44 24 57                     mov byte ptr [rsp + 0x57], al
002FEC5F  44 8D 40 48                     lea r8d, [rax + 0x48]
002FEC63  E8 D8 7F 3C 00                  call 0x1406c6c40
002FEC68  32 C0                           xor al, al
002FEC6A  C7 44 24 38 FF FF FF FF         mov dword ptr [rsp + 0x38], 0xffffffff
002FEC72  45 33 DB                        xor r11d, r11d
002FEC75  66 89 5C 24 30                  mov word ptr [rsp + 0x30], bx
002FEC7A  88 44 24 49                     mov byte ptr [rsp + 0x49], al
002FEC7E  88 44 24 48                     mov byte ptr [rsp + 0x48], al
002FEC82  88 44 24 34                     mov byte ptr [rsp + 0x34], al
002FEC86  88 44 24 4B                     mov byte ptr [rsp + 0x4b], al
002FEC8A  88 44 24 4A                     mov byte ptr [rsp + 0x4a], al
002FEC8E  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
002FEC92  C7 07 FF FF FF FF               mov dword ptr [rdi], 0xffffffff
002FEC98  4C 89 5D F8                     mov qword ptr [rbp - 8], r11
002FEC9C  4C 89 5D 40                     mov qword ptr [rbp + 0x40], r11
002FECA0  48 85 F6                        test rsi, rsi
002FECA3  0F 84 EE 07 00 00               je 0x1402ff497
002FECA9  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
002FECAD  4D 85 C9                        test r9, r9
002FECB0  0F 84 E1 07 00 00               je 0x1402ff497
002FECB6  44 0F 20 C0                     mov rax, cr8
002FECBA  8B 95 00 05 00 00               mov edx, dword ptr [rbp + 0x500]
002FECC0  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
002FECC4  83 FA 04                        cmp edx, 4
002FECC7  0F 82 BD 06 00 00               jb 0x1402ff38a
002FECCD  41 81 39 61 72 74 78            cmp dword ptr [r9], 0x78747261
002FECD4  0F 85 B9 0E 00 00               jne 0x1402ffb93
002FECDA  66 44 89 5C 24 50               mov word ptr [rsp + 0x50], r11w
002FECE0  45 8B EB                        mov r13d, r11d
002FECE3  88 5C 24 54                     mov byte ptr [rsp + 0x54], bl
002FECE7  41 8B F3                        mov esi, r11d
002FECEA  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
002FECEF  45 8B E3                        mov r12d, r11d
002FECF2  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
002FECF7  41 BE 04 00 00 00               mov r14d, 4
002FECFD  44 89 5C 24 68                  mov dword ptr [rsp + 0x68], r11d
002FED02  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
002FED07  66 44 89 5C 24 78               mov word ptr [rsp + 0x78], r11w
002FED0D  88 5C 24 7C                     mov byte ptr [rsp + 0x7c], bl
002FED11  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
002FED15  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
002FED19  44 89 5D 90                     mov dword ptr [rbp - 0x70], r11d
002FED1D  4C 89 5D 98                     mov qword ptr [rbp - 0x68], r11
002FED21  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
002FED26  4C 8D 15 D3 12 D0 FF            lea r10, [rip - 0x2fed2d]
002FED2D  44 3B F2                        cmp r14d, edx
002FED30  0F 83 DE 00 00 00               jae 0x1402fee14
002FED36  45 8B FE                        mov r15d, r14d
002FED39  4D 03 F9                        add r15, r9
002FED3C  41 0F B6 3F                     movzx edi, byte ptr [r15]
002FED40  44 8B C7                        mov r8d, edi
002FED43  81 FF FC 00 00 00               cmp edi, 0xfc
002FED49  0F 84 3D 01 00 00               je 0x1402fee8c
002FED4F  41 81 F8 A2 00 00 00            cmp r8d, 0xa2
002FED56  0F 84 0C 03 00 00               je 0x1402ff068
002FED5C  41 81 F8 8E 00 00 00            cmp r8d, 0x8e
002FED63  0F 84 9C 04 00 00               je 0x1402ff205
002FED69  41 83 F8 51                     cmp r8d, 0x51
002FED6D  0F 85 2A 06 00 00               jne 0x1402ff39d
002FED73  41 83 FC 02                     cmp r12d, 2
002FED77  0F 84 15 0B 00 00               je 0x1402ff892
002FED7D  44 8B 8D 00 05 00 00            mov r9d, dword ptr [rbp + 0x500]
002FED84  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FED89  45 0F B6 17                     movzx r10d, byte ptr [r15]
002FED8D  45 2B CE                        sub r9d, r14d
002FED90  41 8B C4                        mov eax, r12d
002FED93  41 8B DB                        mov ebx, r11d
002FED96  41 B8 01 00 00 00               mov r8d, 1
002FED9C  48 8D 0C 80                     lea rcx, [rax + rax*4]
002FEDA0  66 44 89 1C CA                  mov word ptr [rdx + rcx*8], r11w
002FEDA5  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
002FEDA9  C6 42 04 00                     mov byte ptr [rdx + 4], 0
002FEDAD  44 89 5A 08                     mov dword ptr [rdx + 8], r11d
002FEDB1  C7 42 0C 01 00 00 00            mov dword ptr [rdx + 0xc], 1
002FEDB8  4C 89 5A 10                     mov qword ptr [rdx + 0x10], r11
002FEDBC  44 89 5A 18                     mov dword ptr [rdx + 0x18], r11d
002FEDC0  4C 89 5A 20                     mov qword ptr [rdx + 0x20], r11
002FEDC4  41 83 FA 51                     cmp r10d, 0x51
002FEDC8  0F 85 9B 06 00 00               jne 0x1402ff469
002FEDCE  41 8D 41 FF                     lea eax, [r9 - 1]
002FEDD2  83 F8 04                        cmp eax, 4
002FEDD5  0F 82 9F 04 00 00               jb 0x1402ff27a
002FEDDB  41 80 FA 10                     cmp r10b, 0x10
002FEDDF  0F 85 92 08 00 00               jne 0x1402ff677
002FEDE5  66 C7 02 03 00                  mov word ptr [rdx], 3
002FEDEA  41 8B 4F 01                     mov ecx, dword ptr [r15 + 1]
002FEDEE  41 8D 41 FB                     lea eax, [r9 - 5]
002FEDF2  89 4A 18                        mov dword ptr [rdx + 0x18], ecx
002FEDF5  3B C1                           cmp eax, ecx
002FEDF7  0F 82 7D 04 00 00               jb 0x1402ff27a
002FEDFD  49 8D 47 05                     lea rax, [r15 + 5]
002FEE01  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
002FEE05  44 8D 41 05                     lea r8d, [rcx + 5]
002FEE09  41 FF C4                        inc r12d
002FEE0C  45 03 F0                        add r14d, r8d
002FEE0F  E9 3B 02 00 00                  jmp 0x1402ff04f
002FEE14  41 83 FF 01                     cmp r15d, 1
002FEE18  0F 85 32 08 00 00               jne 0x1402ff650
002FEE1E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FEE23  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
002FEE26  89 06                           mov dword ptr [rsi], eax
002FEE28  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FEE2D  74 0B                           je 0x1402fee3a
002FEE2F  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
002FEE33  33 D2                           xor edx, edx
002FEE35  E8 36 3A 88 00                  call 0x140b82870
002FEE3A  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
002FEE3F  74 0B                           je 0x1402fee4c
002FEE41  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
002FEE45  33 D2                           xor edx, edx
002FEE47  E8 24 3A 88 00                  call 0x140b82870
002FEE4C  80 7C 24 4A 00                  cmp byte ptr [rsp + 0x4a], 0
002FEE51  0F 85 0E 07 00 00               jne 0x1402ff565
002FEE57  85 DB                           test ebx, ebx
002FEE59  0F 88 FB 06 00 00               js 0x1402ff55a
002FEE5F  8B C3                           mov eax, ebx
002FEE61  48 8B 8D 70 04 00 00            mov rcx, qword ptr [rbp + 0x470]
002FEE68  48 33 CC                        xor rcx, rsp
002FEE6B  E8 D0 D7 3A 00                  call 0x1406ac640
002FEE70  48 8B 9C 24 D0 05 00 00         mov rbx, qword ptr [rsp + 0x5d0]
002FEE78  48 81 C4 80 05 00 00            add rsp, 0x580
002FEE7F  41 5F                           pop r15
002FEE81  41 5E                           pop r14
002FEE83  41 5D                           pop r13
002FEE85  41 5C                           pop r12
002FEE87  5F                              pop rdi
002FEE88  5E                              pop rsi
002FEE89  5D                              pop rbp
002FEE8A  C3                              ret
002FEE8B  CC                              int3
002FEE8C  41 FF C6                        inc r14d
002FEE8F  41 83 FC 02                     cmp r12d, 2
002FEE93  0F 84 F6 07 00 00               je 0x1402ff68f
002FEE99  8B C2                           mov eax, edx
002FEE9B  41 2B C6                        sub eax, r14d
002FEE9E  83 F8 04                        cmp eax, 4
002FEEA1  0F 82 D3 03 00 00               jb 0x1402ff27a
002FEEA7  47 8B 3C 0E                     mov r15d, dword ptr [r14 + r9]
002FEEAB  8B C2                           mov eax, edx
002FEEAD  41 83 C6 04                     add r14d, 4
002FEEB1  41 2B C6                        sub eax, r14d
002FEEB4  41 3B C7                        cmp eax, r15d
002FEEB7  0F 82 BD 03 00 00               jb 0x1402ff27a
002FEEBD  41 81 FF FE FF 00 00            cmp r15d, 0xfffe
002FEEC4  0F 87 36 0D 00 00               ja 0x1402ffc00
002FEECA  45 8B EC                        mov r13d, r12d
002FEECD  48 8D 75 F0                     lea rsi, [rbp - 0x10]
002FEED1  41 8B DE                        mov ebx, r14d
002FEED4  49 03 D9                        add rbx, r9
002FEED7  4A 8D 04 ED 00 00 00 00         lea rax, [r13*8]
002FEEDF  42 C6 44 2C 30 00               mov byte ptr [rsp + r13 + 0x30], 0
002FEEE5  49 03 C5                        add rax, r13
002FEEE8  4C 8D 24 C5 00 00 00 00         lea r12, [rax*8]
002FEEF0  49 03 F4                        add rsi, r12
002FEEF3  66 44 89 7E 02                  mov word ptr [rsi + 2], r15w
002FEEF8  66 44 89 3E                     mov word ptr [rsi], r15w
002FEEFC  48 89 5E 08                     mov qword ptr [rsi + 8], rbx
002FEF00  66 45 85 FF                     test r15w, r15w
002FEF04  0F 84 70 03 00 00               je 0x1402ff27a
002FEF0A  48 85 DB                        test rbx, rbx
002FEF0D  0F 84 67 03 00 00               je 0x1402ff27a
002FEF13  F6 C3 01                        test bl, 1
002FEF16  74 30                           je 0x1402fef48
002FEF18  41 0F B7 CF                     movzx ecx, r15w
002FEF1C  41 B8 53 65 47 61               mov r8d, 0x61476553
002FEF22  E8 69 0E 00 00                  call 0x1402ffd90
002FEF27  48 89 46 08                     mov qword ptr [rsi + 8], rax
002FEF2B  48 85 C0                        test rax, rax
002FEF2E  0F 84 26 05 00 00               je 0x1402ff45a
002FEF34  45 8B C7                        mov r8d, r15d
002FEF37  48 8B D3                        mov rdx, rbx
002FEF3A  48 8B C8                        mov rcx, rax
002FEF3D  E8 FE 78 3C 00                  call 0x1406c6840
002FEF42  42 C6 44 2C 30 01               mov byte ptr [rsp + r13 + 0x30], 1
002FEF48  48 8D 75 E0                     lea rsi, [rbp - 0x20]
002FEF4C  49 03 F4                        add rsi, r12
002FEF4F  40 80 FF F9                     cmp dil, 0xf9
002FEF53  0F 84 13 04 00 00               je 0x1402ff36c
002FEF59  40 80 FF FB                     cmp dil, 0xfb
002FEF5D  0F 84 27 0A 00 00               je 0x1402ff98a
002FEF63  40 80 FF FA                     cmp dil, 0xfa
002FEF67  0F 84 04 09 00 00               je 0x1402ff871
002FEF6D  40 80 FF FC                     cmp dil, 0xfc
002FEF71  0F 84 3A 0A 00 00               je 0x1402ff9b1
002FEF77  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
002FEF7B  C7 06 02 00 00 00               mov dword ptr [rsi], 2
002FEF81  49 8B CC                        mov rcx, r12
002FEF84  48 8D 55 E8                     lea rdx, [rbp - 0x18]
002FEF88  48 89 04 0A                     mov qword ptr [rdx + rcx], rax
002FEF8C  48 8D 3C 0A                     lea rdi, [rdx + rcx]
002FEF90  33 C9                           xor ecx, ecx
002FEF92  4A 8D 04 ED 00 00 00 00         lea rax, [r13*8]
002FEF9A  49 03 C5                        add rax, r13
002FEF9D  48 89 4C C5 18                  mov qword ptr [rbp + rax*8 + 0x18], rcx
002FEFA2  48 89 4C C5 20                  mov qword ptr [rbp + rax*8 + 0x20], rcx
002FEFA7  48 8B CE                        mov rcx, rsi
002FEFAA  E8 E1 10 00 00                  call 0x140300090
002FEFAF  8B D8                           mov ebx, eax
002FEFB1  3D 25 02 00 C0                  cmp eax, 0xc0000225
002FEFB6  75 40                           jne 0x1402feff8
002FEFB8  83 3E 02                        cmp dword ptr [rsi], 2
002FEFBB  75 13                           jne 0x1402fefd0
002FEFBD  48 8B 05 9C 99 B0 00            mov rax, qword ptr [rip + 0xb0999c]
002FEFC4  8B 50 10                        mov edx, dword ptr [rax + 0x10]
002FEFC7  F6 C2 01                        test dl, 1
002FEFCA  0F 85 20 04 00 00               jne 0x1402ff3f0
002FEFD0  80 7D D0 02                     cmp byte ptr [rbp - 0x30], 2
002FEFD4  0F 83 3E 03 00 00               jae 0x1402ff318
002FEFDA  83 3E 02                        cmp dword ptr [rsi], 2
002FEFDD  0F 85 35 03 00 00               jne 0x1402ff318
002FEFE3  33 D2                           xor edx, edx
002FEFE5  C7 06 07 00 00 00               mov dword ptr [rsi], 7
002FEFEB  48 8B CE                        mov rcx, rsi
002FEFEE  48 89 17                        mov qword ptr [rdi], rdx
002FEFF1  E8 9A 10 00 00                  call 0x140300090
002FEFF6  8B D8                           mov ebx, eax
002FEFF8  85 DB                           test ebx, ebx
002FEFFA  0F 88 0C 03 00 00               js 0x1402ff30c
002FF000  4A 8D 04 AD 00 00 00 00         lea rax, [r13*4]
002FF008  49 03 C5                        add rax, r13
002FF00B  48 8D 3C C5 00 00 00 00         lea rdi, [rax*8]
002FF013  42 0F B7 44 25 00               movzx eax, word ptr [rbp + r12]
002FF019  66 89 44 3C 50                  mov word ptr [rsp + rdi + 0x50], ax
002FF01E  42 8B 44 25 08                  mov eax, dword ptr [rbp + r12 + 8]
002FF023  89 44 3C 54                     mov dword ptr [rsp + rdi + 0x54], eax
002FF027  48 89 74 3C 60                  mov qword ptr [rsp + rdi + 0x60], rsi
002FF02C  45 33 DB                        xor r11d, r11d
002FF02F  44 8B 64 24 4C                  mov r12d, dword ptr [rsp + 0x4c]
002FF034  8B 06                           mov eax, dword ptr [rsi]
002FF036  41 FF C4                        inc r12d
002FF039  45 03 F7                        add r14d, r15d
002FF03C  44 89 5C 3C 68                  mov dword ptr [rsp + rdi + 0x68], r11d
002FF041  4C 89 5C 3C 70                  mov qword ptr [rsp + rdi + 0x70], r11
002FF046  44 89 5C 3C 58                  mov dword ptr [rsp + rdi + 0x58], r11d
002FF04B  89 44 3C 5C                     mov dword ptr [rsp + rdi + 0x5c], eax
002FF04F  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF054  44 8B 6C 24 5C                  mov r13d, dword ptr [rsp + 0x5c]
002FF059  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FF05E  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
002FF063  E9 8E 01 00 00                  jmp 0x1402ff1f6
002FF068  41 FF C6                        inc r14d
002FF06B  C6 44 24 34 00                  mov byte ptr [rsp + 0x34], 0
002FF070  45 8B C3                        mov r8d, r11d
002FF073  45 3B C4                        cmp r8d, r12d
002FF076  73 33                           jae 0x1402ff0ab
002FF078  41 8B C0                        mov eax, r8d
002FF07B  48 8D 0C 80                     lea rcx, [rax + rax*4]
002FF07F  4C 8D 14 CD 00 00 00 00         lea r10, [rcx*8]
002FF087  46 8B 4C 14 5C                  mov r9d, dword ptr [rsp + r10 + 0x5c]
002FF08C  45 85 C9                        test r9d, r9d
002FF08F  0F 84 E5 01 00 00               je 0x1402ff27a
002FF095  40 0F B6 CF                     movzx ecx, dil
002FF099  E8 AE 14 00 00                  call 0x14030054c
002FF09E  84 C0                           test al, al
002FF0A0  0F 84 7E 04 00 00               je 0x1402ff524
002FF0A6  41 FF C0                        inc r8d
002FF0A9  EB C8                           jmp 0x1402ff073
002FF0AB  40 0F B6 CF                     movzx ecx, dil
002FF0AF  E8 98 14 00 00                  call 0x14030054c
002FF0B4  84 C0                           test al, al
002FF0B6  0F 84 AF 06 00 00               je 0x1402ff76b
002FF0BC  41 83 FC 02                     cmp r12d, 2
002FF0C0  0F 84 B4 01 00 00               je 0x1402ff27a
002FF0C6  41 83 FC 01                     cmp r12d, 1
002FF0CA  0F 85 3F 0B 00 00               jne 0x1402ffc0f
002FF0D0  45 3B EC                        cmp r13d, r12d
002FF0D3  0F 84 A1 01 00 00               je 0x1402ff27a
002FF0D9  48 8B CE                        mov rcx, rsi
002FF0DC  E8 9B 22 00 00                  call 0x14030137c
002FF0E1  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FF0E6  8B F8                           mov edi, eax
002FF0E8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002FF0EC  74 17                           je 0x1402ff105
002FF0EE  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002FF0F2  33 D2                           xor edx, edx
002FF0F4  E8 77 37 88 00                  call 0x140b82870
002FF0F9  45 33 DB                        xor r11d, r11d
002FF0FC  4C 89 5E 18                     mov qword ptr [rsi + 0x18], r11
002FF100  44 88 5C 24 30                  mov byte ptr [rsp + 0x30], r11b
002FF105  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
002FF10A  49 8B F3                        mov rsi, r11
002FF10D  74 1B                           je 0x1402ff12a
002FF10F  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
002FF113  33 D2                           xor edx, edx
002FF115  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
002FF119  E8 52 37 88 00                  call 0x140b82870
002FF11E  45 33 DB                        xor r11d, r11d
002FF121  4C 89 5B 18                     mov qword ptr [rbx + 0x18], r11
002FF125  44 88 5C 24 31                  mov byte ptr [rsp + 0x31], r11b
002FF12A  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF12F  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
002FF133  83 FF FF                        cmp edi, -1
002FF136  0F 84 90 06 00 00               je 0x1402ff7cc
002FF13C  85 FF                           test edi, edi
002FF13E  0F 84 A2 02 00 00               je 0x1402ff3e6
002FF144  41 8B CB                        mov ecx, r11d
002FF147  41 81 FF 00 01 00 00            cmp r15d, 0x100
002FF14E  0F 83 1E 0C 00 00               jae 0x1402ffd72
002FF154  41 8B C7                        mov eax, r15d
002FF157  89 4C 85 70                     mov dword ptr [rbp + rax*4 + 0x70], ecx
002FF15B  41 FF C7                        inc r15d
002FF15E  48 C7 44 24 58 00 00 00 00      mov qword ptr [rsp + 0x58], 0
002FF167  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FF16C  45 8B EB                        mov r13d, r11d
002FF16F  C6 44 24 54 00                  mov byte ptr [rsp + 0x54], 0
002FF174  41 8B DB                        mov ebx, r11d
002FF177  66 44 89 5C 24 50               mov word ptr [rsp + 0x50], r11w
002FF17D  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
002FF182  74 17                           je 0x1402ff19b
002FF184  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002FF188  33 D2                           xor edx, edx
002FF18A  E8 E1 36 88 00                  call 0x140b82870
002FF18F  45 33 DB                        xor r11d, r11d
002FF192  4C 89 5E 18                     mov qword ptr [rsi + 0x18], r11
002FF196  44 88 5C 24 30                  mov byte ptr [rsp + 0x30], r11b
002FF19B  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
002FF1A0  49 8B F3                        mov rsi, r11
002FF1A3  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
002FF1A8  44 89 5C 24 68                  mov dword ptr [rsp + 0x68], r11d
002FF1AD  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
002FF1B2  66 44 89 5C 24 78               mov word ptr [rsp + 0x78], r11w
002FF1B8  C6 44 24 7C 00                  mov byte ptr [rsp + 0x7c], 0
002FF1BD  48 C7 45 80 00 00 00 00         mov qword ptr [rbp - 0x80], 0
002FF1C5  74 1B                           je 0x1402ff1e2
002FF1C7  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
002FF1CB  33 D2                           xor edx, edx
002FF1CD  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
002FF1D1  E8 9A 36 88 00                  call 0x140b82870
002FF1D6  45 33 DB                        xor r11d, r11d
002FF1D9  4C 89 5F 18                     mov qword ptr [rdi + 0x18], r11
002FF1DD  44 88 5C 24 31                  mov byte ptr [rsp + 0x31], r11b
002FF1E2  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
002FF1E6  45 8B E3                        mov r12d, r11d
002FF1E9  44 89 5D 90                     mov dword ptr [rbp - 0x70], r11d
002FF1ED  4C 89 5D 98                     mov qword ptr [rbp - 0x68], r11
002FF1F1  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
002FF1F6  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
002FF1FA  8B 95 00 05 00 00               mov edx, dword ptr [rbp + 0x500]
002FF200  E9 21 FB FF FF                  jmp 0x1402fed26
002FF205  41 FF C6                        inc r14d
002FF208  C6 44 24 34 00                  mov byte ptr [rsp + 0x34], 0
002FF20D  45 8B CB                        mov r9d, r11d
002FF210  45 3B CC                        cmp r9d, r12d
002FF213  73 74                           jae 0x1402ff289
002FF215  41 8B C1                        mov eax, r9d
002FF218  48 8D 0C 80                     lea rcx, [rax + rax*4]
002FF21C  4C 8D 1C CD 00 00 00 00         lea r11, [rcx*8]
002FF224  46 8B 54 1C 5C                  mov r10d, dword ptr [rsp + r11 + 0x5c]
002FF229  45 85 D2                        test r10d, r10d
002FF22C  74 4C                           je 0x1402ff27a
002FF22E  40 0F B6 CF                     movzx ecx, dil
002FF232  E8 15 13 00 00                  call 0x14030054c
002FF237  84 C0                           test al, al
002FF239  0F 84 00 03 00 00               je 0x1402ff53f
002FF23F  41 FF C1                        inc r9d
002FF242  EB CC                           jmp 0x1402ff210
002FF244  41 83 C0 80                     add r8d, -0x80
002FF248  41 83 F8 21                     cmp r8d, 0x21
002FF24C  77 75                           ja 0x1402ff2c3
002FF24E  48 8D 15 AB 0D D0 FF            lea rdx, [rip - 0x2ff255]
002FF255  49 63 C0                        movsxd rax, r8d
002FF258  0F B6 84 02 26 31 04 00         movzx eax, byte ptr [rdx + rax + 0x43126]
002FF260  8B 8C 82 12 31 04 00            mov ecx, dword ptr [rdx + rax*4 + 0x43112]
002FF267  48 03 CA                        add rcx, rdx
002FF26A  FF E1                           jmp rcx
002FF26C  CC                              int3
002FF26D  CC                              int3
002FF26E  CC                              int3
002FF26F  CC                              int3
002FF270  41 83 FD 01                     cmp r13d, 1
002FF274  0F 85 E8 06 00 00               jne 0x1402ff962
002FF27A  BB A2 01 00 C0                  mov ebx, 0xc00001a2
002FF27F  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FF284  E9 9F FB FF FF                  jmp 0x1402fee28
002FF289  40 0F B6 CF                     movzx ecx, dil
002FF28D  E8 BA 12 00 00                  call 0x14030054c
002FF292  84 C0                           test al, al
002FF294  0F 84 E0 04 00 00               je 0x1402ff77a
002FF29A  41 81 F8 A3 00 00 00            cmp r8d, 0xa3
002FF2A1  75 A1                           jne 0x1402ff244
002FF2A3  41 83 FD 01                     cmp r13d, 1
002FF2A7  74 D1                           je 0x1402ff27a
002FF2A9  41 83 FC 02                     cmp r12d, 2
002FF2AD  75 CB                           jne 0x1402ff27a
002FF2AF  40 80 FF 88                     cmp dil, 0x88
002FF2B3  0F 84 53 0A 00 00               je 0x1402ffd0c
002FF2B9  40 80 FF 8F                     cmp dil, 0x8f
002FF2BD  0F 84 49 0A 00 00               je 0x1402ffd0c
002FF2C3  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
002FF2C8  40 0F B6 CF                     movzx ecx, dil
002FF2CC  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FF2D1  E8 A2 12 00 00                  call 0x140300578
002FF2D6  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002FF2DA  40 80 C7 72                     add dil, 0x72
002FF2DE  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FF2E3  40 80 FF 01                     cmp dil, 1
002FF2E7  0F 86 39 0A 00 00               jbe 0x1402ffd26
002FF2ED  45 33 DB                        xor r11d, r11d
002FF2F0  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF2F5  41 81 FF 00 01 00 00            cmp r15d, 0x100
002FF2FC  0F 83 70 0A 00 00               jae 0x1402ffd72
002FF302  42 89 4C BD 70                  mov dword ptr [rbp + r15*4 + 0x70], ecx
002FF307  E9 4F FE FF FF                  jmp 0x1402ff15b
002FF30C  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
002FF312  0F 85 67 FF FF FF               jne 0x1402ff27f
002FF318  45 33 DB                        xor r11d, r11d
002FF31B  4A 8D 04 AD 00 00 00 00         lea rax, [r13*4]
002FF323  49 03 C5                        add rax, r13
002FF326  41 8B DB                        mov ebx, r11d
002FF329  48 8D 3C C5 00 00 00 00         lea rdi, [rax*8]
002FF331  66 44 89 5C 3C 50               mov word ptr [rsp + rdi + 0x50], r11w
002FF337  44 89 5C 3C 54                  mov dword ptr [rsp + rdi + 0x54], r11d
002FF33C  4C 89 5C 3C 60                  mov qword ptr [rsp + rdi + 0x60], r11
002FF341  46 38 5C 2C 30                  cmp byte ptr [rsp + r13 + 0x30], r11b
002FF346  0F 84 E3 FC FF FF               je 0x1402ff02f
002FF34C  4A 8B 4C 25 F8                  mov rcx, qword ptr [rbp + r12 - 8]
002FF351  33 D2                           xor edx, edx
002FF353  E8 18 35 88 00                  call 0x140b82870
002FF358  49 83 FD 02                     cmp r13, 2
002FF35C  0F 83 49 06 00 00               jae 0x1402ff9ab
002FF362  42 88 5C 2C 30                  mov byte ptr [rsp + r13 + 0x30], bl
002FF367  E9 C0 FC FF FF                  jmp 0x1402ff02c
002FF36C  80 BD 10 05 00 00 00            cmp byte ptr [rbp + 0x510], 0
002FF373  48 8B 85 E0 04 00 00            mov rax, qword ptr [rbp + 0x4e0]
002FF37A  48 0F 44 45 C0                  cmove rax, qword ptr [rbp - 0x40]
002FF37F  C7 06 03 00 00 00               mov dword ptr [rsi], 3
002FF385  E9 F7 FB FF FF                  jmp 0x1402fef81
002FF38A  C7 07 01 00 00 00               mov dword ptr [rdi], 1
002FF390  BB 2F 00 00 80                  mov ebx, 0x8000002f
002FF395  48 8B F7                        mov rsi, rdi
002FF398  E9 8B FA FF FF                  jmp 0x1402fee28
002FF39D  41 81 F8 FB 00 00 00            cmp r8d, 0xfb
002FF3A4  0F 87 D0 FE FF FF               ja 0x1402ff27a
002FF3AA  41 0F B6 84 3A 70 31 04 00      movzx eax, byte ptr [r10 + rdi + 0x43170]
002FF3B3  41 8B 8C 82 48 31 04 00         mov ecx, dword ptr [r10 + rax*4 + 0x43148]
002FF3BB  49 03 CA                        add rcx, r10
002FF3BE  FF E1                           jmp rcx
002FF3C0  CC                              int3
002FF3C1  CC                              int3
002FF3C2  CC                              int3
002FF3C3  CC                              int3
002FF3C4  41 FF C6                        inc r14d
002FF3C7  44 3B F2                        cmp r14d, edx
002FF3CA  73 0A                           jae 0x1402ff3d6
002FF3CC  43 80 3C 0E 00                  cmp byte ptr [r14 + r9], 0
002FF3D1  74 F1                           je 0x1402ff3c4
002FF3D3  44 3B F2                        cmp r14d, edx
002FF3D6  0F 85 9E FE FF FF               jne 0x1402ff27a
002FF3DC  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF3E1  E9 47 F9 FF FF                  jmp 0x1402fed2d
002FF3E6  B9 01 00 00 00                  mov ecx, 1
002FF3EB  E9 57 FD FF FF                  jmp 0x1402ff147
002FF3F0  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002FF3F4  F7 80 C8 00 00 00 00 00 02 00   test dword ptr [rax + 0xc8], 0x20000
002FF3FE  0F 85 CC FB FF FF               jne 0x1402fefd0
002FF404  48 8D 4D F0                     lea rcx, [rbp - 0x10]
002FF408  49 03 CC                        add rcx, r12
002FF40B  E8 18 94 0A 00                  call 0x1403a8828
002FF410  84 C0                           test al, al
002FF412  0F 84 B8 FB FF FF               je 0x1402fefd0
002FF418  80 7C 24 4B 00                  cmp byte ptr [rsp + 0x4b], 0
002FF41D  0F 85 AD FB FF FF               jne 0x1402fefd0
002FF423  80 7C 24 4A 00                  cmp byte ptr [rsp + 0x4a], 0
002FF428  0F 85 1C 09 00 00               jne 0x1402ffd4a
002FF42E  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
002FF432  48 8D 55 B8                     lea rdx, [rbp - 0x48]
002FF436  E8 21 8E 1F 00                  call 0x1404f825c
002FF43B  8B D8                           mov ebx, eax
002FF43D  85 C0                           test eax, eax
002FF43F  0F 89 00 09 00 00               jns 0x1402ffd45
002FF445  C6 44 24 4B 01                  mov byte ptr [rsp + 0x4b], 1
002FF44A  3D 25 02 00 C0                  cmp eax, 0xc0000225
002FF44F  0F 84 7B FB FF FF               je 0x1402fefd0
002FF455  E9 B2 FE FF FF                  jmp 0x1402ff30c
002FF45A  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FF45F  BB 17 00 00 C0                  mov ebx, 0xc0000017
002FF464  E9 BF F9 FF FF                  jmp 0x1402fee28
002FF469  41 8D 42 FF                     lea eax, [r10 - 1]
002FF46D  83 F8 4F                        cmp eax, 0x4f
002FF470  0F 87 93 F9 FF FF               ja 0x1402fee09
002FF476  48 8D 3D 83 0B D0 FF            lea rdi, [rip - 0x2ff47d]
002FF47D  48 98                           cdqe
002FF47F  0F B6 84 07 78 32 04 00         movzx eax, byte ptr [rdi + rax + 0x43278]
002FF487  8B 8C 87 6C 32 04 00            mov ecx, dword ptr [rdi + rax*4 + 0x4326c]
002FF48E  48 03 CF                        add rcx, rdi
002FF491  FF E1                           jmp rcx
002FF493  CC                              int3
002FF494  CC                              int3
002FF495  CC                              int3
002FF496  CC                              int3
002FF497  BB 0D 00 00 C0                  mov ebx, 0xc000000d
002FF49C  E9 F4 FE FF FF                  jmp 0x1402ff395
002FF4A1  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
002FF4A6  45 8B C4                        mov r8d, r12d
002FF4A9  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FF4AE  40 0F B6 CF                     movzx ecx, dil
002FF4B2  41 FF C6                        inc r14d
002FF4B5  E8 D6 0E 00 00                  call 0x140300390
002FF4BA  84 C0                           test al, al
002FF4BC  0F 84 B8 FD FF FF               je 0x1402ff27a
002FF4C2  33 D2                           xor edx, edx
002FF4C4  48 85 F6                        test rsi, rsi
002FF4C7  8B CA                           mov ecx, edx
002FF4C9  0F 95 C1                        setne cl
002FF4CC  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FF4D0  40 80 FF 8D                     cmp dil, 0x8d
002FF4D4  0F 84 A6 03 00 00               je 0x1402ff880
002FF4DA  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF4DF  41 81 FF 00 01 00 00            cmp r15d, 0x100
002FF4E6  0F 83 86 08 00 00               jae 0x1402ffd72
002FF4EC  42 89 4C BD 70                  mov dword ptr [rbp + r15*4 + 0x70], ecx
002FF4F1  8B DA                           mov ebx, edx
002FF4F3  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002FF4F8  41 FF C7                        inc r15d
002FF4FB  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002FF500  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
002FF505  E8 86 1C 00 00                  call 0x140301190
002FF50A  44 8B 6C 24 5C                  mov r13d, dword ptr [rsp + 0x5c]
002FF50F  45 33 DB                        xor r11d, r11d
002FF512  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FF517  45 8B E3                        mov r12d, r11d
002FF51A  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
002FF51F  E9 D2 FC FF FF                  jmp 0x1402ff1f6
002FF524  41 83 F9 01                     cmp r9d, 1
002FF528  0F 84 78 FB FF FF               je 0x1402ff0a6
002FF52E  42 83 7C 14 54 01               cmp dword ptr [rsp + r10 + 0x54], 1
002FF534  0F 86 6C FB FF FF               jbe 0x1402ff0a6
002FF53A  E9 3B FD FF FF                  jmp 0x1402ff27a
002FF53F  41 83 FA 01                     cmp r10d, 1
002FF543  0F 84 F6 FC FF FF               je 0x1402ff23f
002FF549  42 83 7C 1C 54 01               cmp dword ptr [rsp + r11 + 0x54], 1
002FF54F  0F 86 EA FC FF FF               jbe 0x1402ff23f
002FF555  E9 08 07 00 00                  jmp 0x1402ffc62
002FF55A  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
002FF560  E9 FA F8 FF FF                  jmp 0x1402fee5f
002FF565  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
002FF569  48 85 FF                        test rdi, rdi
002FF56C  0F 84 E5 F8 FF FF               je 0x1402fee57
002FF572  48 8B CF                        mov rcx, rdi
002FF575  E8 B6 1C 00 00                  call 0x140301230
002FF57A  BA 53 65 41 74                  mov edx, 0x74416553
002FF57F  48 8B CF                        mov rcx, rdi
002FF582  E8 E9 32 88 00                  call 0x140b82870
002FF587  E9 CB F8 FF FF                  jmp 0x1402fee57
002FF58C  41 8D 41 FF                     lea eax, [r9 - 1]
002FF590  83 F8 0A                        cmp eax, 0xa
002FF593  0F 82 E1 FC FF FF               jb 0x1402ff27a
002FF599  49 8D 47 01                     lea rax, [r15 + 1]
002FF59D  66 C7 02 02 00                  mov word ptr [rdx], 2
002FF5A2  41 B8 0B 00 00 00               mov r8d, 0xb
002FF5A8  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
002FF5AC  41 FF C4                        inc r12d
002FF5AF  C7 42 18 0A 00 00 00            mov dword ptr [rdx + 0x18], 0xa
002FF5B6  45 03 F0                        add r14d, r8d
002FF5B9  E9 91 FA FF FF                  jmp 0x1402ff04f
002FF5BE  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
002FF5C3  45 8B C4                        mov r8d, r12d
002FF5C6  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FF5CB  40 0F B6 CF                     movzx ecx, dil
002FF5CF  41 FF C6                        inc r14d
002FF5D2  E8 B9 0D 00 00                  call 0x140300390
002FF5D7  84 C0                           test al, al
002FF5D9  0F 84 9B FC FF FF               je 0x1402ff27a
002FF5DF  41 83 FC 02                     cmp r12d, 2
002FF5E3  0F 84 C5 01 00 00               je 0x1402ff7ae
002FF5E9  41 83 FC 01                     cmp r12d, 1
002FF5ED  0F 84 B3 05 00 00               je 0x1402ffba6
002FF5F3  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF5F8  41 83 FF 01                     cmp r15d, 1
002FF5FC  0F 82 78 FC FF FF               jb 0x1402ff27a
002FF602  41 FF CF                        dec r15d
002FF605  46 8B 54 BD 70                  mov r10d, dword ptr [rbp + r15*4 + 0x70]
002FF60A  41 83 FF 01                     cmp r15d, 1
002FF60E  0F 82 66 FC FF FF               jb 0x1402ff27a
002FF614  41 FF CF                        dec r15d
002FF617  42 8B 44 BD 70                  mov eax, dword ptr [rbp + r15*4 + 0x70]
002FF61C  40 80 FF A0                     cmp dil, 0xa0
002FF620  0F 85 95 05 00 00               jne 0x1402ffbbb
002FF626  45 85 D2                        test r10d, r10d
002FF629  0F 85 A7 01 00 00               jne 0x1402ff7d6
002FF62F  33 D2                           xor edx, edx
002FF631  8B CA                           mov ecx, edx
002FF633  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002FF637  41 81 FF 00 01 00 00            cmp r15d, 0x100
002FF63E  0F 83 2E 07 00 00               jae 0x1402ffd72
002FF644  41 8B C7                        mov eax, r15d
002FF647  89 4C 85 70                     mov dword ptr [rbp + rax*4 + 0x70], ecx
002FF64B  E9 A1 FE FF FF                  jmp 0x1402ff4f1
002FF650  45 85 FF                        test r15d, r15d
002FF653  0F 85 26 FC FF FF               jne 0x1402ff27f
002FF659  41 83 FC 01                     cmp r12d, 1
002FF65D  0F 85 1C FC FF FF               jne 0x1402ff27f
002FF663  48 8B CE                        mov rcx, rsi
002FF666  E8 11 1D 00 00                  call 0x14030137c
002FF66B  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FF670  89 06                           mov dword ptr [rsi], eax
002FF672  E9 B1 F7 FF FF                  jmp 0x1402fee28
002FF677  66 C7 02 10 00                  mov word ptr [rdx], 0x10
002FF67C  41 80 FA 50                     cmp r10b, 0x50
002FF680  0F 85 64 F7 FF FF               jne 0x1402fedea
002FF686  44 88 42 04                     mov byte ptr [rdx + 4], r8b
002FF68A  E9 5B F7 FF FF                  jmp 0x1402fedea
002FF68F  41 83 FD 01                     cmp r13d, 1
002FF693  0F 84 E1 FB FF FF               je 0x1402ff27a
002FF699  48 8B CE                        mov rcx, rsi
002FF69C  E8 DB 1C 00 00                  call 0x14030137c
002FF6A1  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
002FF6A5  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002FF6A9  81 FA 00 01 00 00               cmp edx, 0x100
002FF6AF  0F 83 BD 06 00 00               jae 0x1402ffd72
002FF6B5  89 44 95 70                     mov dword ptr [rbp + rdx*4 + 0x70], eax
002FF6B9  FF C2                           inc edx
002FF6BB  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FF6C0  89 54 24 3C                     mov dword ptr [rsp + 0x3c], edx
002FF6C4  74 0B                           je 0x1402ff6d1
002FF6C6  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002FF6CA  33 D2                           xor edx, edx
002FF6CC  E8 9F 31 88 00                  call 0x140b82870
002FF6D1  0F 10 45 28                     movups xmm0, xmmword ptr [rbp + 0x28]
002FF6D5  48 8D 45 E0                     lea rax, [rbp - 0x20]
002FF6D9  33 D2                           xor edx, edx
002FF6DB  0F 10 4D 38                     movups xmm1, xmmword ptr [rbp + 0x38]
002FF6DF  48 8D 4D 28                     lea rcx, [rbp + 0x28]
002FF6E3  0F 29 45 E0                     movaps xmmword ptr [rbp - 0x20], xmm0
002FF6E7  0F 10 45 48                     movups xmm0, xmmword ptr [rbp + 0x48]
002FF6EB  0F 29 4D F0                     movaps xmmword ptr [rbp - 0x10], xmm1
002FF6EF  0F 10 4D 58                     movups xmm1, xmmword ptr [rbp + 0x58]
002FF6F3  0F 29 45 00                     movaps xmmword ptr [rbp], xmm0
002FF6F7  F2 0F 10 45 68                  movsd xmm0, qword ptr [rbp + 0x68]
002FF6FC  F2 0F 11 45 20                  movsd qword ptr [rbp + 0x20], xmm0
002FF701  0F 10 45 88                     movups xmm0, xmmword ptr [rbp - 0x78]
002FF705  0F 29 4D 10                     movaps xmmword ptr [rbp + 0x10], xmm1
002FF709  0F 10 4C 24 78                  movups xmm1, xmmword ptr [rsp + 0x78]
002FF70E  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
002FF713  0F 57 C0                        xorps xmm0, xmm0
002FF716  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002FF71B  0F B6 44 24 31                  movzx eax, byte ptr [rsp + 0x31]
002FF720  88 44 24 30                     mov byte ptr [rsp + 0x30], al
002FF724  33 C0                           xor eax, eax
002FF726  0F 29 4C 24 50                  movaps xmmword ptr [rsp + 0x50], xmm1
002FF72B  F2 0F 10 4D 98                  movsd xmm1, qword ptr [rbp - 0x68]
002FF730  F2 0F 11 4C 24 70               movsd qword ptr [rsp + 0x70], xmm1
002FF736  44 8D 40 48                     lea r8d, [rax + 0x48]
002FF73A  C6 44 24 31 00                  mov byte ptr [rsp + 0x31], 0
002FF73F  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
002FF744  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002FF748  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
002FF74C  E8 EF 74 3C 00                  call 0x1406c6c40
002FF751  8B 95 00 05 00 00               mov edx, dword ptr [rbp + 0x500]
002FF757  41 BC 01 00 00 00               mov r12d, 1
002FF75D  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
002FF761  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
002FF766  E9 2E F7 FF FF                  jmp 0x1402fee99
002FF76B  41 83 FC 02                     cmp r12d, 2
002FF76F  0F 84 05 FB FF FF               je 0x1402ff27a
002FF775  E9 42 F9 FF FF                  jmp 0x1402ff0bc
002FF77A  41 83 FC 02                     cmp r12d, 2
002FF77E  0F 85 16 FB FF FF               jne 0x1402ff29a
002FF784  B8 FB FF 00 00                  mov eax, 0xfffb
002FF789  66 85 44 24 50                  test word ptr [rsp + 0x50], ax
002FF78E  0F 84 06 FB FF FF               je 0x1402ff29a
002FF794  83 7D 84 01                     cmp dword ptr [rbp - 0x7c], 1
002FF798  0F 85 FC FA FF FF               jne 0x1402ff29a
002FF79E  80 7C 24 7C 00                  cmp byte ptr [rsp + 0x7c], 0
002FF7A3  0F 85 D1 FA FF FF               jne 0x1402ff27a
002FF7A9  E9 EC FA FF FF                  jmp 0x1402ff29a
002FF7AE  48 8B CE                        mov rcx, rsi
002FF7B1  E8 C6 1B 00 00                  call 0x14030137c
002FF7B6  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002FF7BA  44 8B D0                        mov r10d, eax
002FF7BD  E8 BA 1B 00 00                  call 0x14030137c
002FF7C2  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FF7C7  E9 50 FE FF FF                  jmp 0x1402ff61c
002FF7CC  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FF7D1  E9 71 F9 FF FF                  jmp 0x1402ff147
002FF7D6  85 C0                           test eax, eax
002FF7D8  0F 84 51 FE FF FF               je 0x1402ff62f
002FF7DE  83 F8 FF                        cmp eax, -1
002FF7E1  0F 85 E7 04 00 00               jne 0x1402ffcce
002FF7E7  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FF7EC  33 D2                           xor edx, edx
002FF7EE  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FF7F2  E9 40 FE FF FF                  jmp 0x1402ff637
002FF7F7  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
002FF7FC  45 8B C4                        mov r8d, r12d
002FF7FF  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FF804  40 0F B6 CF                     movzx ecx, dil
002FF808  41 FF C6                        inc r14d
002FF80B  E8 80 0B 00 00                  call 0x140300390
002FF810  84 C0                           test al, al
002FF812  0F 84 A8 01 00 00               je 0x1402ff9c0
002FF818  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FF81D  0F 85 0C 04 00 00               jne 0x1402ffc2f
002FF823  40 80 FF 89                     cmp dil, 0x89
002FF827  0F 85 05 02 00 00               jne 0x1402ffa32
002FF82D  B0 01                           mov al, 1
002FF82F  E9 0A 02 00 00                  jmp 0x1402ffa3e
002FF834  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
002FF839  45 8B C4                        mov r8d, r12d
002FF83C  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FF841  40 0F B6 CF                     movzx ecx, dil
002FF845  41 FF C6                        inc r14d
002FF848  E8 43 0B 00 00                  call 0x140300390
002FF84D  84 C0                           test al, al
002FF84F  0F 84 A4 01 00 00               je 0x1402ff9f9
002FF855  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FF85A  0F 85 D9 03 00 00               jne 0x1402ffc39
002FF860  40 80 FF 8A                     cmp dil, 0x8a
002FF864  0F 85 2D 02 00 00               jne 0x1402ffa97
002FF86A  B0 01                           mov al, 1
002FF86C  E9 32 02 00 00                  jmp 0x1402ffaa3
002FF871  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
002FF875  C7 06 04 00 00 00               mov dword ptr [rsi], 4
002FF87B  E9 01 F7 FF FF                  jmp 0x1402fef81
002FF880  8B C2                           mov eax, edx
002FF882  85 C9                           test ecx, ecx
002FF884  0F 94 C0                        sete al
002FF887  8B C8                           mov ecx, eax
002FF889  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002FF88D  E9 48 FC FF FF                  jmp 0x1402ff4da
002FF892  41 83 FD 01                     cmp r13d, 1
002FF896  0F 84 DE F9 FF FF               je 0x1402ff27a
002FF89C  48 8B CE                        mov rcx, rsi
002FF89F  E8 D8 1A 00 00                  call 0x14030137c
002FF8A4  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
002FF8A8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002FF8AC  81 FA 00 01 00 00               cmp edx, 0x100
002FF8B2  0F 83 BA 04 00 00               jae 0x1402ffd72
002FF8B8  89 44 95 70                     mov dword ptr [rbp + rdx*4 + 0x70], eax
002FF8BC  FF C2                           inc edx
002FF8BE  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FF8C3  89 54 24 3C                     mov dword ptr [rsp + 0x3c], edx
002FF8C7  74 0B                           je 0x1402ff8d4
002FF8C9  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002FF8CD  33 D2                           xor edx, edx
002FF8CF  E8 9C 2F 88 00                  call 0x140b82870
002FF8D4  0F 10 45 28                     movups xmm0, xmmword ptr [rbp + 0x28]
002FF8D8  48 8D 45 E0                     lea rax, [rbp - 0x20]
002FF8DC  33 D2                           xor edx, edx
002FF8DE  0F 10 4D 38                     movups xmm1, xmmword ptr [rbp + 0x38]
002FF8E2  48 8D 4D 28                     lea rcx, [rbp + 0x28]
002FF8E6  0F 29 45 E0                     movaps xmmword ptr [rbp - 0x20], xmm0
002FF8EA  0F 10 45 48                     movups xmm0, xmmword ptr [rbp + 0x48]
002FF8EE  0F 29 4D F0                     movaps xmmword ptr [rbp - 0x10], xmm1
002FF8F2  0F 10 4D 58                     movups xmm1, xmmword ptr [rbp + 0x58]
002FF8F6  0F 29 45 00                     movaps xmmword ptr [rbp], xmm0
002FF8FA  F2 0F 10 45 68                  movsd xmm0, qword ptr [rbp + 0x68]
002FF8FF  F2 0F 11 45 20                  movsd qword ptr [rbp + 0x20], xmm0
002FF904  0F 10 45 88                     movups xmm0, xmmword ptr [rbp - 0x78]
002FF908  0F 29 4D 10                     movaps xmmword ptr [rbp + 0x10], xmm1
002FF90C  0F 10 4C 24 78                  movups xmm1, xmmword ptr [rsp + 0x78]
002FF911  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
002FF916  0F 57 C0                        xorps xmm0, xmm0
002FF919  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002FF91E  0F B6 44 24 31                  movzx eax, byte ptr [rsp + 0x31]
002FF923  88 44 24 30                     mov byte ptr [rsp + 0x30], al
002FF927  33 C0                           xor eax, eax
002FF929  0F 29 4C 24 50                  movaps xmmword ptr [rsp + 0x50], xmm1
002FF92E  F2 0F 10 4D 98                  movsd xmm1, qword ptr [rbp - 0x68]
002FF933  F2 0F 11 4C 24 70               movsd qword ptr [rsp + 0x70], xmm1
002FF939  44 8D 40 48                     lea r8d, [rax + 0x48]
002FF93D  C6 44 24 31 00                  mov byte ptr [rsp + 0x31], 0
002FF942  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
002FF947  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002FF94B  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
002FF94F  E8 EC 72 3C 00                  call 0x1406c6c40
002FF954  45 33 DB                        xor r11d, r11d
002FF957  41 BC 01 00 00 00               mov r12d, 1
002FF95D  E9 1B F4 FF FF                  jmp 0x1402fed7d
002FF962  41 83 FC 01                     cmp r12d, 1
002FF966  0F 85 0E F9 FF FF               jne 0x1402ff27a
002FF96C  41 8D 45 FD                     lea eax, [r13 - 3]
002FF970  A9 FD FF FF FF                  test eax, 0xfffffffd
002FF975  0F 85 48 F9 FF FF               jne 0x1402ff2c3
002FF97B  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FF980  BB A2 01 00 C0                  mov ebx, 0xc00001a2
002FF985  E9 9E F4 FF FF                  jmp 0x1402fee28
002FF98A  80 BD 10 05 00 00 00            cmp byte ptr [rbp + 0x510], 0
002FF991  48 8B 85 F0 04 00 00            mov rax, qword ptr [rbp + 0x4f0]
002FF998  48 0F 44 85 E8 04 00 00         cmove rax, qword ptr [rbp + 0x4e8]
002FF9A0  C7 06 05 00 00 00               mov dword ptr [rsi], 5
002FF9A6  E9 D6 F5 FF FF                  jmp 0x1402fef81
002FF9AB  E8 2C 66 1F 00                  call 0x1404f5fdc
002FF9B0  CC                              int3
002FF9B1  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002FF9B5  C7 06 06 00 00 00               mov dword ptr [rsi], 6
002FF9BB  E9 C1 F5 FF FF                  jmp 0x1402fef81
002FF9C0  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FF9C5  BB A2 01 00 C0                  mov ebx, 0xc00001a2
002FF9CA  0F 84 AF F8 FF FF               je 0x1402ff27f
002FF9D0  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FF9D5  33 D2                           xor edx, edx
002FF9D7  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FF9DB  8B C1                           mov eax, ecx
002FF9DD  40 80 C7 70                     add dil, 0x70
002FF9E1  40 F6 C7 FD                     test dil, 0xfd
002FF9E5  0F 85 EF FA FF FF               jne 0x1402ff4da
002FF9EB  83 F8 FF                        cmp eax, -1
002FF9EE  0F 84 E6 FA FF FF               je 0x1402ff4da
002FF9F4  E9 4F 05 3E 00                  jmp 0x1406dff48
002FF9F9  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FF9FE  BB A2 01 00 C0                  mov ebx, 0xc00001a2
002FFA03  0F 84 76 F8 FF FF               je 0x1402ff27f
002FFA09  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FFA0E  33 D2                           xor edx, edx
002FFA10  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFA14  8B C1                           mov eax, ecx
002FFA16  40 80 C7 6F                     add dil, 0x6f
002FFA1A  40 F6 C7 FD                     test dil, 0xfd
002FFA1E  0F 85 B6 FA FF FF               jne 0x1402ff4da
002FFA24  83 F8 FF                        cmp eax, -1
002FFA27  0F 84 AD FA FF FF               je 0x1402ff4da
002FFA2D  E9 16 05 3E 00                  jmp 0x1406dff48
002FFA32  40 80 FF 90                     cmp dil, 0x90
002FFA36  0F 84 F1 FD FF FF               je 0x1402ff82d
002FFA3C  32 C0                           xor al, al
002FFA3E  44 0F B6 8D 10 05 00 00         movzx r9d, byte ptr [rbp + 0x510]
002FFA46  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002FFA4B  44 0F B6 85 08 05 00 00         movzx r8d, byte ptr [rbp + 0x508]
002FFA53  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
002FFA57  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002FFA5C  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002FFA61  88 44 24 20                     mov byte ptr [rsp + 0x20], al
002FFA65  E8 1A 3B 1E 00                  call 0x1404e3584
002FFA6A  8B D8                           mov ebx, eax
002FFA6C  0F B6 44 24 48                  movzx eax, byte ptr [rsp + 0x48]
002FFA71  88 44 24 49                     mov byte ptr [rsp + 0x49], al
002FFA75  85 DB                           test ebx, ebx
002FFA77  0F 88 53 FF FF FF               js 0x1402ff9d0
002FFA7D  33 D2                           xor edx, edx
002FFA7F  84 C0                           test al, al
002FFA81  0F 84 5F 01 00 00               je 0x1402ffbe6
002FFA87  B9 01 00 00 00                  mov ecx, 1
002FFA8C  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFA90  8B C1                           mov eax, ecx
002FFA92  E9 46 FF FF FF                  jmp 0x1402ff9dd
002FFA97  40 80 FF 91                     cmp dil, 0x91
002FFA9B  0F 84 C9 FD FF FF               je 0x1402ff86a
002FFAA1  32 C0                           xor al, al
002FFAA3  44 0F B6 8D 10 05 00 00         movzx r9d, byte ptr [rbp + 0x510]
002FFAAB  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002FFAB0  44 0F B6 85 08 05 00 00         movzx r8d, byte ptr [rbp + 0x508]
002FFAB8  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
002FFABC  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002FFAC1  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002FFAC6  88 44 24 20                     mov byte ptr [rsp + 0x20], al
002FFACA  E8 C5 3B 1E 00                  call 0x1404e3694
002FFACF  8B D8                           mov ebx, eax
002FFAD1  0F B6 44 24 48                  movzx eax, byte ptr [rsp + 0x48]
002FFAD6  88 44 24 49                     mov byte ptr [rsp + 0x49], al
002FFADA  85 DB                           test ebx, ebx
002FFADC  0F 88 27 FF FF FF               js 0x1402ffa09
002FFAE2  33 D2                           xor edx, edx
002FFAE4  84 C0                           test al, al
002FFAE6  0F 84 07 01 00 00               je 0x1402ffbf3
002FFAEC  B9 01 00 00 00                  mov ecx, 1
002FFAF1  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFAF5  8B C1                           mov eax, ecx
002FFAF7  E9 1A FF FF FF                  jmp 0x1402ffa16
002FFAFC  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
002FFB01  45 8B C4                        mov r8d, r12d
002FFB04  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FFB09  40 0F B6 CF                     movzx ecx, dil
002FFB0D  41 FF C6                        inc r14d
002FFB10  E8 7B 08 00 00                  call 0x140300390
002FFB15  84 C0                           test al, al
002FFB17  0F 84 78 01 00 00               je 0x1402ffc95
002FFB1D  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FFB22  0F 85 7D 01 00 00               jne 0x1402ffca5
002FFB28  0F B7 5C 24 50                  movzx ebx, word ptr [rsp + 0x50]
002FFB2D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002FFB32  41 83 FD 01                     cmp r13d, 1
002FFB36  66 0F 44 5C 24 78               cmove bx, word ptr [rsp + 0x78]
002FFB3C  E8 C7 0B 00 00                  call 0x140300708
002FFB41  84 C0                           test al, al
002FFB43  0F 85 99 01 00 00               jne 0x1402ffce2
002FFB49  33 D2                           xor edx, edx
002FFB4B  8B CA                           mov ecx, edx
002FFB4D  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002FFB51  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FFB56  41 81 FF 00 01 00 00            cmp r15d, 0x100
002FFB5D  0F 83 0F 02 00 00               jae 0x1402ffd72
002FFB63  42 89 4C BD 70                  mov dword ptr [rbp + r15*4 + 0x70], ecx
002FFB68  8B DA                           mov ebx, edx
002FFB6A  41 FF C7                        inc r15d
002FFB6D  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002FFB72  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002FFB77  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
002FFB7C  E8 0F 16 00 00                  call 0x140301190
002FFB81  44 8B 6C 24 5C                  mov r13d, dword ptr [rsp + 0x5c]
002FFB86  45 33 DB                        xor r11d, r11d
002FFB89  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FFB8E  E9 63 F6 FF FF                  jmp 0x1402ff1f6
002FFB93  C7 07 01 00 00 00               mov dword ptr [rdi], 1
002FFB99  BB 2F 00 00 80                  mov ebx, 0x8000002f
002FFB9E  48 8B F7                        mov rsi, rdi
002FFBA1  E9 82 F2 FF FF                  jmp 0x1402fee28
002FFBA6  48 8B CE                        mov rcx, rsi
002FFBA9  E8 CE 17 00 00                  call 0x14030137c
002FFBAE  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FFBB3  44 8B D0                        mov r10d, eax
002FFBB6  E9 4F FA FF FF                  jmp 0x1402ff60a
002FFBBB  41 83 FA 01                     cmp r10d, 1
002FFBBF  0F 84 13 01 00 00               je 0x1402ffcd8
002FFBC5  83 F8 FF                        cmp eax, -1
002FFBC8  0F 84 19 FC FF FF               je 0x1402ff7e7
002FFBCE  83 F8 01                        cmp eax, 1
002FFBD1  0F 84 01 01 00 00               je 0x1402ffcd8
002FFBD7  41 83 FA FF                     cmp r10d, -1
002FFBDB  0F 84 06 FC FF FF               je 0x1402ff7e7
002FFBE1  E9 49 FA FF FF                  jmp 0x1402ff62f
002FFBE6  8B CA                           mov ecx, edx
002FFBE8  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002FFBEC  8B C2                           mov eax, edx
002FFBEE  E9 EA FD FF FF                  jmp 0x1402ff9dd
002FFBF3  8B CA                           mov ecx, edx
002FFBF5  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002FFBF9  8B C2                           mov eax, edx
002FFBFB  E9 16 FE FF FF                  jmp 0x1402ffa16
002FFC00  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FFC05  BB 06 01 00 C0                  mov ebx, 0xc0000106
002FFC0A  E9 19 F2 FF FF                  jmp 0x1402fee28
002FFC0F  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
002FFC14  41 83 FF 01                     cmp r15d, 1
002FFC18  0F 82 5C F6 FF FF               jb 0x1402ff27a
002FFC1E  41 FF CF                        dec r15d
002FFC21  42 8B 7C BD 70                  mov edi, dword ptr [rbp + r15*4 + 0x70]
002FFC26  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
002FFC2A  E9 04 F5 FF FF                  jmp 0x1402ff133
002FFC2F  0F B6 44 24 49                  movzx eax, byte ptr [rsp + 0x49]
002FFC34  E9 3C FE FF FF                  jmp 0x1402ffa75
002FFC39  0F B6 44 24 49                  movzx eax, byte ptr [rsp + 0x49]
002FFC3E  E9 97 FE FF FF                  jmp 0x1402ffada
002FFC43  41 83 FC 01                     cmp r12d, 1
002FFC47  0F 85 2D F6 FF FF               jne 0x1402ff27a
002FFC4D  66 83 7C 24 50 05               cmp word ptr [rsp + 0x50], 5
002FFC53  0F 84 6A F6 FF FF               je 0x1402ff2c3
002FFC59  45 3B EC                        cmp r13d, r12d
002FFC5C  0F 84 61 F6 FF FF               je 0x1402ff2c3
002FFC62  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FFC67  C6 44 24 34 01                  mov byte ptr [rsp + 0x34], 1
002FFC6C  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFC70  E9 78 F6 FF FF                  jmp 0x1402ff2ed
002FFC75  33 D2                           xor edx, edx
002FFC77  41 3B D4                        cmp edx, r12d
002FFC7A  0F 83 43 F6 FF FF               jae 0x1402ff2c3
002FFC80  8B C2                           mov eax, edx
002FFC82  48 8D 0C 80                     lea rcx, [rax + rax*4]
002FFC86  83 7C CC 5C 01                  cmp dword ptr [rsp + rcx*8 + 0x5c], 1
002FFC8B  0F 84 E9 F5 FF FF               je 0x1402ff27a
002FFC91  FF C2                           inc edx
002FFC93  EB E2                           jmp 0x1402ffc77
002FFC95  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
002FFC9A  BB A2 01 00 C0                  mov ebx, 0xc00001a2
002FFC9F  0F 84 DA F5 FF FF               je 0x1402ff27f
002FFCA5  B9 FF FF FF FF                  mov ecx, 0xffffffff
002FFCAA  33 D2                           xor edx, edx
002FFCAC  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFCB0  E9 9C FE FF FF                  jmp 0x1402ffb51
002FFCB5  48 85 C0                        test rax, rax
002FFCB8  0F 84 8B FE FF FF               je 0x1402ffb49
002FFCBE  B9 01 00 00 00                  mov ecx, 1
002FFCC3  33 D2                           xor edx, edx
002FFCC5  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002FFCC9  E9 83 FE FF FF                  jmp 0x1402ffb51
002FFCCE  41 83 FA FF                     cmp r10d, -1
002FFCD2  0F 84 0F FB FF FF               je 0x1402ff7e7
002FFCD8  B9 01 00 00 00                  mov ecx, 1
002FFCDD  E9 0A FB FF FF                  jmp 0x1402ff7ec
002FFCE2  40 80 FF A3                     cmp dil, 0xa3
002FFCE6  0F 85 5D FE FF FF               jne 0x1402ffb49
002FFCEC  66 83 FB 02                     cmp bx, 2
002FFCF0  0F 85 53 FE FF FF               jne 0x1402ffb49
002FFCF6  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
002FFCFB  40 0F B6 CF                     movzx ecx, dil
002FFCFF  E8 38 DB 39 00                  call 0x14069d83c
002FFD04  48 83 F8 FF                     cmp rax, -1
002FFD08  74 9B                           je 0x1402ffca5
002FFD0A  EB A9                           jmp 0x1402ffcb5
002FFD0C  83 7D 84 01                     cmp dword ptr [rbp - 0x7c], 1
002FFD10  0F 85 AD F5 FF FF               jne 0x1402ff2c3
002FFD16  80 7C 24 7C 00                  cmp byte ptr [rsp + 0x7c], 0
002FFD1B  0F 84 59 F5 FF FF               je 0x1402ff27a
002FFD21  E9 9D F5 FF FF                  jmp 0x1402ff2c3
002FFD26  45 33 DB                        xor r11d, r11d
002FFD29  83 F9 FF                        cmp ecx, -1
002FFD2C  0F 84 BE F5 FF FF               je 0x1402ff2f0
002FFD32  41 8B C3                        mov eax, r11d
002FFD35  85 C9                           test ecx, ecx
002FFD37  0F 94 C0                        sete al
002FFD3A  8B C8                           mov ecx, eax
002FFD3C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002FFD40  E9 AB F5 FF FF                  jmp 0x1402ff2f0
002FFD45  C6 44 24 4A 01                  mov byte ptr [rsp + 0x4a], 1
002FFD4A  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
002FFD4E  48 8B CE                        mov rcx, rsi
002FFD51  48 89 07                        mov qword ptr [rdi], rax
002FFD54  E8 37 03 00 00                  call 0x140300090
002FFD59  8B D8                           mov ebx, eax
002FFD5B  3D 25 02 00 C0                  cmp eax, 0xc0000225
002FFD60  0F 85 92 F2 FF FF               jne 0x1402feff8
002FFD66  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
002FFD6A  48 89 07                        mov qword ptr [rdi], rax
002FFD6D  E9 5E F2 FF FF                  jmp 0x1402fefd0
002FFD72  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002FFD77  BB 09 04 00 C0                  mov ebx, 0xc0000409
002FFD7C  E9 A7 F0 FF FF                  jmp 0x1402fee28
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepEvaluateAceCondition(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9, __int64 a10, unsigned __int8 a11, __int64 a12)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned int v_stack_m4D8;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F0;
    unsigned __int64 v_stack_m4F8;
    unsigned __int64 v_stack_m500;
    unsigned __int64 v_stack_m508;
    unsigned __int64 v_stack_m510;
    unsigned __int64 v_stack_m518;
    unsigned __int64 v_stack_m520;
    unsigned int v_stack_m528;
    unsigned __int64 v_stack_m530;
    unsigned int v_stack_m534;
    unsigned __int64 v_stack_m538;
    unsigned __int8 v_stack_m53C;
    unsigned __int16 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned int v_stack_m550;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int8 v_stack_m561;
    unsigned __int16 v_stack_m563;
    unsigned __int8 v_stack_m564;
    unsigned __int16 v_stack_m568;
    unsigned int v_stack_m56C;
    unsigned __int8 v_stack_m56D;
    unsigned __int8 v_stack_m56E;
    unsigned __int8 v_stack_m56F;
    unsigned __int8 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned int v_stack_m57C;
    unsigned int v_stack_m580;
    unsigned __int8 v_stack_m584;
    unsigned __int8 v_stack_m587;
    unsigned __int16 v_stack_m588;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int8 v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int8 v_stack_p49;
    unsigned __int8 v_stack_p4A;
    unsigned __int8 v_stack_p4B;
    unsigned int v_stack_p4C;
    unsigned __int16 v_stack_p50;
    unsigned __int8 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int16 v_stack_p78;
    unsigned __int8 v_stack_p7C;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (0x580ULL);
    result = (*(unsigned __int64 *)(v_rip + 11582282)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m518 = a8;
    result = 0;
    v_stack_m4F0 = a3;
    v_stack_m508 = a2;
    v_stack_m510 = a1;
    a2 = 0;
    v_stack_m57C = 0;
    v_stack_m4D8 = 0;
    v_stack_m4D0 = 0;
    v_stack_m4F8 = a4;
    v_stack_m578 = a12;
    result = memset(v_stack_m4C8, a2, 128, a4);
    result = 0;
    a2 = 0;
    v_stack_m563 = 0;
    v_stack_m561 = 0;
    result = memset(v_stack_m560, a2, result + 72, a4);
    result = 0;
    v_stack_m580 = 0xFFFFFFFFULL;
    v_r11 = 0;
    v_stack_m588 = 0;
    v_stack_m56F = 0;
    v_stack_m570 = 0;
    v_stack_m584 = 0;
    v_stack_m56D = 0;
    v_stack_m56E = 0;
    v_stack_m500 = 0;
    *(unsigned int *)(a12) = 0xFFFFFFFFULL;
    v_stack_m4C0 = 0;
    v_stack_m478 = 0;
    if (a1 == 0) goto loc_002FF497;
    if (v_stack_m518 == 0) goto loc_002FF497;
    v_stack_m4E8 = v_cr8;
    if (((unsigned int)((unsigned int)(a9))) < 4) goto loc_002FF38A;
    if ((*(unsigned int *)(v_stack_m518)) != 0x78747261ULL) goto loc_002FFB93;
    v_stack_m568 = 0;
    v_stack_m564 = 0;
    v_stack_m560 = 0;
    v_stack_m558 = 0;
    v_stack_m550 = 0;
    v_stack_m548 = 0;
    v_stack_m540 = 0;
    v_stack_m53C = 0;
    v_stack_m538 = 0;
    v_stack_m530 = 0;
    v_stack_m528 = 0;
    v_stack_m520 = 0;
    v_stack_m56C = 0;
loc_002FED26:
loc_002FED2D:
    if (4 >= ((unsigned int)((unsigned int)(a9)))) goto loc_002FEE14;
    v_r15 = (4) + (v_stack_m518);
    if (((unsigned int)(*(unsigned __int8 *)(v_r15))) == 252) goto loc_002FEE8C;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r15))))) == 162) goto loc_002FF068;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r15))))) == 142) goto loc_002FF205;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r15))))) != 81) goto loc_002FF39D;
    if (0 == 2) goto loc_002FF892;
loc_002FED7D:
    a4 = (unsigned int)(((unsigned int)(a9)) - (4));
    *(unsigned __int16 *)(v_stack_m568 + 0 + 0 * 4 * 8) = 0;
    *(unsigned __int8 *)(v_stack_m568 + 0 + 0 * 4 * 8 + 4) = 0;
    *(unsigned int *)(v_stack_m568 + 0 + 0 * 4 * 8 + 8) = 0;
    *(unsigned int *)(v_stack_m568 + 0 + 0 * 4 * 8 + 12) = 1;
    *(unsigned __int64 *)(v_stack_m568 + 0 + 0 * 4 * 8 + 16) = 0;
    *(unsigned int *)(v_stack_m568 + 0 + 0 * 4 * 8 + 24) = 0;
    *(unsigned __int64 *)(v_stack_m568 + 0 + 0 * 4 * 8 + 32) = 0;
    if (((unsigned int)(*(unsigned __int8 *)(v_r15))) != 81) goto loc_002FF469;
    if (((unsigned int)(a4 - 1)) < 4) goto loc_002FF27A;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15))) != 16) goto loc_002FF677;
    *(unsigned __int16 *)(v_stack_m568 + 0 + 0 * 4 * 8) = 3;
loc_002FEDEA:
    *(unsigned int *)(v_stack_m568 + 0 + 0 * 4 * 8 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 1)));
    if (((unsigned int)(a4 - 5)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 1))))) goto loc_002FF27A;
    *(unsigned __int64 *)(v_stack_m568 + 0 + 0 * 4 * 8 + 32) = v_r15 + 5;
loc_002FEE09:
    v_r12 = (unsigned int)((0) + 1);
    v_r14 = (unsigned int)((4) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 1)) + 5)));
    goto loc_002FF04F;
loc_002FEE14:
    if (((unsigned int)(v_r15)) != 1) goto loc_002FF650;
    *(unsigned int *)(v_stack_m578) = (unsigned int)((unsigned int)(v_stack_m448));
loc_002FEE28:
    result = (unsigned int)(v_stack_m448);
    if (v_stack_m588 != 0) {
        a1 = v_stack_m4C0;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(v_r15 + 1)) + 5, a4);
    }
    if (v_stack_m587 != 0) {
        a1 = v_stack_m478;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(v_r15 + 1)) + 5, a4);
    }
    if (v_stack_m56E != 0) goto loc_002FF565;
loc_002FEE57:
    if (sign_flag) goto loc_002FF55A;
loc_002FEE5F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(*(unsigned int *)(v_r15 + 1)) + 5, a4);
    v_rsp = (v_rsp) + (0x580ULL);
    return result;
loc_002FEE8C:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)(v_r12)) == 2) goto loc_002FF68F;
loc_002FEE99:
    result = (unsigned int)((0) - ((unsigned int)(v_r14)));
    if (((unsigned int)(result)) < 4) goto loc_002FF27A;
    v_r14 = (unsigned int)((v_r14) + (4));
    result = (unsigned int)((0) - ((unsigned int)(v_r14)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1))))) goto loc_002FF27A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)))) > 0xFFFEULL) goto loc_002FFC00;
    v_rbx = ((unsigned int)((unsigned int)(v_r14))) + (a4);
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(v_r12)) * 1 + 48) = 0;
    result = ((unsigned int)((unsigned int)(v_r12)) * 8) + ((unsigned int)((unsigned int)(v_r12)));
    v_rsi = (v_stack_m4C8) + (result * 8);
    *(unsigned __int16 *)(v_rsi + 2) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)));
    *(unsigned __int16 *)(v_rsi) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)));
    *(unsigned __int64 *)(v_rsi + 8) = v_rbx;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1))) == 0) goto loc_002FF27A;
    if (v_rbx == 0) goto loc_002FF27A;
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_002FEF48;
    result = AuthzBasepMemAlloc((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1))), a2, (unsigned int)(0x61476553ULL), a4);
    *(unsigned __int64 *)(v_rsi + 8) = result;
    if (result == 0) goto loc_002FF45A;
    result = memcpy(result, v_rbx, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)))), a4);
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(v_r12)) * 1 + 48) = 1;
loc_002FEF48:
    v_rsi = (v_stack_m4D8) + (result * 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15))) == 249) goto loc_002FF36C;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15))) == 251) goto loc_002FF98A;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15))) == 250) goto loc_002FF871;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15))) == 252) goto loc_002FF9B1;
    *(unsigned int *)(v_rsi) = 2;
loc_002FEF81:
    *(unsigned __int64 *)(v_stack_m4D0 + result * 8 * 1) = v_stack_m508;
    a1 = 0;
    result = ((unsigned int)((unsigned int)(v_r12)) * 8) + ((unsigned int)((unsigned int)(v_r12)));
    *(unsigned __int64 *)(v_stack_m4B8 + result * 8 + 24) = 0;
    *(unsigned __int64 *)(v_stack_m4B8 + result * 8 + 32) = 0;
    result = AuthzBasepQuerySecurityAttributeAndValues(v_rsi, v_stack_m4D0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)))), a4);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_002FEFF8;
    if ((*(unsigned int *)(v_rsi)) != 2) goto loc_002FEFD0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11573660) + 16)))) & (1)) != 0) goto loc_002FF3F0;
loc_002FEFD0:
    if (v_stack_m4E8 >= 2) goto loc_002FF318;
    if ((*(unsigned int *)(v_rsi)) != 2) goto loc_002FF318;
    a2 = 0;
    *(unsigned int *)(v_rsi) = 7;
    *(unsigned __int64 *)(v_stack_m4D0 + result * 8 * 1) = 0;
    result = AuthzBasepQuerySecurityAttributeAndValues(v_rsi, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)))), a4);
loc_002FEFF8:
    if (sign_flag) goto loc_002FF30C;
    result = ((unsigned int)((unsigned int)(v_r12)) * 4) + ((unsigned int)((unsigned int)(v_r12)));
    *(unsigned __int16 *)(v_rsp + result * 8 * 1 + 80) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m4B8 + result * 8 * 1));
    *(unsigned int *)(v_rsp + result * 8 * 1 + 84) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + result * 8 * 1 + 8)));
    *(unsigned __int64 *)(v_rsp + result * 8 * 1 + 96) = v_rsi;
loc_002FF02C:
    v_r11 = 0;
loc_002FF02F:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_p4C)) + 1);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1)))));
    *(unsigned int *)(v_rsp + result * 8 * 1 + 104) = 0;
    *(unsigned __int64 *)(v_rsp + result * 8 * 1 + 112) = 0;
    *(unsigned int *)(v_rsp + result * 8 * 1 + 88) = 0;
    *(unsigned int *)(v_rsp + result * 8 * 1 + 92) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
loc_002FF04F:
    v_stack_p4C = (unsigned int)(v_r12);
    goto loc_002FF1F6;
loc_002FF068:
    v_r14 = (unsigned int)((v_r14) + 1);
    v_stack_p34 = 0;
loc_002FF073:
    if (0 >= ((unsigned int)(v_r12))) goto loc_002FF0AB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92))) == 0) goto loc_002FF27A;
    result = AuthzBasepSupportSetOperation((unsigned __int8)(result * 8), a2, 0, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
    if ((unsigned __int8)(result) == 0) goto loc_002FF524;
loc_002FF0A6:
    a3 = (unsigned int)((0) + 1);
    goto loc_002FF073;
loc_002FF0AB:
    result = AuthzBasepSupportSetOperation((unsigned __int8)(result * 8), a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
    if ((unsigned __int8)(result) == 0) goto loc_002FF76B;
loc_002FF0BC:
    if (((unsigned int)(v_r12)) == 2) goto loc_002FF27A;
    if (((unsigned int)(v_r12)) != 1) goto loc_002FFC0F;
    if (((unsigned int)((unsigned int)(v_stack_p5C))) == ((unsigned int)(v_r12))) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p60, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
    v_stack_p38 = (unsigned int)(result);
    if (v_stack_p30 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p60 + 24);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
        v_r11 = 0;
        *(unsigned __int64 *)(v_stack_p60 + 24) = 0;
        v_stack_p30 = 0;
    }
    v_rbx = (unsigned int)((unsigned int)(result));
    if (v_stack_p31 != 0) {
        v_rbx = v_stack_m530;
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rbx + 24);
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
        v_r11 = 0;
        *(unsigned __int64 *)(v_rbx + 24) = 0;
        v_stack_p31 = 0;
    }
    v_stack_m530 = 0;
loc_002FF133:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_002FF7CC;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_002FF3E6;
loc_002FF147:
    if (((unsigned int)((unsigned int)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(unsigned int *)(v_stack_m4B8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p3C))) * 4 + 112) = 0;
loc_002FF15B:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p3C)) + 1);
    v_stack_p58 = 0;
    v_stack_p54 = 0;
    v_stack_p50 = 0;
    v_stack_p3C = (unsigned int)(v_r15);
    result = (unsigned int)((unsigned int)((unsigned int)(v_stack_p3C)));
    if (v_stack_p30 != 0) {
        a1 = *(unsigned __int64 *)(0 + 24);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
        v_r11 = 0;
        *(unsigned __int64 *)(0 + 24) = 0;
        v_stack_p30 = 0;
    }
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    v_stack_p70 = 0;
    v_stack_p78 = 0;
    v_stack_p7C = 0;
    v_stack_m538 = 0;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (v_stack_p31 != 0) {
        v_rdi = v_stack_m530;
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rdi + 24);
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
        v_r11 = 0;
        *(unsigned __int64 *)(v_rdi + 24) = 0;
        v_stack_p31 = 0;
    }
    v_stack_m530 = 0;
    v_stack_m528 = 0;
    v_stack_m520 = 0;
    v_stack_p4C = 0;
loc_002FF1F6:
    goto loc_002FED26;
loc_002FF205:
    v_r14 = (unsigned int)((v_r14) + 1);
    v_stack_p34 = 0;
loc_002FF210:
    if (0 >= 0) goto loc_002FF289;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92))) == 0) goto loc_002FF27A;
    result = AuthzBasepSupportSetOperation((unsigned __int8)(v_rdi), (unsigned int)(a9), a3, 0);
    if ((unsigned __int8)(result) == 0) goto loc_002FF53F;
loc_002FF23F:
    a4 = (unsigned int)((0) + 1);
    goto loc_002FF210;
loc_002FF244:
    a3 = (unsigned int)((a3) + (-128));
    if (((unsigned int)(a3)) > 33) goto loc_002FF2C3;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3142229 + *(unsigned __int8 *)(v_rip - 3142229 + (int)((unsigned int)(a3)) * 1 + 274726) * 4 + 274706))) + (v_rip - 3142229);
loc_002FF27A:
loc_002FF27F:
    goto loc_002FEE28;
loc_002FF289:
    result = AuthzBasepSupportSetOperation((unsigned __int8)(v_rdi), v_rip - 3142229, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FF77A;
loc_002FF29A:
    if (((unsigned int)(a3)) != 163) goto loc_002FF244;
    if (0 == 1) goto loc_002FF27A;
    if (0 != 2) goto loc_002FF27A;
    if (((unsigned __int8)(v_rdi)) == 136) goto loc_002FFD0C;
    if (((unsigned __int8)(v_rdi)) == 143) goto loc_002FFD0C;
loc_002FF2C3:
    result = AuthzBasepEvaluateExpression((unsigned __int8)(v_rdi), v_stack_p50, v_stack_p38, a4);
    v_rdi = (unsigned __int8)((v_rdi) + (114));
    if (((unsigned __int8)(v_rdi)) <= 1) goto loc_002FFD26;
loc_002FF2ED:
    v_r11 = 0;
loc_002FF2F0:
    if (((unsigned int)((unsigned int)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(unsigned int *)(v_stack_m4B8 + (unsigned int)(v_stack_p3C) * 4 + 112) = (unsigned int)((unsigned int)(v_stack_p38));
    goto loc_002FF15B;
loc_002FF30C:
    if (((unsigned int)((unsigned int)(0xC00001A2ULL))) != 0xC0000225ULL) goto loc_002FF27F;
loc_002FF318:
    v_r11 = 0;
    result = (0 * 4) + (0);
    *(unsigned __int16 *)(v_rsp + result * 8 * 1 + 80) = 0;
    *(unsigned int *)(v_rsp + result * 8 * 1 + 84) = 0;
    *(unsigned __int64 *)(v_rsp + result * 8 * 1 + 96) = 0;
    if ((*(unsigned __int8 *)(v_rsp + 0 * 1 + 48)) == 0) goto loc_002FF02F;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m4B8 + 0 * 1 - 8), a2, v_stack_p38, a4);
    if (0 >= 2) goto loc_002FF9AB;
    *(unsigned __int8 *)(v_rsp + 0 * 1 + 48) = 0;
    goto loc_002FF02C;
loc_002FF36C:
    if (a11 == 0) { a5 = v_stack_m4F8; }
    *(unsigned int *)(v_stack_p60) = 3;
    goto loc_002FEF81;
loc_002FF38A:
    *(unsigned int *)(result * 8) = 1;
loc_002FF395:
    goto loc_002FEE28;
loc_002FF39D:
    if (((unsigned int)(v_stack_p38)) > 251) goto loc_002FF27A;
    a1 = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)) + *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)) + result * 8 * 1 + 274800) * 4 + 274760))) + ((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)));
loc_002FF3E6:
    goto loc_002FF147;
loc_002FF3F0:
    if (((*(unsigned int *)(v_stack_m510 + 200)) & (0x20000ULL)) != 0) goto loc_002FEFD0;
    a1 = (v_stack_m4C8) + (0);
    result = SepPotentialGlobalTableAttribute(a1, a2, v_stack_p38, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FEFD0;
    if (v_stack_p4B != 0) goto loc_002FEFD0;
    if (v_stack_p4A != 0) goto loc_002FFD4A;
    result = SepValidateAndCopyGlobalEntry(v_stack_m508, v_stack_m500, v_stack_p38, a4);
    if (!sign_flag) goto loc_002FFD45;
    v_stack_p4B = 1;
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_002FEFD0;
    goto loc_002FF30C;
loc_002FF45A:
    goto loc_002FEE28;
loc_002FF469:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)) - 1)) > 79) goto loc_002FEE09;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3142781 + *(unsigned __int8 *)(v_rip - 3142781 + (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)) - 1 * 1 + 275064) * 4 + 275052))) + (v_rip - 3142781);
loc_002FF497:
    goto loc_002FF395;
loc_002FF524:
    if (((unsigned int)(a4)) == 1) goto loc_002FF0A6;
    if ((*(unsigned int *)(v_rsp + (unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)) * 1 + 84)) <= 1) goto loc_002FF0A6;
    goto loc_002FF27A;
loc_002FF53F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)))) == 1) goto loc_002FF23F;
    if ((*(unsigned int *)(v_rsp + v_r11 * 1 + 84)) <= 1) goto loc_002FF23F;
    goto loc_002FFC62;
loc_002FF55A:
    *(unsigned int *)(v_stack_p40) = 0xFFFFFFFFULL;
    goto loc_002FEE5F;
loc_002FF565:
    if (v_stack_m500 == 0) goto loc_002FEE57;
    result = AuthzBasepFreeSecurityAttributesList(v_stack_m500, v_stack_m500, v_stack_p38, a4);
    result = ExFreePoolWithTag(v_stack_m500, (unsigned int)(0x74416553ULL), v_stack_p38, a4);
    goto loc_002FEE57;
loc_002FF650:
    if ((unsigned int)((unsigned int)(v_stack_p3C)) != 0) goto loc_002FF27F;
    if (0 != 1) goto loc_002FF27F;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (unsigned int)(0x74416553ULL), v_stack_p38, a4);
    *(unsigned int *)(v_stack_p40) = (unsigned int)(result);
    goto loc_002FEE28;
loc_002FF677:
    *(unsigned __int16 *)((unsigned int)(0x74416553ULL)) = 16;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp + 0 + 0 * 4 * 8 * 1 + 92)))) != 80) goto loc_002FEDEA;
    *(unsigned __int8 *)((unsigned int)(0x74416553ULL) + 4) = (unsigned __int8)(v_stack_p38);
    goto loc_002FEDEA;
loc_002FF68F:
    if (0 == 1) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (unsigned int)(0x74416553ULL), v_stack_p38, a4);
    v_stack_p38 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(unsigned int *)(v_stack_m4B8 + (unsigned int)(v_stack_p3C) * 4 + 112) = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)(v_stack_p3C)) + 1);
    v_stack_p3C = (unsigned int)(a2);
    if (v_stack_p30 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p40 + 24);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_p38, a4);
    }
    a2 = 0;
    v_stack_m4D8 = v_xmm0;
    v_stack_m4C8 = v_xmm1;
    v_stack_m4B8 = v_xmm0;
    v_stack_m498 = v_xmm0;
    v_stack_m4A8 = v_xmm1;
    v_stack_p60 = v_xmm0;
    v_stack_p60 = v_stack_m4D8;
    v_stack_p30 = (unsigned __int8)(v_stack_p31);
    result = 0;
    v_stack_p50 = v_xmm1;
    v_stack_p70 = v_xmm1;
    v_stack_p31 = 0;
    v_stack_p78 = v_xmm0;
    v_stack_m520 = 0;
    v_stack_m530 = v_xmm0;
    result = memset(v_stack_m490, a2, result + 72, a4);
    v_stack_p4C = 1;
    goto loc_002FEE99;
loc_002FF76B:
    if (1 == 2) goto loc_002FF27A;
    goto loc_002FF0BC;
loc_002FF77A:
    if (1 != 2) goto loc_002FF29A;
    if (((v_stack_p50) & ((unsigned __int16)((unsigned int)(0xFFFBULL)))) == 0) goto loc_002FF29A;
    if (v_stack_m534 != 1) goto loc_002FF29A;
    if (v_stack_p7C != 0) goto loc_002FF27A;
    goto loc_002FF29A;
loc_002FF7CC:
    goto loc_002FF147;
loc_002FF871:
    *(unsigned int *)(v_stack_p40) = 4;
    goto loc_002FEF81;
loc_002FF892:
    if (0 == 1) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (unsigned int)(a9), result + 72, v_stack_m518);
    v_stack_p38 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(unsigned int *)(v_stack_m4B8 + (unsigned int)(v_stack_p3C) * 4 + 112) = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)(v_stack_p3C)) + 1);
    v_stack_p3C = (unsigned int)(a2);
    if (v_stack_p30 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p40 + 24);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, result + 72, v_stack_m518);
    }
    a2 = 0;
    v_stack_m4D8 = v_xmm0;
    v_stack_m4C8 = v_xmm1;
    v_stack_m4B8 = v_xmm0;
    v_stack_m498 = v_xmm0;
    v_stack_m4A8 = v_xmm1;
    v_stack_p60 = v_xmm0;
    v_stack_p60 = v_stack_m4D8;
    v_stack_p30 = (unsigned __int8)(v_stack_p31);
    result = 0;
    v_stack_p50 = v_xmm1;
    v_stack_p70 = v_xmm1;
    v_stack_p31 = 0;
    v_stack_p78 = v_xmm0;
    v_stack_m520 = 0;
    v_stack_m530 = v_xmm0;
    result = memset(v_stack_m490, a2, result + 72, v_stack_m518);
    v_r11 = 0;
    goto loc_002FED7D;
loc_002FF98A:
    if (a11 == 0) { a7 = a6; }
    *(unsigned int *)(v_stack_p40) = 5;
    goto loc_002FEF81;
loc_002FF9AB:
    result = _report_rangecheckfailure(v_stack_m490, a2, result + 72, v_stack_m518);
loc_002FF9B1:
    *(unsigned int *)(v_stack_p40) = 6;
    goto loc_002FEF81;
loc_002FFB93:
    *(unsigned int *)(v_stack_m500) = 1;
    goto loc_002FEE28;
loc_002FFC00:
    goto loc_002FEE28;
loc_002FFC0F:
    if (((unsigned int)((unsigned int)(v_stack_p3C))) < 1) goto loc_002FF27A;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p3C)) - 1);
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + v_r15 * 4 + 112)));
    goto loc_002FF133;
loc_002FFC62:
    v_stack_p34 = 1;
    v_stack_p38 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    goto loc_002FF2ED;
loc_002FFD0C:
    if (v_stack_m534 != 1) goto loc_002FF2C3;
    if (v_stack_p7C == 0) goto loc_002FF27A;
    goto loc_002FF2C3;
loc_002FFD26:
    v_r11 = 0;
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == -1) goto loc_002FF2F0;
    result = ((unsigned int)((unsigned int)(0xFFFFFFFFULL)) == 0) ? 1 : 0;
    v_stack_p38 = (unsigned int)(result);
    goto loc_002FF2F0;
loc_002FFD45:
    v_stack_p4A = 1;
loc_002FFD4A:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + v_r15 * 4 + 112))) = v_stack_m500;
    result = AuthzBasepQuerySecurityAttributeAndValues(v_stack_p40, a2, result + 72, v_stack_m518);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_002FEFF8;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + v_r15 * 4 + 112))) = v_stack_m508;
    goto loc_002FEFD0;
loc_002FFD72:
    goto loc_002FEE28;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepEvaluateAceCondition(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, void *Arg9, uint64_t Arg10, uint8_t Arg11, void *Arg12)
{
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg12 = (uint8_t *)Arg12;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m448;
    uint64_t v_stack_m450;
    uint64_t v_stack_m460;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m490;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint32_t v_stack_m4D8;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F0;
    uint64_t v_stack_m4F8;
    uint64_t v_stack_m500;
    uint64_t v_stack_m508;
    uint64_t v_stack_m510;
    uint64_t v_stack_m518;
    uint64_t v_stack_m520;
    uint32_t v_stack_m528;
    uint64_t v_stack_m530;
    uint32_t v_stack_m534;
    uint64_t v_stack_m538;
    uint8_t v_stack_m53C;
    uint16_t v_stack_m540;
    uint64_t v_stack_m548;
    uint32_t v_stack_m550;
    uint64_t v_stack_m558;
    uint64_t v_stack_m560;
    uint8_t v_stack_m561;
    uint16_t v_stack_m563;
    uint8_t v_stack_m564;
    uint16_t v_stack_m568;
    uint32_t v_stack_m56C;
    uint8_t v_stack_m56D;
    uint8_t v_stack_m56E;
    uint8_t v_stack_m56F;
    uint8_t v_stack_m570;
    uint64_t v_stack_m578;
    uint32_t v_stack_m57C;
    uint32_t v_stack_m580;
    uint8_t v_stack_m584;
    uint8_t v_stack_m587;
    uint16_t v_stack_m588;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint8_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint8_t v_stack_p49;
    uint8_t v_stack_p4A;
    uint8_t v_stack_p4B;
    uint32_t v_stack_p4C;
    uint16_t v_stack_p50;
    uint8_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint16_t v_stack_p78;
    uint8_t v_stack_p7C;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (0x580ULL);
    result = (*(uint64_t *)(v_rip + 0xB0BB4A)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m518 = Arg8;
    result = 0;
    v_stack_m4F0 = Arg3;
    v_stack_m508 = Arg2;
    v_stack_m510 = Arg1;
    Arg2 = 0;
    v_stack_m57C = 0;
    v_stack_m4D8 = 0;
    v_stack_m4D0 = 0;
    v_stack_m4F8 = Arg4;
    v_stack_m578 = Arg12;
    result = memset(v_stack_m4C8, Arg2, 128, Arg4);
    result = 0;
    Arg2 = 0;
    v_stack_m563 = 0;
    v_stack_m561 = 0;
    result = memset(v_stack_m560, Arg2, result + 72, Arg4);
    result = 0;
    v_stack_m580 = 0xFFFFFFFFULL;
    local_r11 = 0;
    v_stack_m588 = 0;
    v_stack_m56F = 0;
    v_stack_m570 = 0;
    v_stack_m584 = 0;
    v_stack_m56D = 0;
    v_stack_m56E = 0;
    v_stack_m500 = 0;
    *(uint32_t *)(arg12) = 0xFFFFFFFFULL;
    v_stack_m4C0 = 0;
    v_stack_m478 = 0;
    if (Arg1 == 0) goto loc_002FF497;
    if (v_stack_m518 == 0) goto loc_002FF497;
    v_stack_m4E8 = v_cr8;
    if (((uint32_t)((uint32_t)(Arg9))) < 4) goto loc_002FF38A;
    if ((*(uint32_t *)(v_stack_m518)) != 0x78747261ULL) goto loc_002FFB93;
    v_stack_m568 = 0;
    v_stack_m564 = 0;
    v_stack_m560 = 0;
    v_stack_m558 = 0;
    v_stack_m550 = 0;
    v_stack_m548 = 0;
    v_stack_m540 = 0;
    v_stack_m53C = 0;
    v_stack_m538 = 0;
    v_stack_m530 = 0;
    v_stack_m528 = 0;
    v_stack_m520 = 0;
    v_stack_m56C = 0;
loc_002FED26:
loc_002FED2D:
    if (4 >= ((uint32_t)((uint32_t)(Arg9)))) goto loc_002FEE14;
    local_r15 = (4) + (v_stack_m518);
    if (((uint32_t)(*(uint8_t *)(local_r15))) == 252) goto loc_002FEE8C;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r15))))) == 162) goto loc_002FF068;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r15))))) == 142) goto loc_002FF205;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r15))))) != 81) goto loc_002FF39D;
    if (0 == 2) goto loc_002FF892;
loc_002FED7D:
    Arg4 = (uint32_t)(((uint32_t)(Arg9)) - (4));
    *(uint16_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8) = 0;
    *(uint8_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x4) = 0;
    *(uint32_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x8) = 0;
    *(uint32_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0xC) = 1;
    *(uint64_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x10) = 0;
    *(uint32_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x18) = 0;
    *(uint64_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x20) = 0;
    if (((uint32_t)(*(uint8_t *)(local_r15))) != 81) goto loc_002FF469;
    if (((uint32_t)(Arg4 - 1)) < 4) goto loc_002FF27A;
    if (((uint8_t)(*(uint8_t *)(local_r15))) != 16) goto loc_002FF677;
    *(uint16_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8) = 3;
loc_002FEDEA:
    *(uint32_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x1)));
    if (((uint32_t)(Arg4 - 5)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x1))))) goto loc_002FF27A;
    *(uint64_t *)(v_stack_m568 + 0x0 + 0x0 * 4 * 8 + 0x20) = local_r15 + 5;
loc_002FEE09:
    local_r12 = (uint32_t)((0) + 1);
    local_r14 = (uint32_t)((4) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x1)) + 5)));
    goto loc_002FF04F;
loc_002FEE14:
    if (((uint32_t)(local_r15)) != 1) goto loc_002FF650;
    *(uint32_t *)(v_stack_m578) = (uint32_t)((uint32_t)(v_stack_m448));
loc_002FEE28:
    result = (uint32_t)(v_stack_m448);
    if (v_stack_m588 != 0) {
        Arg1 = v_stack_m4C0;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_r15 + 0x1)) + 5, Arg4);
    }
    if (v_stack_m587 != 0) {
        Arg1 = v_stack_m478;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_r15 + 0x1)) + 5, Arg4);
    }
    if (v_stack_m56E != 0) goto loc_002FF565;
loc_002FEE57:
    if (sign_flag) goto loc_002FF55A;
loc_002FEE5F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_r15 + 0x1)) + 5, Arg4);
    local_rsp = (local_rsp) + (0x580ULL);
    return result;
loc_002FEE8C:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)(local_r12)) == 2) goto loc_002FF68F;
loc_002FEE99:
    result = (uint32_t)((0) - ((uint32_t)(local_r14)));
    if (((uint32_t)(result)) < 4) goto loc_002FF27A;
    local_r14 = (uint32_t)((local_r14) + (4));
    result = (uint32_t)((0) - ((uint32_t)(local_r14)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1))))) goto loc_002FF27A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)))) > 0xFFFEULL) goto loc_002FFC00;
    local_rbx = ((uint32_t)((uint32_t)(local_r14))) + (Arg4);
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(local_r12)) * 1 + 0x30) = 0;
    result = ((uint32_t)((uint32_t)(local_r12)) * 8) + ((uint32_t)((uint32_t)(local_r12)));
    local_rsi = (v_stack_m4C8) + (result * 8);
    *(uint16_t *)(local_rsi + 0x2) = (uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)));
    *(uint16_t *)(local_rsi) = (uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)));
    *(uint64_t *)(local_rsi + 0x8) = local_rbx;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1))) == 0) goto loc_002FF27A;
    if (local_rbx == 0) goto loc_002FF27A;
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_002FEF48;
    result = AuthzBasepMemAlloc((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1))), Arg2, (uint32_t)(0x61476553ULL), Arg4);
    *(uint64_t *)(local_rsi + 0x8) = result;
    if (result == 0) goto loc_002FF45A;
    result = memcpy(result, local_rbx, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)))), Arg4);
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(local_r12)) * 1 + 0x30) = 1;
loc_002FEF48:
    local_rsi = (v_stack_m4D8) + (result * 8);
    if (((uint8_t)(*(uint8_t *)(local_r15))) == 249) goto loc_002FF36C;
    if (((uint8_t)(*(uint8_t *)(local_r15))) == 251) goto loc_002FF98A;
    if (((uint8_t)(*(uint8_t *)(local_r15))) == 250) goto loc_002FF871;
    if (((uint8_t)(*(uint8_t *)(local_r15))) == 252) goto loc_002FF9B1;
    *(uint32_t *)(local_rsi) = 2;
loc_002FEF81:
    *(uint64_t *)(v_stack_m4D0 + result * 8 * 1) = v_stack_m508;
    Arg1 = 0;
    result = ((uint32_t)((uint32_t)(local_r12)) * 8) + ((uint32_t)((uint32_t)(local_r12)));
    *(uint64_t *)(v_stack_m4B8 + result * 8 + 0x18) = 0;
    *(uint64_t *)(v_stack_m4B8 + result * 8 + 0x20) = 0;
    result = AuthzBasepQuerySecurityAttributeAndValues(local_rsi, v_stack_m4D0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)))), Arg4);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_002FEFF8;
    if ((*(uint32_t *)(local_rsi)) != 2) goto loc_002FEFD0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB0999C) + 0x10)))) & (1)) != 0) goto loc_002FF3F0;
loc_002FEFD0:
    if (v_stack_m4E8 >= 2) goto loc_002FF318;
    if ((*(uint32_t *)(local_rsi)) != 2) goto loc_002FF318;
    Arg2 = 0;
    *(uint32_t *)(local_rsi) = 7;
    *(uint64_t *)(v_stack_m4D0 + result * 8 * 1) = 0;
    result = AuthzBasepQuerySecurityAttributeAndValues(local_rsi, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)))), Arg4);
loc_002FEFF8:
    if (sign_flag) goto loc_002FF30C;
    result = ((uint32_t)((uint32_t)(local_r12)) * 4) + ((uint32_t)((uint32_t)(local_r12)));
    *(uint16_t *)(local_rsp + result * 8 * 1 + 0x50) = (uint16_t)(*(uint16_t *)(v_stack_m4B8 + result * 8 * 1));
    *(uint32_t *)(local_rsp + result * 8 * 1 + 0x54) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + result * 8 * 1 + 0x8)));
    *(uint64_t *)(local_rsp + result * 8 * 1 + 0x60) = local_rsi;
loc_002FF02C:
    local_r11 = 0;
loc_002FF02F:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_p4C)) + 1);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1)))));
    *(uint32_t *)(local_rsp + result * 8 * 1 + 0x68) = 0;
    *(uint64_t *)(local_rsp + result * 8 * 1 + 0x70) = 0;
    *(uint32_t *)(local_rsp + result * 8 * 1 + 0x58) = 0;
    *(uint32_t *)(local_rsp + result * 8 * 1 + 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
loc_002FF04F:
    v_stack_p4C = (uint32_t)(local_r12);
    goto loc_002FF1F6;
loc_002FF068:
    local_r14 = (uint32_t)((local_r14) + 1);
    v_stack_p34 = 0;
loc_002FF073:
    if (0 >= ((uint32_t)(local_r12))) goto loc_002FF0AB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C))) == 0) goto loc_002FF27A;
    result = AuthzBasepSupportSetOperation((uint8_t)(result * 8), Arg2, 0, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
    if ((uint8_t)(result) == 0) goto loc_002FF524;
loc_002FF0A6:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_002FF073;
loc_002FF0AB:
    result = AuthzBasepSupportSetOperation((uint8_t)(result * 8), Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
    if ((uint8_t)(result) == 0) goto loc_002FF76B;
loc_002FF0BC:
    if (((uint32_t)(local_r12)) == 2) goto loc_002FF27A;
    if (((uint32_t)(local_r12)) != 1) goto loc_002FFC0F;
    if (((uint32_t)((uint32_t)(v_stack_p5C))) == ((uint32_t)(local_r12))) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p60, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
    v_stack_p38 = (uint32_t)(result);
    if (v_stack_p30 != 0) {
        Arg1 = *(uint64_t *)(v_stack_p60 + 0x18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
        local_r11 = 0;
        *(uint64_t *)(v_stack_p60 + 0x18) = 0;
        v_stack_p30 = 0;
    }
    local_rbx = (uint32_t)((uint32_t)(result));
    if (v_stack_p31 != 0) {
        local_rbx = v_stack_m530;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rbx + 0x18);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
        local_r11 = 0;
        *(uint64_t *)(local_rbx + 0x18) = 0;
        v_stack_p31 = 0;
    }
    v_stack_m530 = 0;
loc_002FF133:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_002FF7CC;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_002FF3E6;
loc_002FF147:
    if (((uint32_t)((uint32_t)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(uint32_t *)(v_stack_m4B8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p3C))) * 4 + 0x70) = 0;
loc_002FF15B:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p3C)) + 1);
    v_stack_p58 = 0;
    v_stack_p54 = 0;
    v_stack_p50 = 0;
    v_stack_p3C = (uint32_t)(local_r15);
    result = (uint32_t)((uint32_t)((uint32_t)(v_stack_p3C)));
    if (v_stack_p30 != 0) {
        Arg1 = *(uint64_t *)(0 + 0x18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
        local_r11 = 0;
        *(uint64_t *)(0 + 0x18) = 0;
        v_stack_p30 = 0;
    }
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    v_stack_p70 = 0;
    v_stack_p78 = 0;
    v_stack_p7C = 0;
    v_stack_m538 = 0;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (v_stack_p31 != 0) {
        local_rdi = v_stack_m530;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rdi + 0x18);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
        local_r11 = 0;
        *(uint64_t *)(local_rdi + 0x18) = 0;
        v_stack_p31 = 0;
    }
    v_stack_m530 = 0;
    v_stack_m528 = 0;
    v_stack_m520 = 0;
    v_stack_p4C = 0;
loc_002FF1F6:
    goto loc_002FED26;
loc_002FF205:
    local_r14 = (uint32_t)((local_r14) + 1);
    v_stack_p34 = 0;
loc_002FF210:
    if (0 >= 0) goto loc_002FF289;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C))) == 0) goto loc_002FF27A;
    result = AuthzBasepSupportSetOperation((uint8_t)(local_rdi), (uint32_t)(Arg9), Arg3, 0);
    if ((uint8_t)(result) == 0) goto loc_002FF53F;
loc_002FF23F:
    Arg4 = (uint32_t)((0) + 1);
    goto loc_002FF210;
loc_002FF244:
    Arg3 = (uint32_t)((Arg3) + (-128));
    if (((uint32_t)(Arg3)) > 33) goto loc_002FF2C3;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x2FF255 + *(uint8_t *)(v_rip - 0x2FF255 + (int32_t)((uint32_t)(Arg3)) * 1 + 0x43126) * 4 + 0x43112))) + (v_rip - 3142229);
loc_002FF27A:
loc_002FF27F:
    goto loc_002FEE28;
loc_002FF289:
    result = AuthzBasepSupportSetOperation((uint8_t)(local_rdi), v_rip - 3142229, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FF77A;
loc_002FF29A:
    if (((uint32_t)(Arg3)) != 163) goto loc_002FF244;
    if (0 == 1) goto loc_002FF27A;
    if (0 != 2) goto loc_002FF27A;
    if (((uint8_t)(local_rdi)) == 136) goto loc_002FFD0C;
    if (((uint8_t)(local_rdi)) == 143) goto loc_002FFD0C;
loc_002FF2C3:
    result = AuthzBasepEvaluateExpression((uint8_t)(local_rdi), v_stack_p50, v_stack_p38, Arg4);
    local_rdi = (uint8_t)((local_rdi) + (114));
    if (((uint8_t)(local_rdi)) <= 1) goto loc_002FFD26;
loc_002FF2ED:
    local_r11 = 0;
loc_002FF2F0:
    if (((uint32_t)((uint32_t)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(uint32_t *)(v_stack_m4B8 + (uint32_t)(v_stack_p3C) * 4 + 0x70) = (uint32_t)((uint32_t)(v_stack_p38));
    goto loc_002FF15B;
loc_002FF30C:
    if (((uint32_t)((uint32_t)(0xC00001A2ULL))) != 0xC0000225ULL) goto loc_002FF27F;
loc_002FF318:
    local_r11 = 0;
    result = (0 * 4) + (0);
    *(uint16_t *)(local_rsp + result * 8 * 1 + 0x50) = 0;
    *(uint32_t *)(local_rsp + result * 8 * 1 + 0x54) = 0;
    *(uint64_t *)(local_rsp + result * 8 * 1 + 0x60) = 0;
    if ((*(uint8_t *)(local_rsp + 0x0 * 1 + 0x30)) == 0) goto loc_002FF02F;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m4B8 + 0x0 * 1 - 0x8), Arg2, v_stack_p38, Arg4);
    if (0 >= 2) goto loc_002FF9AB;
    *(uint8_t *)(local_rsp + 0x0 * 1 + 0x30) = 0;
    goto loc_002FF02C;
loc_002FF36C:
    if (Arg11 == 0) { Arg5 = v_stack_m4F8; }
    *(uint32_t *)(v_stack_p60) = 3;
    goto loc_002FEF81;
loc_002FF38A:
    *(uint32_t *)(result * 8) = 1;
loc_002FF395:
    goto loc_002FEE28;
loc_002FF39D:
    if (((uint32_t)(v_stack_p38)) > 251) goto loc_002FF27A;
    Arg1 = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)) + *(uint8_t *)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)) + result * 8 * 1 + 0x43170) * 4 + 0x43148))) + ((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)));
loc_002FF3E6:
    goto loc_002FF147;
loc_002FF3F0:
    if (((*(uint32_t *)(v_stack_m510 + 0xC8)) & (0x20000ULL)) != 0) goto loc_002FEFD0;
    Arg1 = (v_stack_m4C8) + (0);
    result = SepPotentialGlobalTableAttribute(Arg1, Arg2, v_stack_p38, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FEFD0;
    if (v_stack_p4B != 0) goto loc_002FEFD0;
    if (v_stack_p4A != 0) goto loc_002FFD4A;
    result = SepValidateAndCopyGlobalEntry(v_stack_m508, v_stack_m500, v_stack_p38, Arg4);
    if (!sign_flag) goto loc_002FFD45;
    v_stack_p4B = 1;
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_002FEFD0;
    goto loc_002FF30C;
loc_002FF45A:
    goto loc_002FEE28;
loc_002FF469:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)) - 1)) > 79) goto loc_002FEE09;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x2FF47D + *(uint8_t *)(v_rip - 0x2FF47D + (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)) - 0x1 * 1 + 0x43278) * 4 + 0x4326C))) + (v_rip - 3142781);
loc_002FF497:
    goto loc_002FF395;
loc_002FF524:
    if (((uint32_t)(Arg4)) == 1) goto loc_002FF0A6;
    if ((*(uint32_t *)(local_rsp + (uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)) * 1 + 0x54)) <= 1) goto loc_002FF0A6;
    goto loc_002FF27A;
loc_002FF53F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)))) == 1) goto loc_002FF23F;
    if ((*(uint32_t *)(local_rsp + local_r11 * 1 + 0x54)) <= 1) goto loc_002FF23F;
    goto loc_002FFC62;
loc_002FF55A:
    *(uint32_t *)(v_stack_p40) = 0xFFFFFFFFULL;
    goto loc_002FEE5F;
loc_002FF565:
    if (v_stack_m500 == 0) goto loc_002FEE57;
    result = AuthzBasepFreeSecurityAttributesList(v_stack_m500, v_stack_m500, v_stack_p38, Arg4);
    result = ExFreePoolWithTag(v_stack_m500, (uint32_t)(0x74416553ULL), v_stack_p38, Arg4);
    goto loc_002FEE57;
loc_002FF650:
    if ((uint32_t)((uint32_t)(v_stack_p3C)) != 0) goto loc_002FF27F;
    if (0 != 1) goto loc_002FF27F;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (uint32_t)(0x74416553ULL), v_stack_p38, Arg4);
    *(uint32_t *)(v_stack_p40) = (uint32_t)(result);
    goto loc_002FEE28;
loc_002FF677:
    *(uint16_t *)((uint32_t)(0x74416553ULL)) = 16;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 + 0x0 * 4 * 8 * 1 + 0x5C)))) != 80) goto loc_002FEDEA;
    *(uint8_t *)((uint32_t)(0x74416553ULL) + 0x4) = (uint8_t)(v_stack_p38);
    goto loc_002FEDEA;
loc_002FF68F:
    if (0 == 1) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (uint32_t)(0x74416553ULL), v_stack_p38, Arg4);
    v_stack_p38 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(uint32_t *)(v_stack_m4B8 + (uint32_t)(v_stack_p3C) * 4 + 0x70) = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p3C)) + 1);
    v_stack_p3C = (uint32_t)(Arg2);
    if (v_stack_p30 != 0) {
        Arg1 = *(uint64_t *)(v_stack_p40 + 0x18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p38, Arg4);
    }
    Arg2 = 0;
    v_stack_m4D8 = v_xmm0;
    v_stack_m4C8 = v_xmm1;
    v_stack_m4B8 = v_xmm0;
    v_stack_m498 = v_xmm0;
    v_stack_m4A8 = v_xmm1;
    v_stack_p60 = v_xmm0;
    v_stack_p60 = v_stack_m4D8;
    v_stack_p30 = (uint8_t)(v_stack_p31);
    result = 0;
    v_stack_p50 = v_xmm1;
    v_stack_p70 = v_xmm1;
    v_stack_p31 = 0;
    v_stack_p78 = v_xmm0;
    v_stack_m520 = 0;
    v_stack_m530 = v_xmm0;
    result = memset(v_stack_m490, Arg2, result + 72, Arg4);
    v_stack_p4C = 1;
    goto loc_002FEE99;
loc_002FF76B:
    if (1 == 2) goto loc_002FF27A;
    goto loc_002FF0BC;
loc_002FF77A:
    if (1 != 2) goto loc_002FF29A;
    if (((v_stack_p50) & ((uint16_t)((uint32_t)(0xFFFBULL)))) == 0) goto loc_002FF29A;
    if (v_stack_m534 != 1) goto loc_002FF29A;
    if (v_stack_p7C != 0) goto loc_002FF27A;
    goto loc_002FF29A;
loc_002FF7CC:
    goto loc_002FF147;
loc_002FF871:
    *(uint32_t *)(v_stack_p40) = 4;
    goto loc_002FEF81;
loc_002FF892:
    if (0 == 1) goto loc_002FF27A;
    result = AuthzBasepEvaluateAttribute(v_stack_p40, (uint32_t)(Arg9), result + 72, v_stack_m518);
    v_stack_p38 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_p3C))) >= 256) goto loc_002FFD72;
    *(uint32_t *)(v_stack_m4B8 + (uint32_t)(v_stack_p3C) * 4 + 0x70) = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p3C)) + 1);
    v_stack_p3C = (uint32_t)(Arg2);
    if (v_stack_p30 != 0) {
        Arg1 = *(uint64_t *)(v_stack_p40 + 0x18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, result + 72, v_stack_m518);
    }
    Arg2 = 0;
    v_stack_m4D8 = v_xmm0;
    v_stack_m4C8 = v_xmm1;
    v_stack_m4B8 = v_xmm0;
    v_stack_m498 = v_xmm0;
    v_stack_m4A8 = v_xmm1;
    v_stack_p60 = v_xmm0;
    v_stack_p60 = v_stack_m4D8;
    v_stack_p30 = (uint8_t)(v_stack_p31);
    result = 0;
    v_stack_p50 = v_xmm1;
    v_stack_p70 = v_xmm1;
    v_stack_p31 = 0;
    v_stack_p78 = v_xmm0;
    v_stack_m520 = 0;
    v_stack_m530 = v_xmm0;
    result = memset(v_stack_m490, Arg2, result + 72, v_stack_m518);
    local_r11 = 0;
    goto loc_002FED7D;
loc_002FF98A:
    if (Arg11 == 0) { Arg7 = Arg6; }
    *(uint32_t *)(v_stack_p40) = 5;
    goto loc_002FEF81;
loc_002FF9AB:
    result = _report_rangecheckfailure(v_stack_m490, Arg2, result + 72, v_stack_m518);
loc_002FF9B1:
    *(uint32_t *)(v_stack_p40) = 6;
    goto loc_002FEF81;
loc_002FFB93:
    *(uint32_t *)(v_stack_m500) = 1;
    goto loc_002FEE28;
loc_002FFC00:
    goto loc_002FEE28;
loc_002FFC0F:
    if (((uint32_t)((uint32_t)(v_stack_p3C))) < 1) goto loc_002FF27A;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p3C)) - 1);
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + local_r15 * 4 + 0x70)));
    goto loc_002FF133;
loc_002FFC62:
    v_stack_p34 = 1;
    v_stack_p38 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    goto loc_002FF2ED;
loc_002FFD0C:
    if (v_stack_m534 != 1) goto loc_002FF2C3;
    if (v_stack_p7C == 0) goto loc_002FF27A;
    goto loc_002FF2C3;
loc_002FFD26:
    local_r11 = 0;
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == -1) goto loc_002FF2F0;
    result = ((uint32_t)((uint32_t)(0xFFFFFFFFULL)) == 0) ? 1 : 0;
    v_stack_p38 = (uint32_t)(result);
    goto loc_002FF2F0;
loc_002FFD45:
    v_stack_p4A = 1;
loc_002FFD4A:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + local_r15 * 4 + 0x70))) = v_stack_m500;
    result = AuthzBasepQuerySecurityAttributeAndValues(v_stack_p40, Arg2, result + 72, v_stack_m518);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_002FEFF8;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + local_r15 * 4 + 0x70))) = v_stack_m508;
    goto loc_002FEFD0;
loc_002FFD72:
    goto loc_002FEE28;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg9` | `- 0x5` | `32` | `R` |
| `Arg9` | `- 0x1` | `32` | `R` |
| `Arg12` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FEBD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
