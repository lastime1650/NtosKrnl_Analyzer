# DifExFreePoolWithTagWrapper

- RVA: `0x00620420`–`0x0062057F` (길이 `351` bytes)
- VA: `0x0000000140620420`
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
- `0x00620451` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620479` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006204AC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006204D3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006204EC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006204F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00620520` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620547` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620560` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062048B` → RVA `0x00F048B8` (`.data`; read)
- `0x00620499` → RVA `0x00F04980` (`.data`; read)
- `0x006204A5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006204F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00620420  4C 8B DC                        mov r11, rsp
00620423  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00620427  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062042B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062042F  57                              push rdi
00620430  41 56                           push r14
00620432  41 57                           push r15
00620434  48 83 EC 40                     sub rsp, 0x40
00620438  33 C0                           xor eax, eax
0062043A  0F 57 C0                        xorps xmm0, xmm0
0062043D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00620442  4C 8B F9                        mov r15, rcx
00620445  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00620449  B9 90 01 00 00                  mov ecx, 0x190
0062044E  44 8B F2                        mov r14d, edx
00620451  E8 DE 55 E7 FF                  call 0x140495a34
00620456  48 8B F0                        mov rsi, rax
00620459  48 85 C0                        test rax, rax
0062045C  0F 84 8F 00 00 00               je 0x1406204f1
00620462  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00620465  A8 18                           test al, 0x18
00620467  74 0C                           je 0x140620475
00620469  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062046E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00620473  EB 0E                           jmp 0x140620483
00620475  A8 04                           test al, 4
00620477  74 0A                           je 0x140620483
00620479  E8 8A 37 EB FF                  call 0x1404d3c08
0062047E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00620483  40 32 ED                        xor bpl, bpl
00620486  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062048B  40 38 2D 26 44 8E 00            cmp byte ptr [rip + 0x8e4426], bpl
00620492  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00620497  75 0C                           jne 0x1406204a5
00620499  F7 05 DD 44 8E 00 00 08 00 00   test dword ptr [rip + 0x8e44dd], 0x800
006204A3  74 13                           je 0x1406204b8
006204A5  48 8D 0D D4 39 8E 00            lea rcx, [rip + 0x8e39d4]
006204AC  E8 6F 61 BF FF                  call 0x140216620
006204B1  40 8A E8                        mov bpl, al
006204B4  84 C0                           test al, al
006204B6  74 39                           je 0x1406204f1
006204B8  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006204BC  48 8B 1F                        mov rbx, qword ptr [rdi]
006204BF  EB 1A                           jmp 0x1406204db
006204C1  48 8D 43 F0                     lea rax, [rbx - 0x10]
006204C5  48 85 C0                        test rax, rax
006204C8  74 0E                           je 0x1406204d8
006204CA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006204CE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006204D3  E8 F8 A5 09 00                  call 0x1406baad0
006204D8  48 8B 1B                        mov rbx, qword ptr [rbx]
006204DB  48 3B DF                        cmp rbx, rdi
006204DE  75 E1                           jne 0x1406204c1
006204E0  40 84 ED                        test bpl, bpl
006204E3  74 0C                           je 0x1406204f1
006204E5  48 8D 0D 94 39 8E 00            lea rcx, [rip + 0x8e3994]
006204EC  E8 8F 99 D2 FF                  call 0x140349e80
006204F1  41 8B D6                        mov edx, r14d
006204F4  49 8B CF                        mov rcx, r15
006204F7  E8 74 23 56 00                  call 0x140b82870
006204FC  48 85 F6                        test rsi, rsi
006204FF  74 64                           je 0x140620565
00620501  40 32 FF                        xor dil, dil
00620504  40 38 3D AD 43 8E 00            cmp byte ptr [rip + 0x8e43ad], dil
0062050B  75 0C                           jne 0x140620519
0062050D  F7 05 69 44 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4469], 0x800
00620517  74 13                           je 0x14062052c
00620519  48 8D 0D 60 39 8E 00            lea rcx, [rip + 0x8e3960]
00620520  E8 FB 60 BF FF                  call 0x140216620
00620525  40 8A F8                        mov dil, al
00620528  84 C0                           test al, al
0062052A  74 39                           je 0x140620565
0062052C  48 83 C6 30                     add rsi, 0x30
00620530  48 8B 1E                        mov rbx, qword ptr [rsi]
00620533  EB 1A                           jmp 0x14062054f
00620535  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620539  48 85 C0                        test rax, rax
0062053C  74 0E                           je 0x14062054c
0062053E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620542  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620547  E8 84 A5 09 00                  call 0x1406baad0
0062054C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062054F  48 3B DE                        cmp rbx, rsi
00620552  75 E1                           jne 0x140620535
00620554  40 84 FF                        test dil, dil
00620557  74 0C                           je 0x140620565
00620559  48 8D 0D 20 39 8E 00            lea rcx, [rip + 0x8e3920]
00620560  E8 1B 99 D2 FF                  call 0x140349e80
00620565  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062056A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062056F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00620574  48 83 C4 40                     add rsp, 0x40
00620578  41 5F                           pop r15
0062057A  41 5E                           pop r14
0062057C  5F                              pop rdi
0062057D  C3                              ret
0062057E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExFreePoolWithTagWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(400, a2, a3, a4);
    if (result == 0) goto loc_006204F1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00620475;
    v_stack_m38 = v_stack_p0;
    goto loc_00620483;
loc_00620475:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9323558)) != 0) goto loc_006204A5;
    if (((*(unsigned int *)(v_rip + 9323741)) & (0x800ULL)) == 0) goto loc_006204B8;
loc_006204A5:
    result = ExAcquireRundownProtection(v_rip + 9320916, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006204F1;
loc_006204B8:
    goto loc_006204DB;
loc_006204C1:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006204DB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006204C1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9320852;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExFreePoolWithTag(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_00620565;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9323437)) != 0) goto loc_00620519;
    if (((*(unsigned int *)(v_rip + 9323625)) & (0x800ULL)) == 0) goto loc_0062052C;
loc_00620519:
    result = ExAcquireRundownProtection(v_rip + 9320800, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620565;
loc_0062052C:
    v_rsi = (result) + (48);
    goto loc_0062054F;
loc_00620535:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062054F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00620535;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9320736;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExFreePoolWithTagWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(400, Arg2, a3, a4);
    if (result == 0) goto loc_006204F1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00620475;
    v_stack_m38 = v_stack_p0;
    goto loc_00620483;
loc_00620475:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8E4426)) != 0) goto loc_006204A5;
    if (((*(uint32_t *)(v_rip + 0x8E44DD)) & (0x800ULL)) == 0) goto loc_006204B8;
loc_006204A5:
    result = ExAcquireRundownProtection(v_rip + 9320916, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006204F1;
loc_006204B8:
    goto loc_006204DB;
loc_006204C1:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006204DB:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006204C1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9320852;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ExFreePoolWithTag(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if (result == 0) goto loc_00620565;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E43AD)) != 0) goto loc_00620519;
    if (((*(uint32_t *)(v_rip + 0x8E4469)) & (0x800ULL)) == 0) goto loc_0062052C;
loc_00620519:
    result = ExAcquireRundownProtection(v_rip + 9320800, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620565;
loc_0062052C:
    local_rsi = (result) + (48);
    goto loc_0062054F;
loc_00620535:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_0062054F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00620535;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9320736;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00620420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00620420[BB_00620420]
  bb_00620462[BB_00620462]
  bb_00620469[BB_00620469]
  bb_00620475[BB_00620475]
  bb_00620479[BB_00620479]
  bb_00620483[BB_00620483]
  bb_00620499[BB_00620499]
  bb_006204A5[BB_006204A5]
  bb_006204B8[BB_006204B8]
  bb_006204C1[BB_006204C1]
  bb_006204CA[BB_006204CA]
  bb_006204D8[BB_006204D8]
  bb_006204DB[BB_006204DB]
  bb_006204E0[BB_006204E0]
  bb_006204E5[BB_006204E5]
  bb_006204F1[BB_006204F1]
  bb_00620501[BB_00620501]
  bb_0062050D[BB_0062050D]
  bb_00620519[BB_00620519]
  bb_0062052C[BB_0062052C]
  bb_00620535[BB_00620535]
  bb_0062053E[BB_0062053E]
  bb_0062054C[BB_0062054C]
  bb_0062054F[BB_0062054F]
  bb_00620554[BB_00620554]
  bb_00620559[BB_00620559]
  bb_00620565[BB_00620565]
  bb_0062057E[BB_0062057E]
  bb_00620420 -->|branch| bb_006204F1
  bb_00620420 -->|fallthrough| bb_00620462
  bb_00620462 -->|branch| bb_00620475
  bb_00620462 -->|fallthrough| bb_00620469
  bb_00620469 -->|branch| bb_00620483
  bb_00620475 -->|branch| bb_00620483
  bb_00620475 -->|fallthrough| bb_00620479
  bb_00620479 -->|flow| bb_00620483
  bb_00620483 -->|branch| bb_006204A5
  bb_00620483 -->|fallthrough| bb_00620499
  bb_00620499 -->|branch| bb_006204B8
  bb_00620499 -->|fallthrough| bb_006204A5
  bb_006204A5 -->|branch| bb_006204F1
  bb_006204A5 -->|fallthrough| bb_006204B8
  bb_006204B8 -->|branch| bb_006204DB
  bb_006204C1 -->|branch| bb_006204D8
  bb_006204C1 -->|fallthrough| bb_006204CA
  bb_006204CA -->|flow| bb_006204D8
  bb_006204D8 -->|flow| bb_006204DB
  bb_006204DB -->|branch| bb_006204C1
  bb_006204DB -->|fallthrough| bb_006204E0
  bb_006204E0 -->|branch| bb_006204F1
  bb_006204E0 -->|fallthrough| bb_006204E5
  bb_006204E5 -->|flow| bb_006204F1
  bb_006204F1 -->|branch| bb_00620565
  bb_006204F1 -->|fallthrough| bb_00620501
  bb_00620501 -->|branch| bb_00620519
  bb_00620501 -->|fallthrough| bb_0062050D
  bb_0062050D -->|branch| bb_0062052C
  bb_0062050D -->|fallthrough| bb_00620519
  bb_00620519 -->|branch| bb_00620565
  bb_00620519 -->|fallthrough| bb_0062052C
  bb_0062052C -->|branch| bb_0062054F
  bb_00620535 -->|branch| bb_0062054C
  bb_00620535 -->|fallthrough| bb_0062053E
  bb_0062053E -->|flow| bb_0062054C
  bb_0062054C -->|flow| bb_0062054F
  bb_0062054F -->|branch| bb_00620535
  bb_0062054F -->|fallthrough| bb_00620554
  bb_00620554 -->|branch| bb_00620565
  bb_00620554 -->|fallthrough| bb_00620559
  bb_00620559 -->|flow| bb_00620565
```
