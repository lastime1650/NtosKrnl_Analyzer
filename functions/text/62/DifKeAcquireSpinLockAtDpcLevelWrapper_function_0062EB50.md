# DifKeAcquireSpinLockAtDpcLevelWrapper

- RVA: `0x0062EB50`–`0x0062ECA0` (길이 `336` bytes)
- VA: `0x000000014062EB50`
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
- `0x0062EB78` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062EBA0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062EBCE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EBF5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EC0E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062EC16` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0062EC3F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EC66` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EC7F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062EBB2` → RVA `0x00F048B8` (`.data`; read)
- `0x0062EBBB` → RVA `0x00F04980` (`.data`; read)
- `0x0062EBC7` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062EB50  48 8B C4                        mov rax, rsp
0062EB53  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062EB57  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062EB5B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062EB5F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062EB63  41 56                           push r14
0062EB65  48 83 EC 30                     sub rsp, 0x30
0062EB69  48 8B E9                        mov rbp, rcx
0062EB6C  0F 57 C0                        xorps xmm0, xmm0
0062EB6F  B9 24 01 00 00                  mov ecx, 0x124
0062EB74  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0062EB78  E8 B7 6E E6 FF                  call 0x140495a34
0062EB7D  48 8B F8                        mov rdi, rax
0062EB80  48 85 C0                        test rax, rax
0062EB83  0F 84 8A 00 00 00               je 0x14062ec13
0062EB89  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062EB8C  A8 18                           test al, 0x18
0062EB8E  74 0C                           je 0x14062eb9c
0062EB90  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0062EB95  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062EB9A  EB 0E                           jmp 0x14062ebaa
0062EB9C  A8 04                           test al, 4
0062EB9E  74 0A                           je 0x14062ebaa
0062EBA0  E8 63 50 EA FF                  call 0x1404d3c08
0062EBA5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062EBAA  40 32 F6                        xor sil, sil
0062EBAD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062EBB2  40 38 35 FF 5C 8D 00            cmp byte ptr [rip + 0x8d5cff], sil
0062EBB9  75 0C                           jne 0x14062ebc7
0062EBBB  F7 05 BB 5D 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5dbb], 0x800
0062EBC5  74 13                           je 0x14062ebda
0062EBC7  48 8D 0D B2 52 8D 00            lea rcx, [rip + 0x8d52b2]
0062EBCE  E8 4D 7A BE FF                  call 0x140216620
0062EBD3  40 8A F0                        mov sil, al
0062EBD6  84 C0                           test al, al
0062EBD8  74 39                           je 0x14062ec13
0062EBDA  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062EBDE  49 8B 1E                        mov rbx, qword ptr [r14]
0062EBE1  EB 1A                           jmp 0x14062ebfd
0062EBE3  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EBE7  48 85 C0                        test rax, rax
0062EBEA  74 0E                           je 0x14062ebfa
0062EBEC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EBF0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EBF5  E8 D6 BE 08 00                  call 0x1406baad0
0062EBFA  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EBFD  49 3B DE                        cmp rbx, r14
0062EC00  75 E1                           jne 0x14062ebe3
0062EC02  40 84 F6                        test sil, sil
0062EC05  74 0C                           je 0x14062ec13
0062EC07  48 8D 0D 72 52 8D 00            lea rcx, [rip + 0x8d5272]
0062EC0E  E8 6D B2 D1 FF                  call 0x140349e80
0062EC13  48 8B CD                        mov rcx, rbp
0062EC16  E8 15 98 BD FF                  call 0x140208430
0062EC1B  48 85 FF                        test rdi, rdi
0062EC1E  74 64                           je 0x14062ec84
0062EC20  40 32 F6                        xor sil, sil
0062EC23  40 38 35 8E 5C 8D 00            cmp byte ptr [rip + 0x8d5c8e], sil
0062EC2A  75 0C                           jne 0x14062ec38
0062EC2C  F7 05 4A 5D 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5d4a], 0x800
0062EC36  74 13                           je 0x14062ec4b
0062EC38  48 8D 0D 41 52 8D 00            lea rcx, [rip + 0x8d5241]
0062EC3F  E8 DC 79 BE FF                  call 0x140216620
0062EC44  40 8A F0                        mov sil, al
0062EC47  84 C0                           test al, al
0062EC49  74 39                           je 0x14062ec84
0062EC4B  48 83 C7 30                     add rdi, 0x30
0062EC4F  48 8B 1F                        mov rbx, qword ptr [rdi]
0062EC52  EB 1A                           jmp 0x14062ec6e
0062EC54  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EC58  48 85 C0                        test rax, rax
0062EC5B  74 0E                           je 0x14062ec6b
0062EC5D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EC61  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EC66  E8 65 BE 08 00                  call 0x1406baad0
0062EC6B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EC6E  48 3B DF                        cmp rbx, rdi
0062EC71  75 E1                           jne 0x14062ec54
0062EC73  40 84 F6                        test sil, sil
0062EC76  74 0C                           je 0x14062ec84
0062EC78  48 8D 0D 01 52 8D 00            lea rcx, [rip + 0x8d5201]
0062EC7F  E8 FC B1 D1 FF                  call 0x140349e80
0062EC84  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0062EC89  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062EC8E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0062EC93  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0062EC98  48 83 C4 30                     add rsp, 0x30
0062EC9C  41 5E                           pop r14
0062EC9E  C3                              ret
0062EC9F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeAcquireSpinLockAtDpcLevelWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(292, a2, a3, a4);
    if (result == 0) goto loc_0062EC13;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062EB9C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062EBAA;
loc_0062EB9C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9264383)) != 0) goto loc_0062EBC7;
    if (((*(unsigned int *)(v_rip + 9264571)) & (0x800ULL)) == 0) goto loc_0062EBDA;
loc_0062EBC7:
    result = ExAcquireRundownProtection(v_rip + 9261746, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EC13;
loc_0062EBDA:
    goto loc_0062EBFD;
loc_0062EBE3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EBFD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062EBE3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9261682;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeAcquireSpinLockAtDpcLevel(a1, a2, a3, a4);
    if (result == 0) goto loc_0062EC84;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9264270)) != 0) goto loc_0062EC38;
    if (((*(unsigned int *)(v_rip + 9264458)) & (0x800ULL)) == 0) goto loc_0062EC4B;
loc_0062EC38:
    result = ExAcquireRundownProtection(v_rip + 9261633, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EC84;
loc_0062EC4B:
    v_rdi = (result) + (48);
    goto loc_0062EC6E;
loc_0062EC54:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EC6E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0062EC54;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9261569;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeAcquireSpinLockAtDpcLevelWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(292, a2, a3, a4);
    if (result == 0) goto loc_0062EC13;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062EB9C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062EBAA;
loc_0062EB9C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D5CFF)) != 0) goto loc_0062EBC7;
    if (((*(uint32_t *)(v_rip + 0x8D5DBB)) & (0x800ULL)) == 0) goto loc_0062EBDA;
loc_0062EBC7:
    result = ExAcquireRundownProtection(v_rip + 9261746, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EC13;
loc_0062EBDA:
    goto loc_0062EBFD;
loc_0062EBE3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EBFD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062EBE3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9261682;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeAcquireSpinLockAtDpcLevel(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0062EC84;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D5C8E)) != 0) goto loc_0062EC38;
    if (((*(uint32_t *)(v_rip + 0x8D5D4A)) & (0x800ULL)) == 0) goto loc_0062EC4B;
loc_0062EC38:
    result = ExAcquireRundownProtection(v_rip + 9261633, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EC84;
loc_0062EC4B:
    local_rdi = (result) + (48);
    goto loc_0062EC6E;
loc_0062EC54:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EC6E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0062EC54;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9261569;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062EB50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062EB50[BB_0062EB50]
  bb_0062EB89[BB_0062EB89]
  bb_0062EB90[BB_0062EB90]
  bb_0062EB9C[BB_0062EB9C]
  bb_0062EBA0[BB_0062EBA0]
  bb_0062EBAA[BB_0062EBAA]
  bb_0062EBBB[BB_0062EBBB]
  bb_0062EBC7[BB_0062EBC7]
  bb_0062EBDA[BB_0062EBDA]
  bb_0062EBE3[BB_0062EBE3]
  bb_0062EBEC[BB_0062EBEC]
  bb_0062EBFA[BB_0062EBFA]
  bb_0062EBFD[BB_0062EBFD]
  bb_0062EC02[BB_0062EC02]
  bb_0062EC07[BB_0062EC07]
  bb_0062EC13[BB_0062EC13]
  bb_0062EC20[BB_0062EC20]
  bb_0062EC2C[BB_0062EC2C]
  bb_0062EC38[BB_0062EC38]
  bb_0062EC4B[BB_0062EC4B]
  bb_0062EC54[BB_0062EC54]
  bb_0062EC5D[BB_0062EC5D]
  bb_0062EC6B[BB_0062EC6B]
  bb_0062EC6E[BB_0062EC6E]
  bb_0062EC73[BB_0062EC73]
  bb_0062EC78[BB_0062EC78]
  bb_0062EC84[BB_0062EC84]
  bb_0062EC9F[BB_0062EC9F]
  bb_0062EB50 -->|branch| bb_0062EC13
  bb_0062EB50 -->|fallthrough| bb_0062EB89
  bb_0062EB89 -->|branch| bb_0062EB9C
  bb_0062EB89 -->|fallthrough| bb_0062EB90
  bb_0062EB90 -->|branch| bb_0062EBAA
  bb_0062EB9C -->|branch| bb_0062EBAA
  bb_0062EB9C -->|fallthrough| bb_0062EBA0
  bb_0062EBA0 -->|flow| bb_0062EBAA
  bb_0062EBAA -->|branch| bb_0062EBC7
  bb_0062EBAA -->|fallthrough| bb_0062EBBB
  bb_0062EBBB -->|branch| bb_0062EBDA
  bb_0062EBBB -->|fallthrough| bb_0062EBC7
  bb_0062EBC7 -->|branch| bb_0062EC13
  bb_0062EBC7 -->|fallthrough| bb_0062EBDA
  bb_0062EBDA -->|branch| bb_0062EBFD
  bb_0062EBE3 -->|branch| bb_0062EBFA
  bb_0062EBE3 -->|fallthrough| bb_0062EBEC
  bb_0062EBEC -->|flow| bb_0062EBFA
  bb_0062EBFA -->|flow| bb_0062EBFD
  bb_0062EBFD -->|branch| bb_0062EBE3
  bb_0062EBFD -->|fallthrough| bb_0062EC02
  bb_0062EC02 -->|branch| bb_0062EC13
  bb_0062EC02 -->|fallthrough| bb_0062EC07
  bb_0062EC07 -->|flow| bb_0062EC13
  bb_0062EC13 -->|branch| bb_0062EC84
  bb_0062EC13 -->|fallthrough| bb_0062EC20
  bb_0062EC20 -->|branch| bb_0062EC38
  bb_0062EC20 -->|fallthrough| bb_0062EC2C
  bb_0062EC2C -->|branch| bb_0062EC4B
  bb_0062EC2C -->|fallthrough| bb_0062EC38
  bb_0062EC38 -->|branch| bb_0062EC84
  bb_0062EC38 -->|fallthrough| bb_0062EC4B
  bb_0062EC4B -->|branch| bb_0062EC6E
  bb_0062EC54 -->|branch| bb_0062EC6B
  bb_0062EC54 -->|fallthrough| bb_0062EC5D
  bb_0062EC5D -->|flow| bb_0062EC6B
  bb_0062EC6B -->|flow| bb_0062EC6E
  bb_0062EC6E -->|branch| bb_0062EC54
  bb_0062EC6E -->|fallthrough| bb_0062EC73
  bb_0062EC73 -->|branch| bb_0062EC84
  bb_0062EC73 -->|fallthrough| bb_0062EC78
  bb_0062EC78 -->|flow| bb_0062EC84
```
