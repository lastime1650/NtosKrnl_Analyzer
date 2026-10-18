# DifExReleaseFastMutexWrapper

- RVA: `0x006225A0`–`0x006226F0` (길이 `336` bytes)
- VA: `0x00000001406225A0`
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
- `0x006225C8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006225F0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062261E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00622645` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062265E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00622666` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0062268F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006226B6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006226CF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00622602` → RVA `0x00F048B8` (`.data`; read)
- `0x0062260B` → RVA `0x00F04980` (`.data`; read)
- `0x00622617` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006225A0  48 8B C4                        mov rax, rsp
006225A3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006225A7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006225AB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006225AF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006225B3  41 56                           push r14
006225B5  48 83 EC 30                     sub rsp, 0x30
006225B9  48 8B E9                        mov rbp, rcx
006225BC  0F 57 C0                        xorps xmm0, xmm0
006225BF  B9 86 01 00 00                  mov ecx, 0x186
006225C4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
006225C8  E8 67 34 E7 FF                  call 0x140495a34
006225CD  48 8B F8                        mov rdi, rax
006225D0  48 85 C0                        test rax, rax
006225D3  0F 84 8A 00 00 00               je 0x140622663
006225D9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006225DC  A8 18                           test al, 0x18
006225DE  74 0C                           je 0x1406225ec
006225E0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
006225E5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006225EA  EB 0E                           jmp 0x1406225fa
006225EC  A8 04                           test al, 4
006225EE  74 0A                           je 0x1406225fa
006225F0  E8 13 16 EB FF                  call 0x1404d3c08
006225F5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006225FA  40 32 F6                        xor sil, sil
006225FD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00622602  40 38 35 AF 22 8E 00            cmp byte ptr [rip + 0x8e22af], sil
00622609  75 0C                           jne 0x140622617
0062260B  F7 05 6B 23 8E 00 00 08 00 00   test dword ptr [rip + 0x8e236b], 0x800
00622615  74 13                           je 0x14062262a
00622617  48 8D 0D 62 18 8E 00            lea rcx, [rip + 0x8e1862]
0062261E  E8 FD 3F BF FF                  call 0x140216620
00622623  40 8A F0                        mov sil, al
00622626  84 C0                           test al, al
00622628  74 39                           je 0x140622663
0062262A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062262E  49 8B 1E                        mov rbx, qword ptr [r14]
00622631  EB 1A                           jmp 0x14062264d
00622633  48 8D 43 F0                     lea rax, [rbx - 0x10]
00622637  48 85 C0                        test rax, rax
0062263A  74 0E                           je 0x14062264a
0062263C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00622640  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00622645  E8 86 84 09 00                  call 0x1406baad0
0062264A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062264D  49 3B DE                        cmp rbx, r14
00622650  75 E1                           jne 0x140622633
00622652  40 84 F6                        test sil, sil
00622655  74 0C                           je 0x140622663
00622657  48 8D 0D 22 18 8E 00            lea rcx, [rip + 0x8e1822]
0062265E  E8 1D 78 D2 FF                  call 0x140349e80
00622663  48 8B CD                        mov rcx, rbp
00622666  E8 55 F3 C2 FF                  call 0x1402519c0
0062266B  48 85 FF                        test rdi, rdi
0062266E  74 64                           je 0x1406226d4
00622670  40 32 F6                        xor sil, sil
00622673  40 38 35 3E 22 8E 00            cmp byte ptr [rip + 0x8e223e], sil
0062267A  75 0C                           jne 0x140622688
0062267C  F7 05 FA 22 8E 00 00 08 00 00   test dword ptr [rip + 0x8e22fa], 0x800
00622686  74 13                           je 0x14062269b
00622688  48 8D 0D F1 17 8E 00            lea rcx, [rip + 0x8e17f1]
0062268F  E8 8C 3F BF FF                  call 0x140216620
00622694  40 8A F0                        mov sil, al
00622697  84 C0                           test al, al
00622699  74 39                           je 0x1406226d4
0062269B  48 83 C7 30                     add rdi, 0x30
0062269F  48 8B 1F                        mov rbx, qword ptr [rdi]
006226A2  EB 1A                           jmp 0x1406226be
006226A4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006226A8  48 85 C0                        test rax, rax
006226AB  74 0E                           je 0x1406226bb
006226AD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006226B1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006226B6  E8 15 84 09 00                  call 0x1406baad0
006226BB  48 8B 1B                        mov rbx, qword ptr [rbx]
006226BE  48 3B DF                        cmp rbx, rdi
006226C1  75 E1                           jne 0x1406226a4
006226C3  40 84 F6                        test sil, sil
006226C6  74 0C                           je 0x1406226d4
006226C8  48 8D 0D B1 17 8E 00            lea rcx, [rip + 0x8e17b1]
006226CF  E8 AC 77 D2 FF                  call 0x140349e80
006226D4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006226D9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006226DE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006226E3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
006226E8  48 83 C4 30                     add rsp, 0x30
006226EC  41 5E                           pop r14
006226EE  C3                              ret
006226EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExReleaseFastMutexWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(390, a2, a3, a4);
    if (result == 0) goto loc_00622663;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006225EC;
    v_stack_m18 = v_stack_p0;
    goto loc_006225FA;
loc_006225EC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9314991)) != 0) goto loc_00622617;
    if (((*(unsigned int *)(v_rip + 9315179)) & (0x800ULL)) == 0) goto loc_0062262A;
loc_00622617:
    result = ExAcquireRundownProtection(v_rip + 9312354, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00622663;
loc_0062262A:
    goto loc_0062264D;
loc_00622633:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062264D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00622633;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9312290;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutex(a1, a2, a3, a4);
    if (result == 0) goto loc_006226D4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9314878)) != 0) goto loc_00622688;
    if (((*(unsigned int *)(v_rip + 9315066)) & (0x800ULL)) == 0) goto loc_0062269B;
loc_00622688:
    result = ExAcquireRundownProtection(v_rip + 9312241, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006226D4;
loc_0062269B:
    v_rdi = (result) + (48);
    goto loc_006226BE;
loc_006226A4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006226BE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_006226A4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9312177;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExReleaseFastMutexWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(390, a2, a3, a4);
    if (result == 0) goto loc_00622663;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006225EC;
    v_stack_m18 = v_stack_p0;
    goto loc_006225FA;
loc_006225EC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E22AF)) != 0) goto loc_00622617;
    if (((*(uint32_t *)(v_rip + 0x8E236B)) & (0x800ULL)) == 0) goto loc_0062262A;
loc_00622617:
    result = ExAcquireRundownProtection(v_rip + 9312354, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00622663;
loc_0062262A:
    goto loc_0062264D;
loc_00622633:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062264D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00622633;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9312290;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExReleaseFastMutex(Arg1, a2, a3, a4);
    if (result == 0) goto loc_006226D4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E223E)) != 0) goto loc_00622688;
    if (((*(uint32_t *)(v_rip + 0x8E22FA)) & (0x800ULL)) == 0) goto loc_0062269B;
loc_00622688:
    result = ExAcquireRundownProtection(v_rip + 9312241, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006226D4;
loc_0062269B:
    local_rdi = (result) + (48);
    goto loc_006226BE;
loc_006226A4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006226BE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_006226A4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9312177;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006225A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006225A0[BB_006225A0]
  bb_006225D9[BB_006225D9]
  bb_006225E0[BB_006225E0]
  bb_006225EC[BB_006225EC]
  bb_006225F0[BB_006225F0]
  bb_006225FA[BB_006225FA]
  bb_0062260B[BB_0062260B]
  bb_00622617[BB_00622617]
  bb_0062262A[BB_0062262A]
  bb_00622633[BB_00622633]
  bb_0062263C[BB_0062263C]
  bb_0062264A[BB_0062264A]
  bb_0062264D[BB_0062264D]
  bb_00622652[BB_00622652]
  bb_00622657[BB_00622657]
  bb_00622663[BB_00622663]
  bb_00622670[BB_00622670]
  bb_0062267C[BB_0062267C]
  bb_00622688[BB_00622688]
  bb_0062269B[BB_0062269B]
  bb_006226A4[BB_006226A4]
  bb_006226AD[BB_006226AD]
  bb_006226BB[BB_006226BB]
  bb_006226BE[BB_006226BE]
  bb_006226C3[BB_006226C3]
  bb_006226C8[BB_006226C8]
  bb_006226D4[BB_006226D4]
  bb_006226EF[BB_006226EF]
  bb_006225A0 -->|branch| bb_00622663
  bb_006225A0 -->|fallthrough| bb_006225D9
  bb_006225D9 -->|branch| bb_006225EC
  bb_006225D9 -->|fallthrough| bb_006225E0
  bb_006225E0 -->|branch| bb_006225FA
  bb_006225EC -->|branch| bb_006225FA
  bb_006225EC -->|fallthrough| bb_006225F0
  bb_006225F0 -->|flow| bb_006225FA
  bb_006225FA -->|branch| bb_00622617
  bb_006225FA -->|fallthrough| bb_0062260B
  bb_0062260B -->|branch| bb_0062262A
  bb_0062260B -->|fallthrough| bb_00622617
  bb_00622617 -->|branch| bb_00622663
  bb_00622617 -->|fallthrough| bb_0062262A
  bb_0062262A -->|branch| bb_0062264D
  bb_00622633 -->|branch| bb_0062264A
  bb_00622633 -->|fallthrough| bb_0062263C
  bb_0062263C -->|flow| bb_0062264A
  bb_0062264A -->|flow| bb_0062264D
  bb_0062264D -->|branch| bb_00622633
  bb_0062264D -->|fallthrough| bb_00622652
  bb_00622652 -->|branch| bb_00622663
  bb_00622652 -->|fallthrough| bb_00622657
  bb_00622657 -->|flow| bb_00622663
  bb_00622663 -->|branch| bb_006226D4
  bb_00622663 -->|fallthrough| bb_00622670
  bb_00622670 -->|branch| bb_00622688
  bb_00622670 -->|fallthrough| bb_0062267C
  bb_0062267C -->|branch| bb_0062269B
  bb_0062267C -->|fallthrough| bb_00622688
  bb_00622688 -->|branch| bb_006226D4
  bb_00622688 -->|fallthrough| bb_0062269B
  bb_0062269B -->|branch| bb_006226BE
  bb_006226A4 -->|branch| bb_006226BB
  bb_006226A4 -->|fallthrough| bb_006226AD
  bb_006226AD -->|flow| bb_006226BB
  bb_006226BB -->|flow| bb_006226BE
  bb_006226BE -->|branch| bb_006226A4
  bb_006226BE -->|fallthrough| bb_006226C3
  bb_006226C3 -->|branch| bb_006226D4
  bb_006226C3 -->|fallthrough| bb_006226C8
  bb_006226C8 -->|flow| bb_006226D4
```
