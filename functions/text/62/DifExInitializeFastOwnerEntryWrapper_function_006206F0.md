# DifExInitializeFastOwnerEntryWrapper

- RVA: `0x006206F0`–`0x00620840` (길이 `336` bytes)
- VA: `0x00000001406206F0`
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
- `0x00620718` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620740` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062076E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620795` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006207AE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006207B6` → [ExInitializeFastOwnerEntry](../41/ExInitializeFastOwnerEntry_function_004188D0.md) (function, `0x004188D0`)
- `0x006207DF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620806` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062081F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00620752` → RVA `0x00F048B8` (`.data`; read)
- `0x0062075B` → RVA `0x00F04980` (`.data`; read)
- `0x00620767` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006206F0  48 8B C4                        mov rax, rsp
006206F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006206F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006206FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006206FF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00620703  41 56                           push r14
00620705  48 83 EC 30                     sub rsp, 0x30
00620709  48 8B E9                        mov rbp, rcx
0062070C  0F 57 C0                        xorps xmm0, xmm0
0062070F  B9 BD 01 00 00                  mov ecx, 0x1bd
00620714  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00620718  E8 17 53 E7 FF                  call 0x140495a34
0062071D  48 8B F8                        mov rdi, rax
00620720  48 85 C0                        test rax, rax
00620723  0F 84 8A 00 00 00               je 0x1406207b3
00620729  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062072C  A8 18                           test al, 0x18
0062072E  74 0C                           je 0x14062073c
00620730  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00620735  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062073A  EB 0E                           jmp 0x14062074a
0062073C  A8 04                           test al, 4
0062073E  74 0A                           je 0x14062074a
00620740  E8 C3 34 EB FF                  call 0x1404d3c08
00620745  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062074A  40 32 F6                        xor sil, sil
0062074D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00620752  40 38 35 5F 41 8E 00            cmp byte ptr [rip + 0x8e415f], sil
00620759  75 0C                           jne 0x140620767
0062075B  F7 05 1B 42 8E 00 00 08 00 00   test dword ptr [rip + 0x8e421b], 0x800
00620765  74 13                           je 0x14062077a
00620767  48 8D 0D 12 37 8E 00            lea rcx, [rip + 0x8e3712]
0062076E  E8 AD 5E BF FF                  call 0x140216620
00620773  40 8A F0                        mov sil, al
00620776  84 C0                           test al, al
00620778  74 39                           je 0x1406207b3
0062077A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062077E  49 8B 1E                        mov rbx, qword ptr [r14]
00620781  EB 1A                           jmp 0x14062079d
00620783  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620787  48 85 C0                        test rax, rax
0062078A  74 0E                           je 0x14062079a
0062078C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620790  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620795  E8 36 A3 09 00                  call 0x1406baad0
0062079A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062079D  49 3B DE                        cmp rbx, r14
006207A0  75 E1                           jne 0x140620783
006207A2  40 84 F6                        test sil, sil
006207A5  74 0C                           je 0x1406207b3
006207A7  48 8D 0D D2 36 8E 00            lea rcx, [rip + 0x8e36d2]
006207AE  E8 CD 96 D2 FF                  call 0x140349e80
006207B3  48 8B CD                        mov rcx, rbp
006207B6  E8 15 81 DF FF                  call 0x1404188d0
006207BB  48 85 FF                        test rdi, rdi
006207BE  74 64                           je 0x140620824
006207C0  40 32 F6                        xor sil, sil
006207C3  40 38 35 EE 40 8E 00            cmp byte ptr [rip + 0x8e40ee], sil
006207CA  75 0C                           jne 0x1406207d8
006207CC  F7 05 AA 41 8E 00 00 08 00 00   test dword ptr [rip + 0x8e41aa], 0x800
006207D6  74 13                           je 0x1406207eb
006207D8  48 8D 0D A1 36 8E 00            lea rcx, [rip + 0x8e36a1]
006207DF  E8 3C 5E BF FF                  call 0x140216620
006207E4  40 8A F0                        mov sil, al
006207E7  84 C0                           test al, al
006207E9  74 39                           je 0x140620824
006207EB  48 83 C7 30                     add rdi, 0x30
006207EF  48 8B 1F                        mov rbx, qword ptr [rdi]
006207F2  EB 1A                           jmp 0x14062080e
006207F4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006207F8  48 85 C0                        test rax, rax
006207FB  74 0E                           je 0x14062080b
006207FD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620801  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620806  E8 C5 A2 09 00                  call 0x1406baad0
0062080B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062080E  48 3B DF                        cmp rbx, rdi
00620811  75 E1                           jne 0x1406207f4
00620813  40 84 F6                        test sil, sil
00620816  74 0C                           je 0x140620824
00620818  48 8D 0D 61 36 8E 00            lea rcx, [rip + 0x8e3661]
0062081F  E8 5C 96 D2 FF                  call 0x140349e80
00620824  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00620829  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062082E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00620833  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00620838  48 83 C4 30                     add rsp, 0x30
0062083C  41 5E                           pop r14
0062083E  C3                              ret
0062083F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExInitializeFastOwnerEntryWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(445, a2, a3, a4);
    if (result == 0) goto loc_006207B3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062073C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062074A;
loc_0062073C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9322847)) != 0) goto loc_00620767;
    if (((*(unsigned int *)(v_rip + 9323035)) & (0x800ULL)) == 0) goto loc_0062077A;
loc_00620767:
    result = ExAcquireRundownProtection(v_rip + 9320210, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006207B3;
loc_0062077A:
    goto loc_0062079D;
loc_00620783:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062079D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00620783;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9320146;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExInitializeFastOwnerEntry(a1, a2, a3, a4);
    if (result == 0) goto loc_00620824;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9322734)) != 0) goto loc_006207D8;
    if (((*(unsigned int *)(v_rip + 9322922)) & (0x800ULL)) == 0) goto loc_006207EB;
loc_006207D8:
    result = ExAcquireRundownProtection(v_rip + 9320097, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620824;
loc_006207EB:
    v_rdi = (result) + (48);
    goto loc_0062080E;
loc_006207F4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062080E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_006207F4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9320033;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExInitializeFastOwnerEntryWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(445, a2, a3, a4);
    if (result == 0) goto loc_006207B3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062073C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062074A;
loc_0062073C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E415F)) != 0) goto loc_00620767;
    if (((*(uint32_t *)(v_rip + 0x8E421B)) & (0x800ULL)) == 0) goto loc_0062077A;
loc_00620767:
    result = ExAcquireRundownProtection(v_rip + 9320210, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006207B3;
loc_0062077A:
    goto loc_0062079D;
loc_00620783:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062079D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00620783;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9320146;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExInitializeFastOwnerEntry(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00620824;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E40EE)) != 0) goto loc_006207D8;
    if (((*(uint32_t *)(v_rip + 0x8E41AA)) & (0x800ULL)) == 0) goto loc_006207EB;
loc_006207D8:
    result = ExAcquireRundownProtection(v_rip + 9320097, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620824;
loc_006207EB:
    local_rdi = (result) + (48);
    goto loc_0062080E;
loc_006207F4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062080E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_006207F4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9320033;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006206F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006206F0[BB_006206F0]
  bb_00620729[BB_00620729]
  bb_00620730[BB_00620730]
  bb_0062073C[BB_0062073C]
  bb_00620740[BB_00620740]
  bb_0062074A[BB_0062074A]
  bb_0062075B[BB_0062075B]
  bb_00620767[BB_00620767]
  bb_0062077A[BB_0062077A]
  bb_00620783[BB_00620783]
  bb_0062078C[BB_0062078C]
  bb_0062079A[BB_0062079A]
  bb_0062079D[BB_0062079D]
  bb_006207A2[BB_006207A2]
  bb_006207A7[BB_006207A7]
  bb_006207B3[BB_006207B3]
  bb_006207C0[BB_006207C0]
  bb_006207CC[BB_006207CC]
  bb_006207D8[BB_006207D8]
  bb_006207EB[BB_006207EB]
  bb_006207F4[BB_006207F4]
  bb_006207FD[BB_006207FD]
  bb_0062080B[BB_0062080B]
  bb_0062080E[BB_0062080E]
  bb_00620813[BB_00620813]
  bb_00620818[BB_00620818]
  bb_00620824[BB_00620824]
  bb_0062083F[BB_0062083F]
  bb_006206F0 -->|branch| bb_006207B3
  bb_006206F0 -->|fallthrough| bb_00620729
  bb_00620729 -->|branch| bb_0062073C
  bb_00620729 -->|fallthrough| bb_00620730
  bb_00620730 -->|branch| bb_0062074A
  bb_0062073C -->|branch| bb_0062074A
  bb_0062073C -->|fallthrough| bb_00620740
  bb_00620740 -->|flow| bb_0062074A
  bb_0062074A -->|branch| bb_00620767
  bb_0062074A -->|fallthrough| bb_0062075B
  bb_0062075B -->|branch| bb_0062077A
  bb_0062075B -->|fallthrough| bb_00620767
  bb_00620767 -->|branch| bb_006207B3
  bb_00620767 -->|fallthrough| bb_0062077A
  bb_0062077A -->|branch| bb_0062079D
  bb_00620783 -->|branch| bb_0062079A
  bb_00620783 -->|fallthrough| bb_0062078C
  bb_0062078C -->|flow| bb_0062079A
  bb_0062079A -->|flow| bb_0062079D
  bb_0062079D -->|branch| bb_00620783
  bb_0062079D -->|fallthrough| bb_006207A2
  bb_006207A2 -->|branch| bb_006207B3
  bb_006207A2 -->|fallthrough| bb_006207A7
  bb_006207A7 -->|flow| bb_006207B3
  bb_006207B3 -->|branch| bb_00620824
  bb_006207B3 -->|fallthrough| bb_006207C0
  bb_006207C0 -->|branch| bb_006207D8
  bb_006207C0 -->|fallthrough| bb_006207CC
  bb_006207CC -->|branch| bb_006207EB
  bb_006207CC -->|fallthrough| bb_006207D8
  bb_006207D8 -->|branch| bb_00620824
  bb_006207D8 -->|fallthrough| bb_006207EB
  bb_006207EB -->|branch| bb_0062080E
  bb_006207F4 -->|branch| bb_0062080B
  bb_006207F4 -->|fallthrough| bb_006207FD
  bb_006207FD -->|flow| bb_0062080B
  bb_0062080B -->|flow| bb_0062080E
  bb_0062080E -->|branch| bb_006207F4
  bb_0062080E -->|fallthrough| bb_00620813
  bb_00620813 -->|branch| bb_00620824
  bb_00620813 -->|fallthrough| bb_00620818
  bb_00620818 -->|flow| bb_00620824
```
