# PpmParkApplyPolicyEx

- RVA: `0x004F3090`–`0x004F3949` (길이 `2,233` bytes)
- VA: `0x00000001404F3090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9548`
- 디코드: `552`개 명령, `2,233/2,233` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x004F30E5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F30F6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F3139` → [PpmParkEvalualteSmtUnparkPolicy](../4C/PpmParkEvalualteSmtUnparkPolicy_function_004C0868.md) (function, `0x004C0868`)
- `0x004F3144` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F31D0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F31F1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F32AB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F32CB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F33E2` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x004F33F7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F348F` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004F34B7` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x004F34E2` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x004F3595` → [PpmEventParkNodeParkHintChangedEx](PpmEventParkNodeParkHintChangedEx_function_004F3A34.md) (function, `0x004F3A34`)
- `0x004F36AB` → [PpmConfigureRestrictionPolicy](../4A/PpmConfigureRestrictionPolicy_function_004A0398.md) (function, `0x004A0398`)
- `0x004F380A` → [PpmEventParkNodeCapChangeEx](../5D/PpmEventParkNodeCapChangeEx_function_005DE580.md) (function, `0x005DE580`)
- `0x004F3880` → [PpmEventSoftParkLatencyUpdate](PpmEventSoftParkLatencyUpdate_function_004F3950.md) (function, `0x004F3950`)
- `0x004F38C0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F38D5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F38DA` → [KeUpdateSoftParkRankList](../2D/KeUpdateSoftParkRankList_function_002D5998.md) (function, `0x002D5998`)
- `0x004F38DF` → [PpmEventSoftParkRankListChanged](../2D/PpmEventSoftParkRankListChanged_function_002D58D8.md) (function, `0x002D58D8`)
- `0x004F3908` → [PpmConvertTime](../44/PpmConvertTime_function_00447530.md) (function, `0x00447530`)
- `0x004F3913` → [PpmHeteroHgsCheckContainmentDecision](../3B/PpmHeteroHgsCheckContainmentDecision_function_003BEFF8.md) (function, `0x003BEFF8`)
- `0x004F3922` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkApplyPolicy](../4B/PpmParkApplyPolicy_function_004B613C.md) at `0x004B684D`

### Static image references
- `0x004F30B6` → RVA `0x00E0A740` (`.data`; read)
- `0x004F30FD` → RVA `0x00F083D8` (`.data`; read)
- `0x004F3106` → RVA `0x00F23454` (`.data`; write)
- `0x004F3111` → RVA `0x00E08380` (`.data`; read)
- `0x004F3118` → RVA `0x00F0CE0C` (`.data`; read)
- `0x004F315C` → RVA `0x00FC6D50` (`ALMOSTRO`; read)
- `0x004F3170` → RVA `0x00F083E0` (`.data`; read)
- `0x004F3178` → RVA `0x00F083A2` (`.data`; read)
- `0x004F317F` → RVA `0x00E67A40` (`.data`; read)
- `0x004F3187` → RVA `0x00E67A44` (`.data`; read)
- `0x004F347F` → RVA `0x00F231B8` (`.data`; read)
- `0x004F35C8` → RVA `0x00FC5038` (`ALMOSTRO`; read)
- `0x004F3845` → RVA `0x00F0E0F0` (`.data`; read)
- `0x004F3858` → RVA `0x00FC5094` (`ALMOSTRO`; read)
- `0x004F3889` → RVA `0x00F083C8` (`.data`; read)
- `0x004F3890` → RVA `0x00FC6AF1` (`ALMOSTRO`; write)
- `0x004F38A2` → RVA `0x00F083B8` (`.data`; read)
- `0x004F38AE` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F3090  48 8B C4                        mov rax, rsp
004F3093  48 89 58 08                     mov qword ptr [rax + 8], rbx
004F3097  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
004F309B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
004F309F  55                              push rbp
004F30A0  41 54                           push r12
004F30A2  41 55                           push r13
004F30A4  41 56                           push r14
004F30A6  41 57                           push r15
004F30A8  48 8D A8 38 FE FF FF            lea rbp, [rax - 0x1c8]
004F30AF  48 81 EC A0 02 00 00            sub rsp, 0x2a0
004F30B6  48 8B 05 83 76 91 00            mov rax, qword ptr [rip + 0x917683]
004F30BD  48 33 C4                        xor rax, rsp
004F30C0  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
004F30C7  0F 57 C0                        xorps xmm0, xmm0
004F30CA  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
004F30CF  33 C0                           xor eax, eax
004F30D1  BB 00 01 00 00                  mov ebx, 0x100
004F30D6  44 8B C3                        mov r8d, ebx
004F30D9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004F30DE  33 D2                           xor edx, edx
004F30E0  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
004F30E5  E8 56 3B 1D 00                  call 0x1406c6c40
004F30EA  44 8B C3                        mov r8d, ebx
004F30ED  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
004F30F4  33 D2                           xor edx, edx
004F30F6  E8 45 3B 1D 00                  call 0x1406c6c40
004F30FB  33 DB                           xor ebx, ebx
004F30FD  48 39 1D D4 52 A1 00            cmp qword ptr [rip + 0xa152d4], rbx
004F3104  75 0B                           jne 0x1404f3111
004F3106  89 1D 48 03 A3 00               mov dword ptr [rip + 0xa30348], ebx
004F310C  E9 07 08 00 00                  jmp 0x1404f3918
004F3111  4C 8B 3D 68 52 91 00            mov r15, qword ptr [rip + 0x915268]
004F3118  48 63 05 ED 9C A1 00            movsxd rax, dword ptr [rip + 0xa19ced]
004F311F  49 83 C7 28                     add r15, 0x28
004F3123  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
004F312A  4C 03 F9                        add r15, rcx
004F312D  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
004F3132  41 8A 8F CA 01 00 00            mov cl, byte ptr [r15 + 0x1ca]
004F3139  E8 2A D7 FC FF                  call 0x1404c0868
004F313E  33 C9                           xor ecx, ecx
004F3140  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
004F3144  E8 87 54 DE FF                  call 0x1402d85d0
004F3149  41 B9 01 00 00 00               mov r9d, 1
004F314F  45 8D 61 3F                     lea r12d, [r9 + 0x3f]
004F3153  48 39 98 B0 89 00 00            cmp qword ptr [rax + 0x89b0], rbx
004F315A  75 14                           jne 0x1404f3170
004F315C  8B 05 EE 3B AD 00               mov eax, dword ptr [rip + 0xad3bee]
004F3162  41 3B C4                        cmp eax, r12d
004F3165  77 04                           ja 0x1404f316b
004F3167  44 0F B7 E0                     movzx r12d, ax
004F316B  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
004F3170  8B 1D 6A 52 A1 00               mov ebx, dword ptr [rip + 0xa1526a]
004F3176  33 D2                           xor edx, edx
004F3178  0F B7 0D 23 52 A1 00            movzx ecx, word ptr [rip + 0xa15223]
004F317F  8B 3D BB 48 97 00               mov edi, dword ptr [rip + 0x9748bb]
004F3185  8B C7                           mov eax, edi
004F3187  44 8B 35 B6 48 97 00            mov r14d, dword ptr [rip + 0x9748b6]
004F318E  F7 F3                           div ebx
004F3190  33 D2                           xor edx, edx
004F3192  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
004F3197  44 8B C0                        mov r8d, eax
004F319A  48 C7 44 24 70 01 00 20 00      mov qword ptr [rsp + 0x70], 0x200001
004F31A3  F7 F1                           div ecx
004F31A5  41 8B C6                        mov eax, r14d
004F31A8  44 2B C2                        sub r8d, edx
004F31AB  33 D2                           xor edx, edx
004F31AD  F7 F3                           div ebx
004F31AF  33 D2                           xor edx, edx
004F31B1  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
004F31B6  44 8B E8                        mov r13d, eax
004F31B9  41 B8 00 01 00 00               mov r8d, 0x100
004F31BF  F7 F1                           div ecx
004F31C1  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
004F31C6  44 2B EA                        sub r13d, edx
004F31C9  33 D2                           xor edx, edx
004F31CB  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
004F31D0  E8 6B 3A 1D 00                  call 0x1406c6c40
004F31D5  33 D2                           xor edx, edx
004F31D7  48 C7 85 80 00 00 00 01 00 20 00  mov qword ptr [rbp + 0x80], 0x200001
004F31E2  41 B8 00 01 00 00               mov r8d, 0x100
004F31E8  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
004F31EF  33 F6                           xor esi, esi
004F31F1  E8 4A 3A 1D 00                  call 0x1406c6c40
004F31F6  0F B7 CE                        movzx ecx, si
004F31F9  66 89 4C 24 24                  mov word ptr [rsp + 0x24], cx
004F31FE  85 DB                           test ebx, ebx
004F3200  0F 84 3E 05 00 00               je 0x1404f3744
004F3206  0F B7 B5 80 00 00 00            movzx esi, word ptr [rbp + 0x80]
004F320D  41 BF 01 00 00 00               mov r15d, 1
004F3213  44 0F B7 0D 87 51 A1 00         movzx r9d, word ptr [rip + 0xa15187]
004F321B  0F B7 54 24 40                  movzx edx, word ptr [rsp + 0x40]
004F3220  0F B7 C1                        movzx eax, cx
004F3223  48 69 D8 10 05 00 00            imul rbx, rax, 0x510
004F322A  48 03 1D A7 51 A1 00            add rbx, qword ptr [rip + 0xa151a7]
004F3231  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
004F3236  44 0F B7 43 0A                  movzx r8d, word ptr [rbx + 0xa]
004F323B  41 8B C8                        mov ecx, r8d
004F323E  41 2B C9                        sub ecx, r9d
004F3241  3B D1                           cmp edx, ecx
004F3243  7E 08                           jle 0x1404f324d
004F3245  41 0F B7 D0                     movzx edx, r8w
004F3249  66 41 2B D1                     sub dx, r9w
004F324D  66 89 93 90 04 00 00            mov word ptr [rbx + 0x490], dx
004F3254  41 8B C8                        mov ecx, r8d
004F3257  44 0F B7 0D 43 51 A1 00         movzx r9d, word ptr [rip + 0xa15143]
004F325F  0F B7 C2                        movzx eax, dx
004F3262  41 2B C9                        sub ecx, r9d
004F3265  2B F8                           sub edi, eax
004F3267  41 0F B7 D5                     movzx edx, r13w
004F326B  89 7C 24 2C                     mov dword ptr [rsp + 0x2c], edi
004F326F  3B D1                           cmp edx, ecx
004F3271  7E 08                           jle 0x1404f327b
004F3273  41 0F B7 D0                     movzx edx, r8w
004F3277  66 41 2B D1                     sub dx, r9w
004F327B  0F B7 C2                        movzx eax, dx
004F327E  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
004F3283  44 2B F0                        sub r14d, eax
004F3286  66 89 93 94 04 00 00            mov word ptr [rbx + 0x494], dx
004F328D  44 0F B7 44 24 70               movzx r8d, word ptr [rsp + 0x70]
004F3293  33 D2                           xor edx, edx
004F3295  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
004F329A  45 33 F6                        xor r14d, r14d
004F329D  49 C1 E0 03                     shl r8, 3
004F32A1  45 0F B7 EE                     movzx r13d, r14w
004F32A5  66 44 89 74 24 22               mov word ptr [rsp + 0x22], r14w
004F32AB  E8 90 39 1D 00                  call 0x1406c6c40
004F32B0  44 0F B7 C6                     movzx r8d, si
004F32B4  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
004F32BB  49 C1 E0 03                     shl r8, 3
004F32BF  33 D2                           xor edx, edx
004F32C1  41 0F B7 FF                     movzx edi, r15w
004F32C5  66 44 89 7C 24 70               mov word ptr [rsp + 0x70], r15w
004F32CB  E8 70 39 1D 00                  call 0x1406c6c40
004F32D0  41 8B F7                        mov esi, r15d
004F32D3  66 44 89 BD 80 00 00 00         mov word ptr [rbp + 0x80], r15w
004F32DB  45 8B FE                        mov r15d, r14d
004F32DE  44 38 73 0C                     cmp byte ptr [rbx + 0xc], r14b
004F32E2  0F 86 5A 02 00 00               jbe 0x1404f3542
004F32E8  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
004F32ED  45 8D 4E 01                     lea r9d, [r14 + 1]
004F32F1  41 8B C7                        mov eax, r15d
004F32F4  48 8D 34 80                     lea rsi, [rax + rax*4]
004F32F8  41 8B C7                        mov eax, r15d
004F32FB  48 C1 E6 07                     shl rsi, 7
004F32FF  48 03 B3 08 05 00 00            add rsi, qword ptr [rbx + 0x508]
004F3306  F7 D8                           neg eax
004F3308  41 8B C7                        mov eax, r15d
004F330B  48 1B C9                        sbb rcx, rcx
004F330E  48 F7 D9                        neg rcx
004F3311  F7 D8                           neg eax
004F3313  42 0F B6 94 01 9E 00 00 00      movzx edx, byte ptr [rcx + r8 + 0x9e]
004F331C  48 1B C9                        sbb rcx, rcx
004F331F  48 F7 D9                        neg rcx
004F3322  46 0F B6 94 01 9C 00 00 00      movzx r10d, byte ptr [rcx + r8 + 0x9c]
004F332B  44 38 74 24 20                  cmp byte ptr [rsp + 0x20], r14b
004F3330  74 07                           je 0x1404f3339
004F3332  45 85 FF                        test r15d, r15d
004F3335  45 0F 45 D6                     cmovne r10d, r14d
004F3339  0F B7 06                        movzx eax, word ptr [rsi]
004F333C  66 85 C0                        test ax, ax
004F333F  0F 84 CC 01 00 00               je 0x1404f3511
004F3345  44 0F B7 1D 55 50 A1 00         movzx r11d, word ptr [rip + 0xa15055]
004F334D  44 8B C8                        mov r9d, eax
004F3350  8B CA                           mov ecx, edx
004F3352  BF 1F 85 EB 51                  mov edi, 0x51eb851f
004F3357  0F AF C8                        imul ecx, eax
004F335A  8B C7                           mov eax, edi
004F335C  83 C1 32                        add ecx, 0x32
004F335F  F7 E1                           mul ecx
004F3361  41 8B C1                        mov eax, r9d
004F3364  44 8B F2                        mov r14d, edx
004F3367  41 C1 EE 05                     shr r14d, 5
004F336B  41 0F B7 CE                     movzx ecx, r14w
004F336F  2B C1                           sub eax, ecx
004F3371  41 0F B6 CA                     movzx ecx, r10b
004F3375  99                              cdq
004F3376  41 0F AF C9                     imul ecx, r9d
004F337A  41 F7 FB                        idiv r11d
004F337D  8B C7                           mov eax, edi
004F337F  83 C1 32                        add ecx, 0x32
004F3382  66 44 03 F2                     add r14w, dx
004F3386  F7 E1                           mul ecx
004F3388  8B FA                           mov edi, edx
004F338A  C1 EF 05                        shr edi, 5
004F338D  0F B7 CF                        movzx ecx, di
004F3390  44 2B C9                        sub r9d, ecx
004F3393  41 8B C1                        mov eax, r9d
004F3396  99                              cdq
004F3397  41 F7 FB                        idiv r11d
004F339A  66 03 FA                        add di, dx
004F339D  45 85 FF                        test r15d, r15d
004F33A0  74 09                           je 0x1404f33ab
004F33A2  66 45 3B F4                     cmp r14w, r12w
004F33A6  66 45 0F 43 F4                  cmovae r14w, r12w
004F33AB  66 85 FF                        test di, di
004F33AE  74 09                           je 0x1404f33b9
004F33B0  66 44 3B DF                     cmp r11w, di
004F33B4  66 41 0F 47 FB                  cmova di, r11w
004F33B9  44 0F B7 8D 82 00 00 00         movzx r9d, word ptr [rbp + 0x82]
004F33C1  4C 8D A6 30 01 00 00            lea r12, [rsi + 0x130]
004F33C8  66 44 3B F7                     cmp r14w, di
004F33CC  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
004F33D3  49 8B D4                        mov rdx, r12
004F33D6  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
004F33DD  66 44 0F 42 F7                  cmovb r14w, di
004F33E2  E8 65 74 EA FF                  call 0x14039a84c
004F33E7  45 0F B7 04 24                  movzx r8d, word ptr [r12]
004F33EC  49 8D 4C 24 08                  lea rcx, [r12 + 8]
004F33F1  49 C1 E0 03                     shl r8, 3
004F33F5  33 D2                           xor edx, edx
004F33F7  E8 44 38 1D 00                  call 0x1406c6c40
004F33FC  48 8D 56 28                     lea rdx, [rsi + 0x28]
004F3400  41 B8 01 00 00 00               mov r8d, 1
004F3406  66 45 89 04 24                  mov word ptr [r12], r8w
004F340B  33 C0                           xor eax, eax
004F340D  4C 8B 62 08                     mov r12, qword ptr [rdx + 8]
004F3411  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
004F3416  44 0F B7 6C 24 58               movzx r13d, word ptr [rsp + 0x58]
004F341C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
004F3421  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
004F3426  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004F342A  48 85 D2                        test rdx, rdx
004F342D  74 05                           je 0x1404f3434
004F342F  0F B7 0A                        movzx ecx, word ptr [rdx]
004F3432  EB 07                           jmp 0x1404f343b
004F3434  41 0F B7 CD                     movzx ecx, r13w
004F3438  41 03 C8                        add ecx, r8d
004F343B  4D 85 E4                        test r12, r12
004F343E  75 23                           jne 0x1404f3463
004F3440  66 45 03 E8                     add r13w, r8w
004F3444  41 0F B7 C5                     movzx eax, r13w
004F3448  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
004F344D  3B C1                           cmp eax, ecx
004F344F  73 7A                           jae 0x1404f34cb
004F3451  4C 8B 64 C2 08                  mov r12, qword ptr [rdx + rax*8 + 8]
004F3456  44 0F B7 6C 24 58               movzx r13d, word ptr [rsp + 0x58]
004F345C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
004F3461  EB D8                           jmp 0x1404f343b
004F3463  49 0F BC D4                     bsf rdx, r12
004F3467  41 0F B7 CD                     movzx ecx, r13w
004F346B  0F B6 C2                        movzx eax, dl
004F346E  49 0F B3 C4                     btr r12, rax
004F3472  C1 E1 06                        shl ecx, 6
004F3475  0F B6 C2                        movzx eax, dl
004F3478  03 C8                           add ecx, eax
004F347A  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
004F347F  48 8B 05 32 FD A2 00            mov rax, qword ptr [rip + 0xa2fd32]
004F3486  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
004F3489  8B C8                           mov ecx, eax
004F348B  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004F348F  E8 3C 51 DE FF                  call 0x1402d85d0
004F3494  33 C9                           xor ecx, ecx
004F3496  48 8D 56 28                     lea rdx, [rsi + 0x28]
004F349A  38 88 4C 8A 00 00               cmp byte ptr [rax + 0x8a4c], cl
004F34A0  8B C1                           mov eax, ecx
004F34A2  44 8D 41 01                     lea r8d, [rcx + 1]
004F34A6  0F 84 7A FF FF FF               je 0x1404f3426
004F34AC  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
004F34B0  48 8D 8E 30 01 00 00            lea rcx, [rsi + 0x130]
004F34B7  E8 34 82 D6 FF                  call 0x14025b6f0
004F34BC  33 C0                           xor eax, eax
004F34BE  48 8D 56 28                     lea rdx, [rsi + 0x28]
004F34C2  44 8D 40 01                     lea r8d, [rax + 1]
004F34C6  E9 5B FF FF FF                  jmp 0x1404f3426
004F34CB  44 0F B7 4C 24 72               movzx r9d, word ptr [rsp + 0x72]
004F34D1  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
004F34D6  48 8D 96 30 01 00 00            lea rdx, [rsi + 0x130]
004F34DD  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F34E2  E8 65 73 EA FF                  call 0x14039a84c
004F34E7  44 0F B7 6C 24 22               movzx r13d, word ptr [rsp + 0x22]
004F34ED  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004F34F2  66 44 03 EF                     add r13w, di
004F34F6  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
004F34FB  66 44 89 76 04                  mov word ptr [rsi + 4], r14w
004F3500  45 33 F6                        xor r14d, r14d
004F3503  66 44 89 6C 24 22               mov word ptr [rsp + 0x22], r13w
004F3509  66 89 7E 02                     mov word ptr [rsi + 2], di
004F350D  45 8D 4E 01                     lea r9d, [r14 + 1]
004F3511  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004F3515  45 03 F9                        add r15d, r9d
004F3518  44 8B 64 24 28                  mov r12d, dword ptr [rsp + 0x28]
004F351D  44 3B F8                        cmp r15d, eax
004F3520  0F 82 CB FD FF FF               jb 0x1404f32f1
004F3526  0F B7 B5 80 00 00 00            movzx esi, word ptr [rbp + 0x80]
004F352D  0F B7 7C 24 70                  movzx edi, word ptr [rsp + 0x70]
004F3532  66 3B F7                        cmp si, di
004F3535  73 0B                           jae 0x1404f3542
004F3537  44 0F B7 C6                     movzx r8d, si
004F353B  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
004F3540  EB 0E                           jmp 0x1404f3550
004F3542  44 0F B7 C7                     movzx r8d, di
004F3546  4C 8D 8D 88 00 00 00            lea r9, [rbp + 0x88]
004F354D  0F B7 FE                        movzx edi, si
004F3550  41 0F B7 D6                     movzx edx, r14w
004F3554  41 BF 01 00 00 00               mov r15d, 1
004F355A  66 41 3B D0                     cmp dx, r8w
004F355E  73 18                           jae 0x1404f3578
004F3560  0F B7 CA                        movzx ecx, dx
004F3563  48 8B 44 CC 78                  mov rax, qword ptr [rsp + rcx*8 + 0x78]
004F3568  48 39 84 CD 88 00 00 00         cmp qword ptr [rbp + rcx*8 + 0x88], rax
004F3570  75 1A                           jne 0x1404f358c
004F3572  66 41 03 D7                     add dx, r15w
004F3576  EB E2                           jmp 0x1404f355a
004F3578  66 3B D7                        cmp dx, di
004F357B  73 1D                           jae 0x1404f359a
004F357D  0F B7 C2                        movzx eax, dx
004F3580  4D 39 34 C1                     cmp qword ptr [r9 + rax*8], r14
004F3584  75 06                           jne 0x1404f358c
004F3586  66 41 03 D7                     add dx, r15w
004F358A  EB EC                           jmp 0x1404f3578
004F358C  48 8D 4B 30                     lea rcx, [rbx + 0x30]
004F3590  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
004F3595  E8 9A 04 00 00                  call 0x1404f3a34
004F359A  66 45 85 ED                     test r13w, r13w
004F359E  75 28                           jne 0x1404f35c8
004F35A0  48 8B 93 08 05 00 00            mov rdx, qword ptr [rbx + 0x508]
004F35A7  0F B7 05 F4 4D A1 00            movzx eax, word ptr [rip + 0xa14df4]
004F35AE  66 89 42 02                     mov word ptr [rdx + 2], ax
004F35B2  0F B7 0D E9 4D A1 00            movzx ecx, word ptr [rip + 0xa14de9]
004F35B9  0F B7 42 04                     movzx eax, word ptr [rdx + 4]
004F35BD  66 3B C8                        cmp cx, ax
004F35C0  66 0F 46 C8                     cmovbe cx, ax
004F35C4  66 89 4A 04                     mov word ptr [rdx + 4], cx
004F35C8  8B 05 6A 1A AD 00               mov eax, dword ptr [rip + 0xad1a6a]
004F35CE  83 F8 02                        cmp eax, 2
004F35D1  75 60                           jne 0x1404f3633
004F35D3  80 8B A0 04 00 00 04            or byte ptr [rbx + 0x4a0], 4
004F35DA  48 8B 83 08 05 00 00            mov rax, qword ptr [rbx + 0x508]
004F35E1  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
004F35E5  66 41 3B CF                     cmp cx, r15w
004F35E9  77 03                           ja 0x1404f35ee
004F35EB  41 8B CF                        mov ecx, r15d
004F35EE  66 89 48 02                     mov word ptr [rax + 2], cx
004F35F2  0F B7 48 04                     movzx ecx, word ptr [rax + 4]
004F35F6  66 41 3B CF                     cmp cx, r15w
004F35FA  77 03                           ja 0x1404f35ff
004F35FC  41 8B CF                        mov ecx, r15d
004F35FF  66 89 48 04                     mov word ptr [rax + 4], cx
004F3603  41 8B D7                        mov edx, r15d
004F3606  44 38 7B 0C                     cmp byte ptr [rbx + 0xc], r15b
004F360A  0F 86 98 00 00 00               jbe 0x1404f36a8
004F3610  8B C2                           mov eax, edx
004F3612  41 03 D7                        add edx, r15d
004F3615  48 8D 0C 80                     lea rcx, [rax + rax*4]
004F3619  48 C1 E1 07                     shl rcx, 7
004F361D  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004F3624  48 83 61 02 00                  and qword ptr [rcx + 2], 0
004F3629  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004F362D  3B D0                           cmp edx, eax
004F362F  72 DF                           jb 0x1404f3610
004F3631  EB 75                           jmp 0x1404f36a8
004F3633  83 F8 03                        cmp eax, 3
004F3636  75 70                           jne 0x1404f36a8
004F3638  44 38 B3 A1 04 00 00            cmp byte ptr [rbx + 0x4a1], r14b
004F363F  74 67                           je 0x1404f36a8
004F3641  80 8B A0 04 00 00 02            or byte ptr [rbx + 0x4a0], 2
004F3648  41 8B D6                        mov edx, r14d
004F364B  44 38 7B 0C                     cmp byte ptr [rbx + 0xc], r15b
004F364F  76 24                           jbe 0x1404f3675
004F3651  8B C2                           mov eax, edx
004F3653  41 03 D7                        add edx, r15d
004F3656  48 8D 0C 80                     lea rcx, [rax + rax*4]
004F365A  48 C1 E1 07                     shl rcx, 7
004F365E  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004F3665  48 83 61 02 00                  and qword ptr [rcx + 2], 0
004F366A  8D 4A 01                        lea ecx, [rdx + 1]
004F366D  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004F3671  3B C8                           cmp ecx, eax
004F3673  72 DC                           jb 0x1404f3651
004F3675  8B C2                           mov eax, edx
004F3677  48 8D 0C 80                     lea rcx, [rax + rax*4]
004F367B  48 C1 E1 07                     shl rcx, 7
004F367F  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004F3686  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
004F368A  66 41 3B C7                     cmp ax, r15w
004F368E  77 03                           ja 0x1404f3693
004F3690  41 8B C7                        mov eax, r15d
004F3693  66 89 41 02                     mov word ptr [rcx + 2], ax
004F3697  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
004F369B  66 41 3B C7                     cmp ax, r15w
004F369F  77 03                           ja 0x1404f36a4
004F36A1  41 8B C7                        mov eax, r15d
004F36A4  66 89 41 04                     mov word ptr [rcx + 4], ax
004F36A8  48 8B CB                        mov rcx, rbx
004F36AB  E8 E8 CC FA FF                  call 0x1404a0398
004F36B0  0F B7 4C 24 24                  movzx ecx, word ptr [rsp + 0x24]
004F36B5  8B 1D 25 4D A1 00               mov ebx, dword ptr [rip + 0xa14d25]
004F36BB  66 41 03 CF                     add cx, r15w
004F36BF  44 8B 64 24 28                  mov r12d, dword ptr [rsp + 0x28]
004F36C4  8B 7C 24 2C                     mov edi, dword ptr [rsp + 0x2c]
004F36C8  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
004F36CD  44 8B 6C 24 44                  mov r13d, dword ptr [rsp + 0x44]
004F36D2  0F B7 C1                        movzx eax, cx
004F36D5  66 89 4C 24 24                  mov word ptr [rsp + 0x24], cx
004F36DA  3B C3                           cmp eax, ebx
004F36DC  0F 82 31 FB FF FF               jb 0x1404f3213
004F36E2  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
004F36E7  33 F6                           xor esi, esi
004F36E9  EB 59                           jmp 0x1404f3744
004F36EB  0F B7 D6                        movzx edx, si
004F36EE  85 DB                           test ebx, ebx
004F36F0  74 52                           je 0x1404f3744
004F36F2  85 FF                           test edi, edi
004F36F4  0F 84 A7 00 00 00               je 0x1404f37a1
004F36FA  0F B7 C2                        movzx eax, dx
004F36FD  48 69 C8 10 05 00 00            imul rcx, rax, 0x510
004F3704  48 03 0D CD 4C A1 00            add rcx, qword ptr [rip + 0xa14ccd]
004F370B  44 0F B7 41 0A                  movzx r8d, word ptr [rcx + 0xa]
004F3710  66 45 85 C0                     test r8w, r8w
004F3714  74 24                           je 0x1404f373a
004F3716  0F B7 05 85 4C A1 00            movzx eax, word ptr [rip + 0xa14c85]
004F371D  66 03 81 90 04 00 00            add ax, word ptr [rcx + 0x490]
004F3724  66 41 3B C0                     cmp ax, r8w
004F3728  73 10                           jae 0x1404f373a
004F372A  66 89 81 90 04 00 00            mov word ptr [rcx + 0x490], ax
004F3731  0F B7 05 6A 4C A1 00            movzx eax, word ptr [rip + 0xa14c6a]
004F3738  2B F8                           sub edi, eax
004F373A  66 FF C2                        inc dx
004F373D  0F B7 C2                        movzx eax, dx
004F3740  3B C3                           cmp eax, ebx
004F3742  72 AE                           jb 0x1404f36f2
004F3744  85 FF                           test edi, edi
004F3746  75 A3                           jne 0x1404f36eb
004F3748  EB 57                           jmp 0x1404f37a1
004F374A  0F B7 D6                        movzx edx, si
004F374D  85 DB                           test ebx, ebx
004F374F  74 50                           je 0x1404f37a1
004F3751  45 85 F6                        test r14d, r14d
004F3754  74 50                           je 0x1404f37a6
004F3756  0F B7 C2                        movzx eax, dx
004F3759  48 69 C8 10 05 00 00            imul rcx, rax, 0x510
004F3760  48 03 0D 71 4C A1 00            add rcx, qword ptr [rip + 0xa14c71]
004F3767  44 0F B7 41 0A                  movzx r8d, word ptr [rcx + 0xa]
004F376C  66 45 85 C0                     test r8w, r8w
004F3770  74 25                           je 0x1404f3797
004F3772  0F B7 81 94 04 00 00            movzx eax, word ptr [rcx + 0x494]
004F3779  66 03 05 22 4C A1 00            add ax, word ptr [rip + 0xa14c22]
004F3780  66 41 3B C0                     cmp ax, r8w
004F3784  73 11                           jae 0x1404f3797
004F3786  66 89 81 94 04 00 00            mov word ptr [rcx + 0x494], ax
004F378D  0F B7 05 0E 4C A1 00            movzx eax, word ptr [rip + 0xa14c0e]
004F3794  44 2B F0                        sub r14d, eax
004F3797  66 FF C2                        inc dx
004F379A  0F B7 C2                        movzx eax, dx
004F379D  3B C3                           cmp eax, ebx
004F379F  72 B0                           jb 0x1404f3751
004F37A1  45 85 F6                        test r14d, r14d
004F37A4  75 A4                           jne 0x1404f374a
004F37A6  0F B7 FE                        movzx edi, si
004F37A9  85 DB                           test ebx, ebx
004F37AB  0F 84 94 00 00 00               je 0x1404f3845
004F37B1  41 BF 01 00 00 00               mov r15d, 1
004F37B7  0F B7 C7                        movzx eax, di
004F37BA  48 69 D8 10 05 00 00            imul rbx, rax, 0x510
004F37C1  48 03 1D 10 4C A1 00            add rbx, qword ptr [rip + 0xa14c10]
004F37C8  0F B7 53 0A                     movzx edx, word ptr [rbx + 0xa]
004F37CC  48 8D B3 94 04 00 00            lea rsi, [rbx + 0x494]
004F37D3  44 0F B7 83 90 04 00 00         movzx r8d, word ptr [rbx + 0x490]
004F37DB  4C 8D B3 96 04 00 00            lea r14, [rbx + 0x496]
004F37E2  0F B7 83 92 04 00 00            movzx eax, word ptr [rbx + 0x492]
004F37E9  8B CA                           mov ecx, edx
004F37EB  41 2B C8                        sub ecx, r8d
004F37EE  3B C1                           cmp eax, ecx
004F37F0  75 0D                           jne 0x1404f37ff
004F37F2  0F B7 06                        movzx eax, word ptr [rsi]
004F37F5  2B D0                           sub edx, eax
004F37F7  41 0F B7 06                     movzx eax, word ptr [r14]
004F37FB  3B C2                           cmp eax, edx
004F37FD  74 2C                           je 0x1404f382b
004F37FF  44 0F B7 0E                     movzx r9d, word ptr [rsi]
004F3803  48 8D 53 30                     lea rdx, [rbx + 0x30]
004F3807  0F B7 CF                        movzx ecx, di
004F380A  E8 71 AD 0E 00                  call 0x1405de580
004F380F  0F B7 4B 0A                     movzx ecx, word ptr [rbx + 0xa]
004F3813  0F B7 C1                        movzx eax, cx
004F3816  66 2B 83 90 04 00 00            sub ax, word ptr [rbx + 0x490]
004F381D  66 2B 0E                        sub cx, word ptr [rsi]
004F3820  66 41 89 0E                     mov word ptr [r14], cx
004F3824  66 89 83 92 04 00 00            mov word ptr [rbx + 0x492], ax
004F382B  66 41 03 FF                     add di, r15w
004F382F  0F B7 C7                        movzx eax, di
004F3832  3B 05 A8 4B A1 00               cmp eax, dword ptr [rip + 0xa14ba8]
004F3838  0F 82 79 FF FF FF               jb 0x1404f37b7
004F383E  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
004F3843  33 F6                           xor esi, esi
004F3845  40 38 35 A4 A8 A1 00            cmp byte ptr [rip + 0xa1a8a4], sil
004F384C  40 8A D6                        mov dl, sil
004F384F  41 8B 9F A0 00 00 00            mov ebx, dword ptr [r15 + 0xa0]
004F3856  74 1E                           je 0x1404f3876
004F3858  8B 05 36 18 AD 00               mov eax, dword ptr [rip + 0xad1836]
004F385E  85 C0                           test eax, eax
004F3860  74 14                           je 0x1404f3876
004F3862  85 DB                           test ebx, ebx
004F3864  74 04                           je 0x1404f386a
004F3866  3B C3                           cmp eax, ebx
004F3868  73 0C                           jae 0x1404f3876
004F386A  BF 01 00 00 00                  mov edi, 1
004F386F  8B D8                           mov ebx, eax
004F3871  40 8A D7                        mov dl, dil
004F3874  EB 05                           jmp 0x1404f387b
004F3876  BF 01 00 00 00                  mov edi, 1
004F387B  44 8B C3                        mov r8d, ebx
004F387E  33 C9                           xor ecx, ecx
004F3880  E8 CB 00 00 00                  call 0x1404f3950
004F3885  85 DB                           test ebx, ebx
004F3887  75 5D                           jne 0x1404f38e6
004F3889  48 8B 0D 38 4B A1 00            mov rcx, qword ptr [rip + 0xa14b38]
004F3890  40 88 35 5A 32 AD 00            mov byte ptr [rip + 0xad325a], sil
004F3897  89 35 B7 FB A2 00               mov dword ptr [rip + 0xa2fbb7], esi
004F389D  48 85 C9                        test rcx, rcx
004F38A0  74 71                           je 0x1404f3913
004F38A2  48 8B 1D 0F 4B A1 00            mov rbx, qword ptr [rip + 0xa14b0f]
004F38A9  48 85 DB                        test rbx, rbx
004F38AC  74 65                           je 0x1404f3913
004F38AE  44 8B 05 33 32 AD 00            mov r8d, dword ptr [rip + 0xad3233]
004F38B5  BF FF 00 00 00                  mov edi, 0xff
004F38BA  49 C1 E0 02                     shl r8, 2
004F38BE  8B D7                           mov edx, edi
004F38C0  E8 7B 33 1D 00                  call 0x1406c6c40
004F38C5  44 8B 05 1C 32 AD 00            mov r8d, dword ptr [rip + 0xad321c]
004F38CC  8B D7                           mov edx, edi
004F38CE  49 C1 E0 02                     shl r8, 2
004F38D2  48 8B CB                        mov rcx, rbx
004F38D5  E8 66 33 1D 00                  call 0x1406c6c40
004F38DA  E8 B9 20 DE FF                  call 0x1402d5998
004F38DF  E8 F4 1F DE FF                  call 0x1402d58d8
004F38E4  EB 2D                           jmp 0x1404f3913
004F38E6  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
004F38EF  BA 40 42 0F 00                  mov edx, 0xf4240
004F38F4  44 8B C3                        mov r8d, ebx
004F38F7  40 88 3D F3 31 AD 00            mov byte ptr [rip + 0xad31f3], dil
004F38FE  8B 48 44                        mov ecx, dword ptr [rax + 0x44]
004F3901  48 69 C9 40 42 0F 00            imul rcx, rcx, 0xf4240
004F3908  E8 23 3C F5 FF                  call 0x140447530
004F390D  89 05 41 FB A2 00               mov dword ptr [rip + 0xa2fb41], eax
004F3913  E8 E0 B6 EC FF                  call 0x1403beff8
004F3918  48 8B 8D 90 01 00 00            mov rcx, qword ptr [rbp + 0x190]
004F391F  48 33 CC                        xor rcx, rsp
004F3922  E8 19 8D 1B 00                  call 0x1406ac640
004F3927  4C 8D 9C 24 A0 02 00 00         lea r11, [rsp + 0x2a0]
004F392F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
004F3933  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
004F3937  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
004F393B  49 8B E3                        mov rsp, r11
004F393E  41 5F                           pop r15
004F3940  41 5E                           pop r14
004F3942  41 5D                           pop r13
004F3944  41 5C                           pop r12
004F3946  5D                              pop rbp
004F3947  C3                              ret
004F3948  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkApplyPolicyEx(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m250;
    unsigned __int16 v_stack_m256;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m294;
    unsigned int v_stack_m298;
    unsigned int v_stack_m29C;
    unsigned int v_stack_m2A0;
    unsigned __int16 v_stack_m2A4;
    unsigned __int16 v_stack_m2A6;
    unsigned __int8 v_stack_m2A8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (672);
    result = (*(unsigned __int64 *)(v_rip + 9533059)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 456 + 400) = result;
    result = 0;
    v_stack_m270 = 0;
    a2 = 0;
    v_stack_m280 = v_xmm0;
    result = memset(v_stack_m250, a2, 256, a4);
    a2 = 0;
    result = memset(v_rsp - 456 + 136, a2, 256, a4);
    v_rbx = 0;
    if ((*(unsigned __int64 *)(v_rip + 10572500)) != 0) goto loc_004F3111;
    *(unsigned int *)(v_rip + 10683208) = 0;
    goto loc_004F3918;
loc_004F3111:
    v_r15 = (*(unsigned __int64 *)(v_rip + 9523816)) + (40);
    a1 = (v_rsp - 456 + 136) * ((int)(*(unsigned int *)(v_rip + 10591469)));
    v_r15 = (v_r15) + (a1);
    v_stack_m290 = v_r15;
    result = PpmParkEvalualteSmtUnparkPolicy(*(unsigned __int8 *)(v_r15 + 458), a2, 256, a4);
    a1 = 0;
    v_stack_m2A8 = 0;
    result = KeGetPrcb(a1, a2, 256, a4);
    if ((*(unsigned __int64 *)(result + 35248)) != 0) goto loc_004F3170;
    v_r12 = 1 + 63;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11353070)))) <= ((unsigned int)(1 + 63))) {
        v_r12 = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 11353070)));
    }
    v_stack_m2A8 = 1;
loc_004F3170:
    a2 = 0;
    a2 = 0;
    v_stack_m2A0 = (unsigned int)(v_r12);
    v_stack_m258 = 0x200001ULL;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9914555))))))) - (0));
    a2 = 0;
    a2 = 0;
    v_stack_m288 = (unsigned int)(a3);
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9914550))))))) - (0));
    a2 = 0;
    v_stack_m284 = (unsigned int)(v_r13);
    result = memset(v_stack_m250, a2, 256, 1);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 456 + 128) = 0x200001ULL;
    v_rsi = 0;
    result = memset(v_rsp - 456 + 136, a2, 256, 1);
    v_stack_m2A4 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10572394))) == 0) goto loc_004F3744;
loc_004F3213:
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rip + 10572394))) * (0);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 10572199));
    v_stack_m268 = v_rbx;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 10)))) - ((unsigned int)(*(unsigned __int16 *)(v_rip + 10572167))));
    if (((unsigned int)(v_stack_m288)) >= = ((unsigned int)(a1))) {
        a2 = (unsigned __int16)(*(unsigned __int16 *)(v_rbx + 10));
        a2 = (unsigned __int16)((a2) - ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10572167))));
    }
    *(unsigned __int16 *)(v_rbx + 1168) = (unsigned __int16)(a2);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 10)))) - ((unsigned int)(*(unsigned __int16 *)(v_rip + 10572099))));
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9914555))) - ((unsigned int)((unsigned __int16)(a2))));
    v_stack_m29C = (unsigned int)(v_rdi);
    if (((unsigned int)((unsigned __int16)(v_r13))) >= = ((unsigned int)(a1))) {
        a2 = (unsigned __int16)(*(unsigned __int16 *)(v_rbx + 10));
        a2 = (unsigned __int16)((a2) - ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10572099))));
    }
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9914550))) - ((unsigned int)((unsigned __int16)(a2))));
    *(unsigned __int16 *)(v_rbx + 1172) = (unsigned __int16)(a2);
    a2 = 0;
    v_stack_m298 = (unsigned int)(v_r14);
    v_r14 = 0;
    a3 = (v_stack_m258) << (3);
    v_stack_m2A6 = 0;
    result = memset(v_stack_m250, a2, a3, *(unsigned __int16 *)(v_rip + 10572099));
    a3 = ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 456 + 128))) << (3);
    a2 = 0;
    v_stack_m258 = 1;
    result = memset(v_rsp - 456 + 136, a2, a3, *(unsigned __int16 *)(v_rip + 10572099));
    *(unsigned __int16 *)(v_rsp - 456 + 128) = 1;
    if ((*(unsigned __int8 *)(v_rbx + 12)) <= 0) goto loc_004F3542;
loc_004F32F1:
    v_rsi = (0 + 0 * 4) << (7);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rbx + 1288));
    result = (unsigned int)(-(0));
    a1 = -(v_rsp - 456 + 136);
    result = (unsigned int)(-(0));
    a1 = -(a1);
    v_r10 = *(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 156);
    if (v_stack_m2A8 != 0) {
        v_r10 = *(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 156);
        if (0 != 0) { v_r10 = 0; }
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_004F3511;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 158)))) * ((unsigned int)(*(unsigned __int16 *)(v_rsi))));
    a1 = (unsigned int)((a1) + (50));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 158)))) >> (5));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi)))))) - ((unsigned int)((unsigned __int16)(v_r14))));
    a1 = (unsigned int)(((unsigned __int8)(v_r10)) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi))))));
    a1 = (unsigned int)((a1) + (50));
    v_r14 = (unsigned __int16)((v_r14) + ((unsigned __int16)(*(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 158))));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 158)))) >> (5));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi)))) - ((unsigned int)((unsigned __int16)(v_rdi))));
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)(*(unsigned __int8 *)(a1 + v_stack_m290 * 1 + 158))));
    if (0 != 0) {
        if (((unsigned __int16)(v_r14)) >= ((unsigned __int16)(v_r12))) { v_r14 = (unsigned __int16)(v_r12); }
    }
    if ((unsigned __int16)(v_rdi) != 0) {
        if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10571861))) > ((unsigned __int16)(v_rdi))) { v_rdi = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 10571861)); }
    }
    if (((unsigned __int16)(v_r14)) < ((unsigned __int16)(v_rdi))) { v_r14 = (unsigned __int16)(v_rdi); }
    result = KiOrAffinityEx(v_rsp - 456 + 128, v_rsi + 304, v_rsp - 456 + 128, *(unsigned __int16 *)(v_rsp - 456 + 130));
    a3 = (*(unsigned __int16 *)(v_rsi + 304)) << (3);
    a2 = 0;
    result = memset(v_rsi + 304 + 8, a2, a3, *(unsigned __int16 *)(v_rsp - 456 + 130));
    *(unsigned __int16 *)(v_rsi + 304) = 1;
    result = 0;
    v_stack_m270 = 0;
    v_stack_m278 = *(unsigned __int64 *)(v_rsi + 40 + 8);
    v_stack_m280 = v_rsi + 40;
loc_004F3426:
    v_stack_m294 = 0;
    if (v_rsi + 40 == 0) goto loc_004F3434;
    goto loc_004F343B;
loc_004F3434:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m270)) + (1));
loc_004F343B:
    if (*(unsigned __int64 *)(v_rsi + 40 + 8) != 0) goto loc_004F3463;
    v_r13 = (unsigned __int16)((v_stack_m270) + (1));
    v_stack_m270 = (unsigned __int16)((unsigned __int16)(v_r13));
    if (((unsigned int)((unsigned __int16)(v_r13))) >= ((unsigned int)(a1))) goto loc_004F34CB;
    v_stack_m278 = *(unsigned __int64 *)(v_rsi + 40 + (unsigned __int16)(v_r13) * 8 + 8);
    goto loc_004F343B;
loc_004F3463:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m270)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_rsi + 40))));
    v_stack_m278 = *(unsigned __int64 *)(v_rsi + 40 + (unsigned __int16)(v_r13) * 8 + 8);
    v_stack_m294 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10681650) + a1 * 4)));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10681650) + a1 * 4)))), v_rsi + 40, 1, *(unsigned __int16 *)(v_rsp - 456 + 130));
    a1 = 0;
    if ((*(unsigned __int8 *)(result + 35404)) == 0) goto loc_004F3426;
    result = KeAddProcessorAffinityEx(v_rsi + 304, (unsigned int)(v_stack_m294), a1 + 1, *(unsigned __int16 *)(v_rsp - 456 + 130));
    result = 0;
    goto loc_004F3426;
loc_004F34CB:
    result = KiOrAffinityEx(v_stack_m258, v_rsi + 304, v_stack_m258, v_stack_m256);
    v_r13 = (unsigned __int16)((v_stack_m2A6) + ((unsigned __int16)(v_rdi)));
    *(unsigned __int16 *)(v_rsi + 4) = (unsigned __int16)(v_r14);
    v_r14 = 0;
    v_stack_m2A6 = (unsigned __int16)(v_r13);
    *(unsigned __int16 *)(v_rsi + 2) = (unsigned __int16)(v_rdi);
loc_004F3511:
    v_r15 = (unsigned int)((0) + ((unsigned int)(v_r14 + 1)));
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m268 + 12)))) goto loc_004F32F1;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 456 + 128))) >= ((unsigned __int16)(v_stack_m258))) goto loc_004F3542;
    goto loc_004F3550;
loc_004F3542:
loc_004F3550:
loc_004F355A:
    if (0 >= ((unsigned __int16)((unsigned __int16)(v_stack_m258)))) goto loc_004F3578;
    if ((*(unsigned __int64 *)(v_rsp - 456 + 0 * 8 + 136)) != (*(unsigned __int64 *)(v_rsp + 0 * 8 + 120))) goto loc_004F358C;
    a2 = (unsigned __int16)((0) + (1));
    goto loc_004F355A;
loc_004F3578:
    if (((unsigned __int16)(a2)) >= ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 456 + 128))))) goto loc_004F359A;
    if ((*(unsigned __int64 *)(v_rsp - 456 + 136 + (unsigned __int16)(a2) * 8)) != 0) goto loc_004F358C;
    a2 = (unsigned __int16)((a2) + (1));
    goto loc_004F3578;
loc_004F358C:
    result = PpmEventParkNodeParkHintChangedEx(v_stack_m268 + 48, v_stack_m258, (unsigned __int16)(v_stack_m258), v_rsp - 456 + 136);
loc_004F359A:
    if ((unsigned __int16)(v_r13) == 0) {
        a2 = *(unsigned __int64 *)(v_stack_m268 + 1288);
        result = *(unsigned __int16 *)(v_rip + 10571252);
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(result);
        a1 = *(unsigned __int16 *)(v_rip + 10571241);
        result = *(unsigned __int16 *)(a2 + 4);
        if (((unsigned __int16)(a1)) <= ((unsigned __int16)(result))) { a1 = (unsigned __int16)(result); }
        *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11344490)))) != 2) goto loc_004F3633;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m268 + 1288) + 2))) <= 1) {
        a1 = 1;
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m268 + 1288) + 2) = (unsigned __int16)(a1);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m268 + 1288) + 4))) <= 1) {
        a1 = 1;
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m268 + 1288) + 4) = (unsigned __int16)(a1);
    if ((*(unsigned __int8 *)(v_stack_m268 + 12)) <= 1) goto loc_004F36A8;
loc_004F3610:
    a2 = (unsigned int)((1) + (1));
    a1 = (1 + 1 * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m268 + 1288));
    if (a2 < ((unsigned int)(*(unsigned __int8 *)(v_stack_m268 + 12)))) goto loc_004F3610;
    goto loc_004F36A8;
loc_004F3633:
    if (((unsigned int)(*(unsigned __int8 *)(v_stack_m268 + 12))) != 3) goto loc_004F36A8;
    if ((*(unsigned __int8 *)(v_stack_m268 + 1185)) == 0) goto loc_004F36A8;
    if ((*(unsigned __int8 *)(v_stack_m268 + 12)) <= 1) goto loc_004F3675;
loc_004F3651:
    a2 = (unsigned int)((0) + (1));
    a1 = (0 + 0 * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m268 + 1288));
    if (((unsigned int)(a2 + 1)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m268 + 12)))) goto loc_004F3651;
loc_004F3675:
    a1 = ((unsigned int)(a2) + (unsigned int)(a2) * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m268 + 1288));
    result = *(unsigned __int16 *)(a1 + 2);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) <= 1) {
        result = 1;
    }
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)(result);
    result = *(unsigned __int16 *)(a1 + 4);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 4))) <= 1) {
        result = 1;
    }
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
loc_004F36A8:
    result = PpmConfigureRestrictionPolicy(v_stack_m268, a2, (unsigned __int16)(v_stack_m258), v_rsp - 456 + 136);
    a1 = (unsigned __int16)((v_stack_m2A4) + (1));
    v_stack_m2A4 = (unsigned __int16)(a1);
    if (((unsigned int)((unsigned __int16)(a1))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))))) goto loc_004F3213;
    v_rsi = 0;
    goto loc_004F3744;
loc_004F36EB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))) == 0) goto loc_004F3744;
loc_004F36F2:
    if ((unsigned int)((unsigned int)(v_stack_m29C)) == 0) goto loc_004F37A1;
    a1 = (a1) * (0);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10570957));
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)) == 0) goto loc_004F373A;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rip + 10570885)) + (*(unsigned __int16 *)(a1 + 1168)));
    v_rdi = (unsigned int)(v_stack_m29C);
    if (((unsigned __int16)(result)) < ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)))) {
        *(unsigned __int16 *)(a1 + 1168) = (unsigned __int16)(result);
        result = *(unsigned __int16 *)(v_rip + 10570858);
        v_rdi = (unsigned int)(((unsigned int)(v_stack_m29C)) - ((unsigned int)(result)));
    }
    a2 = (unsigned __int16)((0) + 1);
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))))) goto loc_004F36F2;
loc_004F3744:
    if ((unsigned int)(v_rdi) != 0) goto loc_004F36EB;
    goto loc_004F37A1;
loc_004F374A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))) == 0) goto loc_004F37A1;
loc_004F3751:
    if ((unsigned int)((unsigned int)(v_stack_m298)) == 0) goto loc_004F37A6;
    a1 = (a1) * (0);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10570865));
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)) == 0) goto loc_004F3797;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 1172)) + (*(unsigned __int16 *)(v_rip + 10570786)));
    v_r14 = (unsigned int)(v_stack_m298);
    if (((unsigned __int16)(result)) < ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)))) {
        *(unsigned __int16 *)(a1 + 1172) = (unsigned __int16)(result);
        result = *(unsigned __int16 *)(v_rip + 10570766);
        v_r14 = (unsigned int)(((unsigned int)(v_stack_m298)) - ((unsigned int)(result)));
    }
    a2 = (unsigned __int16)((0) + 1);
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))))) goto loc_004F3751;
loc_004F37A1:
    if ((unsigned int)(v_r14) != 0) goto loc_004F374A;
loc_004F37A6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10571045))) == 0) goto loc_004F3845;
loc_004F37B7:
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rip + 10571045))) * (0);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 10570768));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 10)))) - ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1168))));
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 1170))) != ((unsigned int)(a1))) goto loc_004F37FF;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rbx + 10)) - ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1172))));
    result = *(unsigned __int16 *)(v_rbx + 1174);
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 1174))) != a2) {
        a4 = *(unsigned __int16 *)(v_rbx + 1172);
        a2 = v_rbx + 48;
        a1 = 0;
        result = PpmEventParkNodeCapChangeEx(a1, a2, *(unsigned __int16 *)(v_rbx + 1168), a4);
        a1 = *(unsigned __int16 *)(v_rbx + 10);
        result = (unsigned __int16)(a1);
        result = (unsigned __int16)((result) - (*(unsigned __int16 *)(v_rbx + 1168)));
        a1 = (unsigned __int16)((a1) - (*(unsigned __int16 *)(v_rbx + 1172)));
        *(unsigned __int16 *)(v_rbx + 1174) = (unsigned __int16)(a1);
        *(unsigned __int16 *)(v_rbx + 1170) = (unsigned __int16)(result);
    }
    v_rdi = (unsigned __int16)((0) + (1));
    if (((unsigned int)((unsigned __int16)(v_rdi))) < (*(unsigned int *)(v_rip + 10570664))) goto loc_004F37B7;
    v_rsi = 0;
loc_004F3845:
    if ((*(unsigned __int8 *)(v_rip + 10594468)) == 0) goto loc_004F3876;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11343926))) == 0) goto loc_004F3876;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m290 + 160))) == 0) goto loc_004F386A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11343926)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m290 + 160))))) goto loc_004F3876;
loc_004F386A:
    goto loc_004F387B;
loc_004F3876:
loc_004F387B:
    a1 = 0;
    result = PpmEventSoftParkLatencyUpdate(a1, 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11343926)))))), a4);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11343926))))) != 0) goto loc_004F38E6;
    *(unsigned __int8 *)(v_rip + 11350618) = 0;
    *(unsigned int *)(v_rip + 10681271) = 0;
    if (*(unsigned __int64 *)(v_rip + 10570552) == 0) goto loc_004F3913;
    if (*(unsigned __int64 *)(v_rip + 10570511) == 0) goto loc_004F3913;
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11350579))) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 10570552), 255, a3, a4);
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11350556))) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 10570511), 255, a3, a4);
    result = KeUpdateSoftParkRankList(*(unsigned __int64 *)(v_rip + 10570511), 255, a3, a4);
    result = PpmEventSoftParkRankListChanged(*(unsigned __int64 *)(v_rip + 10570511), 255, a3, a4);
    goto loc_004F3913;
loc_004F38E6:
    *(unsigned __int8 *)(v_rip + 11350515) = 255;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 68))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 68)));
    result = PpmConvertTime(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10570511))), a4);
    *(unsigned int *)(v_rip + 10681153) = (unsigned int)(result);
loc_004F3913:
    result = PpmHeteroHgsCheckContainmentDecision(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10570511))), a4);
loc_004F3918:
    a1 = (*(unsigned __int64 *)(v_rsp - 456 + 400)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10570511))), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkApplyPolicyEx(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m250;
    uint16_t v_stack_m256;
    uint64_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m294;
    uint32_t v_stack_m298;
    uint32_t v_stack_m29C;
    uint32_t v_stack_m2A0;
    uint16_t v_stack_m2A4;
    uint16_t v_stack_m2A6;
    uint8_t v_stack_m2A8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (672);
    result = (*(uint64_t *)(v_rip + 0x917683)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1C8 + 0x190) = result;
    result = 0;
    v_stack_m270 = 0;
    Arg2 = 0;
    v_stack_m280 = v_xmm0;
    result = memset(v_stack_m250, Arg2, 256, a4);
    Arg2 = 0;
    result = memset(local_rsp - 456 + 136, Arg2, 256, a4);
    local_rbx = 0;
    if ((*(uint64_t *)(v_rip + 0xA152D4)) != 0) goto loc_004F3111;
    *(uint32_t *)(v_rip + 0xA30348) = 0;
    goto loc_004F3918;
loc_004F3111:
    local_r15 = (*(uint64_t *)(v_rip + 0x915268)) + (40);
    Arg1 = (local_rsp - 456 + 136) * ((int32_t)(*(uint32_t *)(v_rip + 0xA19CED)));
    local_r15 = (local_r15) + (Arg1);
    v_stack_m290 = local_r15;
    result = PpmParkEvalualteSmtUnparkPolicy(*(uint8_t *)(local_r15 + 0x1CA), Arg2, 256, a4);
    Arg1 = 0;
    v_stack_m2A8 = 0;
    result = KeGetPrcb(Arg1, Arg2, 256, a4);
    if ((*(uint64_t *)(result + 0x89B0)) != 0) goto loc_004F3170;
    local_r12 = 1 + 63;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD3BEE)))) <= ((uint32_t)(1 + 63))) {
        local_r12 = (uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD3BEE)));
    }
    v_stack_m2A8 = 1;
loc_004F3170:
    Arg2 = 0;
    Arg2 = 0;
    v_stack_m2A0 = (uint32_t)(local_r12);
    v_stack_m258 = 0x200001ULL;
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9748BB))))))) - (0));
    Arg2 = 0;
    Arg2 = 0;
    v_stack_m288 = (uint32_t)(a3);
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9748B6))))))) - (0));
    Arg2 = 0;
    v_stack_m284 = (uint32_t)(local_r13);
    result = memset(v_stack_m250, Arg2, 256, 1);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x1C8 + 0x80) = 0x200001ULL;
    local_rsi = 0;
    result = memset(local_rsp - 456 + 136, Arg2, 256, 1);
    v_stack_m2A4 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA1526A))) == 0) goto loc_004F3744;
loc_004F3213:
    local_rbx = ((uint32_t)(*(uint32_t *)(v_rip + 0xA1526A))) * (0);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xA151A7));
    v_stack_m268 = local_rbx;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0xA)))) - ((uint32_t)(*(uint16_t *)(v_rip + 0xA15187))));
    if (((uint32_t)(v_stack_m288)) >= = ((uint32_t)(Arg1))) {
        Arg2 = (uint16_t)(*(uint16_t *)(local_rbx + 0xA));
        Arg2 = (uint16_t)((Arg2) - ((uint16_t)(*(uint16_t *)(v_rip + 0xA15187))));
    }
    *(uint16_t *)(local_rbx + 0x490) = (uint16_t)(Arg2);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0xA)))) - ((uint32_t)(*(uint16_t *)(v_rip + 0xA15143))));
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9748BB))) - ((uint32_t)((uint16_t)(Arg2))));
    v_stack_m29C = (uint32_t)(local_rdi);
    if (((uint32_t)((uint16_t)(local_r13))) >= = ((uint32_t)(Arg1))) {
        Arg2 = (uint16_t)(*(uint16_t *)(local_rbx + 0xA));
        Arg2 = (uint16_t)((Arg2) - ((uint16_t)(*(uint16_t *)(v_rip + 0xA15143))));
    }
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9748B6))) - ((uint32_t)((uint16_t)(Arg2))));
    *(uint16_t *)(local_rbx + 0x494) = (uint16_t)(Arg2);
    Arg2 = 0;
    v_stack_m298 = (uint32_t)(local_r14);
    local_r14 = 0;
    a3 = (v_stack_m258) << (3);
    v_stack_m2A6 = 0;
    result = memset(v_stack_m250, Arg2, a3, *(uint16_t *)(v_rip + 0xA15143));
    a3 = ((uint16_t)(*(uint16_t *)(local_rsp - 0x1C8 + 0x80))) << (3);
    Arg2 = 0;
    v_stack_m258 = 1;
    result = memset(local_rsp - 456 + 136, Arg2, a3, *(uint16_t *)(v_rip + 0xA15143));
    *(uint16_t *)(local_rsp - 0x1C8 + 0x80) = 1;
    if ((*(uint8_t *)(local_rbx + 0xC)) <= 0) goto loc_004F3542;
loc_004F32F1:
    local_rsi = (0 + 0 * 4) << (7);
    local_rsi = (local_rsi) + (*(uint64_t *)(local_rbx + 0x508));
    result = (uint32_t)(-(0));
    Arg1 = -(local_rsp - 456 + 136);
    result = (uint32_t)(-(0));
    Arg1 = -(Arg1);
    local_r10 = *(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9C);
    if (v_stack_m2A8 != 0) {
        local_r10 = *(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9C);
        if (0 != 0) { local_r10 = 0; }
    }
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_004F3511;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9E)))) * ((uint32_t)(*(uint16_t *)(local_rsi))));
    Arg1 = (uint32_t)((Arg1) + (50));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9E)))) >> (5));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi)))))) - ((uint32_t)((uint16_t)(local_r14))));
    Arg1 = (uint32_t)(((uint8_t)(local_r10)) * ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi))))));
    Arg1 = (uint32_t)((Arg1) + (50));
    local_r14 = (uint16_t)((local_r14) + ((uint16_t)(*(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9E))));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9E)))) >> (5));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi)))) - ((uint32_t)((uint16_t)(local_rdi))));
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)(*(uint8_t *)(Arg1 + v_stack_m290 * 1 + 0x9E))));
    if (0 != 0) {
        if (((uint16_t)(local_r14)) >= ((uint16_t)(local_r12))) { local_r14 = (uint16_t)(local_r12); }
    }
    if ((uint16_t)(local_rdi) != 0) {
        if (((uint16_t)(*(uint16_t *)(v_rip + 0xA15055))) > ((uint16_t)(local_rdi))) { local_rdi = (uint16_t)(*(uint16_t *)(v_rip + 0xA15055)); }
    }
    if (((uint16_t)(local_r14)) < ((uint16_t)(local_rdi))) { local_r14 = (uint16_t)(local_rdi); }
    result = KiOrAffinityEx(local_rsp - 456 + 128, local_rsi + 304, local_rsp - 456 + 128, *(uint16_t *)(local_rsp - 0x1C8 + 0x82));
    a3 = (*(uint16_t *)(local_rsi + 0x130)) << (3);
    Arg2 = 0;
    result = memset(local_rsi + 304 + 8, Arg2, a3, *(uint16_t *)(local_rsp - 0x1C8 + 0x82));
    *(uint16_t *)(local_rsi + 0x130) = 1;
    result = 0;
    v_stack_m270 = 0;
    v_stack_m278 = *(uint64_t *)(local_rsi + 0x28 + 0x8);
    v_stack_m280 = local_rsi + 40;
loc_004F3426:
    v_stack_m294 = 0;
    if (local_rsi + 40 == 0) goto loc_004F3434;
    goto loc_004F343B;
loc_004F3434:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m270)) + (1));
loc_004F343B:
    if (*(uint64_t *)(local_rsi + 0x28 + 0x8) != 0) goto loc_004F3463;
    local_r13 = (uint16_t)((v_stack_m270) + (1));
    v_stack_m270 = (uint16_t)((uint16_t)(local_r13));
    if (((uint32_t)((uint16_t)(local_r13))) >= ((uint32_t)(Arg1))) goto loc_004F34CB;
    v_stack_m278 = *(uint64_t *)(local_rsi + 0x28 + (uint16_t)(local_r13) * 8 + 0x8);
    goto loc_004F343B;
loc_004F3463:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m270)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(local_rsi + 40))));
    v_stack_m278 = *(uint64_t *)(local_rsi + 0x28 + (uint16_t)(local_r13) * 8 + 0x8);
    v_stack_m294 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA2FD32) + Arg1 * 4)));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA2FD32) + Arg1 * 4)))), local_rsi + 40, 1, *(uint16_t *)(local_rsp - 0x1C8 + 0x82));
    Arg1 = 0;
    if ((*(uint8_t *)(result + 0x8A4C)) == 0) goto loc_004F3426;
    result = KeAddProcessorAffinityEx(local_rsi + 304, (uint32_t)(v_stack_m294), Arg1 + 1, *(uint16_t *)(local_rsp - 0x1C8 + 0x82));
    result = 0;
    goto loc_004F3426;
loc_004F34CB:
    result = KiOrAffinityEx(v_stack_m258, local_rsi + 304, v_stack_m258, v_stack_m256);
    local_r13 = (uint16_t)((v_stack_m2A6) + ((uint16_t)(local_rdi)));
    *(uint16_t *)(local_rsi + 0x4) = (uint16_t)(local_r14);
    local_r14 = 0;
    v_stack_m2A6 = (uint16_t)(local_r13);
    *(uint16_t *)(local_rsi + 0x2) = (uint16_t)(local_rdi);
loc_004F3511:
    local_r15 = (uint32_t)((0) + ((uint32_t)(local_r14 + 1)));
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(v_stack_m268 + 0xC)))) goto loc_004F32F1;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x1C8 + 0x80))) >= ((uint16_t)(v_stack_m258))) goto loc_004F3542;
    goto loc_004F3550;
loc_004F3542:
loc_004F3550:
loc_004F355A:
    if (0 >= ((uint16_t)((uint16_t)(v_stack_m258)))) goto loc_004F3578;
    if ((*(uint64_t *)(local_rsp - 0x1C8 + 0x0 * 8 + 0x88)) != (*(uint64_t *)(local_rsp + 0x0 * 8 + 0x78))) goto loc_004F358C;
    Arg2 = (uint16_t)((0) + (1));
    goto loc_004F355A;
loc_004F3578:
    if (((uint16_t)(Arg2)) >= ((uint16_t)((uint16_t)(*(uint16_t *)(local_rsp - 0x1C8 + 0x80))))) goto loc_004F359A;
    if ((*(uint64_t *)(local_rsp - 0x1C8 + 0x88 + (uint16_t)(Arg2) * 8)) != 0) goto loc_004F358C;
    Arg2 = (uint16_t)((Arg2) + (1));
    goto loc_004F3578;
loc_004F358C:
    result = PpmEventParkNodeParkHintChangedEx(v_stack_m268 + 48, v_stack_m258, (uint16_t)(v_stack_m258), local_rsp - 456 + 136);
loc_004F359A:
    if ((uint16_t)(local_r13) == 0) {
        Arg2 = *(uint64_t *)(v_stack_m268 + 0x508);
        result = *(uint16_t *)(v_rip + 0xA14DF4);
        *(uint16_t *)(Arg2 + 0x2) = (uint16_t)(result);
        Arg1 = *(uint16_t *)(v_rip + 0xA14DE9);
        result = *(uint16_t *)(Arg2 + 0x4);
        if (((uint16_t)(Arg1)) <= ((uint16_t)(result))) { Arg1 = (uint16_t)(result); }
        *(uint16_t *)(Arg2 + 0x4) = (uint16_t)(Arg1);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1A6A)))) != 2) goto loc_004F3633;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m268 + 0x508) + 0x2))) <= 1) {
        Arg1 = 1;
    }
    *(uint16_t *)(*(uint64_t *)(v_stack_m268 + 0x508) + 0x2) = (uint16_t)(Arg1);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m268 + 0x508) + 0x4))) <= 1) {
        Arg1 = 1;
    }
    *(uint16_t *)(*(uint64_t *)(v_stack_m268 + 0x508) + 0x4) = (uint16_t)(Arg1);
    if ((*(uint8_t *)(v_stack_m268 + 0xC)) <= 1) goto loc_004F36A8;
loc_004F3610:
    Arg2 = (uint32_t)((1) + (1));
    Arg1 = (1 + 1 * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m268 + 0x508));
    if (Arg2 < ((uint32_t)(*(uint8_t *)(v_stack_m268 + 0xC)))) goto loc_004F3610;
    goto loc_004F36A8;
loc_004F3633:
    if (((uint32_t)(*(uint8_t *)(v_stack_m268 + 0xC))) != 3) goto loc_004F36A8;
    if ((*(uint8_t *)(v_stack_m268 + 0x4A1)) == 0) goto loc_004F36A8;
    if ((*(uint8_t *)(v_stack_m268 + 0xC)) <= 1) goto loc_004F3675;
loc_004F3651:
    Arg2 = (uint32_t)((0) + (1));
    Arg1 = (0 + 0 * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m268 + 0x508));
    if (((uint32_t)(Arg2 + 1)) < ((uint32_t)(*(uint8_t *)(v_stack_m268 + 0xC)))) goto loc_004F3651;
loc_004F3675:
    Arg1 = ((uint32_t)(Arg2) + (uint32_t)(Arg2) * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m268 + 0x508));
    result = *(uint16_t *)(Arg1 + 0x2);
    if (((uint16_t)(*(uint16_t *)(Arg1 + 0x2))) <= 1) {
        result = 1;
    }
    *(uint16_t *)(Arg1 + 0x2) = (uint16_t)(result);
    result = *(uint16_t *)(Arg1 + 0x4);
    if (((uint16_t)(*(uint16_t *)(Arg1 + 0x4))) <= 1) {
        result = 1;
    }
    *(uint16_t *)(Arg1 + 0x4) = (uint16_t)(result);
loc_004F36A8:
    result = PpmConfigureRestrictionPolicy(v_stack_m268, Arg2, (uint16_t)(v_stack_m258), local_rsp - 456 + 136);
    Arg1 = (uint16_t)((v_stack_m2A4) + (1));
    v_stack_m2A4 = (uint16_t)(Arg1);
    if (((uint32_t)((uint16_t)(Arg1))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))))) goto loc_004F3213;
    local_rsi = 0;
    goto loc_004F3744;
loc_004F36EB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))) == 0) goto loc_004F3744;
loc_004F36F2:
    if ((uint32_t)((uint32_t)(v_stack_m29C)) == 0) goto loc_004F37A1;
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA14CCD));
    if ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)) == 0) goto loc_004F373A;
    result = (uint16_t)((*(uint16_t *)(v_rip + 0xA14C85)) + (*(uint16_t *)(Arg1 + 0x490)));
    local_rdi = (uint32_t)(v_stack_m29C);
    if (((uint16_t)(result)) < ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)))) {
        *(uint16_t *)(Arg1 + 0x490) = (uint16_t)(result);
        result = *(uint16_t *)(v_rip + 0xA14C6A);
        local_rdi = (uint32_t)(((uint32_t)(v_stack_m29C)) - ((uint32_t)(result)));
    }
    Arg2 = (uint16_t)((0) + 1);
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))))) goto loc_004F36F2;
loc_004F3744:
    if ((uint32_t)(local_rdi) != 0) goto loc_004F36EB;
    goto loc_004F37A1;
loc_004F374A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))) == 0) goto loc_004F37A1;
loc_004F3751:
    if ((uint32_t)((uint32_t)(v_stack_m298)) == 0) goto loc_004F37A6;
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA14C71));
    if ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)) == 0) goto loc_004F3797;
    result = (uint16_t)((*(uint16_t *)(Arg1 + 0x494)) + (*(uint16_t *)(v_rip + 0xA14C22)));
    local_r14 = (uint32_t)(v_stack_m298);
    if (((uint16_t)(result)) < ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)))) {
        *(uint16_t *)(Arg1 + 0x494) = (uint16_t)(result);
        result = *(uint16_t *)(v_rip + 0xA14C0E);
        local_r14 = (uint32_t)(((uint32_t)(v_stack_m298)) - ((uint32_t)(result)));
    }
    Arg2 = (uint16_t)((0) + 1);
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))))) goto loc_004F3751;
loc_004F37A1:
    if ((uint32_t)(local_r14) != 0) goto loc_004F374A;
loc_004F37A6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))) == 0) goto loc_004F3845;
loc_004F37B7:
    local_rbx = ((uint32_t)(*(uint32_t *)(v_rip + 0xA14D25))) * (0);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xA14C10));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0xA)))) - ((uint32_t)(*(uint16_t *)(local_rbx + 0x490))));
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x492))) != ((uint32_t)(Arg1))) goto loc_004F37FF;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rbx + 0xA)) - ((uint32_t)(*(uint16_t *)(local_rbx + 0x494))));
    result = *(uint16_t *)(local_rbx + 0x496);
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x496))) != Arg2) {
        a4 = *(uint16_t *)(local_rbx + 0x494);
        Arg2 = local_rbx + 48;
        Arg1 = 0;
        result = PpmEventParkNodeCapChangeEx(Arg1, Arg2, *(uint16_t *)(local_rbx + 0x490), a4);
        Arg1 = *(uint16_t *)(local_rbx + 0xA);
        result = (uint16_t)(Arg1);
        result = (uint16_t)((result) - (*(uint16_t *)(local_rbx + 0x490)));
        Arg1 = (uint16_t)((Arg1) - (*(uint16_t *)(local_rbx + 0x494)));
        *(uint16_t *)(local_rbx + 0x496) = (uint16_t)(Arg1);
        *(uint16_t *)(local_rbx + 0x492) = (uint16_t)(result);
    }
    local_rdi = (uint16_t)((0) + (1));
    if (((uint32_t)((uint16_t)(local_rdi))) < (*(uint32_t *)(v_rip + 0xA14BA8))) goto loc_004F37B7;
    local_rsi = 0;
loc_004F3845:
    if ((*(uint8_t *)(v_rip + 0xA1A8A4)) == 0) goto loc_004F3876;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1836))) == 0) goto loc_004F3876;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0xA0))) == 0) goto loc_004F386A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1836)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0xA0))))) goto loc_004F3876;
loc_004F386A:
    goto loc_004F387B;
loc_004F3876:
loc_004F387B:
    Arg1 = 0;
    result = PpmEventSoftParkLatencyUpdate(Arg1, 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1836)))))), a4);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1836))))) != 0) goto loc_004F38E6;
    *(uint8_t *)(v_rip + 0xAD325A) = 0;
    *(uint32_t *)(v_rip + 0xA2FBB7) = 0;
    if (*(uint64_t *)(v_rip + 0xA14B38) == 0) goto loc_004F3913;
    if (*(uint64_t *)(v_rip + 0xA14B0F) == 0) goto loc_004F3913;
    a3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAD3233))) << (2);
    result = memset(*(uint64_t *)(v_rip + 0xA14B38), 255, a3, a4);
    a3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAD321C))) << (2);
    result = memset(*(uint64_t *)(v_rip + 0xA14B0F), 255, a3, a4);
    result = KeUpdateSoftParkRankList(*(uint64_t *)(v_rip + 0xA14B0F), 255, a3, a4);
    result = PpmEventSoftParkRankListChanged(*(uint64_t *)(v_rip + 0xA14B0F), 255, a3, a4);
    goto loc_004F3913;
loc_004F38E6:
    *(uint8_t *)(v_rip + 0xAD31F3) = 255;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x44))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x44)));
    result = PpmConvertTime(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA14B0F))), a4);
    *(uint32_t *)(v_rip + 0xA2FB41) = (uint32_t)(result);
loc_004F3913:
    result = PpmHeteroHgsCheckContainmentDecision(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA14B0F))), a4);
loc_004F3918:
    Arg1 = (*(uint64_t *)(local_rsp - 0x1C8 + 0x190)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA14B0F))), a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F3090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
