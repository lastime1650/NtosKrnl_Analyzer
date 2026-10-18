# PoEnergyContextUpdateComponentPower

- RVA: `0x0098CA08`–`0x0098CF8D` (길이 `1,413` bytes)
- VA: `0x000000014098CA08`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000987D0`
- 디코드: `328`개 명령, `1,413/1,413` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0098CA4E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0098CA69` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x0098CA98` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CACF` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (function, `0x003FFED0`)
- `0x0098CB0C` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (function, `0x003FFED0`)
- `0x0098CB14` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x0098CB24` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0098CB66` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (function, `0x003FFED0`)
- `0x0098CC21` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CCC6` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CCF5` → [PopEtEnergyContextSetState](PopEtEnergyContextSetState_function_0098CF94.md) (function, `0x0098CF94`)
- `0x0098CD53` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (function, `0x00499538`)
- `0x0098CD5B` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CD86` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (function, `0x003FFED0`)
- `0x0098CD8E` → [PopEtEnergyContextProcessStateUpdate](PopEtEnergyContextProcessStateUpdate_function_0098E418.md) (function, `0x0098E418`)
- `0x0098CDC5` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (function, `0x00499538`)
- `0x0098CDCD` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CE05` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CE5B` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (function, `0x00499538`)
- `0x0098CE62` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098CE7D` → [RtlTimelineBitmapUpdateRange](../../text/43/RtlTimelineBitmapUpdateRange_function_00437C30.md) (function, `0x00437C30`)
- `0x0098CEA4` → [RtlTimelineBitmapUpdateRange](../../text/43/RtlTimelineBitmapUpdateRange_function_00437C30.md) (function, `0x00437C30`)
- `0x0098CF29` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (function, `0x00499538`)
- `0x0098CF30` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)

### Direct callers
- [PsUpdateComponentPower](../../text/43/PsUpdateComponentPower_function_00434CF0.md) at `0x00434DC7`
- [PopPowerRequestCallbackDisplayRequired](PopPowerRequestCallbackDisplayRequired_function_0098C820.md) at `0x0098C855`
- [NtSetThreadExecutionState](../AC/NtSetThreadExecutionState_function_00AC0A40.md) at `0x00AC0C50`
- [NtSetThreadExecutionState](../AC/NtSetThreadExecutionState_function_00AC0A40.md) at `0x00AC0CB5`

### Static image references
- `0x0098CA1B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x0098CA4E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0098CA69` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x0098CA98` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CACF` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (`PAGE` → `.text`)
  - `0x0098CB0C` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (`PAGE` → `.text`)
  - `0x0098CB14` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x0098CB24` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0098CB66` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (`PAGE` → `.text`)
  - `0x0098CC21` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CCC6` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CD53` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (`PAGE` → `.text`)
  - `0x0098CD5B` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CD86` → [RtlTimelineBitmapUpdate](../../text/3F/RtlTimelineBitmapUpdate_function_003FFED0.md) (`PAGE` → `.text`)
  - `0x0098CDC5` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (`PAGE` → `.text`)
  - `0x0098CDCD` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CE05` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CE5B` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (`PAGE` → `.text`)
  - `0x0098CE62` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098CE7D` → [RtlTimelineBitmapUpdateRange](../../text/43/RtlTimelineBitmapUpdateRange_function_00437C30.md) (`PAGE` → `.text`)
  - `0x0098CEA4` → [RtlTimelineBitmapUpdateRange](../../text/43/RtlTimelineBitmapUpdateRange_function_00437C30.md) (`PAGE` → `.text`)
  - `0x0098CF29` → [RtlStateDurationUpdate](../../text/49/RtlStateDurationUpdate_function_00499538.md) (`PAGE` → `.text`)
  - `0x0098CF30` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098CA08  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0098CA0D  55                              push rbp
0098CA0E  56                              push rsi
0098CA0F  57                              push rdi
0098CA10  41 56                           push r14
0098CA12  41 57                           push r15
0098CA14  48 81 EC D0 00 00 00            sub rsp, 0xd0
0098CA1B  48 8B 05 1E DD 47 00            mov rax, qword ptr [rip + 0x47dd1e]
0098CA22  48 33 C4                        xor rax, rsp
0098CA25  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0098CA2D  48 8B B9 68 06 00 00            mov rdi, qword ptr [rcx + 0x668]
0098CA34  49 8B F0                        mov rsi, r8
0098CA37  8B DA                           mov ebx, edx
0098CA39  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0098CA3E  48 8B E9                        mov rbp, rcx
0098CA41  33 D2                           xor edx, edx
0098CA43  41 B8 90 00 00 00               mov r8d, 0x90
0098CA49  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0098CA4E  E8 ED A1 D3 FF                  call 0x1406c6c40
0098CA53  45 33 FF                        xor r15d, r15d
0098CA56  48 85 FF                        test rdi, rdi
0098CA59  0F 84 BA 00 00 00               je 0x14098cb19
0098CA5F  4C 8D B7 B8 01 00 00            lea r14, [rdi + 0x1b8]
0098CA66  49 8B CE                        mov rcx, r14
0098CA69  E8 D6 40 AA FF                  call 0x140430b44
0098CA6E  83 FB 0A                        cmp ebx, 0xa
0098CA71  0F 8F F9 00 00 00               jg 0x14098cb70
0098CA77  0F 84 99 03 00 00               je 0x14098ce16
0098CA7D  83 EB 04                        sub ebx, 4
0098CA80  0F 84 A0 02 00 00               je 0x14098cd26
0098CA86  83 EB 01                        sub ebx, 1
0098CA89  0F 84 09 03 00 00               je 0x14098cd98
0098CA8F  83 EB 02                        sub ebx, 2
0098CA92  0F 85 98 01 00 00               jne 0x14098cc30
0098CA98  E8 2F 08 AD FF                  call 0x14045d2cc
0098CA9D  41 83 C9 FF                     or r9d, 0xffffffff
0098CAA1  8B D0                           mov edx, eax
0098CAA3  66 85 F6                        test si, si
0098CAA6  74 2C                           je 0x14098cad4
0098CAA8  44 8B 87 80 00 00 00            mov r8d, dword ptr [rdi + 0x80]
0098CAAF  0F B7 C6                        movzx eax, si
0098CAB2  8B C8                           mov ecx, eax
0098CAB4  F7 D1                           not ecx
0098CAB6  41 3B C8                        cmp ecx, r8d
0098CAB9  0F 82 1A 02 00 00               jb 0x14098ccd9
0098CABF  41 03 C0                        add eax, r8d
0098CAC2  48 8D 8F 40 01 00 00            lea rcx, [rdi + 0x140]
0098CAC9  89 87 80 00 00 00               mov dword ptr [rdi + 0x80], eax
0098CACF  E8 FC 33 A7 FF                  call 0x1403ffed0
0098CAD4  0F B7 44 24 2A                  movzx eax, word ptr [rsp + 0x2a]
0098CAD9  66 85 C0                        test ax, ax
0098CADC  75 63                           jne 0x14098cb41
0098CADE  8B 44 24 2C                     mov eax, dword ptr [rsp + 0x2c]
0098CAE2  66 85 C0                        test ax, ax
0098CAE5  74 2A                           je 0x14098cb11
0098CAE7  44 8B 87 88 00 00 00            mov r8d, dword ptr [rdi + 0x88]
0098CAEE  0F B7 C8                        movzx ecx, ax
0098CAF1  8B C1                           mov eax, ecx
0098CAF3  F7 D0                           not eax
0098CAF5  41 3B C0                        cmp eax, r8d
0098CAF8  72 04                           jb 0x14098cafe
0098CAFA  45 8D 0C 08                     lea r9d, [r8 + rcx]
0098CAFE  44 89 8F 88 00 00 00            mov dword ptr [rdi + 0x88], r9d
0098CB05  48 8D 8F 50 01 00 00            lea rcx, [rdi + 0x150]
0098CB0C  E8 BF 33 A7 FF                  call 0x1403ffed0
0098CB11  49 8B CE                        mov rcx, r14
0098CB14  E8 A3 30 95 FF                  call 0x1402dfbbc
0098CB19  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0098CB21  48 33 CC                        xor rcx, rsp
0098CB24  E8 17 FB D1 FF                  call 0x1406ac640
0098CB29  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
0098CB31  48 81 C4 D0 00 00 00            add rsp, 0xd0
0098CB38  41 5F                           pop r15
0098CB3A  41 5E                           pop r14
0098CB3C  5F                              pop rdi
0098CB3D  5E                              pop rsi
0098CB3E  5D                              pop rbp
0098CB3F  C3                              ret
0098CB40  CC                              int3
0098CB41  44 8B 87 84 00 00 00            mov r8d, dword ptr [rdi + 0x84]
0098CB48  8B C8                           mov ecx, eax
0098CB4A  F7 D0                           not eax
0098CB4C  41 3B C0                        cmp eax, r8d
0098CB4F  41 8D 04 08                     lea eax, [r8 + rcx]
0098CB53  0F 82 C5 01 00 00               jb 0x14098cd1e
0098CB59  48 8D 8F 48 01 00 00            lea rcx, [rdi + 0x148]
0098CB60  89 87 84 00 00 00               mov dword ptr [rdi + 0x84], eax
0098CB66  E8 65 33 A7 FF                  call 0x1403ffed0
0098CB6B  E9 6E FF FF FF                  jmp 0x14098cade
0098CB70  8B CB                           mov ecx, ebx
0098CB72  83 E9 0B                        sub ecx, 0xb
0098CB75  0F 84 9B 02 00 00               je 0x14098ce16
0098CB7B  83 E9 01                        sub ecx, 1
0098CB7E  0F 85 7B 01 00 00               jne 0x14098ccff
0098CB84  48 8D AF 70 01 00 00            lea rbp, [rdi + 0x170]
0098CB8B  4C 8D 9F 98 01 00 00            lea r11, [rdi + 0x198]
0098CB92  83 FE 03                        cmp esi, 3
0098CB95  0F 85 3A 03 00 00               jne 0x14098ced5
0098CB9B  45 39 7B 04                     cmp dword ptr [r11 + 4], r15d
0098CB9F  0F 8C 6C FF FF FF               jl 0x14098cb11
0098CBA5  49 8B 03                        mov rax, qword ptr [r11]
0098CBA8  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CBB2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0098CBB7  41 B8 00 10 00 00               mov r8d, 0x1000
0098CBBD  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CBC7  48 8B 00                        mov rax, qword ptr [rax]
0098CBCA  8B 09                           mov ecx, dword ptr [rcx]
0098CBCC  48 0F AF C8                     imul rcx, rax
0098CBD0  48 C1 E9 18                     shr rcx, 0x18
0098CBD4  8B C1                           mov eax, ecx
0098CBD6  2B 44 24 20                     sub eax, dword ptr [rsp + 0x20]
0098CBDA  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0098CBDE  41 3B C0                        cmp eax, r8d
0098CBE1  0F 86 7F 03 00 00               jbe 0x14098cf66
0098CBE7  44 8B 54 24 24                  mov r10d, dword ptr [rsp + 0x24]
0098CBEC  B9 FF FF FF 7F                  mov ecx, 0x7fffffff
0098CBF1  41 8B D2                        mov edx, r10d
0098CBF4  41 8B C0                        mov eax, r8d
0098CBF7  23 D1                           and edx, ecx
0098CBF9  F7 D0                           not eax
0098CBFB  3B C2                           cmp eax, edx
0098CBFD  0F 82 52 03 00 00               jb 0x14098cf55
0098CC03  46 8D 0C 02                     lea r9d, [rdx + r8]
0098CC07  44 23 C9                        and r9d, ecx
0098CC0A  41 81 E2 00 00 00 80            and r10d, 0x80000000
0098CC11  45 0B CA                        or r9d, r10d
0098CC14  44 89 4C 24 24                  mov dword ptr [rsp + 0x24], r9d
0098CC19  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
0098CC1E  49 89 03                        mov qword ptr [r11], rax
0098CC21  E8 A6 06 AD FF                  call 0x14045d2cc
0098CC26  8B D0                           mov edx, eax
0098CC28  48 8B CD                        mov rcx, rbp
0098CC2B  E9 DC FE FF FF                  jmp 0x14098cb0c
0098CC30  83 EB 01                        sub ebx, 1
0098CC33  0F 84 A8 00 00 00               je 0x14098cce1
0098CC39  83 FB 01                        cmp ebx, 1
0098CC3C  0F 85 CF FE FF FF               jne 0x14098cb11
0098CC42  48 8B 87 80 01 00 00            mov rax, qword ptr [rdi + 0x180]
0098CC49  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CC53  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0098CC58  41 B8 E8 03 00 00               mov r8d, 0x3e8
0098CC5E  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CC68  48 8B 00                        mov rax, qword ptr [rax]
0098CC6B  8B 09                           mov ecx, dword ptr [rcx]
0098CC6D  48 0F AF C8                     imul rcx, rax
0098CC71  48 C1 E9 18                     shr rcx, 0x18
0098CC75  8B C1                           mov eax, ecx
0098CC77  2B 44 24 20                     sub eax, dword ptr [rsp + 0x20]
0098CC7B  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0098CC7F  41 3B C0                        cmp eax, r8d
0098CC82  0F 86 D6 02 00 00               jbe 0x14098cf5e
0098CC88  44 8B 54 24 24                  mov r10d, dword ptr [rsp + 0x24]
0098CC8D  B9 FF FF FF 7F                  mov ecx, 0x7fffffff
0098CC92  41 8B D2                        mov edx, r10d
0098CC95  41 8B C0                        mov eax, r8d
0098CC98  23 D1                           and edx, ecx
0098CC9A  F7 D0                           not eax
0098CC9C  3B C2                           cmp eax, edx
0098CC9E  0F 82 A8 02 00 00               jb 0x14098cf4c
0098CCA4  46 8D 0C 02                     lea r9d, [rdx + r8]
0098CCA8  44 23 C9                        and r9d, ecx
0098CCAB  41 81 E2 00 00 00 80            and r10d, 0x80000000
0098CCB2  45 0B CA                        or r9d, r10d
0098CCB5  44 89 4C 24 24                  mov dword ptr [rsp + 0x24], r9d
0098CCBA  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
0098CCBF  48 89 87 80 01 00 00            mov qword ptr [rdi + 0x180], rax
0098CCC6  E8 01 06 AD FF                  call 0x14045d2cc
0098CCCB  48 8D 8F 58 01 00 00            lea rcx, [rdi + 0x158]
0098CCD2  8B D0                           mov edx, eax
0098CCD4  E9 33 FE FF FF                  jmp 0x14098cb0c
0098CCD9  41 8B C1                        mov eax, r9d
0098CCDC  E9 E1 FD FF FF                  jmp 0x14098cac2
0098CCE1  8B 44 24 2C                     mov eax, dword ptr [rsp + 0x2c]
0098CCE5  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0098CCEA  48 8B CD                        mov rcx, rbp
0098CCED  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0098CCF1  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0098CCF5  E8 9A 02 00 00                  call 0x14098cf94
0098CCFA  E9 12 FE FF FF                  jmp 0x14098cb11
0098CCFF  83 E9 01                        sub ecx, 1
0098CD02  0F 84 F2 00 00 00               je 0x14098cdfa
0098CD08  83 F9 01                        cmp ecx, 1
0098CD0B  0F 85 00 FE FF FF               jne 0x14098cb11
0098CD11  01 8F AC 01 00 00               add dword ptr [rdi + 0x1ac], ecx
0098CD17  8B D1                           mov edx, ecx
0098CD19  E9 F3 FD FF FF                  jmp 0x14098cb11
0098CD1E  41 8B C1                        mov eax, r9d
0098CD21  E9 33 FE FF FF                  jmp 0x14098cb59
0098CD26  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CD30  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CD3A  85 F6                           test esi, esi
0098CD3C  0F 95 C3                        setne bl
0098CD3F  48 8B 00                        mov rax, qword ptr [rax]
0098CD42  8A D3                           mov dl, bl
0098CD44  44 8B 01                        mov r8d, dword ptr [rcx]
0098CD47  48 8D 4F 68                     lea rcx, [rdi + 0x68]
0098CD4B  4C 0F AF C0                     imul r8, rax
0098CD4F  49 C1 E8 18                     shr r8, 0x18
0098CD53  E8 E0 C7 B0 FF                  call 0x140499538
0098CD58  44 8B C8                        mov r9d, eax
0098CD5B  E8 6C 05 AD FF                  call 0x14045d2cc
0098CD60  44 0F B7 87 D8 01 00 00         movzx r8d, word ptr [rdi + 0x1d8]
0098CD68  48 8D 8F 30 01 00 00            lea rcx, [rdi + 0x130]
0098CD6F  84 DB                           test bl, bl
0098CD71  0F 84 10 01 00 00               je 0x14098ce87
0098CD77  66 41 83 C8 01                  or r8w, 1
0098CD7C  8B D0                           mov edx, eax
0098CD7E  66 44 89 87 D8 01 00 00         mov word ptr [rdi + 0x1d8], r8w
0098CD86  E8 45 31 A7 FF                  call 0x1403ffed0
0098CD8B  48 8B CD                        mov rcx, rbp
0098CD8E  E8 85 16 00 00                  call 0x14098e418
0098CD93  E9 79 FD FF FF                  jmp 0x14098cb11
0098CD98  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CDA2  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CDAC  85 F6                           test esi, esi
0098CDAE  0F 95 C3                        setne bl
0098CDB1  48 8B 00                        mov rax, qword ptr [rax]
0098CDB4  8A D3                           mov dl, bl
0098CDB6  44 8B 01                        mov r8d, dword ptr [rcx]
0098CDB9  48 8D 4F 70                     lea rcx, [rdi + 0x70]
0098CDBD  4C 0F AF C0                     imul r8, rax
0098CDC1  49 C1 E8 18                     shr r8, 0x18
0098CDC5  E8 6E C7 B0 FF                  call 0x140499538
0098CDCA  44 8B C8                        mov r9d, eax
0098CDCD  E8 FA 04 AD FF                  call 0x14045d2cc
0098CDD2  0F B7 97 D8 01 00 00            movzx edx, word ptr [rdi + 0x1d8]
0098CDD9  44 8B C0                        mov r8d, eax
0098CDDC  48 8D 8F 38 01 00 00            lea rcx, [rdi + 0x138]
0098CDE3  84 DB                           test bl, bl
0098CDE5  0F 84 C3 00 00 00               je 0x14098ceae
0098CDEB  66 83 CA 02                     or dx, 2
0098CDEF  66 89 97 D8 01 00 00            mov word ptr [rdi + 0x1d8], dx
0098CDF6  8B D0                           mov edx, eax
0098CDF8  EB 8C                           jmp 0x14098cd86
0098CDFA  BA 01 00 00 00                  mov edx, 1
0098CDFF  01 97 A8 01 00 00               add dword ptr [rdi + 0x1a8], edx
0098CE05  E8 C2 04 AD FF                  call 0x14045d2cc
0098CE0A  48 8D 8F 78 01 00 00            lea rcx, [rdi + 0x178]
0098CE11  E9 BC FE FF FF                  jmp 0x14098ccd2
0098CE16  85 F6                           test esi, esi
0098CE18  40 0F 95 C6                     setne sil
0098CE1C  83 FB 0B                        cmp ebx, 0xb
0098CE1F  0F 85 9D 00 00 00               jne 0x14098cec2
0098CE25  48 8D 9F 68 01 00 00            lea rbx, [rdi + 0x168]
0098CE2C  48 81 C7 90 01 00 00            add rdi, 0x190
0098CE33  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CE3D  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CE47  40 8A D6                        mov dl, sil
0098CE4A  48 8B 00                        mov rax, qword ptr [rax]
0098CE4D  44 8B 01                        mov r8d, dword ptr [rcx]
0098CE50  48 8B CF                        mov rcx, rdi
0098CE53  4C 0F AF C0                     imul r8, rax
0098CE57  49 C1 E8 18                     shr r8, 0x18
0098CE5B  E8 D8 C6 B0 FF                  call 0x140499538
0098CE60  8B C8                           mov ecx, eax
0098CE62  E8 65 04 AD FF                  call 0x14045d2cc
0098CE67  8B D0                           mov edx, eax
0098CE69  40 84 F6                        test sil, sil
0098CE6C  0F 85 13 01 00 00               jne 0x14098cf85
0098CE72  C1 E9 0C                        shr ecx, 0xc
0098CE75  2B D1                           sub edx, ecx
0098CE77  48 8B CB                        mov rcx, rbx
0098CE7A  44 8B C0                        mov r8d, eax
0098CE7D  E8 AE AD AA FF                  call 0x140437c30
0098CE82  E9 8A FC FF FF                  jmp 0x14098cb11
0098CE87  BA FE FF 00 00                  mov edx, 0xfffe
0098CE8C  66 44 23 C2                     and r8w, dx
0098CE90  8B D0                           mov edx, eax
0098CE92  66 44 89 87 D8 01 00 00         mov word ptr [rdi + 0x1d8], r8w
0098CE9A  44 8B C0                        mov r8d, eax
0098CE9D  41 C1 E9 0C                     shr r9d, 0xc
0098CEA1  41 2B D1                        sub edx, r9d
0098CEA4  E8 87 AD AA FF                  call 0x140437c30
0098CEA9  E9 DD FE FF FF                  jmp 0x14098cd8b
0098CEAE  B8 FD FF 00 00                  mov eax, 0xfffd
0098CEB3  66 23 D0                        and dx, ax
0098CEB6  66 89 97 D8 01 00 00            mov word ptr [rdi + 0x1d8], dx
0098CEBD  41 8B D0                        mov edx, r8d
0098CEC0  EB DB                           jmp 0x14098ce9d
0098CEC2  48 8D 9F 60 01 00 00            lea rbx, [rdi + 0x160]
0098CEC9  48 81 C7 88 01 00 00            add rdi, 0x188
0098CED0  E9 5E FF FF FF                  jmp 0x14098ce33
0098CED5  8D 46 FF                        lea eax, [rsi - 1]
0098CED8  BA 01 00 00 00                  mov edx, 1
0098CEDD  3B C2                           cmp eax, edx
0098CEDF  0F 87 2C FC FF FF               ja 0x14098cb11
0098CEE5  8B 9F E0 01 00 00               mov ebx, dword ptr [rdi + 0x1e0]
0098CEEB  3B F2                           cmp esi, edx
0098CEED  75 7F                           jne 0x14098cf6e
0098CEEF  FF C3                           inc ebx
0098CEF1  89 9F E0 01 00 00               mov dword ptr [rdi + 0x1e0], ebx
0098CEF7  3B DA                           cmp ebx, edx
0098CEF9  0F 87 12 FC FF FF               ja 0x14098cb11
0098CEFF  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0098CF09  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0098CF13  48 8B 00                        mov rax, qword ptr [rax]
0098CF16  44 8B 01                        mov r8d, dword ptr [rcx]
0098CF19  49 8B CB                        mov rcx, r11
0098CF1C  4C 0F AF C0                     imul r8, rax
0098CF20  49 C1 E8 18                     shr r8, 0x18
0098CF24  85 DB                           test ebx, ebx
0098CF26  0F 95 C2                        setne dl
0098CF29  E8 0A C6 B0 FF                  call 0x140499538
0098CF2E  8B C8                           mov ecx, eax
0098CF30  E8 97 03 AD FF                  call 0x14045d2cc
0098CF35  8B D0                           mov edx, eax
0098CF37  85 DB                           test ebx, ebx
0098CF39  0F 85 E9 FC FF FF               jne 0x14098cc28
0098CF3F  C1 E9 0C                        shr ecx, 0xc
0098CF42  2B D1                           sub edx, ecx
0098CF44  48 8B CD                        mov rcx, rbp
0098CF47  E9 2E FF FF FF                  jmp 0x14098ce7a
0098CF4C  41 83 C9 FF                     or r9d, 0xffffffff
0098CF50  E9 53 FD FF FF                  jmp 0x14098cca8
0098CF55  41 83 C9 FF                     or r9d, 0xffffffff
0098CF59  E9 A9 FC FF FF                  jmp 0x14098cc07
0098CF5E  44 8B C0                        mov r8d, eax
0098CF61  E9 22 FD FF FF                  jmp 0x14098cc88
0098CF66  44 8B C0                        mov r8d, eax
0098CF69  E9 79 FC FF FF                  jmp 0x14098cbe7
0098CF6E  85 DB                           test ebx, ebx
0098CF70  74 8D                           je 0x14098ceff
0098CF72  2B DA                           sub ebx, edx
0098CF74  89 9F E0 01 00 00               mov dword ptr [rdi + 0x1e0], ebx
0098CF7A  0F 85 91 FB FF FF               jne 0x14098cb11
0098CF80  E9 7A FF FF FF                  jmp 0x14098ceff
0098CF85  48 8B CB                        mov rcx, rbx
0098CF88  E9 7F FB FF FF                  jmp 0x14098cb0c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoEnergyContextUpdateComponentPower(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int16 v_stack_mCE;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p2C;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p34;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 4709662)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_mD0 = a3;
    a2 = 0;
    result = memset(v_stack_mC8, a2, 144, a4);
    v_r15 = 0;
    if (*(unsigned __int64 *)(a1 + 1640) == 0) goto loc_0098CB19;
    result = PopAcquireRwLockExclusive(*(unsigned __int64 *)(a1 + 1640) + 440, a2, 144, a4);
    if (((unsigned int)((unsigned int)(a2))) > 10) goto loc_0098CB70;
    if (((unsigned int)((unsigned int)(a2))) == 10) goto loc_0098CE16;
    v_rbx = (unsigned int)(((unsigned int)(a2)) - (4));
    if (condition_is_equal) goto loc_0098CD26;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0098CD98;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_not_equal) goto loc_0098CC30;
    result = KeQueryTimelineBitmapTime(*(unsigned __int64 *)(a1 + 1640) + 440, a2, 144, a4);
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    if ((unsigned __int16)(a3) == 0) goto loc_0098CAD4;
    a1 = (unsigned int)(~((unsigned int)((unsigned int)((unsigned __int16)(a3)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 128))))) goto loc_0098CCD9;
    result = (unsigned int)(((unsigned __int16)(a3)) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 128)))));
loc_0098CAC2:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 128) = (unsigned int)(result);
    result = RtlTimelineBitmapUpdate(*(unsigned __int64 *)(a1 + 1640) + 320, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 128)), a4);
loc_0098CAD4:
    if ((unsigned __int16)(v_stack_mCE) != 0) goto loc_0098CB41;
loc_0098CADE:
    if ((unsigned __int16)((unsigned int)(v_stack_mCC)) == 0) goto loc_0098CB11;
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(v_stack_mCC))))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136))))) {
        a4 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136)) + (unsigned __int16)((unsigned int)(v_stack_mCC)) * 1;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136) = a4;
loc_0098CB0C:
    result = RtlTimelineBitmapUpdate(*(unsigned __int64 *)(a1 + 1640) + 336, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136)), a4);
loc_0098CB11:
    result = PopReleaseRwLock(*(unsigned __int64 *)(a1 + 1640) + 440, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136)), a4);
loc_0098CB19:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 136)), a4);
    v_rsp = (v_rsp) + (208);
    return result;
loc_0098CB41:
    result = (unsigned int)(~(result));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 132))))) goto loc_0098CD1E;
loc_0098CB59:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 132) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 132)) + (unsigned int)((unsigned int)(result)) * 1);
    result = RtlTimelineBitmapUpdate(*(unsigned __int64 *)(a1 + 1640) + 328, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 132)), a4);
    goto loc_0098CADE;
loc_0098CB70:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p10))) - (11));
    if (condition_is_equal) goto loc_0098CE16;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0098CCFF;
    if (((unsigned int)(a3)) != 3) goto loc_0098CED5;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 408 + 4)) < 0) goto loc_0098CB11;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 408);
    a1 = ((unsigned int)(*(unsigned int *)(a1))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 408)));
    a1 = (a1) >> (24);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - (v_stack_p20));
    v_stack_p20 = (unsigned int)(a1);
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_0098CF66;
loc_0098CBE7:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p24)))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))));
    if (((unsigned int)(result)) < a2) goto loc_0098CF55;
loc_0098CC07:
    a4 = (unsigned int)((a2 + (unsigned int)(0x1000ULL) * 1) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p24)) & (0x80000000ULL));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_r10)));
    v_stack_p24 = a4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 408) = v_stack_p20;
    result = KeQueryTimelineBitmapTime((unsigned int)(0x7FFFFFFFULL), a2, (unsigned int)(0x1000ULL), a4);
loc_0098CC28:
    goto loc_0098CB0C;
loc_0098CC30:
    v_rbx = (unsigned int)((v_stack_p10) - (1));
    if (condition_is_equal) goto loc_0098CCE1;
    if (((unsigned int)(v_rbx)) != 1) goto loc_0098CB11;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 384);
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 368))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 384)));
    a1 = (a1) >> (24);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - (v_stack_p20));
    v_stack_p20 = (unsigned int)(a1);
    if (((unsigned int)(result)) <= 1000) goto loc_0098CF5E;
loc_0098CC88:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p24)))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    result = (unsigned int)(~(1000));
    if (((unsigned int)(result)) < a2) goto loc_0098CF4C;
loc_0098CCA8:
    a4 = (unsigned int)((a2 + 1000 * 1) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p24)) & (0x80000000ULL));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_r10)));
    v_stack_p24 = a4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1640) + 384) = v_stack_p20;
    result = KeQueryTimelineBitmapTime((unsigned int)(0x7FFFFFFFULL), a2, 1000, a4);
loc_0098CCD2:
    goto loc_0098CB0C;
loc_0098CCD9:
    goto loc_0098CAC2;
loc_0098CCE1:
    v_stack_p34 = (unsigned int)((unsigned int)(v_stack_p2C));
    v_stack_p30 = (unsigned int)(a3);
    result = PopEtEnergyContextSetState(*(unsigned __int64 *)(a1 + 1640) + 368, v_stack_p30, 1000, a4);
    goto loc_0098CB11;
loc_0098CCFF:
    a1 = (unsigned int)((*(unsigned __int64 *)(a1 + 1640) + 368) - (1));
    if (condition_is_equal) goto loc_0098CDFA;
    if (((unsigned int)(a1)) != 1) goto loc_0098CB11;
    goto loc_0098CB11;
loc_0098CD1E:
    goto loc_0098CB59;
loc_0098CD26:
    v_rbx = ((unsigned int)(a3) != 0) ? 1 : 0;
    a3 = ((unsigned int)(*(unsigned int *)(a1))) * (*(unsigned __int64 *)((unsigned int)(a4)));
    a3 = (a3) >> (24);
    result = RtlStateDurationUpdate(*(unsigned __int64 *)(a1 + 1640) + 104, (unsigned __int8)(v_rbx), a3, a4);
    result = KeQueryTimelineBitmapTime(*(unsigned __int64 *)(a1 + 1640) + 104, (unsigned __int8)(v_rbx), a3, (unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)(v_rbx) == 0) goto loc_0098CE87;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1640) + 472)) | (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1640) + 472) = (unsigned __int16)(a3);
loc_0098CD86:
    result = RtlTimelineBitmapUpdate(*(unsigned __int64 *)(a1 + 1640) + 304, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
loc_0098CD8B:
    result = PopEtEnergyContextProcessStateUpdate(*(unsigned __int64 *)(a1 + 1640) + 368, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
    goto loc_0098CB11;
loc_0098CD98:
    v_rbx = ((unsigned int)(a3) != 0) ? 1 : 0;
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 368))) * (*(unsigned __int64 *)(result));
    a3 = (a3) >> (24);
    result = RtlStateDurationUpdate(*(unsigned __int64 *)(a1 + 1640) + 112, (unsigned __int8)(v_rbx), a3, (unsigned int)((unsigned int)(result)));
    result = KeQueryTimelineBitmapTime(*(unsigned __int64 *)(a1 + 1640) + 112, (unsigned __int8)(v_rbx), a3, (unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)(v_rbx) == 0) goto loc_0098CEAE;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1640) + 472)) | (2));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 1640) + 472) = (unsigned __int16)(a2);
    goto loc_0098CD86;
loc_0098CDFA:
    result = KeQueryTimelineBitmapTime(*(unsigned __int64 *)(a1 + 1640) + 312, 1, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(result)));
    goto loc_0098CCD2;
loc_0098CE16:
    v_rsi = ((unsigned int)(a3) != 0) ? 1 : 0;
    if (((unsigned int)(v_rbx)) != 11) goto loc_0098CEC2;
    v_rdi = (*(unsigned __int64 *)(a1 + 1640)) + (400);
loc_0098CE33:
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 376))) * (*(unsigned __int64 *)(result));
    a3 = (a3) >> (24);
    result = RtlStateDurationUpdate(v_rdi, (unsigned __int8)(v_rsi), a3, (unsigned int)((unsigned int)(result)));
    result = KeQueryTimelineBitmapTime((unsigned int)((unsigned int)(result)), (unsigned __int8)(v_rsi), a3, (unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)(v_rsi) != 0) goto loc_0098CF85;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (12));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a1)));
loc_0098CE7A:
    result = RtlTimelineBitmapUpdateRange(*(unsigned __int64 *)(a1 + 1640) + 360, a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(result)));
    goto loc_0098CB11;
loc_0098CE87:
    a3 = (unsigned __int16)(((unsigned int)((unsigned int)(result))) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rdi + 472) = (unsigned __int16)(a3);
loc_0098CE9D:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (12));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (a4));
    result = RtlTimelineBitmapUpdateRange(*(unsigned __int64 *)(a1 + 1640) + 360, a2, (unsigned int)((unsigned int)(result)), a4);
    goto loc_0098CD8B;
loc_0098CEAE:
    a2 = (unsigned __int16)((a2) & ((unsigned __int16)((unsigned int)(0xFFFDULL))));
    *(unsigned __int16 *)(v_rdi + 472) = (unsigned __int16)(a2);
    goto loc_0098CE9D;
loc_0098CEC2:
    v_rdi = (v_rdi) + (392);
    goto loc_0098CE33;
loc_0098CED5:
    if (((unsigned int)(v_rsi - 1)) > 1) goto loc_0098CB11;
    if (((unsigned int)(v_rsi)) != 1) goto loc_0098CF6E;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 480))) + 1);
    *(unsigned int *)(v_rdi + 480) = (unsigned int)(v_rbx);
    if (((unsigned int)(v_rbx)) > 1) goto loc_0098CB11;
loc_0098CEFF:
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1640) + 360))) * (*(unsigned __int64 *)(v_rsi - 1));
    a3 = (a3) >> (24);
    a2 = ((unsigned int)(v_rbx) != 0) ? 1 : 0;
    result = RtlStateDurationUpdate(*(unsigned __int64 *)(a1 + 1640) + 408, a2, a3, a4);
    result = KeQueryTimelineBitmapTime((unsigned int)((unsigned int)(result)), a2, a3, a4);
    if ((unsigned int)(v_rbx) != 0) goto loc_0098CC28;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (12));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a1)));
    goto loc_0098CE7A;
loc_0098CF4C:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    goto loc_0098CCA8;
loc_0098CF55:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    goto loc_0098CC07;
loc_0098CF5E:
    goto loc_0098CC88;
loc_0098CF66:
    goto loc_0098CBE7;
loc_0098CF6E:
    if ((unsigned int)(v_rbx) == 0) goto loc_0098CEFF;
    v_rbx = (unsigned int)((v_rbx) - (a2));
    *(unsigned int *)(v_rdi + 480) = (unsigned int)(v_rbx);
    if (condition_is_not_equal) goto loc_0098CB11;
    goto loc_0098CEFF;
loc_0098CF85:
    goto loc_0098CB0C;
}
```

## 5. (Beta) C Style

```c
int64_t PoEnergyContextUpdateComponentPower(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint16_t v_stack_mCE;
    uint64_t v_stack_mD0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p2C;
    uint64_t v_stack_p30;
    uint32_t v_stack_p34;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x47DD1E)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_mD0 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 144, Arg4);
    local_r15 = 0;
    if (*(uint64_t *)(arg1 + 0x668) == 0) goto loc_0098CB19;
    result = PopAcquireRwLockExclusive(*(uint64_t *)(arg1 + 0x668) + 440, Arg2, 144, Arg4);
    if (((uint32_t)((uint32_t)(Arg2))) > 10) goto loc_0098CB70;
    if (((uint32_t)((uint32_t)(Arg2))) == 10) goto loc_0098CE16;
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) - (4));
    if (condition_is_equal) goto loc_0098CD26;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0098CD98;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_not_equal) goto loc_0098CC30;
    result = KeQueryTimelineBitmapTime(*(uint64_t *)(arg1 + 0x668) + 440, Arg2, 144, Arg4);
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    if ((uint16_t)(Arg3) == 0) goto loc_0098CAD4;
    Arg1 = (uint32_t)(~((uint32_t)((uint32_t)((uint16_t)(Arg3)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x80))))) goto loc_0098CCD9;
    result = (uint32_t)(((uint16_t)(Arg3)) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x80)))));
loc_0098CAC2:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x80) = (uint32_t)(result);
    result = RtlTimelineBitmapUpdate(*(uint64_t *)(arg1 + 0x668) + 320, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x80)), Arg4);
loc_0098CAD4:
    if ((uint16_t)(v_stack_mCE) != 0) goto loc_0098CB41;
loc_0098CADE:
    if ((uint16_t)((uint32_t)(v_stack_mCC)) == 0) goto loc_0098CB11;
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint16_t)((uint32_t)(v_stack_mCC))))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88))))) {
        Arg4 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88)) + (uint16_t)((uint32_t)(v_stack_mCC)) * 1;
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88) = Arg4;
loc_0098CB0C:
    result = RtlTimelineBitmapUpdate(*(uint64_t *)(arg1 + 0x668) + 336, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88)), Arg4);
loc_0098CB11:
    result = PopReleaseRwLock(*(uint64_t *)(arg1 + 0x668) + 440, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88)), Arg4);
loc_0098CB19:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x88)), Arg4);
    local_rsp = (local_rsp) + (208);
    return result;
loc_0098CB41:
    result = (uint32_t)(~(result));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x84))))) goto loc_0098CD1E;
loc_0098CB59:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x84) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x84)) + (uint32_t)((uint32_t)(result)) * 1);
    result = RtlTimelineBitmapUpdate(*(uint64_t *)(arg1 + 0x668) + 328, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x84)), Arg4);
    goto loc_0098CADE;
loc_0098CB70:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p10))) - (11));
    if (condition_is_equal) goto loc_0098CE16;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0098CCFF;
    if (((uint32_t)(Arg3)) != 3) goto loc_0098CED5;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x198 + 0x4)) < 0) goto loc_0098CB11;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x198);
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1))) * (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x198)));
    Arg1 = (Arg1) >> (24);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - (v_stack_p20));
    v_stack_p20 = (uint32_t)(Arg1);
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_0098CF66;
loc_0098CBE7:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p24)))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))));
    if (((uint32_t)(result)) < Arg2) goto loc_0098CF55;
loc_0098CC07:
    Arg4 = (uint32_t)((Arg2 + (uint32_t)(0x1000ULL) * 1) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p24)) & (0x80000000ULL));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_r10)));
    v_stack_p24 = Arg4;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x198) = v_stack_p20;
    result = KeQueryTimelineBitmapTime((uint32_t)(0x7FFFFFFFULL), Arg2, (uint32_t)(0x1000ULL), Arg4);
loc_0098CC28:
    goto loc_0098CB0C;
loc_0098CC30:
    local_rbx = (uint32_t)((v_stack_p10) - (1));
    if (condition_is_equal) goto loc_0098CCE1;
    if (((uint32_t)(local_rbx)) != 1) goto loc_0098CB11;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x180);
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x170))) * (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x180)));
    Arg1 = (Arg1) >> (24);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - (v_stack_p20));
    v_stack_p20 = (uint32_t)(Arg1);
    if (((uint32_t)(result)) <= 1000) goto loc_0098CF5E;
loc_0098CC88:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p24)))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    result = (uint32_t)(~(1000));
    if (((uint32_t)(result)) < Arg2) goto loc_0098CF4C;
loc_0098CCA8:
    Arg4 = (uint32_t)((Arg2 + 1000 * 1) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p24)) & (0x80000000ULL));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_r10)));
    v_stack_p24 = Arg4;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x668) + 0x180) = v_stack_p20;
    result = KeQueryTimelineBitmapTime((uint32_t)(0x7FFFFFFFULL), Arg2, 1000, Arg4);
loc_0098CCD2:
    goto loc_0098CB0C;
loc_0098CCD9:
    goto loc_0098CAC2;
loc_0098CCE1:
    v_stack_p34 = (uint32_t)((uint32_t)(v_stack_p2C));
    v_stack_p30 = (uint32_t)(Arg3);
    result = PopEtEnergyContextSetState(*(uint64_t *)(arg1 + 0x668) + 368, v_stack_p30, 1000, Arg4);
    goto loc_0098CB11;
loc_0098CCFF:
    Arg1 = (uint32_t)((*(uint64_t *)(arg1 + 0x668) + 368) - (1));
    if (condition_is_equal) goto loc_0098CDFA;
    if (((uint32_t)(Arg1)) != 1) goto loc_0098CB11;
    goto loc_0098CB11;
loc_0098CD1E:
    goto loc_0098CB59;
loc_0098CD26:
    local_rbx = ((uint32_t)(Arg3) != 0) ? 1 : 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1))) * (*(uint64_t *)((uint32_t)(Arg4)));
    Arg3 = (Arg3) >> (24);
    result = RtlStateDurationUpdate(*(uint64_t *)(arg1 + 0x668) + 104, (uint8_t)(local_rbx), Arg3, Arg4);
    result = KeQueryTimelineBitmapTime(*(uint64_t *)(arg1 + 0x668) + 104, (uint8_t)(local_rbx), Arg3, (uint32_t)((uint32_t)(result)));
    if ((uint8_t)(local_rbx) == 0) goto loc_0098CE87;
    Arg3 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x668) + 0x1D8)) | (1));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x668) + 0x1D8) = (uint16_t)(Arg3);
loc_0098CD86:
    result = RtlTimelineBitmapUpdate(*(uint64_t *)(arg1 + 0x668) + 304, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)((uint32_t)(result)));
loc_0098CD8B:
    result = PopEtEnergyContextProcessStateUpdate(*(uint64_t *)(arg1 + 0x668) + 368, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)((uint32_t)(result)));
    goto loc_0098CB11;
loc_0098CD98:
    local_rbx = ((uint32_t)(Arg3) != 0) ? 1 : 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x170))) * (*(uint64_t *)(result));
    Arg3 = (Arg3) >> (24);
    result = RtlStateDurationUpdate(*(uint64_t *)(arg1 + 0x668) + 112, (uint8_t)(local_rbx), Arg3, (uint32_t)((uint32_t)(result)));
    result = KeQueryTimelineBitmapTime(*(uint64_t *)(arg1 + 0x668) + 112, (uint8_t)(local_rbx), Arg3, (uint32_t)((uint32_t)(result)));
    if ((uint8_t)(local_rbx) == 0) goto loc_0098CEAE;
    Arg2 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x668) + 0x1D8)) | (2));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x668) + 0x1D8) = (uint16_t)(Arg2);
    goto loc_0098CD86;
loc_0098CDFA:
    result = KeQueryTimelineBitmapTime(*(uint64_t *)(arg1 + 0x668) + 312, 1, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(result)));
    goto loc_0098CCD2;
loc_0098CE16:
    local_rsi = ((uint32_t)(Arg3) != 0) ? 1 : 0;
    if (((uint32_t)(local_rbx)) != 11) goto loc_0098CEC2;
    local_rdi = (*(uint64_t *)(arg1 + 0x668)) + (400);
loc_0098CE33:
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x178))) * (*(uint64_t *)(result));
    Arg3 = (Arg3) >> (24);
    result = RtlStateDurationUpdate(local_rdi, (uint8_t)(local_rsi), Arg3, (uint32_t)((uint32_t)(result)));
    result = KeQueryTimelineBitmapTime((uint32_t)((uint32_t)(result)), (uint8_t)(local_rsi), Arg3, (uint32_t)((uint32_t)(result)));
    if ((uint8_t)(local_rsi) != 0) goto loc_0098CF85;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (12));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg1)));
loc_0098CE7A:
    result = RtlTimelineBitmapUpdateRange(*(uint64_t *)(arg1 + 0x668) + 360, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(result)));
    goto loc_0098CB11;
loc_0098CE87:
    Arg3 = (uint16_t)(((uint32_t)((uint32_t)(result))) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rdi + 0x1D8) = (uint16_t)(Arg3);
loc_0098CE9D:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (12));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (Arg4));
    result = RtlTimelineBitmapUpdateRange(*(uint64_t *)(arg1 + 0x668) + 360, Arg2, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_0098CD8B;
loc_0098CEAE:
    Arg2 = (uint16_t)((Arg2) & ((uint16_t)((uint32_t)(0xFFFDULL))));
    *(uint16_t *)(local_rdi + 0x1D8) = (uint16_t)(Arg2);
    goto loc_0098CE9D;
loc_0098CEC2:
    local_rdi = (local_rdi) + (392);
    goto loc_0098CE33;
loc_0098CED5:
    if (((uint32_t)(local_rsi - 1)) > 1) goto loc_0098CB11;
    if (((uint32_t)(local_rsi)) != 1) goto loc_0098CF6E;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x1E0))) + 1);
    *(uint32_t *)(local_rdi + 0x1E0) = (uint32_t)(local_rbx);
    if (((uint32_t)(local_rbx)) > 1) goto loc_0098CB11;
loc_0098CEFF:
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x668) + 0x168))) * (*(uint64_t *)(local_rsi - 0x1));
    Arg3 = (Arg3) >> (24);
    Arg2 = ((uint32_t)(local_rbx) != 0) ? 1 : 0;
    result = RtlStateDurationUpdate(*(uint64_t *)(arg1 + 0x668) + 408, Arg2, Arg3, Arg4);
    result = KeQueryTimelineBitmapTime((uint32_t)((uint32_t)(result)), Arg2, Arg3, Arg4);
    if ((uint32_t)(local_rbx) != 0) goto loc_0098CC28;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (12));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg1)));
    goto loc_0098CE7A;
loc_0098CF4C:
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    goto loc_0098CCA8;
loc_0098CF55:
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    goto loc_0098CC07;
loc_0098CF5E:
    goto loc_0098CC88;
loc_0098CF66:
    goto loc_0098CBE7;
loc_0098CF6E:
    if ((uint32_t)(local_rbx) == 0) goto loc_0098CEFF;
    local_rbx = (uint32_t)((local_rbx) - (Arg2));
    *(uint32_t *)(local_rdi + 0x1E0) = (uint32_t)(local_rbx);
    if (condition_is_not_equal) goto loc_0098CB11;
    goto loc_0098CEFF;
loc_0098CF85:
    goto loc_0098CB0C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x668` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098CA08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
