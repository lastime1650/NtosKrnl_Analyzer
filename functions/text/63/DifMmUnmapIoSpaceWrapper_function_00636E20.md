# DifMmUnmapIoSpaceWrapper

- RVA: `0x00636E20`–`0x00636F82` (길이 `354` bytes)
- VA: `0x0000000140636E20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `354/354` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00636E51` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00636E79` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00636EAC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00636ED3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636EEC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00636EFA` → [MiUnmapContiguousMemory](../3F/MiUnmapContiguousMemory_function_003F7908.md) (function, `0x003F7908`)
- `0x00636F23` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00636F4A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636F63` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00636E8B` → RVA `0x00F048B8` (`.data`; read)
- `0x00636E99` → RVA `0x00F04980` (`.data`; read)
- `0x00636EA5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636E20  4C 8B DC                        mov r11, rsp
00636E23  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00636E27  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00636E2B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00636E2F  57                              push rdi
00636E30  41 56                           push r14
00636E32  41 57                           push r15
00636E34  48 83 EC 40                     sub rsp, 0x40
00636E38  33 C0                           xor eax, eax
00636E3A  0F 57 C0                        xorps xmm0, xmm0
00636E3D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00636E42  4C 8B F9                        mov r15, rcx
00636E45  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00636E49  B9 D3 00 00 00                  mov ecx, 0xd3
00636E4E  4C 8B F2                        mov r14, rdx
00636E51  E8 DE EB E5 FF                  call 0x140495a34
00636E56  48 8B F0                        mov rsi, rax
00636E59  48 85 C0                        test rax, rax
00636E5C  0F 84 8F 00 00 00               je 0x140636ef1
00636E62  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00636E65  A8 18                           test al, 0x18
00636E67  74 0C                           je 0x140636e75
00636E69  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00636E6E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00636E73  EB 0E                           jmp 0x140636e83
00636E75  A8 04                           test al, 4
00636E77  74 0A                           je 0x140636e83
00636E79  E8 8A CD E9 FF                  call 0x1404d3c08
00636E7E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00636E83  40 32 ED                        xor bpl, bpl
00636E86  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00636E8B  40 38 2D 26 DA 8C 00            cmp byte ptr [rip + 0x8cda26], bpl
00636E92  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00636E97  75 0C                           jne 0x140636ea5
00636E99  F7 05 DD DA 8C 00 00 08 00 00   test dword ptr [rip + 0x8cdadd], 0x800
00636EA3  74 13                           je 0x140636eb8
00636EA5  48 8D 0D D4 CF 8C 00            lea rcx, [rip + 0x8ccfd4]
00636EAC  E8 6F F7 BD FF                  call 0x140216620
00636EB1  40 8A E8                        mov bpl, al
00636EB4  84 C0                           test al, al
00636EB6  74 39                           je 0x140636ef1
00636EB8  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00636EBC  48 8B 1F                        mov rbx, qword ptr [rdi]
00636EBF  EB 1A                           jmp 0x140636edb
00636EC1  48 8D 43 F0                     lea rax, [rbx - 0x10]
00636EC5  48 85 C0                        test rax, rax
00636EC8  74 0E                           je 0x140636ed8
00636ECA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00636ECE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00636ED3  E8 F8 3B 08 00                  call 0x1406baad0
00636ED8  48 8B 1B                        mov rbx, qword ptr [rbx]
00636EDB  48 3B DF                        cmp rbx, rdi
00636EDE  75 E1                           jne 0x140636ec1
00636EE0  40 84 ED                        test bpl, bpl
00636EE3  74 0C                           je 0x140636ef1
00636EE5  48 8D 0D 94 CF 8C 00            lea rcx, [rip + 0x8ccf94]
00636EEC  E8 8F 2F D1 FF                  call 0x140349e80
00636EF1  41 B0 01                        mov r8b, 1
00636EF4  49 8B D6                        mov rdx, r14
00636EF7  49 8B CF                        mov rcx, r15
00636EFA  E8 09 0A DC FF                  call 0x1403f7908
00636EFF  48 85 F6                        test rsi, rsi
00636F02  74 64                           je 0x140636f68
00636F04  40 32 FF                        xor dil, dil
00636F07  40 38 3D AA D9 8C 00            cmp byte ptr [rip + 0x8cd9aa], dil
00636F0E  75 0C                           jne 0x140636f1c
00636F10  F7 05 66 DA 8C 00 00 08 00 00   test dword ptr [rip + 0x8cda66], 0x800
00636F1A  74 13                           je 0x140636f2f
00636F1C  48 8D 0D 5D CF 8C 00            lea rcx, [rip + 0x8ccf5d]
00636F23  E8 F8 F6 BD FF                  call 0x140216620
00636F28  40 8A F8                        mov dil, al
00636F2B  84 C0                           test al, al
00636F2D  74 39                           je 0x140636f68
00636F2F  48 83 C6 30                     add rsi, 0x30
00636F33  48 8B 1E                        mov rbx, qword ptr [rsi]
00636F36  EB 1A                           jmp 0x140636f52
00636F38  48 8D 43 F0                     lea rax, [rbx - 0x10]
00636F3C  48 85 C0                        test rax, rax
00636F3F  74 0E                           je 0x140636f4f
00636F41  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00636F45  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00636F4A  E8 81 3B 08 00                  call 0x1406baad0
00636F4F  48 8B 1B                        mov rbx, qword ptr [rbx]
00636F52  48 3B DE                        cmp rbx, rsi
00636F55  75 E1                           jne 0x140636f38
00636F57  40 84 FF                        test dil, dil
00636F5A  74 0C                           je 0x140636f68
00636F5C  48 8D 0D 1D CF 8C 00            lea rcx, [rip + 0x8ccf1d]
00636F63  E8 18 2F D1 FF                  call 0x140349e80
00636F68  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00636F6D  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00636F72  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00636F77  48 83 C4 40                     add rsp, 0x40
00636F7B  41 5F                           pop r15
00636F7D  41 5E                           pop r14
00636F7F  5F                              pop rdi
00636F80  C3                              ret
00636F81  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmUnmapIoSpaceWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(211, a2, a3, a4);
    if (result == 0) goto loc_00636EF1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00636E75;
    v_stack_m38 = v_stack_p0;
    goto loc_00636E83;
loc_00636E75:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9230886)) != 0) goto loc_00636EA5;
    if (((*(unsigned int *)(v_rip + 9231069)) & (0x800ULL)) == 0) goto loc_00636EB8;
loc_00636EA5:
    result = ExAcquireRundownProtection(v_rip + 9228244, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00636EF1;
loc_00636EB8:
    goto loc_00636EDB;
loc_00636EC1:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00636EDB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00636EC1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9228180;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MiUnmapContiguousMemory(a1, a2, 1, a4);
    if (result == 0) goto loc_00636F68;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9230762)) != 0) goto loc_00636F1C;
    if (((*(unsigned int *)(v_rip + 9230950)) & (0x800ULL)) == 0) goto loc_00636F2F;
loc_00636F1C:
    result = ExAcquireRundownProtection(v_rip + 9228125, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00636F68;
loc_00636F2F:
    v_rsi = (result) + (48);
    goto loc_00636F52;
loc_00636F38:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, 1, a4);
    }
loc_00636F52:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00636F38;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9228061;
        result = ExReleaseRundownProtection(a1, a2, 1, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmUnmapIoSpaceWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(211, Arg2, a3, a4);
    if (result == 0) goto loc_00636EF1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00636E75;
    v_stack_m38 = v_stack_p0;
    goto loc_00636E83;
loc_00636E75:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8CDA26)) != 0) goto loc_00636EA5;
    if (((*(uint32_t *)(v_rip + 0x8CDADD)) & (0x800ULL)) == 0) goto loc_00636EB8;
loc_00636EA5:
    result = ExAcquireRundownProtection(v_rip + 9228244, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00636EF1;
loc_00636EB8:
    goto loc_00636EDB;
loc_00636EC1:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00636EDB:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00636EC1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9228180;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = MiUnmapContiguousMemory(Arg1, Arg2, 1, a4);
    if (result == 0) goto loc_00636F68;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CD9AA)) != 0) goto loc_00636F1C;
    if (((*(uint32_t *)(v_rip + 0x8CDA66)) & (0x800ULL)) == 0) goto loc_00636F2F;
loc_00636F1C:
    result = ExAcquireRundownProtection(v_rip + 9228125, Arg2, 1, a4);
    if ((uint8_t)(result) == 0) goto loc_00636F68;
loc_00636F2F:
    local_rsi = (result) + (48);
    goto loc_00636F52;
loc_00636F38:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, 1, a4);
    }
loc_00636F52:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00636F38;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9228061;
        result = ExReleaseRundownProtection(Arg1, Arg2, 1, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636E20[BB_00636E20]
  bb_00636E62[BB_00636E62]
  bb_00636E69[BB_00636E69]
  bb_00636E75[BB_00636E75]
  bb_00636E79[BB_00636E79]
  bb_00636E83[BB_00636E83]
  bb_00636E99[BB_00636E99]
  bb_00636EA5[BB_00636EA5]
  bb_00636EB8[BB_00636EB8]
  bb_00636EC1[BB_00636EC1]
  bb_00636ECA[BB_00636ECA]
  bb_00636ED8[BB_00636ED8]
  bb_00636EDB[BB_00636EDB]
  bb_00636EE0[BB_00636EE0]
  bb_00636EE5[BB_00636EE5]
  bb_00636EF1[BB_00636EF1]
  bb_00636F04[BB_00636F04]
  bb_00636F10[BB_00636F10]
  bb_00636F1C[BB_00636F1C]
  bb_00636F2F[BB_00636F2F]
  bb_00636F38[BB_00636F38]
  bb_00636F41[BB_00636F41]
  bb_00636F4F[BB_00636F4F]
  bb_00636F52[BB_00636F52]
  bb_00636F57[BB_00636F57]
  bb_00636F5C[BB_00636F5C]
  bb_00636F68[BB_00636F68]
  bb_00636F81[BB_00636F81]
  bb_00636E20 -->|branch| bb_00636EF1
  bb_00636E20 -->|fallthrough| bb_00636E62
  bb_00636E62 -->|branch| bb_00636E75
  bb_00636E62 -->|fallthrough| bb_00636E69
  bb_00636E69 -->|branch| bb_00636E83
  bb_00636E75 -->|branch| bb_00636E83
  bb_00636E75 -->|fallthrough| bb_00636E79
  bb_00636E79 -->|flow| bb_00636E83
  bb_00636E83 -->|branch| bb_00636EA5
  bb_00636E83 -->|fallthrough| bb_00636E99
  bb_00636E99 -->|branch| bb_00636EB8
  bb_00636E99 -->|fallthrough| bb_00636EA5
  bb_00636EA5 -->|branch| bb_00636EF1
  bb_00636EA5 -->|fallthrough| bb_00636EB8
  bb_00636EB8 -->|branch| bb_00636EDB
  bb_00636EC1 -->|branch| bb_00636ED8
  bb_00636EC1 -->|fallthrough| bb_00636ECA
  bb_00636ECA -->|flow| bb_00636ED8
  bb_00636ED8 -->|flow| bb_00636EDB
  bb_00636EDB -->|branch| bb_00636EC1
  bb_00636EDB -->|fallthrough| bb_00636EE0
  bb_00636EE0 -->|branch| bb_00636EF1
  bb_00636EE0 -->|fallthrough| bb_00636EE5
  bb_00636EE5 -->|flow| bb_00636EF1
  bb_00636EF1 -->|branch| bb_00636F68
  bb_00636EF1 -->|fallthrough| bb_00636F04
  bb_00636F04 -->|branch| bb_00636F1C
  bb_00636F04 -->|fallthrough| bb_00636F10
  bb_00636F10 -->|branch| bb_00636F2F
  bb_00636F10 -->|fallthrough| bb_00636F1C
  bb_00636F1C -->|branch| bb_00636F68
  bb_00636F1C -->|fallthrough| bb_00636F2F
  bb_00636F2F -->|branch| bb_00636F52
  bb_00636F38 -->|branch| bb_00636F4F
  bb_00636F38 -->|fallthrough| bb_00636F41
  bb_00636F41 -->|flow| bb_00636F4F
  bb_00636F4F -->|flow| bb_00636F52
  bb_00636F52 -->|branch| bb_00636F38
  bb_00636F52 -->|fallthrough| bb_00636F57
  bb_00636F57 -->|branch| bb_00636F68
  bb_00636F57 -->|fallthrough| bb_00636F5C
  bb_00636F5C -->|flow| bb_00636F68
```
