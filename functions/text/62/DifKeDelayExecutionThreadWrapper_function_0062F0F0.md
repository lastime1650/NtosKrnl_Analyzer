# DifKeDelayExecutionThreadWrapper

- RVA: `0x0062F0F0`–`0x0062F26D` (길이 `381` bytes)
- VA: `0x000000014062F0F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `104`개 명령, `381/381` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062F129` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062F151` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062F189` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F1B0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F1C9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062F1D7` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x0062F204` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F22B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F244` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062F163` → RVA `0x00F048B8` (`.data`; read)
- `0x0062F176` → RVA `0x00F04980` (`.data`; read)
- `0x0062F182` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062F0F0  4C 8B DC                        mov r11, rsp
0062F0F3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062F0F7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062F0FB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062F0FF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062F103  41 54                           push r12
0062F105  41 56                           push r14
0062F107  41 57                           push r15
0062F109  48 83 EC 40                     sub rsp, 0x40
0062F10D  33 C0                           xor eax, eax
0062F10F  0F 57 C0                        xorps xmm0, xmm0
0062F112  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062F117  44 8A E1                        mov r12b, cl
0062F11A  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0062F11E  B9 20 01 00 00                  mov ecx, 0x120
0062F123  4D 8B F0                        mov r14, r8
0062F126  44 8A FA                        mov r15b, dl
0062F129  E8 06 69 E6 FF                  call 0x140495a34
0062F12E  48 8B F0                        mov rsi, rax
0062F131  48 85 C0                        test rax, rax
0062F134  0F 84 94 00 00 00               je 0x14062f1ce
0062F13A  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062F13D  A8 18                           test al, 0x18
0062F13F  74 0C                           je 0x14062f14d
0062F141  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062F146  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062F14B  EB 0E                           jmp 0x14062f15b
0062F14D  A8 04                           test al, 4
0062F14F  74 0A                           je 0x14062f15b
0062F151  E8 B2 4A EA FF                  call 0x1404d3c08
0062F156  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062F15B  40 32 ED                        xor bpl, bpl
0062F15E  44 88 64 24 31                  mov byte ptr [rsp + 0x31], r12b
0062F163  40 38 2D 4E 57 8D 00            cmp byte ptr [rip + 0x8d574e], bpl
0062F16A  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0062F16F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0062F174  75 0C                           jne 0x14062f182
0062F176  F7 05 00 58 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5800], 0x800
0062F180  74 13                           je 0x14062f195
0062F182  48 8D 0D F7 4C 8D 00            lea rcx, [rip + 0x8d4cf7]
0062F189  E8 92 74 BE FF                  call 0x140216620
0062F18E  40 8A E8                        mov bpl, al
0062F191  84 C0                           test al, al
0062F193  74 39                           je 0x14062f1ce
0062F195  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062F199  48 8B 1F                        mov rbx, qword ptr [rdi]
0062F19C  EB 1A                           jmp 0x14062f1b8
0062F19E  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F1A2  48 85 C0                        test rax, rax
0062F1A5  74 0E                           je 0x14062f1b5
0062F1A7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F1AB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F1B0  E8 1B B9 08 00                  call 0x1406baad0
0062F1B5  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F1B8  48 3B DF                        cmp rbx, rdi
0062F1BB  75 E1                           jne 0x14062f19e
0062F1BD  40 84 ED                        test bpl, bpl
0062F1C0  74 0C                           je 0x14062f1ce
0062F1C2  48 8D 0D B7 4C 8D 00            lea rcx, [rip + 0x8d4cb7]
0062F1C9  E8 B2 AC D1 FF                  call 0x140349e80
0062F1CE  4D 8B C6                        mov r8, r14
0062F1D1  41 8A D7                        mov dl, r15b
0062F1D4  41 8A CC                        mov cl, r12b
0062F1D7  E8 74 A3 BD FF                  call 0x140209550
0062F1DC  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0062F1E0  48 85 F6                        test rsi, rsi
0062F1E3  74 64                           je 0x14062f249
0062F1E5  40 32 FF                        xor dil, dil
0062F1E8  40 38 3D C9 56 8D 00            cmp byte ptr [rip + 0x8d56c9], dil
0062F1EF  75 0C                           jne 0x14062f1fd
0062F1F1  F7 05 85 57 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5785], 0x800
0062F1FB  74 13                           je 0x14062f210
0062F1FD  48 8D 0D 7C 4C 8D 00            lea rcx, [rip + 0x8d4c7c]
0062F204  E8 17 74 BE FF                  call 0x140216620
0062F209  40 8A F8                        mov dil, al
0062F20C  84 C0                           test al, al
0062F20E  74 39                           je 0x14062f249
0062F210  48 83 C6 30                     add rsi, 0x30
0062F214  48 8B 1E                        mov rbx, qword ptr [rsi]
0062F217  EB 1A                           jmp 0x14062f233
0062F219  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F21D  48 85 C0                        test rax, rax
0062F220  74 0E                           je 0x14062f230
0062F222  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F226  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F22B  E8 A0 B8 08 00                  call 0x1406baad0
0062F230  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F233  48 3B DE                        cmp rbx, rsi
0062F236  75 E1                           jne 0x14062f219
0062F238  40 84 FF                        test dil, dil
0062F23B  74 0C                           je 0x14062f249
0062F23D  48 8D 0D 3C 4C 8D 00            lea rcx, [rip + 0x8d4c3c]
0062F244  E8 37 AC D1 FF                  call 0x140349e80
0062F249  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0062F24D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062F252  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062F257  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062F25C  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062F261  48 83 C4 40                     add rsp, 0x40
0062F265  41 5F                           pop r15
0062F267  41 5E                           pop r14
0062F269  41 5C                           pop r12
0062F26B  C3                              ret
0062F26C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeDelayExecutionThreadWrapper(unsigned __int8 a1, unsigned __int8 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m24;
    unsigned __int8 v_stack_m27;
    unsigned __int8 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(288, a2, a3, a4);
    if (result == 0) goto loc_0062F1CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062F14D;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F15B;
loc_0062F14D:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m27 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9262926)) != 0) goto loc_0062F182;
    if (((*(unsigned int *)(v_rip + 9263104)) & (0x800ULL)) == 0) goto loc_0062F195;
loc_0062F182:
    result = ExAcquireRundownProtection(v_rip + 9260279, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F1CE;
loc_0062F195:
    goto loc_0062F1B8;
loc_0062F19E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F1B8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062F19E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260215;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeDelayExecutionThread(a1, a2, a3, a4);
    v_stack_m24 = (unsigned int)(result);
    if (result == 0) goto loc_0062F249;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9262793)) != 0) goto loc_0062F1FD;
    if (((*(unsigned int *)(v_rip + 9262981)) & (0x800ULL)) == 0) goto loc_0062F210;
loc_0062F1FD:
    result = ExAcquireRundownProtection(v_rip + 9260156, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F249;
loc_0062F210:
    v_rsi = (result) + (48);
    goto loc_0062F233;
loc_0062F219:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F233:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062F219;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260092;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m24);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeDelayExecutionThreadWrapper(uint8_t Arg1, uint8_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m24;
    uint8_t v_stack_m27;
    uint8_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(288, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062F1CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062F14D;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F15B;
loc_0062F14D:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m27 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D574E)) != 0) goto loc_0062F182;
    if (((*(uint32_t *)(v_rip + 0x8D5800)) & (0x800ULL)) == 0) goto loc_0062F195;
loc_0062F182:
    result = ExAcquireRundownProtection(v_rip + 9260279, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F1CE;
loc_0062F195:
    goto loc_0062F1B8;
loc_0062F19E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062F1B8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062F19E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260215;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = KeDelayExecutionThread(Arg1, Arg2, Arg3, a4);
    v_stack_m24 = (uint32_t)(result);
    if (result == 0) goto loc_0062F249;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D56C9)) != 0) goto loc_0062F1FD;
    if (((*(uint32_t *)(v_rip + 0x8D5785)) & (0x800ULL)) == 0) goto loc_0062F210;
loc_0062F1FD:
    result = ExAcquireRundownProtection(v_rip + 9260156, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F249;
loc_0062F210:
    local_rsi = (result) + (48);
    goto loc_0062F233;
loc_0062F219:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062F233:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062F219;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260092;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m24);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062F0F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062F0F0[BB_0062F0F0]
  bb_0062F13A[BB_0062F13A]
  bb_0062F141[BB_0062F141]
  bb_0062F14D[BB_0062F14D]
  bb_0062F151[BB_0062F151]
  bb_0062F15B[BB_0062F15B]
  bb_0062F176[BB_0062F176]
  bb_0062F182[BB_0062F182]
  bb_0062F195[BB_0062F195]
  bb_0062F19E[BB_0062F19E]
  bb_0062F1A7[BB_0062F1A7]
  bb_0062F1B5[BB_0062F1B5]
  bb_0062F1B8[BB_0062F1B8]
  bb_0062F1BD[BB_0062F1BD]
  bb_0062F1C2[BB_0062F1C2]
  bb_0062F1CE[BB_0062F1CE]
  bb_0062F1E5[BB_0062F1E5]
  bb_0062F1F1[BB_0062F1F1]
  bb_0062F1FD[BB_0062F1FD]
  bb_0062F210[BB_0062F210]
  bb_0062F219[BB_0062F219]
  bb_0062F222[BB_0062F222]
  bb_0062F230[BB_0062F230]
  bb_0062F233[BB_0062F233]
  bb_0062F238[BB_0062F238]
  bb_0062F23D[BB_0062F23D]
  bb_0062F249[BB_0062F249]
  bb_0062F26C[BB_0062F26C]
  bb_0062F0F0 -->|branch| bb_0062F1CE
  bb_0062F0F0 -->|fallthrough| bb_0062F13A
  bb_0062F13A -->|branch| bb_0062F14D
  bb_0062F13A -->|fallthrough| bb_0062F141
  bb_0062F141 -->|branch| bb_0062F15B
  bb_0062F14D -->|branch| bb_0062F15B
  bb_0062F14D -->|fallthrough| bb_0062F151
  bb_0062F151 -->|flow| bb_0062F15B
  bb_0062F15B -->|branch| bb_0062F182
  bb_0062F15B -->|fallthrough| bb_0062F176
  bb_0062F176 -->|branch| bb_0062F195
  bb_0062F176 -->|fallthrough| bb_0062F182
  bb_0062F182 -->|branch| bb_0062F1CE
  bb_0062F182 -->|fallthrough| bb_0062F195
  bb_0062F195 -->|branch| bb_0062F1B8
  bb_0062F19E -->|branch| bb_0062F1B5
  bb_0062F19E -->|fallthrough| bb_0062F1A7
  bb_0062F1A7 -->|flow| bb_0062F1B5
  bb_0062F1B5 -->|flow| bb_0062F1B8
  bb_0062F1B8 -->|branch| bb_0062F19E
  bb_0062F1B8 -->|fallthrough| bb_0062F1BD
  bb_0062F1BD -->|branch| bb_0062F1CE
  bb_0062F1BD -->|fallthrough| bb_0062F1C2
  bb_0062F1C2 -->|flow| bb_0062F1CE
  bb_0062F1CE -->|branch| bb_0062F249
  bb_0062F1CE -->|fallthrough| bb_0062F1E5
  bb_0062F1E5 -->|branch| bb_0062F1FD
  bb_0062F1E5 -->|fallthrough| bb_0062F1F1
  bb_0062F1F1 -->|branch| bb_0062F210
  bb_0062F1F1 -->|fallthrough| bb_0062F1FD
  bb_0062F1FD -->|branch| bb_0062F249
  bb_0062F1FD -->|fallthrough| bb_0062F210
  bb_0062F210 -->|branch| bb_0062F233
  bb_0062F219 -->|branch| bb_0062F230
  bb_0062F219 -->|fallthrough| bb_0062F222
  bb_0062F222 -->|flow| bb_0062F230
  bb_0062F230 -->|flow| bb_0062F233
  bb_0062F233 -->|branch| bb_0062F219
  bb_0062F233 -->|fallthrough| bb_0062F238
  bb_0062F238 -->|branch| bb_0062F249
  bb_0062F238 -->|fallthrough| bb_0062F23D
  bb_0062F23D -->|flow| bb_0062F249
```
