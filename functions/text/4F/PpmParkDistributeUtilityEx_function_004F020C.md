# PpmParkDistributeUtilityEx

- RVA: `0x004F020C`–`0x004F083C` (길이 `1,584` bytes)
- VA: `0x00000001404F020C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B2E2C`
- 디코드: `410`개 명령, `1,584/1,584` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004F027E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F0293` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F02B7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F02DC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F02F2` → [KiXorAffinityEx](../2D/KiXorAffinityEx_function_002D62D0.md) (function, `0x002D62D0`)
- `0x004F036E` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F03EF` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x004F047E` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F0490` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x004F055E` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F05A0` → [PpmHeteroNormalizedUtilityToUtility](../45/PpmHeteroNormalizedUtilityToUtility_function_0045A628.md) (function, `0x0045A628`)
- `0x004F065E` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F0671` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x004F06B7` → [PpmHeteroNormalizedUtilityToUtility](../45/PpmHeteroNormalizedUtilityToUtility_function_0045A628.md) (function, `0x0045A628`)
- `0x004F0741` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F074D` → [PpmHeteroNormalizedUtilityToUtility](../45/PpmHeteroNormalizedUtilityToUtility_function_0045A628.md) (function, `0x0045A628`)
- `0x004F0775` → [KeXorAffinityEx2](../2D/KeXorAffinityEx2_function_002D5B70.md) (function, `0x002D5B70`)
- `0x004F0793` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F07AF` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x004F07C0` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x004F07ED` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F0808` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x004F081B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkDistributeAllUtility](../41/PpmParkDistributeAllUtility_function_00412D10.md) at `0x00412DCB`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004EFD27`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004EFE01`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004EFE84`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004EFEE7`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004EFF28`

### Static image references
- `0x004F022B` → RVA `0x00E0A740` (`.data`; read)
- `0x004F035B` → RVA `0x00F231B8` (`.data`; read)
- `0x004F0398` → RVA `0x00F231B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F020C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
004F0211  55                              push rbp
004F0212  56                              push rsi
004F0213  57                              push rdi
004F0214  41 54                           push r12
004F0216  41 55                           push r13
004F0218  41 56                           push r14
004F021A  41 57                           push r15
004F021C  48 8D AC 24 70 FE FF FF         lea rbp, [rsp - 0x190]
004F0224  48 81 EC 90 02 00 00            sub rsp, 0x290
004F022B  48 8B 05 0E A5 91 00            mov rax, qword ptr [rip + 0x91a50e]
004F0232  48 33 C4                        xor rax, rsp
004F0235  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
004F023C  48 8B 85 F8 01 00 00            mov rax, qword ptr [rbp + 0x1f8]
004F0243  41 0F B7 F8                     movzx edi, r8w
004F0247  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004F024C  4C 8B FA                        mov r15, rdx
004F024F  33 C0                           xor eax, eax
004F0251  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
004F0256  48 8B D9                        mov rbx, rcx
004F0259  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004F025E  0F 57 C0                        xorps xmm0, xmm0
004F0261  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
004F0266  41 BC 00 01 00 00               mov r12d, 0x100
004F026C  89 7C 24 2C                     mov dword ptr [rsp + 0x2c], edi
004F0270  45 8B C4                        mov r8d, r12d
004F0273  48 8D 4D 78                     lea rcx, [rbp + 0x78]
004F0277  33 D2                           xor edx, edx
004F0279  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
004F027E  E8 BD 69 1D 00                  call 0x1406c6c40
004F0283  33 FF                           xor edi, edi
004F0285  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
004F028A  45 8B C4                        mov r8d, r12d
004F028D  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
004F0291  33 D2                           xor edx, edx
004F0293  E8 A8 69 1D 00                  call 0x1406c6c40
004F0298  21 7D 74                        and dword ptr [rbp + 0x74], edi
004F029B  48 8D 4D 78                     lea rcx, [rbp + 0x78]
004F029F  45 8B C4                        mov r8d, r12d
004F02A2  66 89 7C 24 28                  mov word ptr [rsp + 0x28], di
004F02A7  33 D2                           xor edx, edx
004F02A9  C7 45 70 01 00 20 00            mov dword ptr [rbp + 0x70], 0x200001
004F02B0  0F B7 F7                        movzx esi, di
004F02B3  44 0F B7 EF                     movzx r13d, di
004F02B7  E8 84 69 1D 00                  call 0x1406c6c40
004F02BC  44 8B A5 F0 01 00 00            mov r12d, dword ptr [rbp + 0x1f0]
004F02C3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
004F02C8  21 7C 24 64                     and dword ptr [rsp + 0x64], edi
004F02CC  33 D2                           xor edx, edx
004F02CE  41 B8 00 01 00 00               mov r8d, 0x100
004F02D4  C7 44 24 60 01 00 20 00         mov dword ptr [rsp + 0x60], 0x200001
004F02DC  E8 5F 69 1D 00                  call 0x1406c6c40
004F02E1  44 0F B7 4C 24 62               movzx r9d, word ptr [rsp + 0x62]
004F02E7  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F02EC  49 8B D7                        mov rdx, r15
004F02EF  48 8B CB                        mov rcx, rbx
004F02F2  E8 D9 5F DE FF                  call 0x1402d62d0
004F02F7  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
004F02FC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
004F0301  44 0F B7 74 24 40               movzx r14d, word ptr [rsp + 0x40]
004F0307  44 8D 4F 01                     lea r9d, [rdi + 1]
004F030B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004F0310  45 33 C0                        xor r8d, r8d
004F0313  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
004F0318  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
004F031D  48 85 DB                        test rbx, rbx
004F0320  75 22                           jne 0x1404f0344
004F0322  66 45 03 F1                     add r14w, r9w
004F0326  41 0F B7 C6                     movzx eax, r14w
004F032A  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F032F  3B C1                           cmp eax, ecx
004F0331  0F 83 CF 00 00 00               jae 0x1404f0406
004F0337  48 8B 5C C4 68                  mov rbx, qword ptr [rsp + rax*8 + 0x68]
004F033C  44 0F B7 74 24 40               movzx r14d, word ptr [rsp + 0x40]
004F0342  EB D9                           jmp 0x1404f031d
004F0344  48 0F BC D3                     bsf rdx, rbx
004F0348  41 0F B7 CE                     movzx ecx, r14w
004F034C  0F B6 C2                        movzx eax, dl
004F034F  C1 E1 06                        shl ecx, 6
004F0352  48 0F B3 C3                     btr rbx, rax
004F0356  0F B6 C2                        movzx eax, dl
004F0359  03 C8                           add ecx, eax
004F035B  48 8B 05 56 2E A3 00            mov rax, qword ptr [rip + 0xa32e56]
004F0362  44 8B 2C 88                     mov r13d, dword ptr [rax + rcx*4]
004F0366  41 8B CD                        mov ecx, r13d
004F0369  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
004F036E  E8 5D 82 DE FF                  call 0x1402d85d0
004F0373  45 33 C0                        xor r8d, r8d
004F0376  4C 8D 88 B0 89 00 00            lea r9, [rax + 0x89b0]
004F037D  44 38 80 08 8A 00 00            cmp byte ptr [rax + 0x8a08], r8b
004F0384  75 12                           jne 0x1404f0398
004F0386  44 0F B7 6C 24 28               movzx r13d, word ptr [rsp + 0x28]
004F038C  66 41 FF C5                     inc r13w
004F0390  66 44 89 6C 24 28               mov word ptr [rsp + 0x28], r13w
004F0396  EB 50                           jmp 0x1404f03e8
004F0398  48 8B 05 11 2E A3 00            mov rax, qword ptr [rip + 0xa32e11]
004F039F  BA 01 00 00 00                  mov edx, 1
004F03A4  66 03 FA                        add di, dx
004F03A7  46 8B 04 A8                     mov r8d, dword ptr [rax + r13*4]
004F03AB  41 8B C8                        mov ecx, r8d
004F03AE  0F B7 45 70                     movzx eax, word ptr [rbp + 0x70]
004F03B2  41 83 E0 3F                     and r8d, 0x3f
004F03B6  C1 E9 06                        shr ecx, 6
004F03B9  3B C1                           cmp eax, ecx
004F03BB  77 0F                           ja 0x1404f03cc
004F03BD  0F B7 45 72                     movzx eax, word ptr [rbp + 0x72]
004F03C1  3B C1                           cmp eax, ecx
004F03C3  76 1A                           jbe 0x1404f03df
004F03C5  8D 04 0A                        lea eax, [rdx + rcx]
004F03C8  66 89 45 70                     mov word ptr [rbp + 0x70], ax
004F03CC  8B D1                           mov edx, ecx
004F03CE  48 8B 4C CD 78                  mov rcx, qword ptr [rbp + rcx*8 + 0x78]
004F03D3  41 8B C0                        mov eax, r8d
004F03D6  48 0F AB C1                     bts rcx, rax
004F03DA  48 89 4C D5 78                  mov qword ptr [rbp + rdx*8 + 0x78], rcx
004F03DF  44 0F B7 6C 24 28               movzx r13d, word ptr [rsp + 0x28]
004F03E5  45 33 C0                        xor r8d, r8d
004F03E8  41 8B 51 28                     mov edx, dword ptr [r9 + 0x28]
004F03EC  49 8B C9                        mov rcx, r9
004F03EF  E8 A0 2F F2 FF                  call 0x140413394
004F03F4  44 03 E0                        add r12d, eax
004F03F7  41 B9 01 00 00 00               mov r9d, 1
004F03FD  66 41 03 F1                     add si, r9w
004F0401  E9 0D FF FF FF                  jmp 0x1404f0313
004F0406  4D 8B 77 08                     mov r14, qword ptr [r15 + 8]
004F040A  66 89 7C 24 48                  mov word ptr [rsp + 0x48], di
004F040F  8B 7C 24 2C                     mov edi, dword ptr [rsp + 0x2c]
004F0413  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F0419  0F B7 5C 24 40                  movzx ebx, word ptr [rsp + 0x40]
004F041E  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
004F0423  44 89 44 24 2C                  mov dword ptr [rsp + 0x2c], r8d
004F0428  4D 85 FF                        test r15, r15
004F042B  74 06                           je 0x1404f0433
004F042D  41 0F B7 0F                     movzx ecx, word ptr [r15]
004F0431  EB 06                           jmp 0x1404f0439
004F0433  0F B7 CB                        movzx ecx, bx
004F0436  41 03 C9                        add ecx, r9d
004F0439  4D 85 F6                        test r14, r14
004F043C  75 1C                           jne 0x1404f045a
004F043E  66 41 03 D9                     add bx, r9w
004F0442  0F B7 C3                        movzx eax, bx
004F0445  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F044A  3B C1                           cmp eax, ecx
004F044C  73 53                           jae 0x1404f04a1
004F044E  4D 8B 74 C7 08                  mov r14, qword ptr [r15 + rax*8 + 8]
004F0453  0F B7 5C 24 40                  movzx ebx, word ptr [rsp + 0x40]
004F0458  EB DF                           jmp 0x1404f0439
004F045A  49 0F BC D6                     bsf rdx, r14
004F045E  0F B7 CB                        movzx ecx, bx
004F0461  0F B6 C2                        movzx eax, dl
004F0464  49 0F B3 C6                     btr r14, rax
004F0468  C1 E1 06                        shl ecx, 6
004F046B  0F B6 C2                        movzx eax, dl
004F046E  03 C8                           add ecx, eax
004F0470  48 8B 05 41 2D A3 00            mov rax, qword ptr [rip + 0xa32d41]
004F0477  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
004F047A  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
004F047E  E8 4D 81 DE FF                  call 0x1402d85d0
004F0483  48 8D 88 B0 89 00 00            lea rcx, [rax + 0x89b0]
004F048A  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
004F048D  2B 51 2C                        sub edx, dword ptr [rcx + 0x2c]
004F0490  E8 FF 2E F2 FF                  call 0x140413394
004F0495  44 03 E0                        add r12d, eax
004F0498  45 33 C0                        xor r8d, r8d
004F049B  45 8D 48 01                     lea r9d, [r8 + 1]
004F049F  EB 82                           jmp 0x1404f0423
004F04A1  66 41 3B F1                     cmp si, r9w
004F04A5  77 03                           ja 0x1404f04aa
004F04A7  41 8B F1                        mov esi, r9d
004F04AA  66 3B FE                        cmp di, si
004F04AD  66 0F 43 FE                     cmovae di, si
004F04B1  66 41 3B F9                     cmp di, r9w
004F04B5  77 03                           ja 0x1404f04ba
004F04B7  41 8B F9                        mov edi, r9d
004F04BA  33 D2                           xor edx, edx
004F04BC  0F B7 CE                        movzx ecx, si
004F04BF  41 8B C4                        mov eax, r12d
004F04C2  F7 F1                           div ecx
004F04C4  33 D2                           xor edx, edx
004F04C6  0F B7 CF                        movzx ecx, di
004F04C9  44 8B F0                        mov r14d, eax
004F04CC  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
004F04D0  41 8B C4                        mov eax, r12d
004F04D3  F7 F1                           div ecx
004F04D5  66 45 85 ED                     test r13w, r13w
004F04D9  44 8A 6C 24 20                  mov r13b, byte ptr [rsp + 0x20]
004F04DE  44 8B E0                        mov r12d, eax
004F04E1  0F 84 05 01 00 00               je 0x1404f05ec
004F04E7  66 44 39 44 24 48               cmp word ptr [rsp + 0x48], r8w
004F04ED  0F 86 F9 00 00 00               jbe 0x1404f05ec
004F04F3  48 8B 75 78                     mov rsi, qword ptr [rbp + 0x78]
004F04F7  48 8D 45 70                     lea rax, [rbp + 0x70]
004F04FB  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F0501  44 0F B7 74 24 40               movzx r14d, word ptr [rsp + 0x40]
004F0507  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004F050C  0F B7 4D 70                     movzx ecx, word ptr [rbp + 0x70]
004F0510  48 85 F6                        test rsi, rsi
004F0513  75 22                           jne 0x1404f0537
004F0515  66 45 03 F1                     add r14w, r9w
004F0519  41 0F B7 C6                     movzx eax, r14w
004F051D  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F0522  3B C1                           cmp eax, ecx
004F0524  0F 83 BD 00 00 00               jae 0x1404f05e7
004F052A  48 8B 74 C5 78                  mov rsi, qword ptr [rbp + rax*8 + 0x78]
004F052F  44 0F B7 74 24 40               movzx r14d, word ptr [rsp + 0x40]
004F0535  EB D9                           jmp 0x1404f0510
004F0537  48 0F BC D6                     bsf rdx, rsi
004F053B  41 0F B7 CE                     movzx ecx, r14w
004F053F  0F B6 C2                        movzx eax, dl
004F0542  C1 E1 06                        shl ecx, 6
004F0545  48 0F B3 C6                     btr rsi, rax
004F0549  0F B6 C2                        movzx eax, dl
004F054C  03 C8                           add ecx, eax
004F054E  48 8B 05 63 2C A3 00            mov rax, qword ptr [rip + 0xa32c63]
004F0555  8B 1C 88                        mov ebx, dword ptr [rax + rcx*4]
004F0558  8B CB                           mov ecx, ebx
004F055A  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
004F055E  E8 6D 80 DE FF                  call 0x1402d85d0
004F0563  48 8B 0D 46 2C A3 00            mov rcx, qword ptr [rip + 0xa32c46]
004F056A  4C 8B C8                        mov r9, rax
004F056D  44 8B 04 99                     mov r8d, dword ptr [rcx + rbx*4]
004F0571  41 8B C0                        mov eax, r8d
004F0574  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
004F0579  C1 E8 06                        shr eax, 6
004F057C  3B C8                           cmp ecx, eax
004F057E  76 16                           jbe 0x1404f0596
004F0580  8B D0                           mov edx, eax
004F0582  41 8B C8                        mov ecx, r8d
004F0585  48 8B 44 C4 68                  mov rax, qword ptr [rsp + rax*8 + 0x68]
004F058A  83 E1 3F                        and ecx, 0x3f
004F058D  48 0F B3 C8                     btr rax, rcx
004F0591  48 89 44 D4 68                  mov qword ptr [rsp + rdx*8 + 0x68], rax
004F0596  41 8B D4                        mov edx, r12d
004F0599  49 8D 89 B0 89 00 00            lea rcx, [r9 + 0x89b0]
004F05A0  E8 83 A0 F6 FF                  call 0x14045a628
004F05A5  45 33 C0                        xor r8d, r8d
004F05A8  8B C8                           mov ecx, eax
004F05AA  41 3B 81 D8 89 00 00            cmp eax, dword ptr [r9 + 0x89d8]
004F05B1  77 11                           ja 0x1404f05c4
004F05B3  45 84 ED                        test r13b, r13b
004F05B6  74 13                           je 0x1404f05cb
004F05B8  41 8B 81 DC 89 00 00            mov eax, dword ptr [r9 + 0x89dc]
004F05BF  3B C1                           cmp eax, ecx
004F05C1  0F 47 C8                        cmova ecx, eax
004F05C4  41 89 89 D8 89 00 00            mov dword ptr [r9 + 0x89d8], ecx
004F05CB  0F B7 C7                        movzx eax, di
004F05CE  41 B9 01 00 00 00               mov r9d, 1
004F05D4  66 41 2B C1                     sub ax, r9w
004F05D8  66 85 FF                        test di, di
004F05DB  66 0F 44 C7                     cmove ax, di
004F05DF  0F B7 F8                        movzx edi, ax
004F05E2  E9 25 FF FF FF                  jmp 0x1404f050c
004F05E7  44 8B 74 24 2C                  mov r14d, dword ptr [rsp + 0x2c]
004F05EC  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
004F05F1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
004F05F6  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F05FC  0F B7 5C 24 40                  movzx ebx, word ptr [rsp + 0x40]
004F0601  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004F0606  EB 06                           jmp 0x1404f060e
004F0608  41 B9 01 00 00 00               mov r9d, 1
004F060E  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
004F0613  48 85 FF                        test rdi, rdi
004F0616  75 20                           jne 0x1404f0638
004F0618  66 41 03 D9                     add bx, r9w
004F061C  0F B7 C3                        movzx eax, bx
004F061F  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F0624  3B C1                           cmp eax, ecx
004F0626  0F 83 B6 00 00 00               jae 0x1404f06e2
004F062C  48 8B 7C C4 68                  mov rdi, qword ptr [rsp + rax*8 + 0x68]
004F0631  0F B7 5C 24 40                  movzx ebx, word ptr [rsp + 0x40]
004F0636  EB DB                           jmp 0x1404f0613
004F0638  48 0F BC D7                     bsf rdx, rdi
004F063C  0F B7 CB                        movzx ecx, bx
004F063F  0F B6 C2                        movzx eax, dl
004F0642  C1 E1 06                        shl ecx, 6
004F0645  48 0F B3 C7                     btr rdi, rax
004F0649  0F B6 C2                        movzx eax, dl
004F064C  03 C8                           add ecx, eax
004F064E  48 8B 05 63 2B A3 00            mov rax, qword ptr [rip + 0xa32b63]
004F0655  8B 34 88                        mov esi, dword ptr [rax + rcx*4]
004F0658  8B CE                           mov ecx, esi
004F065A  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
004F065E  E8 6D 7F DE FF                  call 0x1402d85d0
004F0663  4C 8D 88 B0 89 00 00            lea r9, [rax + 0x89b0]
004F066A  41 8B 51 28                     mov edx, dword ptr [r9 + 0x28]
004F066E  49 8B C9                        mov rcx, r9
004F0671  E8 1E 2D F2 FF                  call 0x140413394
004F0676  41 B8 00 00 00 00               mov r8d, 0
004F067C  44 3B F0                        cmp r14d, eax
004F067F  77 87                           ja 0x1404f0608
004F0681  48 8B 0D 28 2B A3 00            mov rcx, qword ptr [rip + 0xa32b28]
004F0688  0F B7 44 24 60                  movzx eax, word ptr [rsp + 0x60]
004F068D  44 8B 04 B1                     mov r8d, dword ptr [rcx + rsi*4]
004F0691  41 8B C8                        mov ecx, r8d
004F0694  C1 E9 06                        shr ecx, 6
004F0697  3B C1                           cmp eax, ecx
004F0699  76 16                           jbe 0x1404f06b1
004F069B  8B D1                           mov edx, ecx
004F069D  41 8B C8                        mov ecx, r8d
004F06A0  83 E1 3F                        and ecx, 0x3f
004F06A3  48 8B 44 D4 68                  mov rax, qword ptr [rsp + rdx*8 + 0x68]
004F06A8  48 0F B3 C8                     btr rax, rcx
004F06AC  48 89 44 D4 68                  mov qword ptr [rsp + rdx*8 + 0x68], rax
004F06B1  41 8B D4                        mov edx, r12d
004F06B4  49 8B C9                        mov rcx, r9
004F06B7  E8 6C 9F F6 FF                  call 0x14045a628
004F06BC  45 33 C0                        xor r8d, r8d
004F06BF  8B C8                           mov ecx, eax
004F06C1  41 3B 41 28                     cmp eax, dword ptr [r9 + 0x28]
004F06C5  77 12                           ja 0x1404f06d9
004F06C7  45 84 ED                        test r13b, r13b
004F06CA  0F 84 38 FF FF FF               je 0x1404f0608
004F06D0  41 8B 41 2C                     mov eax, dword ptr [r9 + 0x2c]
004F06D4  3B C1                           cmp eax, ecx
004F06D6  0F 47 C8                        cmova ecx, eax
004F06D9  41 89 49 28                     mov dword ptr [r9 + 0x28], ecx
004F06DD  E9 26 FF FF FF                  jmp 0x1404f0608
004F06E2  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
004F06E7  BE B0 89 00 00                  mov esi, 0x89b0
004F06EC  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F06F2  0F B7 7C 24 40                  movzx edi, word ptr [rsp + 0x40]
004F06F7  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
004F06FC  48 85 DB                        test rbx, rbx
004F06FF  75 1C                           jne 0x1404f071d
004F0701  66 41 03 F9                     add di, r9w
004F0705  0F B7 C7                        movzx eax, di
004F0708  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F070D  3B C1                           cmp eax, ecx
004F070F  73 4D                           jae 0x1404f075e
004F0711  48 8B 5C C4 68                  mov rbx, qword ptr [rsp + rax*8 + 0x68]
004F0716  0F B7 7C 24 40                  movzx edi, word ptr [rsp + 0x40]
004F071B  EB DF                           jmp 0x1404f06fc
004F071D  48 0F BC D3                     bsf rdx, rbx
004F0721  0F B7 CF                        movzx ecx, di
004F0724  0F B6 C2                        movzx eax, dl
004F0727  48 0F B3 C3                     btr rbx, rax
004F072B  C1 E1 06                        shl ecx, 6
004F072E  0F B6 C2                        movzx eax, dl
004F0731  03 C8                           add ecx, eax
004F0733  48 8B 05 7E 2A A3 00            mov rax, qword ptr [rip + 0xa32a7e]
004F073A  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
004F073D  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
004F0741  E8 8A 7E DE FF                  call 0x1402d85d0
004F0746  41 8B D6                        mov edx, r14d
004F0749  48 8D 0C 06                     lea rcx, [rsi + rax]
004F074D  E8 D6 9E F6 FF                  call 0x14045a628
004F0752  45 33 C0                        xor r8d, r8d
004F0755  89 41 28                        mov dword ptr [rcx + 0x28], eax
004F0758  45 8D 48 01                     lea r9d, [r8 + 1]
004F075C  EB 99                           jmp 0x1404f06f7
004F075E  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
004F0763  48 85 FF                        test rdi, rdi
004F0766  74 66                           je 0x1404f07ce
004F0768  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004F076D  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0772  49 8B D7                        mov rdx, r15
004F0775  E8 F6 53 DE FF                  call 0x1402d5b70
004F077A  33 C0                           xor eax, eax
004F077C  8B D8                           mov ebx, eax
004F077E  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
004F0783  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004F0788  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004F078D  EB 27                           jmp 0x1404f07b6
004F078F  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
004F0793  E8 38 7E DE FF                  call 0x1402d85d0
004F0798  48 03 C6                        add rax, rsi
004F079B  8B 50 28                        mov edx, dword ptr [rax + 0x28]
004F079E  81 FA 10 27 00 00               cmp edx, 0x2710
004F07A4  76 10                           jbe 0x1404f07b6
004F07A6  81 C2 F0 D8 FF FF               add edx, 0xffffd8f0
004F07AC  48 8B C8                        mov rcx, rax
004F07AF  E8 E0 2B F2 FF                  call 0x140413394
004F07B4  03 D8                           add ebx, eax
004F07B6  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
004F07BB  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
004F07C0  E8 BB 4C F2 FF                  call 0x140415480
004F07C5  45 33 C0                        xor r8d, r8d
004F07C8  85 C0                           test eax, eax
004F07CA  74 C3                           je 0x1404f078f
004F07CC  89 1F                           mov dword ptr [rdi], ebx
004F07CE  45 84 ED                        test r13b, r13b
004F07D1  74 3E                           je 0x1404f0811
004F07D3  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
004F07D7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004F07DC  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F07E2  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
004F07E7  EB 15                           jmp 0x1404f07fe
004F07E9  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
004F07ED  E8 DE 7D DE FF                  call 0x1402d85d0
004F07F2  8B 88 DC 89 00 00               mov ecx, dword ptr [rax + 0x89dc]
004F07F8  89 88 D8 89 00 00               mov dword ptr [rax + 0x89d8], ecx
004F07FE  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
004F0803  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
004F0808  E8 73 4C F2 FF                  call 0x140415480
004F080D  85 C0                           test eax, eax
004F080F  74 D8                           je 0x1404f07e9
004F0811  48 8B 8D 80 01 00 00            mov rcx, qword ptr [rbp + 0x180]
004F0818  48 33 CC                        xor rcx, rsp
004F081B  E8 20 BE 1B 00                  call 0x1406ac640
004F0820  48 8B 9C 24 E0 02 00 00         mov rbx, qword ptr [rsp + 0x2e0]
004F0828  48 81 C4 90 02 00 00            add rsp, 0x290
004F082F  41 5F                           pop r15
004F0831  41 5E                           pop r14
004F0833  41 5D                           pop r13
004F0835  41 5C                           pop r12
004F0837  5F                              pop rdi
004F0838  5E                              pop rsi
004F0839  5D                              pop rbp
004F083A  C3                              ret
004F083B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkDistributeUtilityEx(__int64 a1, __int64 a2, unsigned __int16 a3, unsigned __int8 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int16 v_stack_m156;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m264;
    unsigned __int16 v_stack_m266;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned int v_stack_m29C;
    unsigned __int16 v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned __int8 v_stack_m2A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (656);
    result = (*(unsigned __int64 *)(v_rip + 9544974)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m278 = a6;
    result = 0;
    v_stack_m270 = a1;
    v_stack_m288 = 0;
    v_stack_m2A8 = a4;
    v_stack_m29C = a3;
    a2 = 0;
    v_stack_m298 = v_xmm0;
    result = memset(v_stack_m150, a2, 256, a4);
    v_rdi = 0;
    v_stack_m2A4 = 0;
    a2 = 0;
    result = memset(v_stack_m260, a2, 256, a4);
    v_stack_m2A0 = 0;
    a2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, a2, 256, a4);
    a2 = 0;
    v_stack_m268 = 0x200001ULL;
    result = memset(v_stack_m260, a2, 256, a4);
    result = KiXorAffinityEx(a1, 0, v_stack_m268, v_stack_m266);
    v_stack_m298 = v_stack_m268;
    a3 = 0;
loc_004F0313:
    v_stack_m280 = 0;
loc_004F031D:
    if (v_stack_m260 != 0) goto loc_004F0344;
    v_r14 = (unsigned __int16)((v_stack_m288) + ((unsigned __int16)(v_rdi + 1)));
    v_stack_m288 = (unsigned __int16)((unsigned __int16)(v_r14));
    if (((unsigned int)((unsigned __int16)(v_r14))) >= ((unsigned int)(v_stack_m268))) goto loc_004F0406;
    goto loc_004F031D;
loc_004F0344:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) << (6));
    a1 = (unsigned int)((a1) + (0));
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10694230) + a1 * 4)));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10694230) + a1 * 4)))), 0, a3, v_rdi + 1);
    a3 = 0;
    if ((*(unsigned __int8 *)(result + 35336)) != 0) goto loc_004F0398;
    v_r13 = (unsigned __int16)((v_stack_m2A0) + 1);
    v_stack_m2A0 = (unsigned __int16)(v_r13);
    goto loc_004F03E8;
loc_004F0398:
    v_rdi = (unsigned __int16)((v_rdi) + (1));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10694161) + v_r13 * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10694161) + v_r13 * 4))))) >> (6));
    if (((unsigned int)(v_stack_m158)) > ((unsigned int)(a1))) goto loc_004F03CC;
    if (((unsigned int)(v_stack_m156)) <= ((unsigned int)(a1))) goto loc_004F03DF;
    v_stack_m158 = (unsigned __int16)(1 + a1 * 1);
loc_004F03CC:
    *(unsigned __int64 *)(v_stack_m1C8 + (unsigned int)((unsigned int)(a1)) * 8 + 120) = *(unsigned __int64 *)(v_stack_m1C8 + a1 * 8 + 120);
loc_004F03DF:
    a3 = 0;
loc_004F03E8:
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (unsigned int)(*(unsigned int *)(result + 35248 + 40)), a3, result + 35248);
    v_r12 = (unsigned int)(((unsigned int)(a5)) + ((unsigned int)(result)));
    v_rsi = (unsigned __int16)((0) + (1));
    goto loc_004F0313;
loc_004F0406:
    v_stack_m280 = (unsigned __int16)(v_rdi);
    v_stack_m288 = 0;
    v_stack_m298 = 0;
loc_004F0423:
    v_stack_m29C = 0;
    if (0 == 0) goto loc_004F0433;
    goto loc_004F0439;
loc_004F0433:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) + (1));
loc_004F0439:
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_004F045A;
    v_rbx = (unsigned __int16)((v_stack_m288) + (1));
    v_stack_m288 = (unsigned __int16)((unsigned __int16)(v_rbx));
    if (((unsigned int)((unsigned __int16)(v_rbx))) >= ((unsigned int)(a1))) goto loc_004F04A1;
    goto loc_004F0439;
loc_004F045A:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 35248 + 40))))));
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693953) + a1 * 4)));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693953) + a1 * 4)), (unsigned int)(*(unsigned int *)(result + 35248 + 40)), a3, 1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 35248 + 40))) - (*(unsigned int *)(result + 35248 + 44)));
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, a2, a3, 1);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(result)));
    a3 = 0;
    goto loc_004F0423;
loc_004F04A1:
    if (((unsigned __int16)(v_rsi)) <= ((unsigned __int16)(a3 + 1))) {
        v_rsi = (unsigned int)(a3 + 1);
    }
    v_rdi = (unsigned int)(v_stack_m29C);
    if (((unsigned __int16)((unsigned int)(v_stack_m29C))) >= ((unsigned __int16)(v_rsi))) { v_rdi = (unsigned __int16)(v_rsi); }
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)(a3 + 1))) {
        v_rdi = (unsigned int)(a3 + 1);
    }
    a2 = 0;
    a2 = 0;
    v_stack_m29C = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    if ((unsigned __int16)(v_stack_m2A0) == 0) goto loc_004F05EC;
    if (v_stack_m280 <= 0) goto loc_004F05EC;
    v_stack_m288 = 0;
    v_stack_m298 = v_stack_m158;
loc_004F050C:
loc_004F0510:
    if (v_stack_m150 != 0) goto loc_004F0537;
    v_r14 = (unsigned __int16)((v_stack_m288) + ((unsigned __int16)(a3 + 1)));
    v_stack_m288 = (unsigned __int16)((unsigned __int16)(v_r14));
    if (((unsigned int)((unsigned __int16)(v_r14))) >= ((unsigned int)(v_stack_m158))) goto loc_004F05E7;
    goto loc_004F0510;
loc_004F0537:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) << (6));
    a1 = (unsigned int)((a1) + (0));
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693731) + a1 * 4)));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693731) + a1 * 4)))), a2, a3, a3 + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693702) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693731) + a1 * 4)) * 4))))) >> (6));
    if (((unsigned int)(v_stack_m268)) >= = ((unsigned int)(result))) {
        a2 = (unsigned int)(result);
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693702) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693731) + a1 * 4)) * 4)));
        result = *(unsigned __int64 *)(v_rsp + result * 8 + 104);
        a1 = (unsigned int)((a1) & (63));
        *(unsigned __int64 *)(v_rsp + a2 * 8 + 104) = result;
    }
    result = PpmHeteroNormalizedUtilityToUtility(result + 35248, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693702) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693731) + a1 * 4)) * 4)), result);
    a3 = 0;
    if (((unsigned int)(result)) > (*(unsigned int *)(result + 35288))) goto loc_004F05C4;
    if ((unsigned __int8)(v_stack_m2A8) == 0) goto loc_004F05CB;
    a1 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 35292)))) > ((unsigned int)((unsigned int)((unsigned int)(result))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 35292))); }
loc_004F05C4:
    *(unsigned int *)(result + 35288) = (unsigned int)(a1);
loc_004F05CB:
    result = (unsigned __int16)(((unsigned __int16)(v_rdi)) - (1));
    if ((unsigned __int16)(v_rdi) == 0) { result = (unsigned __int16)(v_rdi); }
    goto loc_004F050C;
loc_004F05E7:
loc_004F05EC:
    v_stack_m288 = 0;
    v_stack_m298 = v_stack_m268;
    goto loc_004F060E;
loc_004F0608:
loc_004F060E:
loc_004F0613:
    if (v_stack_m260 != 0) goto loc_004F0638;
    v_rbx = (unsigned __int16)((v_stack_m288) + (1));
    v_stack_m288 = (unsigned __int16)((unsigned __int16)(v_rbx));
    if (((unsigned int)((unsigned __int16)(v_rbx))) >= ((unsigned int)(v_stack_m268))) goto loc_004F06E2;
    goto loc_004F0613;
loc_004F0638:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))))))))));
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693475) + a1 * 4)));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693475) + a1 * 4)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))), a3, 1);
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (unsigned int)(*(unsigned int *)(result + 35248 + 40)), a3, result + 35248);
    if (((unsigned int)((unsigned int)(v_stack_m29C))) > ((unsigned int)(result))) goto loc_004F0608;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693416) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693475) + a1 * 4)) * 4))))) >> (6));
    result = v_stack_m268;
    if (((unsigned int)(v_stack_m268)) >= = ((unsigned int)(a1))) {
        a2 = (unsigned int)(a1);
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693416) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693475) + a1 * 4)) * 4)));
        a1 = (unsigned int)((a1) & (63));
        result = *(unsigned __int64 *)(v_rsp + a2 * 8 + 104);
        *(unsigned __int64 *)(v_rsp + a2 * 8 + 104) = result;
    }
    result = PpmHeteroNormalizedUtilityToUtility(result + 35248, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693416) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693475) + a1 * 4)) * 4)), result + 35248);
    a3 = 0;
    if (((unsigned int)(result)) > (*(unsigned int *)(result + 35248 + 40))) goto loc_004F06D9;
    if ((unsigned __int8)(v_stack_m2A8) == 0) goto loc_004F0608;
    a1 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 35248 + 44)))) > ((unsigned int)((unsigned int)((unsigned int)(result))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 35248 + 44))); }
loc_004F06D9:
    *(unsigned int *)(result + 35248 + 40) = (unsigned int)(a1);
    goto loc_004F0608;
loc_004F06E2:
    v_stack_m288 = 0;
loc_004F06F7:
loc_004F06FC:
    if (v_stack_m260 != 0) goto loc_004F071D;
    v_rdi = (unsigned __int16)((v_stack_m288) + ((unsigned __int16)(result + 35248)));
    v_stack_m288 = (unsigned __int16)((unsigned __int16)(v_rdi));
    if (((unsigned int)((unsigned __int16)(v_rdi))) >= ((unsigned int)(v_stack_m268))) goto loc_004F075E;
    goto loc_004F06FC;
loc_004F071D:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m288)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))))))))));
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693246) + a1 * 4)));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10693246) + a1 * 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))), a3, result + 35248);
    result = PpmHeteroNormalizedUtilityToUtility((unsigned int)(0x89B0ULL) + result * 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m29C))), a3, result + 35248);
    a3 = 0;
    *(unsigned int *)((unsigned int)(0x89B0ULL) + result * 1 + 40) = (unsigned int)(result);
    goto loc_004F06F7;
loc_004F075E:
    if (v_stack_m278 == 0) goto loc_004F07CE;
    result = KeXorAffinityEx2(v_stack_m270, a2, v_stack_m268, a3 + 1);
    result = 0;
    v_stack_m288 = 0;
    v_stack_m290 = v_stack_m260;
    goto loc_004F07B6;
loc_004F078F:
    result = KeGetPrcb((unsigned int)(v_stack_m2A4), a2, v_stack_m268, a3 + 1);
    result = (result) + ((unsigned int)(0x89B0ULL));
    v_rbx = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 40)))) >= = 0x2710ULL) {
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) + (0xFFFFD8F0ULL));
        a1 = result;
        result = PpmHeteroUtilityToNormalizedUtility(a1, a2, v_stack_m268, a3 + 1);
        v_rbx = (unsigned int)((0) + ((unsigned int)(result)));
    }
    result = KeEnumerateNextProcessor(v_stack_m2A4, v_stack_m298, v_stack_m268, a3 + 1);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_004F078F;
    *(unsigned int *)(v_stack_m278) = (unsigned int)(v_rbx);
loc_004F07CE:
    if ((unsigned __int8)(v_stack_m2A8) == 0) goto loc_004F0811;
    v_stack_m290 = *(unsigned __int64 *)(a2 + 8);
    v_stack_m288 = 0;
    v_stack_m298 = a2;
    goto loc_004F07FE;
loc_004F07E9:
    result = KeGetPrcb((unsigned int)(v_stack_m2A4), v_stack_m298, a3, a3 + 1);
    *(unsigned int *)(result + 35288) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 35292)));
loc_004F07FE:
    result = KeEnumerateNextProcessor(v_stack_m2A4, v_stack_m298, a3, a3 + 1);
    if ((unsigned int)(result) == 0) goto loc_004F07E9;
loc_004F0811:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m298, a3, a3 + 1);
    v_rsp = (v_rsp) + (656);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkDistributeUtilityEx(int64_t Arg1, void *Arg2, uint16_t Arg3, uint8_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint16_t v_stack_m156;
    uint32_t v_stack_m158;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m260;
    uint32_t v_stack_m264;
    uint16_t v_stack_m266;
    uint32_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint32_t v_stack_m29C;
    uint16_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint8_t v_stack_m2A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (656);
    result = (*(uint64_t *)(v_rip + 0x91A50E)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m278 = Arg6;
    result = 0;
    v_stack_m270 = Arg1;
    v_stack_m288 = 0;
    v_stack_m2A8 = Arg4;
    v_stack_m29C = Arg3;
    Arg2 = 0;
    v_stack_m298 = v_xmm0;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    local_rdi = 0;
    v_stack_m2A4 = 0;
    Arg2 = 0;
    result = memset(v_stack_m260, Arg2, 256, Arg4);
    v_stack_m2A0 = 0;
    Arg2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    Arg2 = 0;
    v_stack_m268 = 0x200001ULL;
    result = memset(v_stack_m260, Arg2, 256, Arg4);
    result = KiXorAffinityEx(Arg1, 0, v_stack_m268, v_stack_m266);
    v_stack_m298 = v_stack_m268;
    Arg3 = 0;
loc_004F0313:
    v_stack_m280 = 0;
loc_004F031D:
    if (v_stack_m260 != 0) goto loc_004F0344;
    local_r14 = (uint16_t)((v_stack_m288) + ((uint16_t)(local_rdi + 1)));
    v_stack_m288 = (uint16_t)((uint16_t)(local_r14));
    if (((uint32_t)((uint16_t)(local_r14))) >= ((uint32_t)(v_stack_m268))) goto loc_004F0406;
    goto loc_004F031D;
loc_004F0344:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32E56) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32E56) + Arg1 * 4)))), 0, Arg3, local_rdi + 1);
    Arg3 = 0;
    if ((*(uint8_t *)(result + 0x8A08)) != 0) goto loc_004F0398;
    local_r13 = (uint16_t)((v_stack_m2A0) + 1);
    v_stack_m2A0 = (uint16_t)(local_r13);
    goto loc_004F03E8;
loc_004F0398:
    local_rdi = (uint16_t)((local_rdi) + (1));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32E11) + local_r13 * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32E11) + local_r13 * 4))))) >> (6));
    if (((uint32_t)(v_stack_m158)) > ((uint32_t)(Arg1))) goto loc_004F03CC;
    if (((uint32_t)(v_stack_m156)) <= ((uint32_t)(Arg1))) goto loc_004F03DF;
    v_stack_m158 = (uint16_t)(1 + Arg1 * 1);
loc_004F03CC:
    *(uint64_t *)(v_stack_m1C8 + (uint32_t)((uint32_t)(Arg1)) * 8 + 0x78) = *(uint64_t *)(v_stack_m1C8 + Arg1 * 8 + 0x78);
loc_004F03DF:
    Arg3 = 0;
loc_004F03E8:
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28)), Arg3, result + 35248);
    local_r12 = (uint32_t)(((uint32_t)(Arg5)) + ((uint32_t)(result)));
    local_rsi = (uint16_t)((0) + (1));
    goto loc_004F0313;
loc_004F0406:
    v_stack_m280 = (uint16_t)(local_rdi);
    v_stack_m288 = 0;
    v_stack_m298 = 0;
loc_004F0423:
    v_stack_m29C = 0;
    if (0 == 0) goto loc_004F0433;
    goto loc_004F0439;
loc_004F0433:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) + (1));
loc_004F0439:
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_004F045A;
    local_rbx = (uint16_t)((v_stack_m288) + (1));
    v_stack_m288 = (uint16_t)((uint16_t)(local_rbx));
    if (((uint32_t)((uint16_t)(local_rbx))) >= ((uint32_t)(Arg1))) goto loc_004F04A1;
    goto loc_004F0439;
loc_004F045A:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28))))));
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32D41) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32D41) + Arg1 * 4)), (uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28)), Arg3, 1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28))) - (*(uint32_t *)(result + 0x89B0 + 0x2C)));
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, Arg2, Arg3, 1);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(result)));
    Arg3 = 0;
    goto loc_004F0423;
loc_004F04A1:
    if (((uint16_t)(local_rsi)) <= ((uint16_t)(Arg3 + 1))) {
        local_rsi = (uint32_t)(Arg3 + 1);
    }
    local_rdi = (uint32_t)(v_stack_m29C);
    if (((uint16_t)((uint32_t)(v_stack_m29C))) >= ((uint16_t)(local_rsi))) { local_rdi = (uint16_t)(local_rsi); }
    if (((uint16_t)(local_rdi)) <= ((uint16_t)(Arg3 + 1))) {
        local_rdi = (uint32_t)(Arg3 + 1);
    }
    Arg2 = 0;
    Arg2 = 0;
    v_stack_m29C = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    if ((uint16_t)(v_stack_m2A0) == 0) goto loc_004F05EC;
    if (v_stack_m280 <= 0) goto loc_004F05EC;
    v_stack_m288 = 0;
    v_stack_m298 = v_stack_m158;
loc_004F050C:
loc_004F0510:
    if (v_stack_m150 != 0) goto loc_004F0537;
    local_r14 = (uint16_t)((v_stack_m288) + ((uint16_t)(Arg3 + 1)));
    v_stack_m288 = (uint16_t)((uint16_t)(local_r14));
    if (((uint32_t)((uint16_t)(local_r14))) >= ((uint32_t)(v_stack_m158))) goto loc_004F05E7;
    goto loc_004F0510;
loc_004F0537:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C63) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C63) + Arg1 * 4)))), Arg2, Arg3, Arg3 + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C46) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C63) + Arg1 * 4)) * 4))))) >> (6));
    if (((uint32_t)(v_stack_m268)) >= = ((uint32_t)(result))) {
        Arg2 = (uint32_t)(result);
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C46) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C63) + Arg1 * 4)) * 4)));
        result = *(uint64_t *)(local_rsp + result * 8 + 0x68);
        Arg1 = (uint32_t)((Arg1) & (63));
        *(uint64_t *)(local_rsp + arg2 * 8 + 0x68) = result;
    }
    result = PpmHeteroNormalizedUtilityToUtility(result + 35248, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C46) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32C63) + Arg1 * 4)) * 4)), result);
    Arg3 = 0;
    if (((uint32_t)(result)) > (*(uint32_t *)(result + 0x89D8))) goto loc_004F05C4;
    if ((uint8_t)(v_stack_m2A8) == 0) goto loc_004F05CB;
    Arg1 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC)))) > ((uint32_t)((uint32_t)((uint32_t)(result))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC))); }
loc_004F05C4:
    *(uint32_t *)(result + 0x89D8) = (uint32_t)(Arg1);
loc_004F05CB:
    result = (uint16_t)(((uint16_t)(local_rdi)) - (1));
    if ((uint16_t)(local_rdi) == 0) { result = (uint16_t)(local_rdi); }
    goto loc_004F050C;
loc_004F05E7:
loc_004F05EC:
    v_stack_m288 = 0;
    v_stack_m298 = v_stack_m268;
    goto loc_004F060E;
loc_004F0608:
loc_004F060E:
loc_004F0613:
    if (v_stack_m260 != 0) goto loc_004F0638;
    local_rbx = (uint16_t)((v_stack_m288) + (1));
    v_stack_m288 = (uint16_t)((uint16_t)(local_rbx));
    if (((uint32_t)((uint16_t)(local_rbx))) >= ((uint32_t)(v_stack_m268))) goto loc_004F06E2;
    goto loc_004F0613;
loc_004F0638:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))))))))));
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B63) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B63) + Arg1 * 4)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))), Arg3, 1);
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28)), Arg3, result + 35248);
    if (((uint32_t)((uint32_t)(v_stack_m29C))) > ((uint32_t)(result))) goto loc_004F0608;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B28) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B63) + Arg1 * 4)) * 4))))) >> (6));
    result = v_stack_m268;
    if (((uint32_t)(v_stack_m268)) >= = ((uint32_t)(Arg1))) {
        Arg2 = (uint32_t)(Arg1);
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B28) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B63) + Arg1 * 4)) * 4)));
        Arg1 = (uint32_t)((Arg1) & (63));
        result = *(uint64_t *)(local_rsp + arg2 * 8 + 0x68);
        *(uint64_t *)(local_rsp + arg2 * 8 + 0x68) = result;
    }
    result = PpmHeteroNormalizedUtilityToUtility(result + 35248, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B28) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32B63) + Arg1 * 4)) * 4)), result + 35248);
    Arg3 = 0;
    if (((uint32_t)(result)) > (*(uint32_t *)(result + 0x89B0 + 0x28))) goto loc_004F06D9;
    if ((uint8_t)(v_stack_m2A8) == 0) goto loc_004F0608;
    Arg1 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x2C)))) > ((uint32_t)((uint32_t)((uint32_t)(result))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x2C))); }
loc_004F06D9:
    *(uint32_t *)(result + 0x89B0 + 0x28) = (uint32_t)(Arg1);
    goto loc_004F0608;
loc_004F06E2:
    v_stack_m288 = 0;
loc_004F06F7:
loc_004F06FC:
    if (v_stack_m260 != 0) goto loc_004F071D;
    local_rdi = (uint16_t)((v_stack_m288) + ((uint16_t)(result + 35248)));
    v_stack_m288 = (uint16_t)((uint16_t)(local_rdi));
    if (((uint32_t)((uint16_t)(local_rdi))) >= ((uint32_t)(v_stack_m268))) goto loc_004F075E;
    goto loc_004F06FC;
loc_004F071D:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m288)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))))))))));
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32A7E) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA32A7E) + Arg1 * 4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))), Arg3, result + 35248);
    result = PpmHeteroNormalizedUtilityToUtility((uint32_t)(0x89B0ULL) + result * 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m29C))), Arg3, result + 35248);
    Arg3 = 0;
    *(uint32_t *)((uint32_t)(0x89B0ULL) + result * 1 + 0x28) = (uint32_t)(result);
    goto loc_004F06F7;
loc_004F075E:
    if (v_stack_m278 == 0) goto loc_004F07CE;
    result = KeXorAffinityEx2(v_stack_m270, Arg2, v_stack_m268, Arg3 + 1);
    result = 0;
    v_stack_m288 = 0;
    v_stack_m290 = v_stack_m260;
    goto loc_004F07B6;
loc_004F078F:
    result = KeGetPrcb((uint32_t)(v_stack_m2A4), Arg2, v_stack_m268, Arg3 + 1);
    result = (result) + ((uint32_t)(0x89B0ULL));
    local_rbx = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) >= = 0x2710ULL) {
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) + (0xFFFFD8F0ULL));
        Arg1 = result;
        result = PpmHeteroUtilityToNormalizedUtility(Arg1, Arg2, v_stack_m268, Arg3 + 1);
        local_rbx = (uint32_t)((0) + ((uint32_t)(result)));
    }
    result = KeEnumerateNextProcessor(v_stack_m2A4, v_stack_m298, v_stack_m268, Arg3 + 1);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_004F078F;
    *(uint32_t *)(v_stack_m278) = (uint32_t)(local_rbx);
loc_004F07CE:
    if ((uint8_t)(v_stack_m2A8) == 0) goto loc_004F0811;
    v_stack_m290 = *(uint64_t *)(arg2 + 0x8);
    v_stack_m288 = 0;
    v_stack_m298 = Arg2;
    goto loc_004F07FE;
loc_004F07E9:
    result = KeGetPrcb((uint32_t)(v_stack_m2A4), v_stack_m298, Arg3, Arg3 + 1);
    *(uint32_t *)(result + 0x89D8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC)));
loc_004F07FE:
    result = KeEnumerateNextProcessor(v_stack_m2A4, v_stack_m298, Arg3, Arg3 + 1);
    if ((uint32_t)(result) == 0) goto loc_004F07E9;
loc_004F0811:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m298, Arg3, Arg3 + 1);
    local_rsp = (local_rsp) + (656);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F020C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
