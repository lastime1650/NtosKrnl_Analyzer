# DifExReleaseDisownedFastResourceSharedWrapper

- RVA: `0x00622160`–`0x006222BF` (길이 `351` bytes)
- VA: `0x0000000140622160`
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
- `0x00622191` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006221B9` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006221EC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00622213` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062222C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00622237` → [ExReleaseDisownedFastResourceShared](../65/ExReleaseDisownedFastResourceShared_function_006587C0.md) (function, `0x006587C0`)
- `0x00622260` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00622287` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006222A0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006221CB` → RVA `0x00F048B8` (`.data`; read)
- `0x006221D9` → RVA `0x00F04980` (`.data`; read)
- `0x006221E5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00622160  4C 8B DC                        mov r11, rsp
00622163  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00622167  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062216B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062216F  57                              push rdi
00622170  41 56                           push r14
00622172  41 57                           push r15
00622174  48 83 EC 40                     sub rsp, 0x40
00622178  33 C0                           xor eax, eax
0062217A  0F 57 C0                        xorps xmm0, xmm0
0062217D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00622182  4C 8B F9                        mov r15, rcx
00622185  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00622189  B9 C6 01 00 00                  mov ecx, 0x1c6
0062218E  4C 8B F2                        mov r14, rdx
00622191  E8 9E 38 E7 FF                  call 0x140495a34
00622196  48 8B F0                        mov rsi, rax
00622199  48 85 C0                        test rax, rax
0062219C  0F 84 8F 00 00 00               je 0x140622231
006221A2  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006221A5  A8 18                           test al, 0x18
006221A7  74 0C                           je 0x1406221b5
006221A9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006221AE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006221B3  EB 0E                           jmp 0x1406221c3
006221B5  A8 04                           test al, 4
006221B7  74 0A                           je 0x1406221c3
006221B9  E8 4A 1A EB FF                  call 0x1404d3c08
006221BE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006221C3  40 32 ED                        xor bpl, bpl
006221C6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006221CB  40 38 2D E6 26 8E 00            cmp byte ptr [rip + 0x8e26e6], bpl
006221D2  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006221D7  75 0C                           jne 0x1406221e5
006221D9  F7 05 9D 27 8E 00 00 08 00 00   test dword ptr [rip + 0x8e279d], 0x800
006221E3  74 13                           je 0x1406221f8
006221E5  48 8D 0D 94 1C 8E 00            lea rcx, [rip + 0x8e1c94]
006221EC  E8 2F 44 BF FF                  call 0x140216620
006221F1  40 8A E8                        mov bpl, al
006221F4  84 C0                           test al, al
006221F6  74 39                           je 0x140622231
006221F8  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006221FC  48 8B 1F                        mov rbx, qword ptr [rdi]
006221FF  EB 1A                           jmp 0x14062221b
00622201  48 8D 43 F0                     lea rax, [rbx - 0x10]
00622205  48 85 C0                        test rax, rax
00622208  74 0E                           je 0x140622218
0062220A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062220E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00622213  E8 B8 88 09 00                  call 0x1406baad0
00622218  48 8B 1B                        mov rbx, qword ptr [rbx]
0062221B  48 3B DF                        cmp rbx, rdi
0062221E  75 E1                           jne 0x140622201
00622220  40 84 ED                        test bpl, bpl
00622223  74 0C                           je 0x140622231
00622225  48 8D 0D 54 1C 8E 00            lea rcx, [rip + 0x8e1c54]
0062222C  E8 4F 7C D2 FF                  call 0x140349e80
00622231  49 8B D6                        mov rdx, r14
00622234  49 8B CF                        mov rcx, r15
00622237  E8 84 65 03 00                  call 0x1406587c0
0062223C  48 85 F6                        test rsi, rsi
0062223F  74 64                           je 0x1406222a5
00622241  40 32 FF                        xor dil, dil
00622244  40 38 3D 6D 26 8E 00            cmp byte ptr [rip + 0x8e266d], dil
0062224B  75 0C                           jne 0x140622259
0062224D  F7 05 29 27 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2729], 0x800
00622257  74 13                           je 0x14062226c
00622259  48 8D 0D 20 1C 8E 00            lea rcx, [rip + 0x8e1c20]
00622260  E8 BB 43 BF FF                  call 0x140216620
00622265  40 8A F8                        mov dil, al
00622268  84 C0                           test al, al
0062226A  74 39                           je 0x1406222a5
0062226C  48 83 C6 30                     add rsi, 0x30
00622270  48 8B 1E                        mov rbx, qword ptr [rsi]
00622273  EB 1A                           jmp 0x14062228f
00622275  48 8D 43 F0                     lea rax, [rbx - 0x10]
00622279  48 85 C0                        test rax, rax
0062227C  74 0E                           je 0x14062228c
0062227E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00622282  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00622287  E8 44 88 09 00                  call 0x1406baad0
0062228C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062228F  48 3B DE                        cmp rbx, rsi
00622292  75 E1                           jne 0x140622275
00622294  40 84 FF                        test dil, dil
00622297  74 0C                           je 0x1406222a5
00622299  48 8D 0D E0 1B 8E 00            lea rcx, [rip + 0x8e1be0]
006222A0  E8 DB 7B D2 FF                  call 0x140349e80
006222A5  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006222AA  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006222AF  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006222B4  48 83 C4 40                     add rsp, 0x40
006222B8  41 5F                           pop r15
006222BA  41 5E                           pop r14
006222BC  5F                              pop rdi
006222BD  C3                              ret
006222BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExReleaseDisownedFastResourceSharedWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(454, a2, a3, a4);
    if (result == 0) goto loc_00622231;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006221B5;
    v_stack_m38 = v_stack_p0;
    goto loc_006221C3;
loc_006221B5:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9316070)) != 0) goto loc_006221E5;
    if (((*(unsigned int *)(v_rip + 9316253)) & (0x800ULL)) == 0) goto loc_006221F8;
loc_006221E5:
    result = ExAcquireRundownProtection(v_rip + 9313428, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00622231;
loc_006221F8:
    goto loc_0062221B;
loc_00622201:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062221B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00622201;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9313364;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExReleaseDisownedFastResourceShared(a1, a2, a3, a4);
    if (result == 0) goto loc_006222A5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9315949)) != 0) goto loc_00622259;
    if (((*(unsigned int *)(v_rip + 9316137)) & (0x800ULL)) == 0) goto loc_0062226C;
loc_00622259:
    result = ExAcquireRundownProtection(v_rip + 9313312, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006222A5;
loc_0062226C:
    v_rsi = (result) + (48);
    goto loc_0062228F;
loc_00622275:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062228F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00622275;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9313248;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExReleaseDisownedFastResourceSharedWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(454, Arg2, a3, a4);
    if (result == 0) goto loc_00622231;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006221B5;
    v_stack_m38 = v_stack_p0;
    goto loc_006221C3;
loc_006221B5:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8E26E6)) != 0) goto loc_006221E5;
    if (((*(uint32_t *)(v_rip + 0x8E279D)) & (0x800ULL)) == 0) goto loc_006221F8;
loc_006221E5:
    result = ExAcquireRundownProtection(v_rip + 9313428, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00622231;
loc_006221F8:
    goto loc_0062221B;
loc_00622201:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062221B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00622201;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9313364;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ExReleaseDisownedFastResourceShared(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_006222A5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E266D)) != 0) goto loc_00622259;
    if (((*(uint32_t *)(v_rip + 0x8E2729)) & (0x800ULL)) == 0) goto loc_0062226C;
loc_00622259:
    result = ExAcquireRundownProtection(v_rip + 9313312, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006222A5;
loc_0062226C:
    local_rsi = (result) + (48);
    goto loc_0062228F;
loc_00622275:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062228F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00622275;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9313248;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00622160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00622160[BB_00622160]
  bb_006221A2[BB_006221A2]
  bb_006221A9[BB_006221A9]
  bb_006221B5[BB_006221B5]
  bb_006221B9[BB_006221B9]
  bb_006221C3[BB_006221C3]
  bb_006221D9[BB_006221D9]
  bb_006221E5[BB_006221E5]
  bb_006221F8[BB_006221F8]
  bb_00622201[BB_00622201]
  bb_0062220A[BB_0062220A]
  bb_00622218[BB_00622218]
  bb_0062221B[BB_0062221B]
  bb_00622220[BB_00622220]
  bb_00622225[BB_00622225]
  bb_00622231[BB_00622231]
  bb_00622241[BB_00622241]
  bb_0062224D[BB_0062224D]
  bb_00622259[BB_00622259]
  bb_0062226C[BB_0062226C]
  bb_00622275[BB_00622275]
  bb_0062227E[BB_0062227E]
  bb_0062228C[BB_0062228C]
  bb_0062228F[BB_0062228F]
  bb_00622294[BB_00622294]
  bb_00622299[BB_00622299]
  bb_006222A5[BB_006222A5]
  bb_006222BE[BB_006222BE]
  bb_00622160 -->|branch| bb_00622231
  bb_00622160 -->|fallthrough| bb_006221A2
  bb_006221A2 -->|branch| bb_006221B5
  bb_006221A2 -->|fallthrough| bb_006221A9
  bb_006221A9 -->|branch| bb_006221C3
  bb_006221B5 -->|branch| bb_006221C3
  bb_006221B5 -->|fallthrough| bb_006221B9
  bb_006221B9 -->|flow| bb_006221C3
  bb_006221C3 -->|branch| bb_006221E5
  bb_006221C3 -->|fallthrough| bb_006221D9
  bb_006221D9 -->|branch| bb_006221F8
  bb_006221D9 -->|fallthrough| bb_006221E5
  bb_006221E5 -->|branch| bb_00622231
  bb_006221E5 -->|fallthrough| bb_006221F8
  bb_006221F8 -->|branch| bb_0062221B
  bb_00622201 -->|branch| bb_00622218
  bb_00622201 -->|fallthrough| bb_0062220A
  bb_0062220A -->|flow| bb_00622218
  bb_00622218 -->|flow| bb_0062221B
  bb_0062221B -->|branch| bb_00622201
  bb_0062221B -->|fallthrough| bb_00622220
  bb_00622220 -->|branch| bb_00622231
  bb_00622220 -->|fallthrough| bb_00622225
  bb_00622225 -->|flow| bb_00622231
  bb_00622231 -->|branch| bb_006222A5
  bb_00622231 -->|fallthrough| bb_00622241
  bb_00622241 -->|branch| bb_00622259
  bb_00622241 -->|fallthrough| bb_0062224D
  bb_0062224D -->|branch| bb_0062226C
  bb_0062224D -->|fallthrough| bb_00622259
  bb_00622259 -->|branch| bb_006222A5
  bb_00622259 -->|fallthrough| bb_0062226C
  bb_0062226C -->|branch| bb_0062228F
  bb_00622275 -->|branch| bb_0062228C
  bb_00622275 -->|fallthrough| bb_0062227E
  bb_0062227E -->|flow| bb_0062228C
  bb_0062228C -->|flow| bb_0062228F
  bb_0062228F -->|branch| bb_00622275
  bb_0062228F -->|fallthrough| bb_00622294
  bb_00622294 -->|branch| bb_006222A5
  bb_00622294 -->|fallthrough| bb_00622299
  bb_00622299 -->|flow| bb_006222A5
```
