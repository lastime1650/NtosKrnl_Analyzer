# DifIoFreeIrpWrapper

- RVA: `0x0062A470`–`0x0062A5C0` (길이 `336` bytes)
- VA: `0x000000014062A470`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062A498` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062A4C0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062A4EE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A515` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A52E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062A536` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0062A55F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A586` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A59F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062A4D2` → RVA `0x00F048B8` (`.data`; read)
- `0x0062A4DB` → RVA `0x00F04980` (`.data`; read)
- `0x0062A4E7` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062A470  48 8B C4                        mov rax, rsp
0062A473  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062A477  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062A47B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062A47F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062A483  41 56                           push r14
0062A485  48 83 EC 30                     sub rsp, 0x30
0062A489  48 8B E9                        mov rbp, rcx
0062A48C  0F 57 C0                        xorps xmm0, xmm0
0062A48F  B9 54 01 00 00                  mov ecx, 0x154
0062A494  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0062A498  E8 97 B5 E6 FF                  call 0x140495a34
0062A49D  48 8B F8                        mov rdi, rax
0062A4A0  48 85 C0                        test rax, rax
0062A4A3  0F 84 8A 00 00 00               je 0x14062a533
0062A4A9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062A4AC  A8 18                           test al, 0x18
0062A4AE  74 0C                           je 0x14062a4bc
0062A4B0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0062A4B5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062A4BA  EB 0E                           jmp 0x14062a4ca
0062A4BC  A8 04                           test al, 4
0062A4BE  74 0A                           je 0x14062a4ca
0062A4C0  E8 43 97 EA FF                  call 0x1404d3c08
0062A4C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062A4CA  40 32 F6                        xor sil, sil
0062A4CD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062A4D2  40 38 35 DF A3 8D 00            cmp byte ptr [rip + 0x8da3df], sil
0062A4D9  75 0C                           jne 0x14062a4e7
0062A4DB  F7 05 9B A4 8D 00 00 08 00 00   test dword ptr [rip + 0x8da49b], 0x800
0062A4E5  74 13                           je 0x14062a4fa
0062A4E7  48 8D 0D 92 99 8D 00            lea rcx, [rip + 0x8d9992]
0062A4EE  E8 2D C1 BE FF                  call 0x140216620
0062A4F3  40 8A F0                        mov sil, al
0062A4F6  84 C0                           test al, al
0062A4F8  74 39                           je 0x14062a533
0062A4FA  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062A4FE  49 8B 1E                        mov rbx, qword ptr [r14]
0062A501  EB 1A                           jmp 0x14062a51d
0062A503  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A507  48 85 C0                        test rax, rax
0062A50A  74 0E                           je 0x14062a51a
0062A50C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A510  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062A515  E8 B6 05 09 00                  call 0x1406baad0
0062A51A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A51D  49 3B DE                        cmp rbx, r14
0062A520  75 E1                           jne 0x14062a503
0062A522  40 84 F6                        test sil, sil
0062A525  74 0C                           je 0x14062a533
0062A527  48 8D 0D 52 99 8D 00            lea rcx, [rip + 0x8d9952]
0062A52E  E8 4D F9 D1 FF                  call 0x140349e80
0062A533  48 8B CD                        mov rcx, rbp
0062A536  E8 35 3A C2 FF                  call 0x14024df70
0062A53B  48 85 FF                        test rdi, rdi
0062A53E  74 64                           je 0x14062a5a4
0062A540  40 32 F6                        xor sil, sil
0062A543  40 38 35 6E A3 8D 00            cmp byte ptr [rip + 0x8da36e], sil
0062A54A  75 0C                           jne 0x14062a558
0062A54C  F7 05 2A A4 8D 00 00 08 00 00   test dword ptr [rip + 0x8da42a], 0x800
0062A556  74 13                           je 0x14062a56b
0062A558  48 8D 0D 21 99 8D 00            lea rcx, [rip + 0x8d9921]
0062A55F  E8 BC C0 BE FF                  call 0x140216620
0062A564  40 8A F0                        mov sil, al
0062A567  84 C0                           test al, al
0062A569  74 39                           je 0x14062a5a4
0062A56B  48 83 C7 30                     add rdi, 0x30
0062A56F  48 8B 1F                        mov rbx, qword ptr [rdi]
0062A572  EB 1A                           jmp 0x14062a58e
0062A574  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A578  48 85 C0                        test rax, rax
0062A57B  74 0E                           je 0x14062a58b
0062A57D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A581  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062A586  E8 45 05 09 00                  call 0x1406baad0
0062A58B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A58E  48 3B DF                        cmp rbx, rdi
0062A591  75 E1                           jne 0x14062a574
0062A593  40 84 F6                        test sil, sil
0062A596  74 0C                           je 0x14062a5a4
0062A598  48 8D 0D E1 98 8D 00            lea rcx, [rip + 0x8d98e1]
0062A59F  E8 DC F8 D1 FF                  call 0x140349e80
0062A5A4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0062A5A9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062A5AE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0062A5B3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0062A5B8  48 83 C4 30                     add rsp, 0x30
0062A5BC  41 5E                           pop r14
0062A5BE  C3                              ret
0062A5BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoFreeIrpWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(340, a2, a3, a4);
    if (result == 0) goto loc_0062A533;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062A4BC;
    v_stack_m18 = v_stack_p0;
    goto loc_0062A4CA;
loc_0062A4BC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9282527)) != 0) goto loc_0062A4E7;
    if (((*(unsigned int *)(v_rip + 9282715)) & (0x800ULL)) == 0) goto loc_0062A4FA;
loc_0062A4E7:
    result = ExAcquireRundownProtection(v_rip + 9279890, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A533;
loc_0062A4FA:
    goto loc_0062A51D;
loc_0062A503:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A51D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062A503;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9279826;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoFreeIrp(a1, a2, a3, a4);
    if (result == 0) goto loc_0062A5A4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9282414)) != 0) goto loc_0062A558;
    if (((*(unsigned int *)(v_rip + 9282602)) & (0x800ULL)) == 0) goto loc_0062A56B;
loc_0062A558:
    result = ExAcquireRundownProtection(v_rip + 9279777, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A5A4;
loc_0062A56B:
    v_rdi = (result) + (48);
    goto loc_0062A58E;
loc_0062A574:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A58E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0062A574;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9279713;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoFreeIrpWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(340, a2, a3, a4);
    if (result == 0) goto loc_0062A533;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062A4BC;
    v_stack_m18 = v_stack_p0;
    goto loc_0062A4CA;
loc_0062A4BC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8DA3DF)) != 0) goto loc_0062A4E7;
    if (((*(uint32_t *)(v_rip + 0x8DA49B)) & (0x800ULL)) == 0) goto loc_0062A4FA;
loc_0062A4E7:
    result = ExAcquireRundownProtection(v_rip + 9279890, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062A533;
loc_0062A4FA:
    goto loc_0062A51D;
loc_0062A503:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062A51D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062A503;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9279826;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = IoFreeIrp(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0062A5A4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DA36E)) != 0) goto loc_0062A558;
    if (((*(uint32_t *)(v_rip + 0x8DA42A)) & (0x800ULL)) == 0) goto loc_0062A56B;
loc_0062A558:
    result = ExAcquireRundownProtection(v_rip + 9279777, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062A5A4;
loc_0062A56B:
    local_rdi = (result) + (48);
    goto loc_0062A58E;
loc_0062A574:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062A58E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0062A574;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9279713;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062A470&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062A470[BB_0062A470]
  bb_0062A4A9[BB_0062A4A9]
  bb_0062A4B0[BB_0062A4B0]
  bb_0062A4BC[BB_0062A4BC]
  bb_0062A4C0[BB_0062A4C0]
  bb_0062A4CA[BB_0062A4CA]
  bb_0062A4DB[BB_0062A4DB]
  bb_0062A4E7[BB_0062A4E7]
  bb_0062A4FA[BB_0062A4FA]
  bb_0062A503[BB_0062A503]
  bb_0062A50C[BB_0062A50C]
  bb_0062A51A[BB_0062A51A]
  bb_0062A51D[BB_0062A51D]
  bb_0062A522[BB_0062A522]
  bb_0062A527[BB_0062A527]
  bb_0062A533[BB_0062A533]
  bb_0062A540[BB_0062A540]
  bb_0062A54C[BB_0062A54C]
  bb_0062A558[BB_0062A558]
  bb_0062A56B[BB_0062A56B]
  bb_0062A574[BB_0062A574]
  bb_0062A57D[BB_0062A57D]
  bb_0062A58B[BB_0062A58B]
  bb_0062A58E[BB_0062A58E]
  bb_0062A593[BB_0062A593]
  bb_0062A598[BB_0062A598]
  bb_0062A5A4[BB_0062A5A4]
  bb_0062A5BF[BB_0062A5BF]
  bb_0062A470 -->|branch| bb_0062A533
  bb_0062A470 -->|fallthrough| bb_0062A4A9
  bb_0062A4A9 -->|branch| bb_0062A4BC
  bb_0062A4A9 -->|fallthrough| bb_0062A4B0
  bb_0062A4B0 -->|branch| bb_0062A4CA
  bb_0062A4BC -->|branch| bb_0062A4CA
  bb_0062A4BC -->|fallthrough| bb_0062A4C0
  bb_0062A4C0 -->|flow| bb_0062A4CA
  bb_0062A4CA -->|branch| bb_0062A4E7
  bb_0062A4CA -->|fallthrough| bb_0062A4DB
  bb_0062A4DB -->|branch| bb_0062A4FA
  bb_0062A4DB -->|fallthrough| bb_0062A4E7
  bb_0062A4E7 -->|branch| bb_0062A533
  bb_0062A4E7 -->|fallthrough| bb_0062A4FA
  bb_0062A4FA -->|branch| bb_0062A51D
  bb_0062A503 -->|branch| bb_0062A51A
  bb_0062A503 -->|fallthrough| bb_0062A50C
  bb_0062A50C -->|flow| bb_0062A51A
  bb_0062A51A -->|flow| bb_0062A51D
  bb_0062A51D -->|branch| bb_0062A503
  bb_0062A51D -->|fallthrough| bb_0062A522
  bb_0062A522 -->|branch| bb_0062A533
  bb_0062A522 -->|fallthrough| bb_0062A527
  bb_0062A527 -->|flow| bb_0062A533
  bb_0062A533 -->|branch| bb_0062A5A4
  bb_0062A533 -->|fallthrough| bb_0062A540
  bb_0062A540 -->|branch| bb_0062A558
  bb_0062A540 -->|fallthrough| bb_0062A54C
  bb_0062A54C -->|branch| bb_0062A56B
  bb_0062A54C -->|fallthrough| bb_0062A558
  bb_0062A558 -->|branch| bb_0062A5A4
  bb_0062A558 -->|fallthrough| bb_0062A56B
  bb_0062A56B -->|branch| bb_0062A58E
  bb_0062A574 -->|branch| bb_0062A58B
  bb_0062A574 -->|fallthrough| bb_0062A57D
  bb_0062A57D -->|flow| bb_0062A58B
  bb_0062A58B -->|flow| bb_0062A58E
  bb_0062A58E -->|branch| bb_0062A574
  bb_0062A58E -->|fallthrough| bb_0062A593
  bb_0062A593 -->|branch| bb_0062A5A4
  bb_0062A593 -->|fallthrough| bb_0062A598
  bb_0062A598 -->|flow| bb_0062A5A4
```
