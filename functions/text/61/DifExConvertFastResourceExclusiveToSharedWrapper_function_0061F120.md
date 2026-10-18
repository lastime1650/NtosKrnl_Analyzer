# DifExConvertFastResourceExclusiveToSharedWrapper

- RVA: `0x0061F120`–`0x0061F27F` (길이 `351` bytes)
- VA: `0x000000014061F120`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `97`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061F151` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061F179` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061F1AC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F1D3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F1EC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061F1F7` → [ExConvertFastResourceExclusiveToShared](../41/ExConvertFastResourceExclusiveToShared_function_00415AB0.md) (function, `0x00415AB0`)
- `0x0061F220` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F247` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F260` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061F18B` → RVA `0x00F048B8` (`.data`; read)
- `0x0061F199` → RVA `0x00F04980` (`.data`; read)
- `0x0061F1A5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061F120  4C 8B DC                        mov r11, rsp
0061F123  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061F127  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061F12B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061F12F  57                              push rdi
0061F130  41 56                           push r14
0061F132  41 57                           push r15
0061F134  48 83 EC 40                     sub rsp, 0x40
0061F138  33 C0                           xor eax, eax
0061F13A  0F 57 C0                        xorps xmm0, xmm0
0061F13D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061F142  4C 8B F9                        mov r15, rcx
0061F145  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0061F149  B9 C9 01 00 00                  mov ecx, 0x1c9
0061F14E  4C 8B F2                        mov r14, rdx
0061F151  E8 DE 68 E7 FF                  call 0x140495a34
0061F156  48 8B F0                        mov rsi, rax
0061F159  48 85 C0                        test rax, rax
0061F15C  0F 84 8F 00 00 00               je 0x14061f1f1
0061F162  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061F165  A8 18                           test al, 0x18
0061F167  74 0C                           je 0x14061f175
0061F169  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0061F16E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061F173  EB 0E                           jmp 0x14061f183
0061F175  A8 04                           test al, 4
0061F177  74 0A                           je 0x14061f183
0061F179  E8 8A 4A EB FF                  call 0x1404d3c08
0061F17E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061F183  40 32 ED                        xor bpl, bpl
0061F186  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0061F18B  40 38 2D 26 57 8E 00            cmp byte ptr [rip + 0x8e5726], bpl
0061F192  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0061F197  75 0C                           jne 0x14061f1a5
0061F199  F7 05 DD 57 8E 00 00 08 00 00   test dword ptr [rip + 0x8e57dd], 0x800
0061F1A3  74 13                           je 0x14061f1b8
0061F1A5  48 8D 0D D4 4C 8E 00            lea rcx, [rip + 0x8e4cd4]
0061F1AC  E8 6F 74 BF FF                  call 0x140216620
0061F1B1  40 8A E8                        mov bpl, al
0061F1B4  84 C0                           test al, al
0061F1B6  74 39                           je 0x14061f1f1
0061F1B8  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061F1BC  48 8B 1F                        mov rbx, qword ptr [rdi]
0061F1BF  EB 1A                           jmp 0x14061f1db
0061F1C1  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F1C5  48 85 C0                        test rax, rax
0061F1C8  74 0E                           je 0x14061f1d8
0061F1CA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F1CE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F1D3  E8 F8 B8 09 00                  call 0x1406baad0
0061F1D8  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F1DB  48 3B DF                        cmp rbx, rdi
0061F1DE  75 E1                           jne 0x14061f1c1
0061F1E0  40 84 ED                        test bpl, bpl
0061F1E3  74 0C                           je 0x14061f1f1
0061F1E5  48 8D 0D 94 4C 8E 00            lea rcx, [rip + 0x8e4c94]
0061F1EC  E8 8F AC D2 FF                  call 0x140349e80
0061F1F1  49 8B D6                        mov rdx, r14
0061F1F4  49 8B CF                        mov rcx, r15
0061F1F7  E8 B4 68 DF FF                  call 0x140415ab0
0061F1FC  48 85 F6                        test rsi, rsi
0061F1FF  74 64                           je 0x14061f265
0061F201  40 32 FF                        xor dil, dil
0061F204  40 38 3D AD 56 8E 00            cmp byte ptr [rip + 0x8e56ad], dil
0061F20B  75 0C                           jne 0x14061f219
0061F20D  F7 05 69 57 8E 00 00 08 00 00   test dword ptr [rip + 0x8e5769], 0x800
0061F217  74 13                           je 0x14061f22c
0061F219  48 8D 0D 60 4C 8E 00            lea rcx, [rip + 0x8e4c60]
0061F220  E8 FB 73 BF FF                  call 0x140216620
0061F225  40 8A F8                        mov dil, al
0061F228  84 C0                           test al, al
0061F22A  74 39                           je 0x14061f265
0061F22C  48 83 C6 30                     add rsi, 0x30
0061F230  48 8B 1E                        mov rbx, qword ptr [rsi]
0061F233  EB 1A                           jmp 0x14061f24f
0061F235  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F239  48 85 C0                        test rax, rax
0061F23C  74 0E                           je 0x14061f24c
0061F23E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F242  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F247  E8 84 B8 09 00                  call 0x1406baad0
0061F24C  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F24F  48 3B DE                        cmp rbx, rsi
0061F252  75 E1                           jne 0x14061f235
0061F254  40 84 FF                        test dil, dil
0061F257  74 0C                           je 0x14061f265
0061F259  48 8D 0D 20 4C 8E 00            lea rcx, [rip + 0x8e4c20]
0061F260  E8 1B AC D2 FF                  call 0x140349e80
0061F265  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0061F26A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0061F26F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0061F274  48 83 C4 40                     add rsp, 0x40
0061F278  41 5F                           pop r15
0061F27A  41 5E                           pop r14
0061F27C  5F                              pop rdi
0061F27D  C3                              ret
0061F27E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExConvertFastResourceExclusiveToSharedWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(457, a2, a3, a4);
    if (result == 0) goto loc_0061F1F1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061F175;
    v_stack_m38 = v_stack_p0;
    goto loc_0061F183;
loc_0061F175:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9328422)) != 0) goto loc_0061F1A5;
    if (((*(unsigned int *)(v_rip + 9328605)) & (0x800ULL)) == 0) goto loc_0061F1B8;
loc_0061F1A5:
    result = ExAcquireRundownProtection(v_rip + 9325780, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F1F1;
loc_0061F1B8:
    goto loc_0061F1DB;
loc_0061F1C1:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F1DB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061F1C1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9325716;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExConvertFastResourceExclusiveToShared(a1, a2, a3, a4);
    if (result == 0) goto loc_0061F265;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9328301)) != 0) goto loc_0061F219;
    if (((*(unsigned int *)(v_rip + 9328489)) & (0x800ULL)) == 0) goto loc_0061F22C;
loc_0061F219:
    result = ExAcquireRundownProtection(v_rip + 9325664, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F265;
loc_0061F22C:
    v_rsi = (result) + (48);
    goto loc_0061F24F;
loc_0061F235:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F24F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061F235;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9325600;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExConvertFastResourceExclusiveToSharedWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(457, Arg2, a3, a4);
    if (result == 0) goto loc_0061F1F1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061F175;
    v_stack_m38 = v_stack_p0;
    goto loc_0061F183;
loc_0061F175:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8E5726)) != 0) goto loc_0061F1A5;
    if (((*(uint32_t *)(v_rip + 0x8E57DD)) & (0x800ULL)) == 0) goto loc_0061F1B8;
loc_0061F1A5:
    result = ExAcquireRundownProtection(v_rip + 9325780, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F1F1;
loc_0061F1B8:
    goto loc_0061F1DB;
loc_0061F1C1:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0061F1DB:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061F1C1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9325716;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ExConvertFastResourceExclusiveToShared(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_0061F265;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E56AD)) != 0) goto loc_0061F219;
    if (((*(uint32_t *)(v_rip + 0x8E5769)) & (0x800ULL)) == 0) goto loc_0061F22C;
loc_0061F219:
    result = ExAcquireRundownProtection(v_rip + 9325664, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F265;
loc_0061F22C:
    local_rsi = (result) + (48);
    goto loc_0061F24F;
loc_0061F235:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0061F24F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061F235;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9325600;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061F120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061F120[BB_0061F120]
  bb_0061F162[BB_0061F162]
  bb_0061F169[BB_0061F169]
  bb_0061F175[BB_0061F175]
  bb_0061F179[BB_0061F179]
  bb_0061F183[BB_0061F183]
  bb_0061F199[BB_0061F199]
  bb_0061F1A5[BB_0061F1A5]
  bb_0061F1B8[BB_0061F1B8]
  bb_0061F1C1[BB_0061F1C1]
  bb_0061F1CA[BB_0061F1CA]
  bb_0061F1D8[BB_0061F1D8]
  bb_0061F1DB[BB_0061F1DB]
  bb_0061F1E0[BB_0061F1E0]
  bb_0061F1E5[BB_0061F1E5]
  bb_0061F1F1[BB_0061F1F1]
  bb_0061F201[BB_0061F201]
  bb_0061F20D[BB_0061F20D]
  bb_0061F219[BB_0061F219]
  bb_0061F22C[BB_0061F22C]
  bb_0061F235[BB_0061F235]
  bb_0061F23E[BB_0061F23E]
  bb_0061F24C[BB_0061F24C]
  bb_0061F24F[BB_0061F24F]
  bb_0061F254[BB_0061F254]
  bb_0061F259[BB_0061F259]
  bb_0061F265[BB_0061F265]
  bb_0061F27E[BB_0061F27E]
  bb_0061F120 -->|branch| bb_0061F1F1
  bb_0061F120 -->|fallthrough| bb_0061F162
  bb_0061F162 -->|branch| bb_0061F175
  bb_0061F162 -->|fallthrough| bb_0061F169
  bb_0061F169 -->|branch| bb_0061F183
  bb_0061F175 -->|branch| bb_0061F183
  bb_0061F175 -->|fallthrough| bb_0061F179
  bb_0061F179 -->|flow| bb_0061F183
  bb_0061F183 -->|branch| bb_0061F1A5
  bb_0061F183 -->|fallthrough| bb_0061F199
  bb_0061F199 -->|branch| bb_0061F1B8
  bb_0061F199 -->|fallthrough| bb_0061F1A5
  bb_0061F1A5 -->|branch| bb_0061F1F1
  bb_0061F1A5 -->|fallthrough| bb_0061F1B8
  bb_0061F1B8 -->|branch| bb_0061F1DB
  bb_0061F1C1 -->|branch| bb_0061F1D8
  bb_0061F1C1 -->|fallthrough| bb_0061F1CA
  bb_0061F1CA -->|flow| bb_0061F1D8
  bb_0061F1D8 -->|flow| bb_0061F1DB
  bb_0061F1DB -->|branch| bb_0061F1C1
  bb_0061F1DB -->|fallthrough| bb_0061F1E0
  bb_0061F1E0 -->|branch| bb_0061F1F1
  bb_0061F1E0 -->|fallthrough| bb_0061F1E5
  bb_0061F1E5 -->|flow| bb_0061F1F1
  bb_0061F1F1 -->|branch| bb_0061F265
  bb_0061F1F1 -->|fallthrough| bb_0061F201
  bb_0061F201 -->|branch| bb_0061F219
  bb_0061F201 -->|fallthrough| bb_0061F20D
  bb_0061F20D -->|branch| bb_0061F22C
  bb_0061F20D -->|fallthrough| bb_0061F219
  bb_0061F219 -->|branch| bb_0061F265
  bb_0061F219 -->|fallthrough| bb_0061F22C
  bb_0061F22C -->|branch| bb_0061F24F
  bb_0061F235 -->|branch| bb_0061F24C
  bb_0061F235 -->|fallthrough| bb_0061F23E
  bb_0061F23E -->|flow| bb_0061F24C
  bb_0061F24C -->|flow| bb_0061F24F
  bb_0061F24F -->|branch| bb_0061F235
  bb_0061F24F -->|fallthrough| bb_0061F254
  bb_0061F254 -->|branch| bb_0061F265
  bb_0061F254 -->|fallthrough| bb_0061F259
  bb_0061F259 -->|flow| bb_0061F265
```
