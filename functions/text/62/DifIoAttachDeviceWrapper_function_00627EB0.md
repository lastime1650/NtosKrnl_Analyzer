# DifIoAttachDeviceWrapper

- RVA: `0x00627EB0`–`0x00628027` (길이 `375` bytes)
- VA: `0x0000000140627EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00627EEE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00627F14` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00627F48` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627F6E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627F87` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00627F95` → [IoAttachDevice](../../page/71/IoAttachDevice_function_0071CE80.md) (function, `0x0071CE80`)
- `0x00627FC1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627FE7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00628000` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00627F24` → RVA `0x00F048B8` (`.data`; read)
- `0x00627F35` → RVA `0x00F04980` (`.data`; read)
- `0x00627F41` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00627F95` → [IoAttachDevice](../../page/71/IoAttachDevice_function_0071CE80.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00627EB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00627EB5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00627EBA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00627EBF  55                              push rbp
00627EC0  41 54                           push r12
00627EC2  41 55                           push r13
00627EC4  41 56                           push r14
00627EC6  41 57                           push r15
00627EC8  48 8B EC                        mov rbp, rsp
00627ECB  48 83 EC 50                     sub rsp, 0x50
00627ECF  0F 57 C0                        xorps xmm0, xmm0
00627ED2  33 C0                           xor eax, eax
00627ED4  4C 8B E9                        mov r13, rcx
00627ED7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00627EDB  B9 6B 01 00 00                  mov ecx, 0x16b
00627EE0  4D 8B F8                        mov r15, r8
00627EE3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00627EE7  4C 8B E2                        mov r12, rdx
00627EEA  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00627EEE  E8 41 DB E6 FF                  call 0x140495a34
00627EF3  48 8B F0                        mov rsi, rax
00627EF6  48 85 C0                        test rax, rax
00627EF9  0F 84 8D 00 00 00               je 0x140627f8c
00627EFF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00627F02  A8 18                           test al, 0x18
00627F04  74 0A                           je 0x140627f10
00627F06  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00627F0A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00627F0E  EB 0D                           jmp 0x140627f1d
00627F10  A8 04                           test al, 4
00627F12  74 09                           je 0x140627f1d
00627F14  E8 EF BC EA FF                  call 0x1404d3c08
00627F19  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00627F1D  45 32 F6                        xor r14b, r14b
00627F20  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00627F24  44 38 35 8D C9 8D 00            cmp byte ptr [rip + 0x8dc98d], r14b
00627F2B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00627F2F  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00627F33  75 0C                           jne 0x140627f41
00627F35  F7 05 41 CA 8D 00 00 08 00 00   test dword ptr [rip + 0x8dca41], 0x800
00627F3F  74 13                           je 0x140627f54
00627F41  48 8D 0D 38 BF 8D 00            lea rcx, [rip + 0x8dbf38]
00627F48  E8 D3 E6 BE FF                  call 0x140216620
00627F4D  44 8A F0                        mov r14b, al
00627F50  84 C0                           test al, al
00627F52  74 38                           je 0x140627f8c
00627F54  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00627F58  48 8B 1F                        mov rbx, qword ptr [rdi]
00627F5B  EB 19                           jmp 0x140627f76
00627F5D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627F61  48 85 C0                        test rax, rax
00627F64  74 0D                           je 0x140627f73
00627F66  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00627F6A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00627F6E  E8 5D 2B 09 00                  call 0x1406baad0
00627F73  48 8B 1B                        mov rbx, qword ptr [rbx]
00627F76  48 3B DF                        cmp rbx, rdi
00627F79  75 E2                           jne 0x140627f5d
00627F7B  45 84 F6                        test r14b, r14b
00627F7E  74 0C                           je 0x140627f8c
00627F80  48 8D 0D F9 BE 8D 00            lea rcx, [rip + 0x8dbef9]
00627F87  E8 F4 1E D2 FF                  call 0x140349e80
00627F8C  4D 8B C7                        mov r8, r15
00627F8F  49 8B D4                        mov rdx, r12
00627F92  49 8B CD                        mov rcx, r13
00627F95  E8 E6 4E 0F 00                  call 0x14071ce80
00627F9A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00627F9D  48 85 F6                        test rsi, rsi
00627FA0  74 63                           je 0x140628005
00627FA2  40 32 FF                        xor dil, dil
00627FA5  40 38 3D 0C C9 8D 00            cmp byte ptr [rip + 0x8dc90c], dil
00627FAC  75 0C                           jne 0x140627fba
00627FAE  F7 05 C8 C9 8D 00 00 08 00 00   test dword ptr [rip + 0x8dc9c8], 0x800
00627FB8  74 13                           je 0x140627fcd
00627FBA  48 8D 0D BF BE 8D 00            lea rcx, [rip + 0x8dbebf]
00627FC1  E8 5A E6 BE FF                  call 0x140216620
00627FC6  40 8A F8                        mov dil, al
00627FC9  84 C0                           test al, al
00627FCB  74 38                           je 0x140628005
00627FCD  48 83 C6 30                     add rsi, 0x30
00627FD1  48 8B 1E                        mov rbx, qword ptr [rsi]
00627FD4  EB 19                           jmp 0x140627fef
00627FD6  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627FDA  48 85 C0                        test rax, rax
00627FDD  74 0D                           je 0x140627fec
00627FDF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00627FE3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00627FE7  E8 E4 2A 09 00                  call 0x1406baad0
00627FEC  48 8B 1B                        mov rbx, qword ptr [rbx]
00627FEF  48 3B DE                        cmp rbx, rsi
00627FF2  75 E2                           jne 0x140627fd6
00627FF4  40 84 FF                        test dil, dil
00627FF7  74 0C                           je 0x140628005
00627FF9  48 8D 0D 80 BE 8D 00            lea rcx, [rip + 0x8dbe80]
00628000  E8 7B 1E D2 FF                  call 0x140349e80
00628005  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00628008  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062800D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00628011  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00628015  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00628019  49 8B E3                        mov rsp, r11
0062801C  41 5F                           pop r15
0062801E  41 5E                           pop r14
00628020  41 5D                           pop r13
00628022  41 5C                           pop r12
00628024  5D                              pop rbp
00628025  C3                              ret
00628026  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoAttachDeviceWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(363, a2, a3, a4);
    if (result == 0) goto loc_00627F8C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00627F10;
    v_stack_m58 = v_stack_p0;
    goto loc_00627F1D;
loc_00627F10:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9292173)) != 0) goto loc_00627F41;
    if (((*(unsigned int *)(v_rip + 9292353)) & (0x800ULL)) == 0) goto loc_00627F54;
loc_00627F41:
    result = ExAcquireRundownProtection(v_rip + 9289528, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00627F8C;
loc_00627F54:
    goto loc_00627F76;
loc_00627F5D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627F76:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00627F5D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9289465;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoAttachDevice(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00628005;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9292044)) != 0) goto loc_00627FBA;
    if (((*(unsigned int *)(v_rip + 9292232)) & (0x800ULL)) == 0) goto loc_00627FCD;
loc_00627FBA:
    result = ExAcquireRundownProtection(v_rip + 9289407, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00628005;
loc_00627FCD:
    v_rsi = (result) + (48);
    goto loc_00627FEF;
loc_00627FD6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627FEF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00627FD6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9289344;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoAttachDeviceWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(363, Arg2, Arg3, a4);
    if (result == 0) goto loc_00627F8C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00627F10;
    v_stack_m58 = v_stack_p0;
    goto loc_00627F1D;
loc_00627F10:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8DC98D)) != 0) goto loc_00627F41;
    if (((*(uint32_t *)(v_rip + 0x8DCA41)) & (0x800ULL)) == 0) goto loc_00627F54;
loc_00627F41:
    result = ExAcquireRundownProtection(v_rip + 9289528, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00627F8C;
loc_00627F54:
    goto loc_00627F76;
loc_00627F5D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00627F76:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00627F5D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9289465;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoAttachDevice(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00628005;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DC90C)) != 0) goto loc_00627FBA;
    if (((*(uint32_t *)(v_rip + 0x8DC9C8)) & (0x800ULL)) == 0) goto loc_00627FCD;
loc_00627FBA:
    result = ExAcquireRundownProtection(v_rip + 9289407, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00628005;
loc_00627FCD:
    local_rsi = (result) + (48);
    goto loc_00627FEF;
loc_00627FD6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00627FEF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00627FD6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9289344;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00627EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00627EB0[BB_00627EB0]
  bb_00627EFF[BB_00627EFF]
  bb_00627F06[BB_00627F06]
  bb_00627F10[BB_00627F10]
  bb_00627F14[BB_00627F14]
  bb_00627F1D[BB_00627F1D]
  bb_00627F35[BB_00627F35]
  bb_00627F41[BB_00627F41]
  bb_00627F54[BB_00627F54]
  bb_00627F5D[BB_00627F5D]
  bb_00627F66[BB_00627F66]
  bb_00627F73[BB_00627F73]
  bb_00627F76[BB_00627F76]
  bb_00627F7B[BB_00627F7B]
  bb_00627F80[BB_00627F80]
  bb_00627F8C[BB_00627F8C]
  bb_00627FA2[BB_00627FA2]
  bb_00627FAE[BB_00627FAE]
  bb_00627FBA[BB_00627FBA]
  bb_00627FCD[BB_00627FCD]
  bb_00627FD6[BB_00627FD6]
  bb_00627FDF[BB_00627FDF]
  bb_00627FEC[BB_00627FEC]
  bb_00627FEF[BB_00627FEF]
  bb_00627FF4[BB_00627FF4]
  bb_00627FF9[BB_00627FF9]
  bb_00628005[BB_00628005]
  bb_00628026[BB_00628026]
  bb_00627EB0 -->|branch| bb_00627F8C
  bb_00627EB0 -->|fallthrough| bb_00627EFF
  bb_00627EFF -->|branch| bb_00627F10
  bb_00627EFF -->|fallthrough| bb_00627F06
  bb_00627F06 -->|branch| bb_00627F1D
  bb_00627F10 -->|branch| bb_00627F1D
  bb_00627F10 -->|fallthrough| bb_00627F14
  bb_00627F14 -->|flow| bb_00627F1D
  bb_00627F1D -->|branch| bb_00627F41
  bb_00627F1D -->|fallthrough| bb_00627F35
  bb_00627F35 -->|branch| bb_00627F54
  bb_00627F35 -->|fallthrough| bb_00627F41
  bb_00627F41 -->|branch| bb_00627F8C
  bb_00627F41 -->|fallthrough| bb_00627F54
  bb_00627F54 -->|branch| bb_00627F76
  bb_00627F5D -->|branch| bb_00627F73
  bb_00627F5D -->|fallthrough| bb_00627F66
  bb_00627F66 -->|flow| bb_00627F73
  bb_00627F73 -->|flow| bb_00627F76
  bb_00627F76 -->|branch| bb_00627F5D
  bb_00627F76 -->|fallthrough| bb_00627F7B
  bb_00627F7B -->|branch| bb_00627F8C
  bb_00627F7B -->|fallthrough| bb_00627F80
  bb_00627F80 -->|flow| bb_00627F8C
  bb_00627F8C -->|branch| bb_00628005
  bb_00627F8C -->|fallthrough| bb_00627FA2
  bb_00627FA2 -->|branch| bb_00627FBA
  bb_00627FA2 -->|fallthrough| bb_00627FAE
  bb_00627FAE -->|branch| bb_00627FCD
  bb_00627FAE -->|fallthrough| bb_00627FBA
  bb_00627FBA -->|branch| bb_00628005
  bb_00627FBA -->|fallthrough| bb_00627FCD
  bb_00627FCD -->|branch| bb_00627FEF
  bb_00627FD6 -->|branch| bb_00627FEC
  bb_00627FD6 -->|fallthrough| bb_00627FDF
  bb_00627FDF -->|flow| bb_00627FEC
  bb_00627FEC -->|flow| bb_00627FEF
  bb_00627FEF -->|branch| bb_00627FD6
  bb_00627FEF -->|fallthrough| bb_00627FF4
  bb_00627FF4 -->|branch| bb_00628005
  bb_00627FF4 -->|fallthrough| bb_00627FF9
  bb_00627FF9 -->|flow| bb_00628005
```
