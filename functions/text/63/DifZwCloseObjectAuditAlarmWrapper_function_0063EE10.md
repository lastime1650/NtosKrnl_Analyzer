# DifZwCloseObjectAuditAlarmWrapper

- RVA: `0x0063EE10`–`0x0063EF87` (길이 `375` bytes)
- VA: `0x000000014063EE10`
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
- `0x0063EE4E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063EE74` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063EEA8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063EECE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063EEE7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063EEF5` → [ZwCloseObjectAuditAlarm](../6A/ZwCloseObjectAuditAlarm_function_006AD830.md) (function, `0x006AD830`)
- `0x0063EF21` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063EF47` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063EF60` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063EE84` → RVA `0x00F048B8` (`.data`; read)
- `0x0063EE95` → RVA `0x00F04980` (`.data`; read)
- `0x0063EEA1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063EE10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063EE15  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063EE1A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063EE1F  55                              push rbp
0063EE20  41 54                           push r12
0063EE22  41 55                           push r13
0063EE24  41 56                           push r14
0063EE26  41 57                           push r15
0063EE28  48 8B EC                        mov rbp, rsp
0063EE2B  48 83 EC 50                     sub rsp, 0x50
0063EE2F  0F 57 C0                        xorps xmm0, xmm0
0063EE32  33 C0                           xor eax, eax
0063EE34  4C 8B E9                        mov r13, rcx
0063EE37  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063EE3B  B9 82 00 00 00                  mov ecx, 0x82
0063EE40  45 8A F8                        mov r15b, r8b
0063EE43  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063EE47  4C 8B E2                        mov r12, rdx
0063EE4A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063EE4E  E8 E1 6B E5 FF                  call 0x140495a34
0063EE53  48 8B F0                        mov rsi, rax
0063EE56  48 85 C0                        test rax, rax
0063EE59  0F 84 8D 00 00 00               je 0x14063eeec
0063EE5F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063EE62  A8 18                           test al, 0x18
0063EE64  74 0A                           je 0x14063ee70
0063EE66  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063EE6A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063EE6E  EB 0D                           jmp 0x14063ee7d
0063EE70  A8 04                           test al, 4
0063EE72  74 09                           je 0x14063ee7d
0063EE74  E8 8F 4D E9 FF                  call 0x1404d3c08
0063EE79  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063EE7D  45 32 F6                        xor r14b, r14b
0063EE80  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063EE84  44 38 35 2D 5A 8C 00            cmp byte ptr [rip + 0x8c5a2d], r14b
0063EE8B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063EE8F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063EE93  75 0C                           jne 0x14063eea1
0063EE95  F7 05 E1 5A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5ae1], 0x800
0063EE9F  74 13                           je 0x14063eeb4
0063EEA1  48 8D 0D D8 4F 8C 00            lea rcx, [rip + 0x8c4fd8]
0063EEA8  E8 73 77 BD FF                  call 0x140216620
0063EEAD  44 8A F0                        mov r14b, al
0063EEB0  84 C0                           test al, al
0063EEB2  74 38                           je 0x14063eeec
0063EEB4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063EEB8  48 8B 1F                        mov rbx, qword ptr [rdi]
0063EEBB  EB 19                           jmp 0x14063eed6
0063EEBD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063EEC1  48 85 C0                        test rax, rax
0063EEC4  74 0D                           je 0x14063eed3
0063EEC6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063EECA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063EECE  E8 FD BB 07 00                  call 0x1406baad0
0063EED3  48 8B 1B                        mov rbx, qword ptr [rbx]
0063EED6  48 3B DF                        cmp rbx, rdi
0063EED9  75 E2                           jne 0x14063eebd
0063EEDB  45 84 F6                        test r14b, r14b
0063EEDE  74 0C                           je 0x14063eeec
0063EEE0  48 8D 0D 99 4F 8C 00            lea rcx, [rip + 0x8c4f99]
0063EEE7  E8 94 AF D0 FF                  call 0x140349e80
0063EEEC  45 8A C7                        mov r8b, r15b
0063EEEF  49 8B D4                        mov rdx, r12
0063EEF2  49 8B CD                        mov rcx, r13
0063EEF5  E8 36 E9 06 00                  call 0x1406ad830
0063EEFA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063EEFD  48 85 F6                        test rsi, rsi
0063EF00  74 63                           je 0x14063ef65
0063EF02  40 32 FF                        xor dil, dil
0063EF05  40 38 3D AC 59 8C 00            cmp byte ptr [rip + 0x8c59ac], dil
0063EF0C  75 0C                           jne 0x14063ef1a
0063EF0E  F7 05 68 5A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5a68], 0x800
0063EF18  74 13                           je 0x14063ef2d
0063EF1A  48 8D 0D 5F 4F 8C 00            lea rcx, [rip + 0x8c4f5f]
0063EF21  E8 FA 76 BD FF                  call 0x140216620
0063EF26  40 8A F8                        mov dil, al
0063EF29  84 C0                           test al, al
0063EF2B  74 38                           je 0x14063ef65
0063EF2D  48 83 C6 30                     add rsi, 0x30
0063EF31  48 8B 1E                        mov rbx, qword ptr [rsi]
0063EF34  EB 19                           jmp 0x14063ef4f
0063EF36  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063EF3A  48 85 C0                        test rax, rax
0063EF3D  74 0D                           je 0x14063ef4c
0063EF3F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063EF43  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063EF47  E8 84 BB 07 00                  call 0x1406baad0
0063EF4C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063EF4F  48 3B DE                        cmp rbx, rsi
0063EF52  75 E2                           jne 0x14063ef36
0063EF54  40 84 FF                        test dil, dil
0063EF57  74 0C                           je 0x14063ef65
0063EF59  48 8D 0D 20 4F 8C 00            lea rcx, [rip + 0x8c4f20]
0063EF60  E8 1B AF D0 FF                  call 0x140349e80
0063EF65  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063EF68  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063EF6D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063EF71  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063EF75  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063EF79  49 8B E3                        mov rsp, r11
0063EF7C  41 5F                           pop r15
0063EF7E  41 5E                           pop r14
0063EF80  41 5D                           pop r13
0063EF82  41 5C                           pop r12
0063EF84  5D                              pop rbp
0063EF85  C3                              ret
0063EF86  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCloseObjectAuditAlarmWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    unsigned __int8 v_stack_m50;
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
    result = DifGetAPIThunkContextById(130, a2, a3, a4);
    if (result == 0) goto loc_0063EEEC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063EE70;
    v_stack_m58 = v_stack_p0;
    goto loc_0063EE7D;
loc_0063EE70:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9198125)) != 0) goto loc_0063EEA1;
    if (((*(unsigned int *)(v_rip + 9198305)) & (0x800ULL)) == 0) goto loc_0063EEB4;
loc_0063EEA1:
    result = ExAcquireRundownProtection(v_rip + 9195480, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063EEEC;
loc_0063EEB4:
    goto loc_0063EED6;
loc_0063EEBD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063EED6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063EEBD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9195417;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCloseObjectAuditAlarm(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063EF65;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9197996)) != 0) goto loc_0063EF1A;
    if (((*(unsigned int *)(v_rip + 9198184)) & (0x800ULL)) == 0) goto loc_0063EF2D;
loc_0063EF1A:
    result = ExAcquireRundownProtection(v_rip + 9195359, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063EF65;
loc_0063EF2D:
    v_rsi = (result) + (48);
    goto loc_0063EF4F;
loc_0063EF36:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063EF4F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063EF36;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9195296;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCloseObjectAuditAlarmWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    uint8_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(130, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063EEEC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063EE70;
    v_stack_m58 = v_stack_p0;
    goto loc_0063EE7D;
loc_0063EE70:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C5A2D)) != 0) goto loc_0063EEA1;
    if (((*(uint32_t *)(v_rip + 0x8C5AE1)) & (0x800ULL)) == 0) goto loc_0063EEB4;
loc_0063EEA1:
    result = ExAcquireRundownProtection(v_rip + 9195480, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063EEEC;
loc_0063EEB4:
    goto loc_0063EED6;
loc_0063EEBD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063EED6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063EEBD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9195417;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwCloseObjectAuditAlarm(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063EF65;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C59AC)) != 0) goto loc_0063EF1A;
    if (((*(uint32_t *)(v_rip + 0x8C5A68)) & (0x800ULL)) == 0) goto loc_0063EF2D;
loc_0063EF1A:
    result = ExAcquireRundownProtection(v_rip + 9195359, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063EF65;
loc_0063EF2D:
    local_rsi = (result) + (48);
    goto loc_0063EF4F;
loc_0063EF36:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063EF4F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063EF36;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9195296;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063EE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063EE10[BB_0063EE10]
  bb_0063EE5F[BB_0063EE5F]
  bb_0063EE66[BB_0063EE66]
  bb_0063EE70[BB_0063EE70]
  bb_0063EE74[BB_0063EE74]
  bb_0063EE7D[BB_0063EE7D]
  bb_0063EE95[BB_0063EE95]
  bb_0063EEA1[BB_0063EEA1]
  bb_0063EEB4[BB_0063EEB4]
  bb_0063EEBD[BB_0063EEBD]
  bb_0063EEC6[BB_0063EEC6]
  bb_0063EED3[BB_0063EED3]
  bb_0063EED6[BB_0063EED6]
  bb_0063EEDB[BB_0063EEDB]
  bb_0063EEE0[BB_0063EEE0]
  bb_0063EEEC[BB_0063EEEC]
  bb_0063EF02[BB_0063EF02]
  bb_0063EF0E[BB_0063EF0E]
  bb_0063EF1A[BB_0063EF1A]
  bb_0063EF2D[BB_0063EF2D]
  bb_0063EF36[BB_0063EF36]
  bb_0063EF3F[BB_0063EF3F]
  bb_0063EF4C[BB_0063EF4C]
  bb_0063EF4F[BB_0063EF4F]
  bb_0063EF54[BB_0063EF54]
  bb_0063EF59[BB_0063EF59]
  bb_0063EF65[BB_0063EF65]
  bb_0063EF86[BB_0063EF86]
  bb_0063EE10 -->|branch| bb_0063EEEC
  bb_0063EE10 -->|fallthrough| bb_0063EE5F
  bb_0063EE5F -->|branch| bb_0063EE70
  bb_0063EE5F -->|fallthrough| bb_0063EE66
  bb_0063EE66 -->|branch| bb_0063EE7D
  bb_0063EE70 -->|branch| bb_0063EE7D
  bb_0063EE70 -->|fallthrough| bb_0063EE74
  bb_0063EE74 -->|flow| bb_0063EE7D
  bb_0063EE7D -->|branch| bb_0063EEA1
  bb_0063EE7D -->|fallthrough| bb_0063EE95
  bb_0063EE95 -->|branch| bb_0063EEB4
  bb_0063EE95 -->|fallthrough| bb_0063EEA1
  bb_0063EEA1 -->|branch| bb_0063EEEC
  bb_0063EEA1 -->|fallthrough| bb_0063EEB4
  bb_0063EEB4 -->|branch| bb_0063EED6
  bb_0063EEBD -->|branch| bb_0063EED3
  bb_0063EEBD -->|fallthrough| bb_0063EEC6
  bb_0063EEC6 -->|flow| bb_0063EED3
  bb_0063EED3 -->|flow| bb_0063EED6
  bb_0063EED6 -->|branch| bb_0063EEBD
  bb_0063EED6 -->|fallthrough| bb_0063EEDB
  bb_0063EEDB -->|branch| bb_0063EEEC
  bb_0063EEDB -->|fallthrough| bb_0063EEE0
  bb_0063EEE0 -->|flow| bb_0063EEEC
  bb_0063EEEC -->|branch| bb_0063EF65
  bb_0063EEEC -->|fallthrough| bb_0063EF02
  bb_0063EF02 -->|branch| bb_0063EF1A
  bb_0063EF02 -->|fallthrough| bb_0063EF0E
  bb_0063EF0E -->|branch| bb_0063EF2D
  bb_0063EF0E -->|fallthrough| bb_0063EF1A
  bb_0063EF1A -->|branch| bb_0063EF65
  bb_0063EF1A -->|fallthrough| bb_0063EF2D
  bb_0063EF2D -->|branch| bb_0063EF4F
  bb_0063EF36 -->|branch| bb_0063EF4C
  bb_0063EF36 -->|fallthrough| bb_0063EF3F
  bb_0063EF3F -->|flow| bb_0063EF4C
  bb_0063EF4C -->|flow| bb_0063EF4F
  bb_0063EF4F -->|branch| bb_0063EF36
  bb_0063EF4F -->|fallthrough| bb_0063EF54
  bb_0063EF54 -->|branch| bb_0063EF65
  bb_0063EF54 -->|fallthrough| bb_0063EF59
  bb_0063EF59 -->|flow| bb_0063EF65
```
